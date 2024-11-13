import csv
import os
from expense import Expense

filePath = 'expenses.csv'



class CSVdb:

    ### initializes the CSVdb class and sets the file path to 'expenses.csv'
    def __init__(self):
        self.filePath = filePath
        with open(filePath, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'category', 'Amount'])

    #======
    ### Appends an expense record to a CSV file.

    ### This function takes an expense object and writes its CSV representation
    ### to a file specified by the global variable `filePath`. The file is opened
    ### in append mode, allowing new expense records to be added without 
    ### overwriting existing data.

    ### Parameters:
    ###expense (object): An object representing the expense, which must have a 
                        ###method `put_into_csv_row()` that returns a list or tuple 
                        ###suitable for writing as a CSV row.

        ###Raises:
        ###IOError: If the file cannot be opened or written to.   
    def save_expense(expense):
    
        with open(filePath, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(expense.put_into_csv_row())


    #=========
        ###Reads expenses from a CSV file specified by the global variable 'filePath'.
        
        ###This function checks if the file at 'filePath' exists. If it does, it opens the file
        ###in read mode and uses a CSV reader to parse its contents. It skips the header row
        ###and converts each subsequent row into an Expense object using the 'get_from_csv_row' method.
        ###The resulting Expense objects are collected into a list.

        ###Returns:
            ###list: A list of Expense objects read from the CSV file.
    def read_expenses():
        expenses = []
        if os.path.exists(filePath):
            with open(filePath, mode='r', newline='') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    expenses.append(Expense.get_from_csv_row(row))
        return expenses
