item = input("what item would you like to buy?:")
price=float(input("what is the price?:"))
quantity = int(input("how many would you like to buy?:"))

total = price * quantity

print (f"you have bought {quantity}x {item}")
print (f"your total price is {total}")