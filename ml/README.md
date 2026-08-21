# 🎓 Student Performance AI & Early Warning System

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-Learn" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy" />
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" alt="Status" />
</p>

An intelligent machine learning module designed to predict student **Final Exam Marks** and identify academic vulnerability via an integrated **Early Warning System (EWS)**.

---

## 📌 Project Overview

* **Dataset:** 2,000 real student records sourced from Kaggle.
* **Goal:** Predict final exam outcomes and trigger proactive, actionable recommendations for at-risk students.
* **Split:** 80% Training | 20% Testing.

---

## 🚀 Model Architecture & Performance

Five distinct regression models were evaluated:
1. **Linear Regression (Selected)**
2. Decision Tree
3. Random Forest
4. Gradient Boosting
5. XGBoost

| Metric | Score |
| :--- | :--- |
| **MAE** | 3.675 |
| **RMSE** | 4.618 |
| **R² Score** | 0.830 |

---

## ⚙️ How It Works

### 1. Input Features
* `Attendance (%)`
* `Internal Test 1 (out of 40)`
* `Internal Test 2 (out of 40)`
* `Assignment Score (out of 10)`
* `Daily Study Hours`

### 2. Risk Classification

| Risk Level | Score Threshold | System Action |
| :--- | :--- | :--- |
| 🟢 **LOW** | $\ge$ 65 | On-track confirmation |
| 🟡 **MEDIUM** | 50 – 64.9 | Targeted improvement notices |
| 🔴 **HIGH** | < 50 | Academic risk alert + Advisor intervention flag |

---

## 📁 Repository Structure

```text
├── data/
│   └── real_data/
│       ├── Final_Marks_Data.csv
│       ├── prepared_students.csv
│       └── graphs/
├── ml/
│   ├── prepare_real_data.py      # Cleans and preprocesses data
│   ├── real_data_analysis.py    # Exploratory data analysis & correlations
│   ├── train_real_models.py     # Trains & validates models
│   ├── real_predictor.py        # Inference pipeline
│   ├── real_risk_engine.py      # Identifies key risk factors
│   ├── real_recommendations.py  # Generates actionable guidance
│   └── test_real_system.py      # End-to-end integration test
└── real_student_model.pkl       # Serialized production model
