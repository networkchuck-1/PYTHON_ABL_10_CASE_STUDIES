
# Case Study 17: Student Performance Trend Analysis

subjects = ["Python", "Mathematics", "English", "Physics"]

previous = []
latest = []

for subject in subjects:
    mark1 = float(input("Previous exam marks in " + subject + ": "))
    mark2 = float(input("Latest exam marks in " + subject + ": "))

    if not (0 <= mark1 <= 100 and 0 <= mark2 <= 100):
        print("Invalid marks. Enter values from 0 to 100.")
        raise SystemExit

    previous.append(mark1)
    latest.append(mark2)

print("\n===== PERFORMANCE REPORT =====")

total = 0
weak_subjects = []

for i in range(len(subjects)):
    change = latest[i] - previous[i]
    total += latest[i]

    if change > 0:
        trend = "Improved"
    elif change < 0:
        trend = "Declined"
    else:
        trend = "Unchanged"

    print(subjects[i], ":", trend,
          "| Change:", round(change, 2))

    if latest[i] < 40:
        weak_subjects.append(subjects[i])

average = total / len(subjects)

if average >= 75:
    classification = "Excellent"
elif average >= 60:
    classification = "Good"
elif average >= 40:
    classification = "Average"
else:
    classification = "Needs Improvement"

print("Latest average:", round(average, 2))
print("Classification:", classification)

if weak_subjects:
    print("Weak subjects:", weak_subjects)
else:
    print("No weak subjects identified")
