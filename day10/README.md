# Day 10

## Data Science lifecycle

The Data Science lifecycle consists of several key stages that guide the process of extracting insights and knowledge from data. Here are the main stages:

1. **Problem Definition**: Clearly define the problem you want to solve or the question you want to answer using data.
2. **Data Collection**: Gather the necessary data from various sources, which may include databases, APIs, web scraping, or surveys.
3. **Data Cleaning and Preprocessing**: Prepare the data for analysis by handling missing values, removing duplicates, and transforming data into a suitable format.
4. **Exploratory Data Analysis (EDA)**: Analyze the data to understand its structure, patterns, and relationships. This may involve visualizations and statistical summaries.
5. **Feature Engineering**: Create new features or modify existing ones to improve the performance of
    machine learning models.
6. **Model Selection and Training**: Choose appropriate machine learning algorithms and train models using the prepared data.
7. **Model Evaluation**: Assess the performance of the trained models using metrics such as accuracy
    , precision, recall, and F1-score.
8. **Model Deployment**: Implement the model in a production environment where it can make predictions on new data.
9. **Monitoring and Maintenance**: Continuously monitor the model's performance and update it as needed to ensure it remains effective over time.
10. **Communication and Reporting**: Present the findings and insights to stakeholders through reports, dashboards, or presentations.

Understanding and following these stages helps ensure a systematic approach to data science projects, leading to more reliable and actionable results.

## Types of Constraints

Constraints Type and examples:

1. **Equality Constraints**: These constraints require that a certain condition be exactly met.
   - Example: \( x + y = 10 \)
2. **Inequality Constraints**: These constraints specify that a condition must be greater than or less than a certain value.
   - Example: \( x - y \leq 5 \)
3. **Bound Constraints**: These constraints limit the values that a variable can take within a specific range.
   - Example: \( 0 \leq x \leq 100 \)
4. **Integer Constraints**: These constraints require that certain variables take on only integer values.
   - Example: \( x \in \mathbb{Z} \)
5. **Logical Constraints**: These constraints involve logical relationships between variables.
   - Example: If \( x > 5 \), then \( y = 10 \)
6. **Non-negativity Constraints**: These constraints require that variables be non-negative.
   - Example: \( x \geq 0 \)
7. **Cardinality Constraints**: These constraints limit the number of variables that can take on non-zero values.
   - Example: At most 3 variables can be non-zero in a solution.
8. **Resource Constraints**: These constraints limit the use of resources such as time, money, or materials.
   - Example: The total cost must not exceed $1000.
9. **Time Constraints**: These constraints specify deadlines or time limits for completing tasks or processes.
    - Example: A project must be completed within 30 days.
10. **Spatial Constraints**: These constraints involve the physical location or arrangement of objects.
    - Example: Facilities must be located within a certain distance from each other.

Understanding these types of constraints is essential for formulating and solving optimization problems effectively.

## Collect, Clean and Preproces data

# Key data preprocessing steps

Following these steps helps ensure that the data is clean, consistent, and ready for analysis or modeling.

## 1. Data Collection

## 2. Data Cleaning

- Handle missing vaules (drop, simple imputation, advanced imputation) and inconsistencies format
- Numerical: mean, median, mode, interpolation
- Categorical: mode, constant value
- Time-Series: forward fill, backward fill

## 3. Handling Missing Values

- Missing data can bias model outcomes
- Choice of method depends on data type, amount of missing data, and analysis goals
- Avoid blindly dropping rows/columns with missing data
- Techniques:
  - Remove rows/columns with missing data
  - Simple imputation (mean, median, mode)
  - Forward fill, backward fill for time-series

## 4. Data Preprocessing

- Transformation: Normalization, Standardization
- Encoding: Converting categorical text into numbers
  - Ex: One-hot encoding (sparse matrices), Label encoding (for tree models), Target encoding (for high cardinality)
- Feature Engineering: Creating new features from existing data

## 5. Process Data

Encoding categorical data

## Exporatory Data Analysis (EDA)

### Key EDA Techniques

1. **Descriptive Statistics**: Calculate mean, median, standard deviation, and quartiles
2. **Data Visualization**: Create histograms, box plots, scatter plots, and heatmaps
3. **Correlation Analysis**: Identify relationships between variables
4. **Distribution Analysis**: Examine the shape and spread of data
5. **Outlier Detection**: Identify and analyze unusual values
6. **Missing Data Patterns**: Understand the extent and nature of missing values
7. **Feature Relationships**: Explore interactions and dependencies between features
8. **Categorical Analysis**: Examine value counts and proportions

### EDA Workflow

```
Raw Data
    ↓
Summary Statistics
    ↓
Visualizations
    ↓
Pattern Discovery
    ↓
Insights & Decisions
```

Typical EDA techniques include

## Data Splitting

- Common ratios: 70/30, 80/20, 60/20/20
- 2 ways to split data (Simple): 70% train, 30% test
- 3 ways to split data (Advanced): 60% train, 20% validation
- Used for simpler models

## Model Training

- Choose model Families based on problem type (Regression, Classification, Clustering)
- Train model on training data
- Tune hyperparameters using validation data
- Evaluate final model on test data
- Techniques: Cross-validation, Grid search, Random search
- Metrics: Accuracy, Precision, Recall, F1-score for classification; RMSE, MAE for regression
- Avoid overfitting and underfitting
- Overfitting: Model performs well on training data but poorly on test data

The machine learning training process

## Translate business goals in to ML task

Step 1: Understand the Business Goal

- Clearly articulate the business objective
- Idenitfy the decision that needs improvement
- Define success criteria
- Align the goal with measurable KPIs
- Ask why the problem matters to the business

Step 2: Convert Goal into a Predictable Outcome

- ML requires a specific outcome to predict or analyze
- Convert vague goals into clear questions
- Outcomes must be measurable and data-driven

Step 3: Choose the Right ML Task

- Match the outcome to an appropriate ML task
- Selecting the correct task is crucial for effective modeling

Step 4: Define Input and Output Variables

- ML model learn from features (input variables) to predict target (output variable)
- Features come from historical data relevant to the problem
- Labels represent the outcome to predict
- This step often reveals data gaps or quality issues

Step 5: Define Success Metrics

- Business success metrics translate into ML performance metrics
- ML metrics must align with business objectives
- Choose metrics that reflect the impact on the business goal
- Different problems reqiuire different metrics (e.g., accuracy, precision, recall, F1-score, RMSE)

Step 6: Consider Constraints and Feasibility

- Data availability: Ensure necessary data is accessible and of good quality

## Machine Learning Lifecycle

Business Goal -> ML Problem Framing -> Data Processing -> Model Development -> Deployment -> Monitoring & Maintenance -> Feedback Loop

## Why Selecting the Right Problem Type matters

- Different ML problem types require different algorithms and approaches
- Misalignment can lead to poor model performance and wasted resources
- Correct problem framing ensures the model addresses the business need effectively

## Classification

## Regression

## Clustering

## How to Choose the Right ML Problem Type

Quick Decision Table:

| Business Goal Type          | ML Problem Type   | Example                                   |
|-----------------------------|-------------------|-------------------------------------------|
| Predicting categories       | Classification    | Spam detection, Fraud detection           |
| Predicting continuous values| Regression        | House price prediction, Sales forecasting |
| Grouping similar items      | Clustering        | Customer segmentation, Market basket analysis |
Considerations:

- Nature of the target variable (categorical vs continuous)
- Business context and objectives
- Data availability and quality

## Best Practices to Anticipate Challenges

- Perform data audit before model building
- Start with a baseline dataset
- Automate data validation checks
- Plan for continuous monitoring retainning