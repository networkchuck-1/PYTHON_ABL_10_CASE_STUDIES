
# Case Study 13: ATM Transaction Sequence Simulation

balance = 10000
withdrawal_limit = 5000

deposits = 0
withdrawals = 0
rejected = 0

n = int(input("Enter number of transactions: "))

for i in range(n):
    print("\n1. Deposit")
    print("2. Withdraw")

    choice = input("Enter transaction type (1/2): ")
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount")
        rejected += 1

    elif choice == "1":
        balance += amount
        deposits += 1
        print("Deposit successful")

    elif choice == "2":
        if amount > withdrawal_limit:
            print("Withdrawal limit exceeded")
            rejected += 1
        elif amount > balance:
            print("Insufficient balance")
            rejected += 1
        else:
            balance -= amount
            withdrawals += 1
            print("Withdrawal successful")

    else:
        print("Invalid transaction type")
        rejected += 1

print("\n===== ATM SUMMARY =====")
print("Final balance: Rs.", round(balance, 2))
print("Successful deposits:", deposits)
print("Successful withdrawals:", withdrawals)
print("Rejected transactions:", rejected)
