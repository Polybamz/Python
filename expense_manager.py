### expense_manager.py
from datetime import datetime
from CSVdb import *
from expense import Expense


### dictionary for categories
categories = {"Food": [], "Transportation": [], "Utilities": [], "Entertainment": []}

### Load existing expenses into categories
expenses = CSVdb.read_expenses()
for expense in expenses:
    if expense.category in categories:
        categories[expense.category].append(expense)
    else:
        categories[expense.category] = [expense]

### add expense function
 
class ExpenseManager:
    def add_expense():
        try:
            date = input("Enter the date (YYYY-MM-DD): ")
            ### Validate date format
            datetime.strptime(date, '%Y-%m-%d') 
            category = input("Enter the category (Food, Transportation, etc.): ")
            if category not in categories:
                print("Invalid category. Please try again.")
                return
            amount = float(input("Enter the amount: "))
            expense = Expense(date, category, amount)
            categories[category].append(expense)
            CSVdb.save_expense(expense)
            print("Expense added successfully!")
        except ValueError as e:
            print(f"Input error: {e}")


    ### view expenses functions
    def view_expenses_by_category(category):
        if category not in categories:
            print("Invalid category.")
            return
        for expense in categories[category]:
            print(f"Date: {expense.date.strftime('%Y-%m-%d')}, Amount: {expense.amount}")


    ### view all expenses function
    def view_all_expenses():
        print('================================ ALL EXPENCES =================================')
        for category in categories:

            for expense in categories[category]:
                print(f"Date: {expense.date.strftime('%Y-%m-%d')}, Category: {expense.category}, Amount: {expense.amount}")
        print('=================================================================')


    #### view expenses by month function
    def view_expenses_by_month(month):
        month_expenses = [exp for cat in categories.values() for exp in cat if exp.date.month == month]
        print('================================ MONTH =================================')

        for expense in month_expenses:
            print(f"Date: {expense.date.strftime('%Y-%m-%d')}, Category: {expense.category}, Amount: {expense.amount}")
        print('=================================================================')


    ### calculate total expenses functions
    def calculate_total_expenses_by_category(category):
        if category not in categories:
            print("Invalid category.")
            return
        total = sum(exp.amount for exp in categories[category])
        print(f"Total expenses for {category}: {total}")
    ### add new category function
    def add_category():
        category = input("Enter the category name: ")
        if category in categories:
            print("Category already exists.")
            return
        categories[category] = []
        print(f"Category {category} added successfully!")


### show categories function

    def show_categories():

        print("CATEGORIES:")
        for category in categories:
            print(category)
        print('=================================================================')

    ### delete category function
    def delete_category(category):
        if category not in categories:
            print("Invalid category.")
            return
        del categories[category]
        print(f"Category {category} deleted successfully!")

    ### calculate total expenses by month function
    def calculate_total_expenses_by_month(month):
        total = sum(exp.amount for cat in categories.values() for exp in cat if exp.date.month == month)
        print(f"Total expenses for month {month}: {total}")
