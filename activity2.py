print("Profit or Loss")
cp = int(input("What is the cost price "))
sp = int(input("What is the selling price "))
if sp > cp :
    profit = sp - cp
    print("Its a profit of: " , profit)
else:
    loss = cp - sp
    print("Its a loss of:" , loss)

 