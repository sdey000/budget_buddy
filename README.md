# budget_buddy
Budget Buddy: a command-line Python app to track expenses, set category budgets, and check whether you're on pace for a savings goal. Includes reports, CSV export, and saved data.
A command-line budget and expense tracker written in Python for the VITyarthi "Build Your Own Project" submission (Python Essentials). You can log expenses, set a spending limit per category, check whether a savings goal is realistic given your income, and pull basic reports out of your spending - all through a plain numbered menu, with everything saved to text files so it's still there the next time you open it.

## Overview

I split the app into four modules that map onto the four things a budget tracker actually needs to do: recording expenses, checking them against budgets, reporting on them, and tying them to a savings goal. `main.py` is just the menu loop - it doesn't do any of the actual logic itself, it calls into the other four files.

I kept storage as plain `.txt` files with `|` as a field separator and also built the persistence layer(`file_helper.py`) to fully understand the saving process line by line instead of reaching for something imported and generated.

I built this app using basic Python commands and also for reusability which makes it ready to go and to be used in day to day life.
## Features

**1. Expense Management** - `expense_tracker.py`
- Add an expense (amount, category, description, date)
- View all expenses
- Update or delete an expense by ID
- Search by category, amount range, or date range

**2. Budget & Category Management** - `budget_tracker.py`
- Set a spending limit for any category
- Calculate total spent in a category
- Flag whether a category is over its limit

**3. Reporting & Analytics** - `report_tracker.py`
- Total spend and a per-category breakdown
- Basic stats (average / min / max expense)
- CSV export

**4. Savings Goal Tracking** - `savings_tracker.py`
- Set a goal: name, target amount, target date, monthly income
- Check progress - compares projected monthly savings (income minus average monthly spend) against what's actually required per month to hit the target on time

Data lives in `expenses.txt`, `budgets.txt`, and `goals.txt`, loaded on startup and re-saved after every change, so closing the app doesn't lose anything.

## Technologies / Tools Used

- Python 3 (built and tested on 3.12)
- Standard library only - `datetime` for parsing/validating dates, `csv` for the export feature
- No external packages, no database
- Git for version control

## Project Structure

```
budget_buddy/
├── main.py              # Menu loop, input prompts, wiring between modules
├── expense_tracker.py   # Module 1 — Expense Management
├── budget_tracker.py    # Module 2 — Budget & Category Management
├── report_tracker.py    # Module 3 — Reporting & Analytics
├── savings_tracker.py   # Module 4 — Savings Goal Tracking
├── file_helper.py       # Loads/saves expenses, budgets, and the goal to disk
├── README.md
└── statement.md
```

## How to Run It

1. Check you have Python 3.7+:
   ```bash
   python --version
   ```
2. Open a terminal in the project folder.
3. Run:
   ```bash
   python main.py
   ```
4. Pick a number from the menu and follow the prompts. On the very first run, none of the `.txt` data files exist yet — they get created the moment you add your first expense, budget, or goal.

## Testing

There's no automated test suite - I tested this manually by running through every menu option end to end and checking the saved `.txt`/`.csv` files matched what I'd entered. Roughly the same walkthrough, if you want to check it yourself:

1. Add two or three expenses across different categories (option 1), then view them (option 2) and confirm the amounts/categories/dates are right.
2. Set a budget for one of those categories (option 6), then check the budget status (option 7) - confirm the "spent" total and the exceeded flag are correct.
3. Update one expense and delete another (options 3 and 4), then re-view (option 2) to confirm the change stuck.
4. Search by category and by amount range (option 5).
5. Generate a report (option 8) and check the total/breakdown/average against what you'd expect by hand.
6. Set a savings goal (option 9) and check progress (option 10) - do the months-left and required-monthly-savings numbers look right for the date and income you entered?
7. Export to CSV (option 11) and open the file to confirm it matches.
8. Exit and re-run the app - confirm everything you entered is still there (this checks that `file_helper.py`'s load/save actually round-trips correctly).
9. Deliberately enter bad input - letters where an amount or an expense ID is expected, or a date not in `DD-MM-YYYY` - at the add, update, delete and search prompts, and confirm each one re-prompts instead of crashing.

**A bug I actually caught this way:** early on, `get_amount_input()` in `main.py` would crash with an `UnboundLocalError` if you typed something non-numeric, because the `except ValueError` block printed a message but didn't loop back before checking `amount < 0`. Adding a `continue` in the except block fixed it.

Testing the other prompts found more of the same problem: a non-numeric ID at update/delete, and a non-numeric amount at update/search, also crashed, and the dates typed into update and search weren't validated. Those now go through small helpers (`get_id_input`, `get_optional_amount`, `get_optional_date`) in `main.py`.

A different kind of bug: `search_expenses` compared dates as plain text, and since `DD-MM-YYYY` sorts by day first, a date-range search across months or years dropped valid results (a search from 10-12-2026 missed an expense on 05-01-2027). It now converts to real dates before comparing.

## Screenshots
https://github.com/sdey000/budget_buddy/blob/4500cf0e97d381857af5bd8c9dba90bc6a4372a9/Screenshot_Menu.png
https://github.com/sdey000/budget_buddy/blob/main/Screenshot_add_and_view_expense.png
https://github.com/sdey000/budget_buddy/blob/main/Screenshot_budget.png
https://github.com/sdey000/budget_buddy/blob/main/Screenshot_report.png

## Known Limitations

- The `|` separator in the storage files means a category or description containing a literal `|` would break parsing on the next load.
- Only one savings goal can exist at a time; setting a new one replaces the old one.
- A savings goal whose target date has already passed reports "Months Left: 1" rather than warning that the date is in the past.
- The chances of finding more significant limitations are quite less but not 0. So, I am looking forward to finding them and rectifying them in near future.
