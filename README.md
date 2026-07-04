# 🏠 Bengaluru House Price Prediction

## 📌 Project Overview

This project predicts house prices in Bengaluru using Machine Learning. The model is trained on the Bengaluru House Price dataset and deployed with Streamlit, allowing users to enter house details and receive an estimated price.

---

## 🚀 Features

- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Multiple Machine Learning Models
- Model Comparison
- House Price Prediction
- Streamlit Web Application

---

## 📂 Dataset

The dataset contains information about houses in Bengaluru, including:

- Area Type
- Availability
- Location
- Total Square Feet
- Number of Bedrooms (BHK)
- Bathrooms
- Balcony
- Price (Target Variable)

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Pickel
- Streamlit

---

## 🤖 Machine Learning Models

The following regression models were trained and compared:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

### Model Performance

| Model | R² Score | MAE | RMSE |
|--------|---------:|----:|------:|
| Linear Regression | 0.488 | 44.33 | 88.99 |
| Decision Tree Regressor | 0.235 | 39.87 | 108.72 |
| **Random Forest Regressor** | **0.557** | **31.60** | **82.77** |

**Selected Model:** Random Forest Regressor

---

## 📊 Project Workflow

1. Import Dataset
2. Data Cleaning
3. Handle Missing Values
4. Feature Engineering
5. Encoding Categorical Variables
6. Train-Test Split
7. Model Training
8. Model Evaluation
9. Save the Best Model
10. Deploy with Streamlit

---

## 📁 Project Structure

```
Bengaluru-House-Price-Prediction/
│
├── app.py
├── Bengaluru_House_Data.csv
├── House_Price_Prediction.ipynb
├── house_price_model.pkl
├── labelel.pkl
├── requirements.txt

```

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Bengaluru-House-Price-Prediction.git
```

Move into the project folder:

```bash
cd Bengaluru-House-Price-Prediction
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```
## 📷 Application

The Streamlit application allows users to:

- Enter house details
- Predict Bengaluru house prices instantly
- Get an estimated price using the trained Random Forest model

---
**Rahul**

If you found this project useful, feel free to ⭐ this repository.
