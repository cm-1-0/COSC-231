def get_income():
    try:
        income = float(input("Enter your monthly income: $"))
        return income
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return get_income()

def get_expenses():
    expenses = {}
    categories = ["Rent/Mortgage", "Utilities", "Groceries", "Entertainment", "Savings", "Other"]
    for category in categories:
        try:
            expense = float(input(f"Enter your {category} expense: $"))
            expenses[category] = expense
        except ValueError:
            print(f"Invalid input for {category}. Please enter a valid number.")
            return get_expenses()
    return expenses

def calculate_budget(income, expenses):
    total_expenses = sum(expenses.values())
    remaining_budget = income - total_expenses
    return remaining_budget

def main():
    print("Welcome to MoneyMinder Budget Calculator!")
    user_income = get_income()
    user_expenses = get_expenses()
    remaining_budget = calculate_budget(user_income, user_expenses)
    print(f"Your remaining budget after expenses: ${remaining_budget:.2f}")

if __name__ == "__main__":
    main()

