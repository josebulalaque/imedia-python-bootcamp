student_names = ("Juan", "Maria", "Joseph")
student_scores = (70, 90, 81)

# TODO: Print the student scores and names in the following format
""" 
    Student Records:
    Student: Juan scored 70 in the exam.
    Student: Maria scored 90 in the exam.
    Student: Joseph scored 81 in the exam.
"""

print("Student Records:")
for i in range(3):
    name = student_names[i]
    score = student_scores[i]
    print(f"Student: {name} scored {score} in the exam")

print("Student Records:")
for var1 in zip(student_names, student_scores):
    print(f"Student: {var1[0]} scored {var1[1]} in the exam")


comb = zip(student_names, student_scores)
print(list(comb))

