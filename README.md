# Live Demo https://bmiabhinav.streamlit.app/

# 🩺 BMI Health Classification

A Machine Learning project that predicts a BMI category using **Gender, Height, and Weight**.

## 📌 About the Project

This project uses a classification model to predict one of six BMI-related categories based on basic body measurements.

### Input Features

- 👤 Gender
- 📏 Height (cm)
- ⚖️ Weight (kg)

### 🎯 BMI Categories

| Class | Category |
|------:|----------|
| 0 | Extremely Weak |
| 1 | Weak |
| 2 | Normal |
| 3 | Overweight |
| 4 | Obesity |
| 5 | Extreme Obesity |

## 🤖 Machine Learning

The project uses a preprocessing workflow that:

1. Encodes the categorical **Gender** feature.
2. Standardizes **Height** and **Weight**.
3. Passes the transformed features to the trained classification model.
4. Predicts the BMI category.

The trained model and scaler are saved as `.joblib` files and are used by the Streamlit application.

## 🖥️ Web Application

The project includes a Streamlit interface where users can:

- Select their gender
- Select their height
- Select their weight
- Get a predicted BMI category

## 📂 Project Structure

```text
bmi_health_classification/
│
├── bmi_model.joblib
├── data_scaler.joblib
├── model_creation_ntbk.ipynb
├── ui.py
└── README.md
