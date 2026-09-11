def generate_recommendations(missing_skills):

    recommendations = []

    for skill in missing_skills:

        if skill == "python":
            recommendations.append(
                "Learn Python fundamentals and practice with small projects."
            )

        elif skill == "machine learning":
            recommendations.append(
                "Learn supervised and unsupervised machine learning."
            )

        elif skill == "scikit-learn":
            recommendations.append(
                "Practice ML models using Scikit-learn."
            )

        elif skill == "sql":
            recommendations.append(
                "Practice SQL queries, joins and aggregation."
            )

        elif skill == "statistics":
            recommendations.append(
                "Study probability, distributions and basic statistics."
            )

        elif skill == "tensorflow":
            recommendations.append(
                "Learn TensorFlow fundamentals and neural networks."
            )

        elif skill == "deep learning":
            recommendations.append(
                "Learn neural networks, CNNs and deep learning basics."
            )

        elif skill == "data analysis":
            recommendations.append(
                "Practice Pandas, NumPy and data visualization."
            )

        else:
            recommendations.append(
                f"Learn the fundamentals of {skill}."
            )

    return recommendations