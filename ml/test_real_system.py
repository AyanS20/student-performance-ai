from real_predictor import predict_student
from real_risk_engine import calculate_risk
from real_recommendations import generate_recommendations


# ==========================================
# TEST STUDENT
# ==========================================

attendance = 55
internal_test_1 = 15
internal_test_2 = 18
assignment_score = 3
study_hours = 1


# ==========================================
# PREDICTION
# ==========================================

predicted_score = predict_student(
    attendance,
    internal_test_1,
    internal_test_2,
    assignment_score,
    study_hours
)


# ==========================================
# RISK
# ==========================================

risk = calculate_risk(
    predicted_score,
    attendance,
    internal_test_1,
    internal_test_2,
    assignment_score,
    study_hours
)


# ==========================================
# RECOMMENDATIONS
# ==========================================

recommendations = generate_recommendations(
    predicted_score,
    attendance,
    internal_test_1,
    internal_test_2,
    assignment_score,
    study_hours
)


# ==========================================
# DISPLAY RESULT
# ==========================================

print("================================")
print("STUDENT PERFORMANCE RESULT")
print("================================")

print(
    "Predicted Final Exam Score:",
    predicted_score
)

print(
    "Risk Level:",
    risk["risk_level"]
)

print("\nRisk Reasons:")

for reason in risk["risk_reasons"]:

    print("-", reason)


print("\nRecommendations:")

for recommendation in recommendations:

    print("-", recommendation)