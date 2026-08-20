import pandas as pd
import matplotlib.pyplot as plt
import os

# ==========================================
# REAL KAGGLE DATASET ANALYSIS
# ==========================================

# Load dataset
file_path = "data/real_data/Final_Marks_Data.csv"

df = pd.read_csv(file_path)

print("==========================================")
print("REAL STUDENT PERFORMANCE DATASET")
print("==========================================")

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# ==========================================
# CORRELATION WITH FINAL EXAM MARKS
# ==========================================

target = "Final Exam Marks (out of 100)"

numeric_df = df.select_dtypes(include="number")

correlation = numeric_df.corr()[target].sort_values(
    ascending=False
)

print("\n==========================================")
print("CORRELATION WITH FINAL EXAM MARKS")
print("==========================================")

print(correlation)

# ==========================================
# CREATE GRAPH FOLDER
# ==========================================

graph_folder = "data/real_data/graphs"

os.makedirs(graph_folder, exist_ok=True)

# ==========================================
# GRAPH 1: ATTENDANCE VS FINAL MARKS
# ==========================================

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Attendance (%)"],
    df[target]
)

plt.xlabel("Attendance (%)")
plt.ylabel("Final Exam Marks")
plt.title("Attendance vs Final Exam Marks")

plt.savefig(
    f"{graph_folder}/attendance_vs_final.png"
)

plt.close()

# ==========================================
# GRAPH 2: STUDY HOURS VS FINAL MARKS
# ==========================================

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Daily Study Hours"],
    df[target]
)

plt.xlabel("Daily Study Hours")
plt.ylabel("Final Exam Marks")
plt.title("Study Hours vs Final Exam Marks")

plt.savefig(
    f"{graph_folder}/study_hours_vs_final.png"
)

plt.close()

# ==========================================
# GRAPH 3: INTERNAL TEST 1 VS FINAL MARKS
# ==========================================

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Internal Test 1 (out of 40)"],
    df[target]
)

plt.xlabel("Internal Test 1")
plt.ylabel("Final Exam Marks")
plt.title("Internal Test 1 vs Final Exam Marks")

plt.savefig(
    f"{graph_folder}/internal_test1_vs_final.png"
)

plt.close()

# ==========================================
# GRAPH 4: INTERNAL TEST 2 VS FINAL MARKS
# ==========================================

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Internal Test 2 (out of 40)"],
    df[target]
)

plt.xlabel("Internal Test 2")
plt.ylabel("Final Exam Marks")
plt.title("Internal Test 2 vs Final Exam Marks")

plt.savefig(
    f"{graph_folder}/internal_test2_vs_final.png"
)

plt.close()

print("\n==========================================")
print("ANALYSIS COMPLETE")
print("==========================================")

print(
    f"Graphs saved in: {graph_folder}"
)