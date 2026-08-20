import pandas as pd

# ==========================================
# LOAD REAL KAGGLE DATASET
# ==========================================

file_path = "data/real_data/Final_Marks_Data.csv"

df = pd.read_csv(file_path)

print("==========================================")
print("REAL DATA PREPARATION")
print("==========================================")

# ==========================================
# SELECT FEATURES
# ==========================================

features = [
    "Attendance (%)",
    "Internal Test 1 (out of 40)",
    "Internal Test 2 (out of 40)",
    "Assignment Score (out of 10)",
    "Daily Study Hours"
]

target = "Final Exam Marks (out of 100)"

X = df[features]

y = df[target]

# ==========================================
# DISPLAY FEATURES
# ==========================================

print("\nFEATURES (X)")
print(X.head())

print("\nTARGET (y)")
print(y.head())

# ==========================================
# DISPLAY SHAPES
# ==========================================

print("\nX shape:")
print(X.shape)

print("\ny shape:")
print(y.shape)

# ==========================================
# CHECK MISSING VALUES
# ==========================================

print("\nMissing values in X:")
print(X.isnull().sum())

print("\nMissing values in y:")
print(y.isnull().sum())

# ==========================================
# SAVE PREPARED DATA
# ==========================================

prepared_df = X.copy()

prepared_df["final_score"] = y

output_file = "data/real_data/prepared_students.csv"

prepared_df.to_csv(
    output_file,
    index=False
)

print("\n==========================================")
print("DATA PREPARATION COMPLETE")
print("==========================================")

print(f"Prepared dataset saved to:")
print(output_file)