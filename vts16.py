capacity = 1000
water = 500

inflow = int(input("Enter water inflow: "))
outflow = int(input("Enter water outflow: "))

water = water + inflow - outflow

if water > capacity:
    print("Water overflow")
    water = capacity
elif water < 0:
    print("Water shortage")
    water = 0

print("Current water level:", water)