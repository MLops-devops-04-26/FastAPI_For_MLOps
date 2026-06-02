# scripts/train.py
# This script is for training the model.

import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib
import numpy as np

# Load the dataset
df = pd.read_csv('data/house_prices.csv')

# A simple preprocessing function
def preprocess_data(df):
    # For simplicity, we'll fill missing values with the mean of the column.
    # In a real-world scenario, more sophisticated methods should be used.
    for col in df.select_dtypes(include=np.number).columns:
        df[col] = df[col].fillna(df[col].mean())

    # Drop non-numeric columns for this simple model
    df = df.select_dtypes(include=np.number)
    
    # Drop columns with 'Id' in their name
    df = df.loc[:, ~df.columns.str.contains('^Id$', case=False)]
    
    return df

df = preprocess_data(df)

# Define features (X) and target (y)
X = df.drop('SalePrice', axis=1)
y = df['SalePrice']

# Save the columns
model_columns = X.columns
joblib.dump(model_columns, 'models/model_columns.pkl')

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the XGBoost Regressor model
model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=1000, learning_rate=0.05, max_depth=5, subsample=0.8, colsample_bytree=0.8, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Model Mean Squared Error: {mse}")

# Save the model with versioning
model_version = "1.0"
model_path = f'models/house_price_model_v{model_version}.pkl'
joblib.dump(model, model_path)

print(f"Model saved to {model_path}") 