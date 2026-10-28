
# Case Study 89: University Hostel Room Allocation

rooms = [
    ("R101", 2),
    ("R102", 3),
    ("R103", 2)
]

# Each room allocation is a list of student IDs
allocations = []

for room, capacity in rooms:
    allocations.append([])

assigned_ids = []
unallocated = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)

    student_id = input("Enter student ID: ")
    eligible = input(
        "Eligible for hostel? (yes/no): "
    ).lower()

    # Check duplicate ID
    if student_id in assigned_ids:
        print("Duplicate student ID. Record rejected.")
        continue

    if eligible != "yes":
        print("Student is not eligible.")
        unallocated.append(student_id)
        continue

    assigned = False

    # Find first room with available capacity
    for j in range(len(rooms)):
        room_no, capacity = rooms[j]

        if len(allocations[j]) < capacity:
            allocations[j].append(student_id)
            assigned_ids.append(student_id)
            assigned = True
            print("Allocated to room:", room_no)
            break

    if not assigned:
        print("No vacant room available.")
        unallocated.append(student_id)

print("\n===== HOSTEL ALLOCATION REPORT =====")

vacant_total = 0

for i in range(len(rooms)):
    room_no, capacity = rooms[i]
    students = allocations[i]
    vacant = capacity - len(students)
    vacant_total += vacant

    print("\nRoom:", room_no)
    print("Allocated students:", students)
    print("Occupied beds:", len(students))
    print("Vacant beds:", vacant)

print("\nUnallocated students:", unallocated)
print("Total unallocated:", len(unallocated))
print("Total vacant beds:", vacant_total)
