"""
report_tracker.py

Functions for totals, breakdowns, a simple text chart, monthly
trends, and CSV export.
This is Functional Module 3: Reporting & Analytics.
"""
import budget_tracker
import expense_tracker
def generate_report(expense_list, budgets):
    #Generates a report of total expenses, category breakdown, and budget status.
    total_expenses = expense_tracker.get_total_expenses(expense_list)
    category_breakdown = {}
    for category in expense_tracker.get_unique_categories(expense_list):
        category_breakdown[category] = sum(expense["amount"] for expense in expense_list if expense["category"] == category)
    budget_status = budget_tracker.get_budget_status(budgets, expense_list) 
    report = {
        "total_expenses": total_expenses,
        "category_breakdown": category_breakdown,
        "budget_status": budget_status
    }
    return report
def basic_stats(expense_list):
    #Calculates basic statistics: total, average, min, and max expenses.
    if not expense_list:
        return {"total": 0, "average": 0, "min": 0, "max": 0}
    
    total = sum(expense["amount"] for expense in expense_list)
    average = total / len(expense_list)
    min_expense = min(expense["amount"] for expense in expense_list)
    max_expense = max(expense["amount"] for expense in expense_list)
    return {
        "total": total,
        "average": average,
        "min": min_expense,
        "max": max_expense
    }

def export_to_csv(expense_list, filename):
    #Exports the expense list to a CSV file.
    import csv
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Amount", "Category", "Description", "Date"])
        for expense in expense_list:
            writer.writerow([expense["id"], expense["amount"], expense["category"], expense["description"], expense["date"]])
