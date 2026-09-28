"""
main.py

This is the file you run. It shows a text menu and calls the other
files to do the actual work.

Run it with: python main.py
"""

from datetime import datetime

import expense_tracker
import budget_tracker   
import report_tracker
import savings_tracker
import file_helper

EXPENSES_FILE = "expenses.txt"
BUDGETS_FILE = "budgets.txt"
GOALS_FILE = "goals.txt"

def print_menu():
    print("\nMenu:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Search Expenses")
    print("6. Set Budget")
    print("7. View Budget Status")
    print("8. Generate Report")
    print("9. Set Savings Goal")
    print("10. Check Savings Goal Progress")
    print("11. Export Expenses to CSV")
    print("0. Exit")

def get_amount_input(prompt):
    while True:
        try:
            amount = float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue
        if amount < 0:
            print("Amount cannot be negative. Please enter a positive value.")
            continue
        return amount

def get_date_input(prompt):
#Keeps asking the user for a date until they enter a valid date in DD-MM-YYYY format.
    while True:
        date_str = input(prompt)
        try:
            datetime.strptime(date_str, "%d-%m-%Y")
            return date_str
        except ValueError:
            print("Invalid date format. Please enter the date in DD-MM-YYYY format.")

def get_id_input(prompt):
    #Keeps asking until the user enters a whole number.
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def get_optional_amount(prompt):
    #Blank means "skip" (returns None). Otherwise keeps asking until the amount is valid.
    while True:
        text = input(prompt)
        if text == "":
            return None
        try:
            amount = float(text)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue
        if amount < 0:
            print("Amount cannot be negative. Please enter a positive value.")
            continue
        return amount

def get_optional_date(prompt):
    #Blank means "skip" (returns None). Otherwise keeps asking until the date is valid.
    while True:
        text = input(prompt)
        if text == "":
            return None
        try:
            datetime.strptime(text, "%d-%m-%Y")
            return text
        except ValueError:
            print("Invalid date format. Please enter the date in DD-MM-YYYY format.")

def add_expense_flow(expenses):
    amount = get_amount_input("Enter amount: ")
    category = input("Enter category: ")
    description = input("Enter description: ")
    date = get_date_input("Enter date (DD-MM-YYYY): ")
    expense_tracker.add_expense(expenses, amount, category, description, date)
    file_helper.save_expenses(EXPENSES_FILE, expenses)

