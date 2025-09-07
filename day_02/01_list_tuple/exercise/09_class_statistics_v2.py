student_scores = [98, 75, 100, 86, 100, 3]

# TODO: Print the average score
average_score = sum(student_scores) / len(student_scores)
print(f"AVERAGE SCORE: {average_score}")

# TODO: Print the rankings, highest to lowest
print(f"SCORES: {student_scores}")
print(f"ASCENDING: {sorted(student_scores)}")
print(f"DESCENDING: {sorted(student_scores, reverse=True)}")
