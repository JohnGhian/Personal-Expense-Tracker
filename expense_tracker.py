import csv

expenses = []

def add_expense():
    print("\n===== ADD EXPENSE =====")

    name = input("Expense name:")

    try:
        amount = float(input("amount: ₱"))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return   

    category = input("category:")
    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }
    expenses.append(expense)

    print("Expense added succesfully!")

def view_expenses():
    print("\n===== VIEW EXPENSES =====")

    if not expenses:
        print("No expense recorded")
        return

    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['name']} - ₱{expense['amount']:.2f} ({expense['category']})")

def show_total():
    total = sum(expense["amount"] for expense in expenses)

    print(f"\nTotal Expenses: ₱{total:.2f}")

def delete_expense():
    print("\n===== DELETE EXPENSE =====")

    if not expenses:
        print("No expense to delete.")
        return

    view_expenses()

    try:
        number = int(input("Enter the number of the expense number to delete: "))
    except ValueError:
        print('Please enter a valid number')
        return

    if 1 <= number <= len(expenses):
        removed = expenses.pop(number - 1)
        print(f"{removed['name']} was deleted.")
    else:
        print("Invalid expense number.")

def save_expenses():
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Expense", "Amount", "Category"])
        for expense in expenses:
            writer.writerow([expense["name"], 
                             expense["amount"],
                             expense["category"]])
        print("Expenses saved to expenses.csv")

def main():
    while True:
        print("\n=============================")
        print("   PERSONAL EXPENSE TRACKER")
        print("=============================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Expense")
        print("4. Delete Expense")
        print("5. Save Expenses")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            save_expenses()
        elif choice == "6":
            save_expenses()
            print("Thank you for using Personal Expense Tracker!")
            break
        else:
            print("Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    main()
        


                                                              

          