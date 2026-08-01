# 🚗 DriveIntel

>![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)


 **AI-Powered Driving Maneuver Classification using Vehicle Motion Sensor Data**

DriveIntel is an end-to-end Machine Learning project that analyzes vehicle motion sensor data to classify driving maneuvers using accelerometer and gyroscope readings. The project demonstrates the complete data science workflow from SQL analysis and exploratory data analysis to statistical hypothesis testing, machine learning, and deployment using Streamlit.

---

## 📌 Business Problem

Fleet management companies continuously receive large amounts of sensor data from connected vehicles. Manually reviewing this data is impossible at scale.

The objective of this project is to automatically identify driving maneuvers from vehicle sensor readings, enabling fleet operators to better understand driver behavior without manually inspecting every trip.

DriveIntel predicts four driving maneuvers:

- 🚀 Sudden Acceleration
- ↪️ Sudden Right Turn
- ↩️ Sudden Left Turn
- 🛑 Sudden Brake

---

# 📂 Dataset

Source:
Kaggle - Driving Behavior Dataset

The project uses two datasets.

### 1. sensor_raw.csv

Contains raw accelerometer and gyroscope readings.

Features

- AccX
- AccY
- AccZ
- GyroX
- GyroY
- GyroZ

Target Classes

| Class | Driving Maneuver |
|-------|------------------|
| 1 | Sudden Acceleration |
| 2 | Sudden Right Turn |
| 3 | Sudden Left Turn |
| 4 | Sudden Brake |

---

### 2. features_14.csv

Contains engineered statistical features extracted from rolling sensor windows including:

- Mean
- Minimum
- Maximum
- Standard Deviation
- Variance
- Covariance
- Skewness
- Kurtosis

These engineered features provide richer temporal information than individual sensor readings.

---

# 🚀 Project Workflow

```
Business Understanding
        │
        ▼
Data Exploration
        │
        ▼
SQL Analysis
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Statistical Analysis
        │
        ▼
Machine Learning
        │
        ▼
Feature Importance
        │
        ▼
Streamlit Deployment
```

---

# 📊 Exploratory Data Analysis

EDA was performed to better understand the sensor measurements before model development.

The analysis included:

- Dataset inspection
- Missing value analysis
- Duplicate analysis
- Target distribution
- Feature distributions
- Boxplots
- Correlation Heatmap
- Pairplots
- Mean sensor values by driving class

Key findings:

- No missing values
- No duplicate records
- Classes are reasonably balanced
- Gyroscope measurements showed greater separation between driving maneuvers than accelerometer measurements.

---

# 🗄 SQL Analysis

SQLite was used to perform analytical queries on the raw sensor dataset.

Implemented SQL concepts:

- SELECT
- GROUP BY
- Aggregate Functions
- ORDER BY
- Window Functions
- Rolling Average

Example business questions answered:

- How does average acceleration differ across driving maneuvers?
- How does rotational motion vary across different driving behaviors?
- How do acceleration values evolve over time?

---

# 📈 Statistical Analysis

One-Way ANOVA was performed to determine whether sensor measurements differed significantly between driving maneuvers.

### Null Hypothesis

The average sensor values are identical across all driving behavior classes.

### Alternative Hypothesis

At least one driving behavior class differs significantly.

### Findings

- Acceleration intensity was not statistically significant.
- Rotation intensity showed strong statistical significance.

This suggests that rotational movement plays a major role in distinguishing driving maneuvers.

---

# 🤖 Machine Learning Models

Two machine learning models were trained.

### Logistic Regression

Used as a baseline classifier.

### Random Forest

Used to capture complex nonlinear relationships between sensor measurements.

Both models were trained on:

- Raw Sensor Features
- Engineered Statistical Features

---

# 📊 Model Performance

| Dataset | Model | Accuracy |
|---------|-------|----------|
| Raw Sensor Data | Logistic Regression | **43.5%** |
| Raw Sensor Data | Random Forest | **68.2%** |
| Engineered Features | Logistic Regression | **69.2%** |
| Engineered Features | **Random Forest** | **72.4%** |

The Random Forest trained on engineered statistical features achieved the highest performance.

---

# ⭐ Feature Importance

The Random Forest identified the following features as the most influential.

- GyroMeanZ
- AccMaxY
- GyroMinZ
- GyroStdZ
- GyroSumZ
- GyroMaxZ
- GyroVarZ
- GyroCovZ
- AccMaxX
- AccMeanY

These results indicate that rotational motion around the vertical axis (GyroZ) is highly informative for distinguishing different driving maneuvers.

---

# 💻 Streamlit Application

The project includes a Streamlit web application that allows users to:

- Upload engineered feature datasets
- Predict driving maneuvers
- Display maneuver distribution
- Generate session-level driving summaries

The application predicts:

- 🚀 Sudden Acceleration
- ↪️ Sudden Right Turn
- ↩️ Sudden Left Turn
- 🛑 Sudden Brake

---

# 📁 Project Structure

```
DriveIntel/

│
├── data/
│   ├── sensor_raw.csv
│   └── features_14.csv
│
├── models/
│   └── random_forest.pkl
│
├── notebooks/
│   ├── 01_Data_Exploration.ipynb
│   ├── 02_SQL_Analysis.ipynb
│   ├── 03_EDA.ipynb
│   ├── 04_Statistics.ipynb
│   └── 05_Model_Training.ipynb
│
├── reports/
│   └── figures/
│
├── sql/
│   ├── create_database.py
│   └── driveintel.db
│
├── app.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- SQLite
- Matplotlib
- Seaborn
- SciPy
- Scikit-Learn
- Streamlit
- Joblib

---

# 📌 Future Improvements

Potential enhancements include:

- Driver risk scoring based on complete trips
- Hyperparameter tuning
- Cross-validation
- XGBoost implementation
- Real-time sensor streaming
- Cloud deployment
- Fleet dashboard for multiple vehicles

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Harshal Tupke**

Electrical and Computer Science Engineering

VIT Vellore