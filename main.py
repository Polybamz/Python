from expense_manager import *

def main():
    while True:
        print("\nEXPENSE MANAGER")
        print("0. To view all expense")
        print("1. Add Expense")
        print("2. View Expenses by Category")
        print("3. View Expenses by Month")
        print("4. Calculate Total by Category")
        print("5. Calculate Total by Month")
        print("6. Add Category")
        print("7. View all categories")
        print("8. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            ExpenseManager.add_expense()
        elif choice == "2":
            category = input("Enter the category to view: ")
            ExpenseManager.view_expenses_by_category(category)
        elif choice == "3":
            try:
                month = int(input("Enter the month (1-12): "))
                ExpenseManager.view_expenses_by_month(month)
            except ValueError:
                print("Invalid month format.")
        elif choice == "4":
            category = input("Enter the category to calculate total: ")
            ExpenseManager.calculate_total_expenses_by_category(category)
        elif choice == "5":
            try:
                month = int(input("Enter the month (1-12): "))
                ExpenseManager.calculate_total_expenses_by_month(month)
            except ValueError:
                print("Invalid month format.")
        elif choice == "6":
            ExpenseManager.add_category()
        elif choice == "0":
            ExpenseManager.view_all_expenses()
        elif choice == "7":
            ExpenseManager.show_categories()
        elif choice == "8":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
