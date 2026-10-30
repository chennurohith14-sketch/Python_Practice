distance = float(input("Enter distance in km: "))
mileage = float(input("Enter mileage: "))
price = float(input("Enter petrol price per litre: "))

fuel = distance / mileage
cost = fuel * price

print("Fuel required:", fuel, "litres")
print("Total fuel cost:", cost)