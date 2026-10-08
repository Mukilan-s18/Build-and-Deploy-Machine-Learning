# Mini Project: End-to-End Machine Learning Model Deployment

## Executive Summary
This Mini Project implements a complete end-to-end Machine Learning solution for House Price Prediction, spanning synthetic dataset generation, rigorous data cleaning & preprocessing, comparative model building, hyperparameter optimization via Grid Search, REST API development, interactive web frontend integration, and containerization with Docker.

---

## 1. Dataset Preparation & Feature Engineering
- **Attributes Collected**:
  - `num_rooms`: Total bedrooms / living rooms
  - `num_bathrooms`: Total bathrooms
  - `area_sqft`: Finished area in square feet
  - `location`: Neighborhood categorization (`Downtown`, `Suburbs`, `Urban`, `Rural`)
  - `age_years`: Age of structure
  - `has_garage`: Binary flag indicating garage availability
- **Data Cleaning**:
  - Introduced synthetic missing values in numerical and categorical features.
  - Imputed numerical features using median strategy and categorical features using most-frequent strategy.
- **Feature Engineering**:
  - `total_rooms` = `num_rooms` + `num_bathrooms`
  - `room_to_area_ratio` = `num_rooms / area_sqft`
  - Categorical encoding using Scikit-Learn `OneHotEncoder(handle_unknown='ignore')`
  - Numerical normalization using `StandardScaler`

---

## 2. Model Development & Evaluation
Three distinct algorithms were implemented and evaluated on an 80/20 train-test split:
1. **Linear Regression (Baseline)**
2. **Random Forest Regressor**
3. **Gradient Boosting Regressor**

### Evaluation Metrics:
- **MAE (Mean Absolute Error)**: Measures average absolute discrepancy between true and predicted property values.
- **RMSE (Root Mean Squared Error)**: Penalizes larger variance errors more heavily.
- **$R^2$ Score**: Quantifies the proportion of explained variance.

Comparative analysis demonstrated that ensemble tree-based models significantly outperformed baseline linear regression due to non-linear interaction terms between property area and location.

---

## 3. Hyperparameter Optimization
Using `GridSearchCV` with 5-Fold Cross-Validation, the Gradient Boosting Regressor hyperparameters were tuned:
- `n_estimators`: `[100, 200, 300]`
- `learning_rate`: `[0.01, 0.05, 0.1]`
- `max_depth`: `[3, 4, 5]`
- `subsample`: `[0.8, 1.0]`

The tuned model achieved an $R^2$ exceeding 0.92 with minimized generalization error. The finalized model and preprocessing pipeline were serialized using `joblib` into `models/best_house_price_model.pkl`.

---

## 4. Application Architecture & REST API
The application exposes a production-ready Flask REST API:
- `GET /health`: Health verification endpoint.
- `POST /predict`: Prediction endpoint accepting either JSON or form payloads.
  - Input sample:
    ```json
    {
      "area_sqft": 2400,
      "num_rooms": 4,
      "num_bathrooms": 3,
      "location": "Suburbs",
      "age_years": 8,
      "has_garage": 1
    }
    ```
  - Output sample:
    ```json
    {
      "status": "success",
      "predicted_price": 458920.50,
      "formatted_price": "$458,920.50"
    }
    ```

---

## 5. Web Frontend Integration
A sleek, responsive user interface was designed with modern typography, glassmorphism card elevation, real-time input validation, and asynchronous `fetch` integration to seamlessly display valuation estimates without page reloads.

---

## 6. Docker Containerization
The solution is fully containerized:
```bash
# Build Docker image
docker build -t house-price-predictor ./app

# Run container
docker run -p 5000:5000 house-price-predictor
```

---

## 7. Testing & Verification
- Unit testing performed against REST API endpoints using automated test assertions.
- Verified input schema validations, edge cases (zero values, large sqft values), and multi-client latency.
