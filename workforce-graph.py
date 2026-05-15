def calculate_readiness_score(competency_scores):
    if not competency_scores:
        return 0

    total = sum(competency_scores.values())
    return round(total / len(competency_scores), 2)

def identify_strengths(competency_scores, threshold=80):
    return [
        competency
        for competency, score in competency_scores.items()
        if score >= threshold
    ]

def identify_growth_areas(competency_scores, threshold=70):
    return [
        competency
        for competency, score in competency_scores.items()
        if score < threshold
    ]

def recommend_next_step(growth_areas):
    if not growth_areas:
        return "Learner is ready for advanced simulation or certification readiness."

    recommendations = {
        "empathy": "Complete emotional regulation and caregiver communication missions.",
        "safety": "Practice safety and de-escalation scenarios.",
        "observation": "Complete behavior observation and trigger identification missions.",
        "reinforcement": "Review reinforcement and positive behavior support missions.",
        "communication": "Practice simple instruction and transition communication scenarios.",
        "documentation": "Complete documentation and supervision readiness missions."
    }

    first_area = growth_areas[0]
    return recommendations.get(first_area, "Complete targeted remediation missions.")

if __name__ == "__main__":
    sample_scores = {
        "empathy": 85,
        "safety": 78,
        "observation": 72,
        "reinforcement": 88,
        "communication": 80,
        "documentation": 65
    }

    readiness = calculate_readiness_score(sample_scores)
    strengths = identify_strengths(sample_scores)
    growth_areas = identify_growth_areas(sample_scores)
    next_step = recommend_next_step(growth_areas)

    print("Readiness Score:", readiness)
    print("Strengths:", strengths)
    print("Growth Areas:", growth_areas)
    print("Recommended Next Step:", next_step)
