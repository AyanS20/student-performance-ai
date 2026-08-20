def calculate_risk(
    predicted_score,
    attendance,
    internal_test_1,
    internal_test_2,
    assignment_score,
    study_hours
):

    reasons = []

    # Attendance
    if attendance < 75:
        reasons.append("Low attendance")

    # Internal tests
    if internal_test_1 < 20:
        reasons.append("Low Internal Test 1 performance")

    if internal_test_2 < 20:
        reasons.append("Low Internal Test 2 performance")

    # Assignment
    if assignment_score < 5:
        reasons.append("Low assignment performance")

    # Study hours
    if study_hours < 2:
        reasons.append("Low daily study hours")

    # Predicted final score
    if predicted_score < 50:

        risk_level = "HIGH"

    elif predicted_score < 65:

        risk_level = "MEDIUM"

    else:

        risk_level = "LOW"

    # No reasons
    if len(reasons) == 0:

        reasons.append(
            "No major risk factors detected"
        )

    return {
        "risk_level": risk_level,
        "risk_reasons": reasons
    }