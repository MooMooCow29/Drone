# Task 1
# 100500474
import math

# define b1 and b0
b1_cruise = 68.9  
b0_cruise = 16.8

b1_takeoff = 80.4
b0_takeoff = 13.8

b1_landing = 71.5
b0_landing = -24.3

# total energy (a)
def total_energy(m, p, h, V, mode):                                                
    
    if mode == "takeoff":
        energy_val = (b1_takeoff * (m**1.5 / math.sqrt(p)) + b0_takeoff) * (h / V)
    elif mode == "landing":
        energy_val = (b1_landing * (m**1.5 / math.sqrt(p)) + b0_landing) * (h / V)
    else:
        energy_val = 0
        
    return energy_val

# define the maximum range (b)
def calculate_distance(Vcr, m, p, Emax, h_takeoff, h_landing, V_takeoff, V_landing):
    
    # energy used in the vertical phases
    energy_takeoff = total_energy(m, p, h_takeoff, V_takeoff, "takeoff")
    energy_landing = total_energy(m, p, h_landing, V_landing, "landing")

    numerator = (Emax - (energy_takeoff + energy_landing)) * Vcr
    denominator = (b1_cruise * (m**1.5 / math.sqrt(p)) + b0_cruise)
    
    d_cruise = numerator / denominator
    return d_cruise

# defining flight scenarios and calculating distance using for loop
flights = [
    ("a", 12, 5, 1.2250, 1000000, 25, 25, 4, 4),
    ("b", 20, 2, 1.5359, 1000000, 100, 100, 2, 2),
    ("c", 4, 10, 1.0250, 1000000, 50, 100, 3, 1)
]

for flight_scenario, Vcr, m, p, Emax, h_takeoff, h_landing, V_takeoff, V_landing in flights:

    distance = calculate_distance(Vcr, m, p, Emax, h_takeoff, h_landing, V_takeoff, V_landing)

    print("----------------------------------------")
    print(f"Flight {flight_scenario}")
    print(f"Maximum cruise distance: {distance:.2f} meters")

# user-defined input
print("\nEnter custom flight parameters")

Vcr = float(input("Cruise speed(m/s): "))
m = float(input("Mass(kg): "))
p = float(input("Air density(kg/m^3): "))
Emax = float(input("Maximum energy(J): "))
h_takeoff = float(input("Takeoff height(m): "))
h_landing = float(input("Landing height(m): "))
V_takeoff = float(input("Takeoff speed(m/s): "))
V_landing = float(input("Landing speed(m/s): "))

distance = calculate_distance(Vcr, m, p, Emax, h_takeoff, h_landing, V_takeoff, V_landing)

print("Custom flight distance:", distance)