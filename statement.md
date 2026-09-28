# Project Statement - Budget Buddy

## Problem Statement

Tracking spending by memory or in a general notes app falls apart quickly once you're dealing with more than one or two spending categories - there's no easy way to see, at a glance, whether you've blown past what you meant to spend on food this month, or whether your current habits are compatible with something you're actually saving toward (a laptop, a bike, rent). Spreadsheet-based tracking works but has enough setup friction that most people give up on it within a few weeks.

This project is a small terminal application that removes that friction: logging an expense takes one menu option and four prompts, and checking budget status or savings-goal progress is a single keypress away, with no spreadsheet formulas to maintain.

## Scope of the Project

**In scope:**
- Adding, viewing, updating, deleting, and searching individual expenses
- Setting a budget limit per category and checking spend against it
- Reports: totals, category breakdown, average/min/max, a basic text chart, monthly totals
- CSV export of all expenses
- A single savings goal with target amount, target date, and monthly income, checked against actual average spending
- Local persistence via plain text files, so data survives between runs

**Out of scope:**
- Multiple users, accounts, or authentication
- A graphical or web interface - this is a terminal application only
- More than one active savings goal at a time
- Any bank, UPI, or third-party data integration - all entries are manual
- Multiple currencies

## Target Users

Someone comfortable running a Python script from a terminal - realistically, a student or someone early in their career - who wants a fast way to answer "am I overspending?" and "am I on track for my goal?" without adopting a full personal-finance app.

## High-Level Features

- **Expense Management** - record, edit, remove, and search expenses
- **Budget & Category Management** - per-category spending limits with over/under-budget status
- **Reporting & Analytics** - totals, breakdowns, basic statistics, a text chart, monthly trends, CSV export
- **Savings Goal Tracking** - a single goal checked against income and actual average spending
