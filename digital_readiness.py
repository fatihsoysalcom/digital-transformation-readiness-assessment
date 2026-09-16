import json

def assess_digital_readiness(company_data):
    """Assesses a company's digital transformation readiness based on provided data."""
    score = 0
    feedback = []

    # Factor 1: Investment in Technology (Cost Concern)
    if company_data.get('tech_investment_percentage', 0) > 5:
        score += 2
        feedback.append("Strong investment in technology.")
    elif company_data.get('tech_investment_percentage', 0) > 2:
        score += 1
        feedback.append("Moderate investment in technology.")
    else:
        feedback.append("Low investment in technology. Consider increasing budget.")

    # Factor 2: Employee Adaptability (Cultural Resistance)
    if company_data.get('employee_training_hours_per_year', 0) > 20:
        score += 2
        feedback.append("High investment in employee digital training.")
    elif company_data.get('employee_training_hours_per_year', 0) > 10:
        score += 1
        feedback.append("Some investment in employee digital training.")
    else:
        feedback.append("Limited employee digital training. Focus on upskilling.")

    # Factor 3: Existing System Modernization (Technological Competence)
    if company_data.get('legacy_system_percentage', 0) < 30:
        score += 2
        feedback.append("Modernized existing systems.")
    elif company_data.get('legacy_system_percentage', 0) < 60:
        score += 1
        feedback.append("Some legacy systems remain.")
    else:
        feedback.append("Significant reliance on legacy systems. Prioritize modernization.")

    # Factor 4: Leadership Vision (Strategic Alignment)
    if company_data.get('digital_strategy_defined', False):
        score += 2
        feedback.append("Clear digital transformation strategy defined.")
    else:
        feedback.append("Digital strategy needs to be clearly defined.")

    # Determine readiness level
    if score >= 6:
        readiness = "High Readiness"
    elif score >= 3:
        readiness = "Medium Readiness"
    else:
        readiness = "Low Readiness"

    return {
        "readiness_level": readiness,
        "score": score,
        "feedback": feedback
    }

if __name__ == "__main__":
    # Example company data (replace with actual data)
    # This simulates the data points that might cause delays in digital transformation.
    company_profile_1 = {
        "tech_investment_percentage": 3,
        "employee_training_hours_per_year": 15,
        "legacy_system_percentage": 70,
        "digital_strategy_defined": False
    }

    company_profile_2 = {
        "tech_investment_percentage": 8,
        "employee_training_hours_per_year": 30,
        "legacy_system_percentage": 20,
        "digital_strategy_defined": True
    }

    print("--- Company 1 Readiness Assessment ---")
    assessment_1 = assess_digital_readiness(company_profile_1)
    print(json.dumps(assessment_1, indent=2))

    print("\n--- Company 2 Readiness Assessment ---")
    assessment_2 = assess_digital_readiness(company_profile_2)
    print(json.dumps(assessment_2, indent=2))
