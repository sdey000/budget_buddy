"""
savings_tracker.py

Functions for tracking a single savings goal.
A goal is stored as a dictionary:
{"name": "Laptop", "target_amount": 60000, "target_date": "01-03-2027", "monthly_income": 20000}
This is Functional Module 4: Savings Goal Tracking.
"""

def create_goal(name, target_amount, target_date, monthly_income):
    #Creates a new savings goal.
    goal = {
        "name": name,
        "target_amount": target_amount,
        "target_date": target_date,
        "monthly_income": monthly_income
    }
    return goal

def months_remaining(target_date):
    #Calculates the number of months remaining until the target date.
    from datetime import datetime
    target = datetime.strptime(target_date, "%d-%m-%Y")
    today = datetime.now()
    months = (target.year - today.year) * 12 + (target.month - today.month)
    if months < 1:
        months = 1
    return months

def average_monthly_expense(expenses):
    #Calculates the average monthly expense based on the provided expenses.
    if len(expenses) == 0:
        return 0

    months_seen = []
    for exp in expenses:
        month = exp["date"][3:10]  # Extract MM-YYYY from DD-MM-YYYY
        if month not in months_seen:
            months_seen.append(month)

    total = 0
    for exp in expenses:
        total = total + exp["amount"]

    if len(months_seen) == 0:
        return 0
    return total / len(months_seen)

def check_goal_progress(goal, expenses):
    #Checks if the user is on track to meet their savings goal.
    if goal is None:
        return None

    months_left = months_remaining(goal["target_date"])
    avg_expense = average_monthly_expense(expenses)
    monthly_savings = goal["monthly_income"] - avg_expense
    total_savings_possible = monthly_savings * months_left

    if total_savings_possible >= goal["target_amount"]:
        return{
            "goal_name": goal["name"],
            "target_amount": goal["target_amount"],
            "months_left": months_left,
            "total_savings_possible": total_savings_possible,
            "projected_monthly_savings": monthly_savings,
            "required_monthly_savings": goal["target_amount"]/months_left,
            "on_track": True
        }   #On Track
    else:   
        return {
            "goal_name": goal["name"],
            "target_amount": goal["target_amount"],
            "months_left": months_left,
            "total_savings_possible": total_savings_possible,
            "projected_monthly_savings": monthly_savings,
            "required_monthly_savings": goal["target_amount"] / months_left,
            "on_track": False
            }  # Not on track
