import csv

class Expense: #represents individual expenses
    def __init__(self, date, description, amount, category=None):
        self.date = date #date of expense
        self.description = description
        self.amount = float(amount) if amount else 0.0 #just in case
        self.category = category

    def __str__(self):
        return f"Date: {self.date}, Description: {self.description}, Amount: ${self.amount:.2f}, Category: {self.category if self.category else 'Uncategorized'}"

class Budget: #defined for budgetting part
    def __init__(self):
        self.expenses = []
        self.budget = {} #for user categories
        self.categories = { #predefined categories
            1: "Groceries", 2: "Dining Out", 3: "Transportation", 4: "Utilities", 5: "Rent/Mortgage",
            6: "Entertainment", 7: "Shopping", 8: "Healthcare", 9: "Travel", 10: "Other",
        }

    def load_csv(self): #load csv
        file_name = input("Name of CSV File or the path to it:")
        
        with open(file_name, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.expenses.append(Expense(row['Date'], row['Description'], row['Amount']))

    def categorize_expenses(self): #for each expense to categorize
        print("Categories: \n")
        for number, category in self.categories.items():
            print(f"{number}. {category}") 

        for expense in self.expenses:
            if not expense.category:
                print(f"Transaction: {expense}\n")
                while True:
                    category_number = int(input("For what category is this expense for (a number): "))
                    if category_number in self.categories:
                        expense.category = self.categories[category_number] #assign category to the chosen
                        break
                    else:
                        print("Not a category.")

#from now its the budgeting for each category
    def input_budget(self):
        unique_categories = set(expense.category for expense in self.expenses if expense.category)

        print("Please enter your budgeted amount for the category: \n")
        for category in unique_categories:
            while True:
                budget_amount = float(input(f"Budget for '{category}': "))
                self.budget[category] = budget_amount #stores the budget for each category

    def generate_report(self): #generate report and show report

        print("Expense Report")

        category_expenses = {} #for totals
        for expense in self.expenses:
            if expense.category:
                category_expenses[expense.category] = category_expenses.get(expense.category, 0) + expense.amount

        print(f"{'Category':<15} {'Total Expenses':<15} {'Budgeted Amount':<17} {'Net Difference':<15}")

        for category in sorted(category_expenses.keys()):
            expenses = category_expenses[category]
            budgeted = self.budget.get(category, 0)
            net = budgeted - expenses #budget vs spending
            print(f"{category:<15} ${expenses:<14.2f} ${budgeted:<16.2f} ${net:<14.2f}")

def main_loop(): #runs the whole program
    budget_app = Budget() #create the budget 
    budget_app.load_csv()#load csv
    budget_app.categorize_expenses()#categorizes each expense
    budget_app.input_budget()#budget for each
    budget_app.generate_report() #show report

if __name__ == "__main__":
    main_loop()
