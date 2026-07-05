#Shopping cart Program 

item = input("Enter what do u want to buy?:")
price = float(input("What is the price?:"))
quantity = int(input("how many would u like?:"))
total = price * quantity
print(f"You have bought {quantity} x {item}")
print(f"Your total is: ${price}")