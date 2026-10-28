
# Case Study 37: Nested Loop Calendar Generator

month = input("Enter month name: ")
start_day = int(input("Starting weekday (Mon=0, Sun=6): "))
days = int(input("Number of days in month: "))

if start_day < 0 or start_day > 6:
    print("Invalid weekday")
elif days < 28 or days > 31:
    print("Invalid number of days")
else:
    print("\n       ", month.title())
    print("Mon Tue Wed Thu Fri Sat Sun")

    # Print initial empty positions
    for i in range(start_day):
        print("    ", end="")

    # Print dates
    for date in range(1, days + 1):
        print(f"{date:3}", end=" ")

        # Move to next week after Sunday
        if (start_day + date) % 7 == 0:
            print()

    print()
