# 💰 Product Price Prediction using XGBoost

An end-to-end Machine Learning project that predicts the price of an e-commerce product based on its category, discount percentage, customer ratings, and review count. The model is trained using XGBoost and deployed through an interactive Streamlit web application.

---

## 📌 Project Overview

Pricing plays a crucial role in e-commerce platforms. This project aims to predict product prices by analyzing key product attributes and learning patterns from historical data.

The project covers the complete Machine Learning workflow, including:

- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training using XGBoost
- Model Evaluation
- Model Serialization
- Streamlit-based Deployment

---

## 🎯 Problem Statement

Given product information such as:

- Product Subcategory
- Discount Percentage
- Product Rating
- Number of Reviews

predict the expected selling price of the product.

---

## 📊 Dataset Features

| Feature | Description |
|----------|------------|
| Subcategory | Product category |
| Discount | Discount percentage offered |
| Rating | Average customer rating |
| Review Count | Total number of customer reviews |

### Target Variable

| Variable | Description |
|----------|------------|
| Price | Product selling price |

---

## 🔍 Exploratory Data Analysis (EDA)

Before training the model, a comprehensive Exploratory Data Analysis (EDA) was performed to understand the dataset and identify factors affecting product prices.

### Analysis Performed

- Distribution analysis of product prices
- Category-wise price comparison
- Discount vs Price relationship analysis
- Rating vs Price analysis
- Review Count vs Price analysis
- Correlation analysis between numerical features
- Detection of trends, patterns, and outliers

### Key Insights

- Product subcategory significantly influences price.
- Higher-rated products tend to have higher prices.
- Review count provides useful information about product popularity.
- Discount percentage impacts the final selling price.
- Different categories exhibit distinct pricing patterns.

The insights obtained during EDA helped in selecting relevant features and improving model performance.

---

## ⚙️ Machine Learning Pipeline

### 1. Data Preprocessing

- Selected relevant features
- Handled categorical data using Ordinal Encoding
- Prepared training and testing datasets

### 2. Train-Test Split

The dataset was divided into:

- 85% Training Data
- 15% Testing Data

### 3. Model Training

The model was trained using:

```python
XGBRegressor()
```

### 4. Model Evaluation

Performance was evaluated using:

- R² Score
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

### 5. Model Serialization

The trained model and category mappings were saved using Pickle for deployment.

---

## 🚀 Features

- Interactive Streamlit Web Application
- Real-Time Price Prediction
- XGBoost Regression Model
- Category Encoding Support
- Clean User Interface
- Deployment Ready
- End-to-End ML Workflow

---

## 🛠️ Tech Stack

### Programming Language

- Python

### Libraries & Frameworks

- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- Streamlit
- Pickle

### Tools

- Jupyter Notebook
- Git
- GitHub

---

## 📂 Project Structure

```text
product-price-prediction/
│
├── app.py
├── notebook.ipynb
├── xgboost_price_model.pkl
├── subcategory_map.pkl
├── requirements.txt
├── README.md
│
└── screenshots/
    ├── homepage.png
    └── prediction.png
```
## Dataset

The dataset used for this project is not included in this repository due to its size.

Dataset features:
- Subcategory
- Price
- Discount
- Rating
- Review Count

The notebook and application can be adapted to any dataset with a similar schema.
---

## ▶️ Installation & Setup

### Clone the Repository

```bash
git clone https://github.com/your-username/product-price-prediction.git
```

### Navigate to the Project Directory

```bash
cd product-price-prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit Application

```bash
streamlit run app.py
```

---

## 🖥️ Application Workflow

1. Select a Product Subcategory
2. Enter Discount Percentage
3. Enter Product Rating
4. Enter Review Count
5. Click **Predict Price**
6. View the Predicted Product Price

---


## 📈 Model Performance

| Metric | Score |
|----------|----------|
| R² Score | Add Your Score |
| MAE | Add Your Score |
| RMSE | Add Your Score |

---

## 🎓 Learning Outcomes

This project helped me gain practical experience in:

- Exploratory Data Analysis (EDA)
- Data Visualization
- Feature Engineering
- Categorical Encoding
- Regression Modeling
- XGBoost
- Model Evaluation
- Model Serialization
- Streamlit Deployment
- Git & GitHub Project Management

---

## 🔮 Future Improvements

- Hyperparameter Tuning
- Feature Importance Visualization
- Comparison with Random Forest and LightGBM
- Cloud Deployment
- Improved UI/UX
- Real-Time Product Data Integration
- Automated Retraining Pipeline

---

## 👩‍💻 Author

**Sneha Karkoli**

Aspiring AI/ML Engineer with interests in:

- Machine Learning
- Deep Learning
- Natural Language Processing (NLP)
- Generative AI
- Retrieval-Augmented Generation (RAG)

---

## ⭐ Support

If you found this project interesting, consider giving it a ⭐ on GitHub.

Feedback and suggestions are always welcome!