def view_expenses_flow(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    for exp in expenses:
        print(f"ID: {exp['id']}, Amount: {exp['amount']}, Category: {exp['category']}, Description: {exp['description']}, Date: {exp['date']}")

def update_expense_flow(expenses):
    expense_id = get_id_input("Enter expense ID to update: ")
    expense = expense_tracker.find_expense_by_id(expenses, expense_id)
    if not expense:
        print("Expense not found.")
        return
    amount = get_optional_amount("Enter new amount (or leave blank): ")
    category = input("Enter new category (or leave blank): ")
    description = input("Enter new description (or leave blank): ")
    date = get_optional_date("Enter new date (DD-MM-YYYY) (or leave blank): ")
    updated_expense = expense_tracker.update_expense(
        expenses,
        expense_id,
        amount,
        category if category else None,
        description if description else None,
        date if date else None
    )
    if updated_expense:
        file_helper.save_expenses(EXPENSES_FILE, expenses)
        print("Expense updated successfully.")
    else:
        print("Failed to update expense.")

def delete_expense_flow(expenses):
    expense_id = get_id_input("Enter expense ID to delete: ")
    success = expense_tracker.delete_expense(expenses, expense_id)
    if success:
        file_helper.save_expenses(EXPENSES_FILE, expenses)
        print("Expense deleted successfully.")
    else:
        print("Expense not found.")

def search_expenses_flow(expenses):
    category = input("Enter category to search (or leave blank): ")
    min_amount = get_optional_amount("Enter minimum amount to search (or leave blank): ")
    max_amount = get_optional_amount("Enter maximum amount to search (or leave blank): ")
    start_date = get_optional_date("Enter start date (DD-MM-YYYY) (or leave blank): ")
    end_date = get_optional_date("Enter end date (DD-MM-YYYY) (or leave blank): ")

    results = expense_tracker.search_expenses(
        expenses,
        category=category if category else None,
        min_amount=min_amount,
        max_amount=max_amount,
        start_date=start_date,
        end_date=end_date
    )

    if not results:
        print("No expenses found matching the criteria.")
    else:
        for exp in results:
            print(f"ID: {exp['id']}, Amount: {exp['amount']}, Category: {exp['category']}, Description: {exp['description']}, Date: {exp['date']}")

def set_budget_flow(budgets):
    category = input("Enter category for budget: ")
    limit_amount = get_amount_input("Enter budget limit: ")
    budget_tracker.set_budget(budgets, category, limit_amount)
    file_helper.save_budgets(BUDGETS_FILE, budgets)
    print(f"Budget set for category '{category}' with limit {limit_amount}.")

def view_budget_status_flow(budgets, expenses):
    status = budget_tracker.get_budget_status(budgets, expenses)
    if not status:
        print("No budgets set.")
        return
    for cat, info in status.items():
        print(f"{cat}: Spent {info['spent']} / Limit {info['limit']} - Exceeded: {info['exceeded']}")

def view_report_flow(expenses, budgets):
    report = report_tracker.generate_report(expenses, budgets)
    print("Total Expenses:", report["total_expenses"])
    print("Category Breakdown:")
    for category, total in report["category_breakdown"].items():
        print(f"  {category}: {total}")
    average_expense = report_tracker.basic_stats(expenses)["average"]
    print(f"Average Expense: {average_expense}")
    print("Budget Status:")
    for category, info in report["budget_status"].items():
        print(f"  {category}: Spent {info['spent']} / Limit {info['limit']} - Exceeded: {info['exceeded']}")

def set_savings_goal_flow():
    name = input("Enter savings goal name: ")
    target_amount = get_amount_input("Enter target amount: ")
    target_date = get_date_input("Enter target date (DD-MM-YYYY): ")
    monthly_income = get_amount_input("Enter monthly income: ")
    goal = savings_tracker.create_goal(name, target_amount, target_date, monthly_income)
    file_helper.save_goal(GOALS_FILE, goal)
    print(f"Savings goal '{name}' set with target amount {target_amount} by {target_date}.")

def check_savings_goal_progress_flow(goal, expenses):
    if not goal:
        print("No savings goal set.")
        return
    progress = savings_tracker.check_goal_progress(goal, expenses)
    if progress:
        print(f"Goal: {progress['goal_name']}, On Track: {progress['on_track']}, Total Savings Possible: {progress['total_savings_possible']}")
        print(f"Months Left: {progress['months_left']}, Projected Monthly Savings: {progress['projected_monthly_savings']}, Required Monthly Savings: {progress['required_monthly_savings']}")
    else:
        print("No savings goal set.")

def export_expenses_to_csv_flow(expenses):
    filename = input("Enter filename for CSV export: ")
    report_tracker.export_to_csv(expenses, filename)
    print(f"Expenses exported to {filename}")

def main():
    expenses = file_helper.load_expenses(EXPENSES_FILE)
    budgets = file_helper.load_budgets(BUDGETS_FILE)
    goal = file_helper.load_goal(GOALS_FILE)

    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense_flow(expenses)
        elif choice == "2":
            view_expenses_flow(expenses)
        elif choice == "3":
            update_expense_flow(expenses)
        elif choice == "4":
            delete_expense_flow(expenses)
        elif choice == "5":
            search_expenses_flow(expenses)
        elif choice == "6":
            set_budget_flow(budgets)
        elif choice == "7":
            view_budget_status_flow(budgets, expenses)
        elif choice == "8":
            view_report_flow(expenses, budgets)
        elif choice == "9":
            set_savings_goal_flow()
            goal = file_helper.load_goal(GOALS_FILE)  # Reload the goal after setting it
        elif choice == "10":
            check_savings_goal_progress_flow(goal, expenses)
        elif choice == "11":
            export_expenses_to_csv_flow(expenses)
        elif choice == "0":
            print("Exiting Budget Buddy. Goodbye!")
            break

if __name__ == "__main__":
    main()
