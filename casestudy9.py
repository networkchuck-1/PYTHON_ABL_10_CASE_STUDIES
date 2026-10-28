
# Multi-Currency Travel Budget Analysis

exchange_rates = {
    "INR": 1,
    "USD": 88,
    "EUR": 102,
    "GBP": 117
}

conversion_fee_rate = 0.02

budget = float(input("Enter travel budget in INR: "))
n = int(input("Enter number of expenses: "))

expenses = []
category_totals = []

# Input and process expenses
for i in range(n):
    print("\nExpense", i + 1)

    category = input("Enter category: ").lower()
    amount = float(input("Enter expense amount: "))
    currency = input("Enter currency (INR/USD/EUR/GBP): ").upper()

    if amount < 0:
        print("Invalid amount. Expense skipped.")
        continue

    if currency not in exchange_rates:
        print("Unsupported currency. Expense skipped.")
        continue

    converted_amount = amount * exchange_rates[currency]
    fee = converted_amount * conversion_fee_rate
    total = converted_amount + fee

    expenses.append((category, amount, currency, total))

    # Update category total
    found = False

    for j in range(len(category_totals)):
        if category_totals[j][0] == category:
            old_total = category_totals[j][1]
            category_totals[j] = (category, old_total + total)
            found = True
            break

    if not found:
        category_totals.append((category, total))

# Calculate overall spending
total_spending = 0

for category, amount in category_totals:
    total_spending += amount

# Display expense details
print("\n===== TRAVEL EXPENSE REPORT =====")

for category, amount, currency, total in expenses:
    print(category.title(), "-", amount, currency,
          "| Total INR including fee:", round(total, 2))

print("\nTotal spending: Rs.", round(total_spending, 2))
print("Travel budget: Rs.", round(budget, 2))

if total_spending > budget:
    print("Status: Budget exceeded")
    print("Excess amount: Rs.", round(total_spending - budget, 2))
else:
    print("Status: Within budget")
    print("Remaining amount: Rs.", round(budget - total_spending, 2))

# Find largest expense category
if len(category_totals) > 0:
    largest = category_totals[0]

    for item in category_totals:
        if item[1] > largest[1]:
            largest = item

    print("Largest expense category:", largest[0].title())
    print("Category total: Rs.", round(largest[1], 2))
else:
    print("No valid expenses were recorded.")
