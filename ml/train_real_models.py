import pandas as pd
import joblib

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

from xgboost import XGBRegressor


# ==========================================
# LOAD PREPARED REAL DATA
# ==========================================

file_path = "data/real_data/prepared_students.csv"

df = pd.read_csv(file_path)

print("==========================================")
print("REAL DATA ML TRAINING")
print("==========================================")


# ==========================================
# FEATURES AND TARGET
# ==========================================

features = [
    "Attendance (%)",
    "Internal Test 1 (out of 40)",
    "Internal Test 2 (out of 40)",
    "Assignment Score (out of 10)",
    "Daily Study Hours"
]

X = df[features]

y = df["final_score"]


# ==========================================
# TRAIN / TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


print("\nTRAINING DATA")
print("X_train:", X_train.shape)
print("y_train:", y_train.shape)

print("\nTESTING DATA")
print("X_test:", X_test.shape)
print("y_test:", y_test.shape)


# ==========================================
# CREATE MODELS
# ==========================================

models = {

    "Linear Regression":
        LinearRegression(),

    "Decision Tree":
        DecisionTreeRegressor(
            random_state=42
        ),

    "Random Forest":
        RandomForestRegressor(
            n_estimators=200,
            random_state=42
        ),

    "Gradient Boosting":
        GradientBoostingRegressor(
            random_state=42
        ),

    "XGBoost":
        XGBRegressor(
            n_estimators=200,
            max_depth=4,
            learning_rate=0.05,
            random_state=42,
            objective="reg:squarederror"
        )
}


# ==========================================
# TRAIN MODELS
# ==========================================

results = []


for name, model in models.items():

    print(f"\nTraining {name}...")

    model.fit(
        X_train,
        y_train
    )

    predictions = model.predict(
        X_test
    )

    mae = mean_absolute_error(
        y_test,
        predictions
    )

    rmse = mean_squared_error(
        y_test,
        predictions
    ) ** 0.5

    r2 = r2_score(
        y_test,
        predictions
    )

    results.append({
        "Model": name,
        "MAE": round(mae, 3),
        "RMSE": round(rmse, 3),
        "R2": round(r2, 3)
    })


# ==========================================
# MODEL COMPARISON
# ==========================================

results_df = pd.DataFrame(results)

print("\n==========================================")
print("MODEL COMPARISON")
print("==========================================")

print(results_df.to_string(index=False))


# ==========================================
# FIND BEST MODEL
# ==========================================

best_index = results_df["R2"].idxmax()

best_model_name = results_df.loc[
    best_index,
    "Model"
]

best_model = models[
    best_model_name
]


print("\n==========================================")
print("BEST MODEL")
print("==========================================")

print(
    "Model:",
    best_model_name
)

print(
    results_df.loc[
        best_index
    ]
)


# ==========================================
# SAVE BEST MODEL
# ==========================================

output_file = "ml/real_student_model.pkl"

joblib.dump(
    best_model,
    output_file
)


print("\nBest real-data model saved successfully!")

print(
    "File:",
    output_file
)