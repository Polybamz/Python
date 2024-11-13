
from datetime import datetime

class Expense:
    def __init__(self, date, category, amount):
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.category = category
        self.amount = amount



  # Converts the object's attributes into a list formatted for CSV output.

            # Returns:
            #     list: A list containing the date formatted as 'YYYY-MM-DD', 
            #         followed by the category and amount.
    def put_into_csv_row(self):
          
            return [self.date.strftime('%Y-%m-%d'), self.category, self.amount]
    

        # Converts a CSV row into an Expense object.

        # Parameters:
        # row (tuple): A tuple containing three elements - date (str), category (str), and amount (str).

        # Returns:
        # Expense: An instance of the Expense class with the date, category, and amount parsed from the row.
    def get_from_csv_row(row):
      
        date, category, amount = row
        return Expense(date, category, float(amount))
