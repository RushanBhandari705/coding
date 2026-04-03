# Python compund interest calculator 

principle = 0 
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle >=0:
        print("Principle amount must be greater than 0. Please try again.")

print(principle)