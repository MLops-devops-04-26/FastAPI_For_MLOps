# app/main.py
# Created by: Rajinikanth Vadla
# This is the main file for the FastAPI application.

from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel
import os
from typing import List

app = FastAPI(
    title="House Price Prediction API",
    description="An API to predict house prices using an XGBoost model. Created by Rajinikanth Vadla.",
    version="1.0"
)

# Model loading
def get_latest_model_path():
    files = [f for f in os.listdir('models') if f.endswith('.pkl') and 'house_price_model_v' in f]
    if not files:
        return None
    # Sort files by version number (assuming format model_vX.X.pkl)
    files.sort(key=lambda x: float(x.split('_v')[1].split('.pkl')[0]), reverse=True)
    return os.path.join('models', files[0])

model_path = get_latest_model_path()
if model_path:
    model = joblib.load(model_path)
    model_columns = joblib.load('models/model_columns.pkl')
else:
    model = None
    model_columns = None

@app.get("/")
def read_root():
    """
    Root endpoint with a welcome message.
    Created by: Rajinikanth Vadla
    """
    return {
        "message": "Welcome to the House Price Prediction API!",
        "author": "Rajinikanth Vadla",
        "docs_url": "/docs"
    }

@app.get("/health")
def health_check():
    """
    Health check endpoint to ensure the API is running.
    Created by: Rajinikanth Vadla
    """
    return {"status": "ok", "model_loaded": model is not None, "model_path": model_path, "model_columns_loaded": model_columns is not None}

# Define the input data model
class HouseFeatures(BaseModel):
    features: dict

@app.post("/predict")
def predict(data: HouseFeatures):
    """
    Prediction endpoint.
    Created by: Rajinikanth Vadla
    """
    if model is None or model_columns is None:
        return {"error": "Model or model columns not found. Please train a model first."}
    
    try:
        # Create a dataframe from the input features.
        df_for_prediction = pd.DataFrame(data.features, index=[0])
        # Reorder columns to match the model's training order
        df_for_prediction = df_for_prediction.reindex(columns=model_columns, fill_value=0)
        
        prediction = model.predict(df_for_prediction)
        return {"prediction": prediction.tolist()}
    except Exception as e:
        return {"error": str(e)}

@app.post("/retrain")
def retrain():
    """
    Retraining endpoint. This is a placeholder and would trigger a CI/CD pipeline in a real system.
    Created by: Rajinikanth Vadla
    """
    try:
        # In a real-world scenario, this would be an async task or a call to a CI/CD pipeline
        os.system("python scripts/train.py")
        global model, model_path, model_columns
        model_path = get_latest_model_path()
        if model_path:
            model = joblib.load(model_path)
            model_columns = joblib.load('models/model_columns.pkl')
        return {"message": "Model retraining initiated and completed.", "new_model_path": model_path}
    except Exception as e:
        return {"error": f"Retraining failed: {str(e)}"} 