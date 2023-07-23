balance = 5000
money = 15000
if balance > money:
    balance -= money
    print(f"Current balance is {balance}")
    print("Transaction complete, Dont forget your card")
else:
    print("Insufficient funds")
    print(f"Current balance is {balance}")