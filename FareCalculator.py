# FareCalc - CityCab Ride Estimator
rates = {            #Rate Dictionary
    "Economy": 10,                      
    "Premium": 18,
    "SUV": 25
}

# Fare Calculation Function
def calculate_fare(km, vehicle_type, hour):
    # Validate vehicle type
    if vehicle_type not in rates:
        return None

    base_rate = rates[vehicle_type]
    total = km * base_rate

    # Surge pricing 
    if 17 <= hour <= 20:
        total *= 1.5
        surge_applied = True
    else:
        surge_applied = False

    return total, surge_applied

# User Input
try:
    print("---- CityCab Fare Calculator ----")

    km = float(input("Enter distance (in km): "))
    vehicle_type = input("Enter vehicle type (Economy/Premium/SUV): ").title()
    hour = int(input("Enter hour of travel (0-23): "))

    #  Calculate Fare
    result = calculate_fare(km, vehicle_type, hour)

    if result is None:
        print("\n Service Not Available for selected vehicle type.")
    else:
        fare, surge = result
        #  Print Receipt
        print("\n------ Ride Receipt ------")
        print(f"Distance       : {km} km")
        print(f"Vehicle Type   : {vehicle_type}")
        print(f"Rate per km    : ₹{rates[vehicle_type]}")
        if surge:
            print("Surge Pricing  : Applied (1.5x)")
        else:
            print("Surge Pricing  : Not Applied")
        print(f"Total Fare     : ₹{fare:.2f}")
except ValueError:
    print("\nInvalid input! Please enter correct numeric values.")