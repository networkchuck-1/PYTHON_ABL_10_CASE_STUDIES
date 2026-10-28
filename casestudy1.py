
students = []
n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter student name: ")
    aggregate = float(input("Enter aggregate percentage: "))

    marks = []
    subjects = int(input("Enter number of subjects: "))

    for j in range(subjects):
        mark = float(input("Enter mark for subject " + str(j + 1) + ": "))
        marks.append(mark)

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    eligible = (
        aggregate >= 75
        and all(mark >= 60 for mark in marks)
        and attendance >= 75
        and income <= 250000
    )

    if eligible:
        print(name, "is Eligible")
        students.append({
            "name": name,
            "aggregate": aggregate,
            "attendance": attendance,
            "income": income
        })
    else:
        print(name, "is Not Eligible")

# Rank eligible students
students.sort(
    key=lambda s: (
        -s["aggregate"],
        -s["attendance"],
        s["income"],
        s["name"].lower()
    )
)

print("\n--- Scholarship Ranking ---")

if len(students) == 0:
    print("No eligible students found.")
else:
    for rank, student in enumerate(students, start=1):
        print(
            rank, student["name"],
            "| Aggregate:", student["aggregate"],
            "| Attendance:", student["attendance"],
            "| Income:", student["income"]
        )
