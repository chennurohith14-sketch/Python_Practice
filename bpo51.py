capacity = 50
passengers = 0

for i in range(3):
    boarding = int(input("Enter boarding passengers: "))
    passengers = passengers + boarding

    leaving = int(input("Enter leaving passengers: "))
    passengers = passengers - leaving

    if passengers > capacity:
        print("Bus is overloaded")
    else:
        print("Current passengers:", passengers)