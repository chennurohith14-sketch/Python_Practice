old_price = float(input("Enter old price: "))
new_price = float(input("Enter new price: "))

change = new_price - old_price

percentage = (change / old_price) * 100

if change > 0:
    print("Price increased")
elif change < 0:
    print("Price decreased")
else:
    print("No price change")

print("Price change percentage:", abs(percentage), "%")