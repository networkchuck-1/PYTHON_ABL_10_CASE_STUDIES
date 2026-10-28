
# Case Study 21: Traffic Violation Penalty Calculator

fines = {
    "overspeeding": 1000,
    "no helmet": 500,
    "signal violation": 1500,
    "drunk driving": 5000
}

records = []
total_fine = 0
disqualified = False

n = int(input("Enter number of violations: "))

for i in range(n):
    print("\nViolation", i + 1)

    vehicle = input("Vehicle category: ").lower()
    offence = input("Offence type: ").lower()
    repeat = input("Repeat offence? (yes/no): ").lower()

    if offence not in fines:
        print("Unknown offence. Record skipped.")
        continue

    fine = fines[offence]

    if repeat == "yes":
        fine *= 2
    elif repeat != "no":
        print("Invalid repeat status. Record skipped.")
        continue

    if offence == "drunk driving":
        disqualified = True

    total_fine += fine
    records.append((vehicle, offence, fine))

print("\n===== VIOLATION REPORT =====")

for vehicle, offence, fine in records:
    print(vehicle.title(), "|", offence.title(),
          "| Fine: Rs.", fine)

print("Total fine: Rs.", total_fine)

if disqualified:
    print("Disqualification flag: YES")
else:
    print("Disqualification flag: NO")
