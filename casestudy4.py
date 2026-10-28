
# Employee Payroll and Deduction Analysis

name = input("Enter employee name: ")
employee_id = input("Enter employee ID: ")

basic = float(input("Enter basic salary: "))
overtime_hours = float(input("Enter overtime hours: "))
overtime_rate = float(input("Enter overtime rate per hour: "))
incentive = float(input("Enter incentive amount: "))

# Calculate allowances
hra = basic * 0.20
da = basic * 0.10
overtime_pay = overtime_hours * overtime_rate

# Calculate gross salary
gross = basic + hra + da + overtime_pay + incentive

# Progressive deduction calculation
if gross <= 20000:
    deduction = gross * 0.05
elif gross <= 40000:
    deduction = 20000 * 0.05 + (gross - 20000) * 0.10
else:
    deduction = (20000 * 0.05
                 + 20000 * 0.10
                 + (gross - 40000) * 0.15)

net_salary = gross - deduction

# Display salary statement
print("\n========== SALARY STATEMENT ==========")
print("Employee Name:", name)
print("Employee ID:", employee_id)
print("--------------------------------------")
print(f"Basic Salary:       Rs. {basic:.2f}")
print(f"HRA:                Rs. {hra:.2f}")
print(f"DA:                 Rs. {da:.2f}")
print(f"Overtime Pay:       Rs. {overtime_pay:.2f}")
print(f"Incentives:         Rs. {incentive:.2f}")
print("--------------------------------------")
print(f"Gross Salary:       Rs. {gross:.2f}")
print(f"Total Deduction:    Rs. {deduction:.2f}")
print(f"Net Salary:         Rs. {net_salary:.2f}")
print("======================================")
