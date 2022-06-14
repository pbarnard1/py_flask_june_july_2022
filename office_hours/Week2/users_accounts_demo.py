class BankAccount:
    def __init__(self, int_rate, starting_balance):
        self.balance = starting_balance
        self.interest_rate = int_rate

    def deposit(self, amount_to_add):
        self.balance += amount_to_add
        return self

    def withdraw(self, amount_to_remove):
        self.balance -= amount_to_remove
        return self

class User:
    def __init__(self, first_name, last_name, email, starting_balance = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        # self.account = BankAccount(0.05, 500) # Creating ONE account for this user
        self.accounts = {
            "account_one": BankAccount(0.03, starting_balance)
        } # Can hold a bunch of accounts

    def new_account(self, account_name, starting_int_rate = 0.03, starting_balance = 0):
        # Add a new key-value pair where the account_name is the name of the new account
        self.accounts[account_name] = BankAccount(starting_int_rate, starting_balance)
        return self

    def make_deposit(self, amount_to_deposit, account_name = "account_one"):
        self.accounts[account_name].deposit(amount_to_deposit)
        return self

    def make_withdrawal(self, amount_to_withdraw, account_name = "account_one"):
        self.accounts[account_name].withdraw(amount_to_withdraw)
        return self

    def transfer_money(self, amount, other_user, withdraw_from = "account_one", deposit_to = "account_one"):
        # Take money out of first user's account
        self.make_withdrawal(amount, withdraw_from)
        # self.accounts[withdraw_from].withdraw(amount) # Another way
        # Deposit into other user's account
        other_user.make_deposit(amount, deposit_to)
        return self


adrian = User("Adrian","Barnard","a@b.com")

print(adrian.accounts["account_one"].balance)

adrian.new_account("checking",0.01,1000)

print(adrian.accounts["checking"].balance)

print(adrian.accounts)
# Second user
kim = User("Kim","Barnard","k@b.com", 5000)

# Transfer money from Kim to Adrian
kim.transfer_money(500, adrian, "account_one", "checking")
print(kim.accounts["account_one"].balance)
print(adrian.accounts["checking"].balance)
