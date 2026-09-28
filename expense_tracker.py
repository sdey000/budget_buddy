"""
expense_tracker.py

Functions for managing expenses. Each expense is just a dictionary:
{"id": 1, "amount": 500, "category": "Food", "description": "Lunch", "date": "2026-09-20"}
All expenses together are stored in a plain list.
This is Functional Module 1: Expense Management.
"""
from datetime import datetime

def next_id(expense):
    #Returns the next available ID for a new expense.
    if len(expense)==0:
        return 1
    else:
        return max(exp["id"] for exp in expense) + 1

def add_expense(expense_list, amount, category, description, date):
    #Adds a new expense to the list.
    new_id = next_id(expense_list)
    new_expense = {
        "id": new_id,
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }
    expense_list.append(new_expense)
    return new_expense

def find_expense_by_id(expense_list, expense_id):
    #Finds an expense by its ID.
    for expense in expense_list:
        if expense["id"] == expense_id:
            return expense
    return None

def update_expense(expense_list, expense_id, amount=None, category=None, description=None, date=None):
    #Updates an existing expense.
    expense = find_expense_by_id(expense_list, expense_id)
    if expense is not None:
        if amount is not None:
            expense["amount"] = amount
        if category is not None:
            expense["category"] = category
        if description is not None:
            expense["description"] = description
        if date is not None:
            expense["date"] = date
        return expense
    return None

def delete_expense(expense_list, expense_id):
    #Deletes an expense by its ID.
    expense = find_expense_by_id(expense_list, expense_id)
    if expense is not None:
        expense_list.remove(expense)
        return True
    return False

def search_expenses(expense_list, category=None, min_amount=None, max_amount=None, start_date=None, end_date=None):
    #Searches for expenses based on various criteria.
    results = []
    for expense in expense_list:
        if category is not None and expense["category"] != category:
            continue
        if min_amount is not None and expense["amount"] < min_amount:
            continue
        if max_amount is not None and expense["amount"] > max_amount:
            continue
        if start_date is not None or end_date is not None:
            expense_date = datetime.strptime(expense["date"], "%d-%m-%Y")
            if start_date is not None and expense_date < datetime.strptime(start_date, "%d-%m-%Y"):
                continue
            if end_date is not None and expense_date > datetime.strptime(end_date, "%d-%m-%Y"):
                continue
        results.append(expense)
    return results

def get_total_expenses(expense_list):
    #Calculates the total amount of all expenses.
    return sum(expense["amount"] for expense in expense_list)

def get_unique_categories(expense_list):
    #Returns a set of unique categories from the expense list.
    categories = []
    for expense in expense_list:
        if expense["category"] not in categories:
            categories.append(expense["category"])
    return categories
