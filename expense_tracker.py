from expenseclass import Expense

def main():
    print("Welcome to the expense tracker!")
    expense_file_path = "Expenses.csv"
    budget = 2000
    expense = user_input()
    to_file(expense, expense_file_path)
    from_file(expense_file_path, budget)




def user_input():
    name = input("Enter the name of the item: ")
    amount = float(input("Enter the amount of the item: "))
    print(f"You have entered {name} and it costs {amount}")
    
    expense_category = [
        "Food", 
        "Home", 
        "Work", 
        "Fun", 
        "Misc",
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_category): 
            print(f"  {i + 1}. {category_name}")
        
        value_range = f"[1 - {len(expense_category)}]"
        selected_index = int(input(f"Enter category number: {value_range}: ")) - 1
        if selected_index in range (len(expense_category)):
            selected_category = expense_category[selected_index]
            new_expense = Expense(name = name, category = selected_category, amount = amount)
            return new_expense
        else:
            print("Invalid option selected. Please try again")
        
def to_file(expense, expense_file_path):
    print(f"Exporting to file: {expense}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name}, {expense.category}, {expense.amount}\n")


def from_file(expense_file_path, budget):
    print("This is your summary:")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            sripped_line = line.strip()
            expense_name, expense_category, expense_amount = sripped_line.split()
            line_expense = Expense(name = expense_name, category = expense_category, amount = float(expense_amount))
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    print("Expenses by category:")
    for key, amount in amount_by_category.items():
        print(f"  {key} ${amount:.2f}")

    total_spent = sum([ex.amount for ex in expenses])
    print(f"You have spend ${total_spent:.2f} this month")
    remaining_budget = budget - total_spent
    if remaining_budget < 0:
        print(f"You have gone ${abs(remaining_budget):.2f} over your monthly budget")
    else:
        print(f"Budget remaining is: ${remaining_budget:.2f}")

if __name__ == "__main__":
    main()