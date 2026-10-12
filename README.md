# 🚗 Used Car Price Prediction

A Machine Learning web application that estimates the resale price of used cars using regression algorithms and Streamlit.

## 🌐 Live Demo

🚀 **[Try the Live Application](https://used-car-price-prediction-hftmbquztczbn2kf8jsfva.streamlit.app/)**

## 📌 Project Overview

This project predicts the estimated selling price of a used car based on its specifications, including manufacturing year, kilometers driven, fuel type, transmission, mileage, engine capacity, maximum power, previous owner, and number of seats.

It covers data preprocessing, feature engineering, model training, evaluation, and deployment as an interactive web application.

## ✨ Key Features

- Predicts estimated used car resale prices.
- Interactive Streamlit web interface.
- Accepts multiple car specifications as input.
- Displays the estimated selling price and car summary.
- Deployed online using Streamlit Community Cloud.

## 🛠️ Technologies Used

- **Language:** Python
- **Data Processing:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Web Framework:** Streamlit
- **Model Serialization:** Joblib
- **Tools:** Jupyter Notebook, VS Code, Git, GitHub

## 🤖 Machine Learning Models

Four regression algorithms were implemented and evaluated:

- **Linear Regression** — Baseline regression model.
- **Lasso Regression** — Regularized linear regression.
- **Decision Tree Regressor** — Captures nonlinear relationships.
- **Random Forest Regressor** — Selected final model based on test performance.

## 📊 Model Performance

The selected Random Forest Regressor achieved the following results:

| Metric | Result |
|---|---:|
| Training R² Score | 96.65% |
| Test R² Score | 92.76% |
| Test MAE | Approximately ₹73,267 |

*Note: Results are from a single train-test split. Predictions are estimates, not guaranteed market prices.*

## 🔄 Workflow

1. Dataset exploration and data cleaning.
2. Handling missing values and duplicate records.
3. Feature engineering and categorical encoding.
4. Train-test split.
5. Training and comparing four regression models.
6. Evaluating models using R² Score and MAE.
7. Saving the selected model using Joblib.
8. Building and deploying the Streamlit application.

## 📂 Project Structure

```text
Used-Car-Price-Prediction/
├── app.py
├── car_price_model.pkl
├── model_columns.pkl
├── car_hero_image.png
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Usage

### 1. Clone the repository

```bash
git clone https://github.com/AkshatNigam06/Used-Car-Price-Prediction.git
```

### 2. Navigate to the project folder

```bash
cd Used-Car-Price-Prediction
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The app will open in your browser. Enter the car specifications to obtain an estimated resale price.

## 🎥 Project Demo

![Used Car Price Prediction Demo](./used-car-price-prediction-preview.gif)

▶️ [Watch the Full Demo Video](./used-car-price-prediction-demo.mp4)

🌐 [Try the Live Application](https://used-car-price-prediction-hftmbquztczbn2kf8jsfva.streamlit.app/)

## 🚀 Deployment

Deployed using **Streamlit Community Cloud**.

🔗 **[Open Live Application](https://used-car-price-prediction-hftmbquztczbn2kf8jsfva.streamlit.app/)**

## 🎯 Key Learnings

- Data preprocessing and feature engineering
- Regression model training and comparison
- Model evaluation using R² Score and MAE
- Saving and loading models using Joblib
- Building and deploying ML applications with Streamlit

## 👨‍💻 Author

**Akshat Nigam**

Computer Science Student | Aspiring Data Analyst

Interested in Data Analytics, Machine Learning, Python, and SQL.

---

⭐ If you find this project useful, consider giving the repository a star!
