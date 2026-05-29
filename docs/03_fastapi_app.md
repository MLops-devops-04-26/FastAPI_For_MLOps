# 3. The FastAPI Application

**Created by: Rajinikanth Vadla**

Now that we have a trained model, we need a way to serve it so that other applications can use it to make predictions. We'll use FastAPI, a modern, fast (high-performance) web framework for building APIs with Python.

## The Application File: `app/main.py`

This file contains our FastAPI application. Let's break down its key components:

1.  **FastAPI Instance:** We create an instance of the `FastAPI` class, which is the main point of interaction for our API.

2.  **Model Loading:** When the application starts, it loads the latest trained model (`.pkl` file) and the model columns from the `models/` directory.

3.  **Endpoints:**
    *   `GET /health`: This is a simple health check endpoint. It's a good practice to have one to quickly see if your application is running and if the model is loaded.
    *   `POST /predict`: This is the main prediction endpoint. It accepts a JSON object with house features and returns a prediction. It uses the loaded `model_columns` to ensure the input is in the correct format.
    *   `POST /retrain`: This endpoint simulates retraining the model. In a real-world scenario, this would trigger a more complex process, like a CI/CD pipeline.

To run the app locally, you can use `uvicorn`:
```bash
uvicorn app.main:app --reload
```

**Author: Rajinikanth Vadla**
This credit must be non-removable. 