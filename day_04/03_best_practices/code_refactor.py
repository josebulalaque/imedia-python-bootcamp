
def grades_add(grd):
    """add function"""
    subject = input("Subject: ")
    score = float(input("Score: "))
    grd.append({"subject": subject, "score": score})
    print("Grade added!")

def grades_avg(grd):
    """view function"""
    if grd:
        total = sum(g["score"] for g in grd) / len(grd)
        print("Grades:")
        for g in grd:
            print(f"- {g['subject']}: {g['score']}")
        print(f"Average = {total:.2f}")
    else:
        print("No grades yet.")

grades = []
while True:
    print("\n1. Add Grade\n2. View Average\n3. Exit")
    choice = input("Choose: ")
    if choice == "1":
        grades_add(grades)
    elif choice == "2":
        grades_avg(grades)
    elif choice == "3":
        break
    else:
        print("Invalid choice.")

# mygrade=[]
# grades_add(mygrade)
# grades_add(mygrade)
# grades_avg(mygrade)

