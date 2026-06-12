# Expense Tracker

expenses = []

while True:
    print("\nEnter expense details")

    amount = input("Amount: ")

    if amount.lower() == "exit":
        break

    category = input("Category: ")
    note = input("Note: ")
    date = input("Date (optional): ")

    expense = {
        "amount": float(amount),
        "category": category,
        "note": note,
        "date": date
    }

    expenses.append(expense)

print("\nExpense Summary")
print("-" * 30)

total = 0

for expense in expenses:
    print(
        f"₦{expense['amount']} | "
        f"{expense['category']} | "
        f"{expense['note']} | "
        f"{expense['date']}"
    )

    total += expense["amount"]

print("-" * 30)
print("Total Expenses: ₦", total)