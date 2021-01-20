'''Created a class Category which contains some methods which will all-together act like a budget-calculator...'''

class Category:
    '''Initialized name and a list ledger which contains amount and descriptions...'''
    def __init__(self, name):
        self.name = name
        self.ledger = []

    '''Deposit method which takes amount and description. The description may be empty or it may contain a string..'''
    def deposit(self, amount, description=None):
        if description == None:
            self.ledger.append({'amount': (amount), 'description': ''})
        else:
            self.ledger.append({'amount': (amount), 'description': description})

    '''The withdraw method which contains a amount and description but here the value of amount will be negetive 
    as this amount will be deducted. Along with this we are calling the check_funds method so that we can proceed 
    if we are having a certain amount of balance...'''
    def withdraw(self, amount, description=None):
        if self.check_funds(amount) == True:
            if description == None:
                self.ledger.append({'amount': -(amount), 'description': ''})
            else:
                self.ledger.append({'amount': -(amount), 'description': description})
            return True
        else:
            return False

    '''The get_balance method will add the amount in the balance Sothat the the amount of money in the account can be 
    calculated...'''
    def get_balance(self):
        balance = 0
        for items in self.ledger:
            balance += items['amount']
        return balance

    '''The transfer method takes amount and bugdet_category and it proceed once the check_funds is True. In descrtiption 
    here we are using the name of the budget_category like food,entertainment etc...'''
    def transfer(self, amount, budget_category):
        if self.check_funds(amount) == True:
            self.ledger.append({'amount': -(amount),
                                'description': f'Transfer to {budget_category.name}'})
            budget_category.deposit(amount, description=f'Transfer from {self.name}')
            return True
        else:
            return False
    '''The check_funds method used to calculate the balance and called in the withdraw and transfer method...'''
    def check_funds(self, amount):
        return amount <= self.get_balance()

    '''The __str__ method is used to display the description and the amount spent where the agenda is, 
    it should have 30 characters for name and it should be centered. And for description 23 places and for 
    amount 7 places reserved...'''
    def __str__(self):
        output = self.name.center(50, "*") + "\n"
        for items in self.ledger:
            output += f"{items['description'][:43].ljust(43)}{format(items['amount'], '.2f').rjust(7)}\n"
        output += f"Total: {format(self.get_balance(), '.2f')}"
        return output

'''Besides the Category class, create a function (ouside of the class) calledcreate_spend_chart that takes 
a list of categories as an argument. It should return a string that is a bar chart.'''
def create_spend_chart(categories):
    category_names = []
    spent = []
    spent_percentages = []

    for category in categories:
        total = 0
        for items in category.ledger:
            if items['amount'] < 0:
                total -= items['amount']
        spent.append(round(total, 2))
        category_names.append(category.name)

    for amount in spent:
        spent_percentages.append(round(amount / sum(spent), 2) * 100)

    graph = "Percentage spent by category\n"
    labels = range(100, -10, -10)

    for label in labels:
        graph += str(label).rjust(3) + "| "
        for percent in spent_percentages:
            if percent >= label:
                graph += "o  "
            else:
                graph += "   "
        graph += "\n"

    graph += "    ----" + ("---" * (len(category_names) - 1))
    graph += "\n     "

    longest_name_length = 0
    for name in category_names:
        if longest_name_length < len(name):
            longest_name_length = len(name)

    for i in range(longest_name_length):
        for name in category_names:
            if len(name) > i:
                graph += name[i] + "  "
            else:
                graph += "   "
        if i < longest_name_length - 1:
            graph += "\n     "

    return (graph)

