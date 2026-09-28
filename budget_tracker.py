"""
budget_tracker.py

Functions for managing category budgets. Budgets are stored as a
simple dictionary: {"Food": 3000, "Travel": 1500}
This is Functional Module 2: Budget & Category Management.
"""

def set_budget(budgets, category, limit_amount):
    #Sets a budget limit for a specific category.
    budgets[category] = limit_amount
    return budgets

def get_amount_spent(expense_list, category):
    #Calculates the total amount spent in a specific category.
    total = 0
    for expense in expense_list:
        if expense["category"] == category:
            total = total + expense["amount"]
    return total

def get_budget_status(budgets, expense_list):
    #Returns a dictionary with the budget status for all categories.
    status = {}
    for category in budgets:
        spent = get_amount_spent(expense_list, category)
        limit = budgets[category]
        status[category] = {
            "spent": spent,
            "limit": limit,
            "exceeded": spent > limit
        }
    return status