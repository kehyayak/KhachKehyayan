class BankAccount:
    def __init__(self, name, age, savings=0):
        """
        This method is the initialize method in python classes,
        which gets called when an object is created from the class
        which allows the class to initialize the attributes of a class.
        """
        self.name = name
        self.age = age
        self.accounts = {"Savings": savings}

    def getIdentity(self):
        # Outputs the user's identity including their name and age
        print("Name:", self.name)
        print("Age:", self.age)

    def getBalances(self):
        """
        Although not specified, I have used a for loop in this
        method to "nicely" print the account names and their
        balances.
        """
        for key, value in self.accounts.items():
            print(key, ':', '${:.2f}'.format(value))

    def addSubAccount(self, sub_account, sub_account_balance):
        """
        Adds a new 'key' and 'value' to the dictionary of
        user's bank accounts. 'key' and 'value' mean
        bank account name and its balance respectively
        """
        self.accounts[sub_account] = sub_account_balance

    def deposit(self, sub_account, deposit_amount):
        """
        This method takes the account name that the user
        wants to deposit money into and looks for the account
        in the dictionary 'keys' to increase its respective 'value'
        by deposit_amount which is the amount to be deposited.
        """
        self.accounts[sub_account] = self.accounts[sub_account] + deposit_amount

    def withdraw(self, sub_account, withdraw_amount):
        """
        This method takes the account name that the user
        wants to withdraw money from and looks for the account
        in the dictionary 'keys' to decrease its respective 'value'
        by withdraw_amount which is the amount to be withdrawn.
        """
        self.accounts[sub_account] = self.accounts[sub_account] - withdraw_amount

    def printSummary(self):
        """
        The printSummary method prints the bank name,
        all information on the user and their bank accounts.
        Note that we can simply use the getIdentity()
        and the getBalances() methods to define this
        method, as we  created the required code above.
        """
        print("Welcome to Khach Money Bank!")
        self.getIdentity()
        self.getBalances()


# Below, we will test this program by adding a 24 year old
# user named John Doe, who will initially have a chequing
# account with a balance of $3500 and a savings account
# with a balance of $0. We will then deposit $200 into his
# savings account. Next, we will create a new account named
# 'Savings For New Car' to his dictionary of accounts, and
# test our deposit and withdraw functions. Finally, we are
# going to test our print functions.

# Test Cases #
# There is no need to add a third parameter as per the
# requirement that savings account starts with $0.
# Adding a third parameter in the below line would
# change the default amount that is in savings.
testAccount = BankAccount("John Doe", 24)
testAccount.addSubAccount("Chequing", 3500)
testAccount.deposit("Savings", 200)
testAccount.addSubAccount("Savings For New Car", 2000)
testAccount.withdraw("Savings", 50)

# The above lines of code are only to input the information
# into the user's bank account. The below lines of code
# will be to test our print methods, getIdentity(),
# getBalances(), and printSummary().
# Note that getIdentity() and getBalances() is what forms
# printSummary(). Nonetheless, we will  test them individually
# just in case the program user wants to only print the name
# and age of the user.

# Removing the commenting from below code line should only print
# the name and age of the user.
#testAccount.getIdentity()

# Removing the commenting from below code line should only print
# the user's account names and balances.
#testAccount.getBalances()

# Removing the commenting from below line should only print
# both the user's identity, as well as their account names
# and balances.
#testAccount.printSummary()
