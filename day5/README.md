#
## Feature Correlation Heatmap

### Principal Component Analysis (PCA)

- Feature interaction and Multivariate Analysis
- Correlation Analysis in Multivariate Data

## Model Training with Multiple input Variables
- Feature scaling and Normalization
    - Standardization (Z-score normalization)
    - Min-Max Scaling: transforms features to a specific range (e.g., [0, 1])
    - Standardization: transforms features to have a mean of 0 and a standard deviation of 1
    - Tree-based models (e.g., Decision Trees, Random Forests) are less sensitive to feature scaling
    - Feature scalling methods
        - Without scaling: Decision Trees, Random Forests, Gradient Boosting Machines
        - After scaling: Support Vector Machines, K-Nearest Neighbors, Logistic Regression, Neural Networks
            - Min-max
- Multiple Linear Regression
    - Equation: y = β0 + β1x1 + β2x2 + ... + βnxn + ε
    - Each coefficient (βi) represents the change in the dependent variable (y) for a one-unit change in the corresponding independent variable (xi), while holding all other independent variables constant.
- Recursive Feature Elimination (RFE)
- Regularization techniques (L1, L2)
- Hyperparameter tuning (Grid Search, Random Search)

Example:
- Healthcare Multi-Feature Model
- Finance: Credit Risk Scoring
- E-Commerce: Customer Churn Prediction


## Pre-processing
- Missing value
- Outliers (Chọn phương thức xử lý outliers phù hợp với dữ liệu và mục tiêu phân tích)
    - Label
    - One-Hot Encoding
- Categorical variable encoding (One-Hot Encoding, Label Encoding)
- Normalization and Standardization
- Feature selection (Chi-Square, Mutual Information, Recursive Feature Elimination)
- EDA (Exploratory Data Analysis)
- Dirty -> Dectect Outlier -> Transform -> Model -> Min-Max Scaling