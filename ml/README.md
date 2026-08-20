# Student Performance ML Module

## Project Overview

This module predicts a student's **Final Exam Marks** using real student performance data.

The dataset used for the final project was obtained from Kaggle and contains 2,000 student records.

The ML module also includes an **Early Warning System** that identifies students who may be at academic risk and provides recommendations.

---

## Dataset

The real dataset contains the following information:

* Student ID
* Attendance (%)
* Internal Test 1 score (out of 40)
* Internal Test 2 score (out of 40)
* Assignment Score (out of 10)
* Daily Study Hours
* Final Exam Marks (out of 100)

### Dataset Size

* Total records: **2,000**
* Input features: **5**
* Target variable: **Final Exam Marks**

---

## Machine Learning Model

Five regression models were tested:

1. Linear Regression
2. Decision Tree
3. Random Forest
4. Gradient Boosting
5. XGBoost

### Best Model

**Linear Regression** was selected as the best-performing model based on the test results.

### Model Performance

| Metric   | Result |
| -------- | -----: |
| MAE      |  3.675 |
| RMSE     |  4.618 |
| R² Score |  0.830 |

The model was trained using 80% of the dataset and tested using the remaining 20%.

---

## Input Features

The prediction model uses these five features:

* `Attendance (%)`
* `Internal Test 1 (out of 40)`
* `Internal Test 2 (out of 40)`
* `Assignment Score (out of 10)`
* `Daily Study Hours`

---

## Prediction Output

The prediction system returns:

* Predicted Final Exam Score
* Risk Level
* Risk Reasons
* Recommendations

### Risk Levels

| Risk Level | Predicted Score |
| ---------- | --------------- |
| LOW        | 65 or above     |
| MEDIUM     | 50 to below 65  |
| HIGH       | Below 50        |

The system also checks academic factors such as attendance, internal test performance, assignment performance, and daily study hours.

---

## Early Warning System

The system identifies potential risk factors including:

* Low attendance
* Low Internal Test 1 performance
* Low Internal Test 2 performance
* Low assignment performance
* Low daily study hours

Based on these factors, the system generates recommendations such as:

* Improve class attendance
* Focus on internal test topics
* Complete assignments regularly
* Increase daily study consistency
* Consider speaking with a faculty advisor for academic support

---

## Main Files

### Data Preparation

`prepare_real_data.py`

Prepares the real dataset for machine learning.

### Data Analysis

`real_data_analysis.py`

Performs exploratory analysis and calculates correlations between input features and final exam marks.

### Model Training

`train_real_models.py`

Trains and compares the five machine learning models and saves the best model.

### Trained Model

`real_student_model.pkl`

Saved Linear Regression model used for predictions.

### Prediction

`real_predictor.py`

Loads the trained model and predicts a student's final exam score.

### Risk Engine

`real_risk_engine.py`

Determines the student's risk level and identifies risk factors.

### Recommendations

`real_recommendations.py`

Generates recommendations based on the student's performance.

### System Test

`test_real_system.py`

Tests the complete prediction, risk detection, and recommendation system.

---

## Data Files

The real-data files are stored in:

```text
data/real_data/
```

Important files include:

```text
Final_Marks_Data.csv
prepared_students.csv
graphs/
```

---

## How to Run

Make sure the Python virtual environment is activated.

From the project root:

```powershell
python ml/real_data_analysis.py
```

To prepare the data:

```powershell
python ml/prepare_real_data.py
```

To train the models:

```powershell
python ml/train_real_models.py
```

To test the complete prediction and early warning system:

```powershell
python ml/test_real_system.py
```

---

## Example

### Student Input

```text
Attendance: 85
Internal Test 1: 32
Internal Test 2: 34
Assignment Score: 8
Study Hours: 3
```

### Prediction

```text
Predicted Final Exam Score: 67.41
Risk Level: LOW
```

### At-Risk Example

```text
Attendance: 55
Internal Test 1: 15
Internal Test 2: 18
Assignment Score: 3
Study Hours: 1
```

The system identifies multiple risk factors and classifies the student as:

```text
Risk Level: HIGH
```

---

## Module Status

**Status: Completed for ML and Early Warning System integration**

The module is ready to be integrated with the project's backend and frontend components.
