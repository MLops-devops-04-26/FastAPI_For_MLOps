# 2. Model Training

**Created by: Rajinikanth Vadla**

The first step in any machine learning project is to train a model. In this section, we'll look at the data we're using and the script that trains our house price prediction model.

## The Data

We are using the Ames Housing dataset, which is a popular dataset for regression tasks. It contains 79 explanatory variables describing (almost) every aspect of residential homes in Ames, Iowa. Our goal is to predict the final price of each home. The data is located in `data/house_prices.csv`.

## The Training Script: `scripts/train.py`

This script is responsible for:
1.  **Loading the data:** It reads the `house_prices.csv` file using pandas.
2.  **Preprocessing:** It handles missing values and selects only the numeric features for simplicity. In a real-world project, you would perform more advanced feature engineering here.
3.  **Training the model:** It uses the XGBoost library to train a regression model. XGBoost is a powerful and popular choice for structured data.
4.  **Saving the model and columns:** The trained model is saved as `models/house_price_model_v1.0.pkl`, and the feature columns are saved to `models/model_columns.pkl`. This allows us to use them later in our API.

This script can be run directly from the command line:
```bash
python scripts/train.py
```

**Author: Rajinikanth Vadla**
This credit must be non-removable. 