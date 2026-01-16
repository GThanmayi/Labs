class Bank_Account:
    def __init__(self,account_num,balance):
        self.account_num=account_num
        self.balance=balance

s1=Bank_Account("jam",100)

print(s1.account_num,s1.balance)
