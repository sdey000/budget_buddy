"""
file_helper.py

Saves and loads data using plain text files.
Each kind of data uses a simple one-line-per-record format, with the
pipe characters | separating the fields.
"""
def load_expenses(filename):
    #Read expenses from a text file. Returns an empty list if the file is missing.
    expenses = []
    try:
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
    except FileNotFoundError:
        return expenses
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        parts = line.split("|")
        if len(parts) != 5:
            continue
        expense = {
            "id": int(parts[0]),
            "amount": float(parts[1]),
            "category": parts[2],
            "description": parts[3],
            "date": parts[4],
        }
        expenses.append(expense)
    return expenses

def save_expenses(filename, expenses):
    #Write the expense list out to a text file, one expense per line.
    try:
        file = open(filename, "w")
        for exp in expenses:
            line = str(exp["id"]) + "|" + str(exp["amount"]) + "|"
            line = line + exp["category"] + "|" + exp["description"] + "|" + exp["date"]
            file.write(line + "\n")
        file.close()
        return True
    except Exception:
        print("Error: could not save " + filename)
        return False

def load_budgets(filename):
    #Read budgets from a text file into a dictionary. Empty dict if missing.
    budgets = {}
    try:
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
    except FileNotFoundError:
        return budgets
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        parts = line.split("|")
        if len(parts) != 2:
            continue
        budgets[parts[0]] = float(parts[1])
    return budgets

def save_budgets(filename, budgets):
    #Write the budgets dictionary out to a text file, one budget per line.
    try:
        file = open(filename, "w")
        for category, amount in budgets.items():
            file.write(category + "|" + str(amount) + "\n")
        file.close()
        return True
    except Exception:
        print("Error: could not save " + filename)
        return False

def load_goal(filename):
    #Read a savings goal from a text file. Returns None if the file is missing.
    try:
        file = open(filename, "r")
        line = file.readline().strip()
        file.close()
        if line == "":
            return None
        parts = line.split("|")
        if len(parts) != 4:
            return None
        goal = {
            "name": parts[0],
            "target_amount": float(parts[1]),
            "target_date": parts[2],
            "monthly_income": float(parts[3])
        }
        return goal
    except FileNotFoundError:
        return None
    except Exception:
        print("Warning: could not read " + filename + ". Starting fresh.")
        return None

def save_goal(filename, goal):
    #Write a savings goal to a text file.
    try:
        file = open(filename, "w")
        line = goal["name"] + "|" + str(goal["target_amount"]) + "|" + goal["target_date"] + "|" + str(goal["monthly_income"])
        file.write(line)
        file.close()
        return True
    except Exception:
        print("Error: could not save " + filename)
        return False

