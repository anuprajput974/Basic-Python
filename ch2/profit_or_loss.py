cost_price = float(input("enter the cost price: "))

selling_price = float(input("enter the selling price: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("he is in profit by ",profit)
elif selling_price == cost_price:
    print("he is not in loss nor profit")

else:
    loss = cost_price - selling_price
    print("he is in loss by ", loss)