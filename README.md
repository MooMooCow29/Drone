# Drone Energy and Navigation Simulation

## Overview

This project simulates the behaviour of a delivery drone by modelling its **energy consumption, travel range, and route planning**. The system is written in Python and was developed as part of a programming assignment to demonstrate fundamental programming concepts such as functions, dictionaries, validation logic, simple algorithms, and object-oriented design.

The project is organised into four tasks, each building on the previous one to gradually construct a complete drone simulation system.

---

# Project Structure

```
Task1.py
Task2.py
Task3.py
Task4.py
Task4_Data.py
```

Each task focuses on a specific part of the system.

---

# Task 1; Drone Energy Model

Task 1 implements a **mathematical model of drone energy consumption**.

The program calculates the maximum distance a drone can travel by considering:

* Drone mass
* Air density
* Maximum available energy
* Takeoff and landing heights
* Flight speeds

The energy model separates the flight into **three phases**:

1. **Takeoff**
2. **Cruise**
3. **Landing**

Energy for takeoff and landing is calculated using:

```
Energy = (b1 * (m^1.5 / √p) + b0) * (h / V)
```

Where:

* `m` = drone mass
* `p` = air density
* `h` = height
* `V` = velocity
* `b1`, `b0` = experimentally derived constants

The program:

* Calculates energy for each phase
* Subtracts vertical flight energy from the total battery
* Computes the **maximum cruise distance**

The code also allows **custom flight parameters via user input**.

---

# Task 2; Destination Data Validation

Task 2 builds a **data processing system** for drone destinations.

The program reads an array of destination records and converts it into a **dictionary**.

Each destination contains:

```
[name, longitude, latitude, altitude, port_type]
```

Example:

```
["Warehouse4", 63.266, 51.491, 57, "Loading"]
```

### Validation rules

Each entry is checked to ensure:

* Destination names contain only letters, numbers, or `_`
* Longitude and latitude are numeric
* Longitude and latitude are within `-90 to 90`
* Altitude is between `0 and 100`
* Port type is either `Loading` or `Unloading`
* Duplicate names are ignored

Valid destinations are stored as:

```
destinations[name] = [lon, lat, alt, port]
```

The program also allows **users to manually add destinations** through console input, with the same validation rules applied.

---

# Task 3; Route Planning with KNN

Task 3 implements a **simple route generation algorithm** based on the **Nearest Neighbour approach**.

The goal is to create a path between locations by repeatedly selecting the closest destination.

Steps performed by the algorithm:

1. Start from an **origin node**
2. Compute the distance to every other node
3. Select the **nearest neighbour**
4. Add it to the route
5. Repeat until the destination is reached

Distance is calculated using the **Euclidean distance formula**:

```
distance = √((x2 - x1)^2 + (y2 - y1)^2)
```

This produces a route such as:

```
Origin → NodeA → NodeB → NodeC → Destination
```

The resulting path is stored as a **list of node names**.

---

# Task 4; Drone Class Implementation

Task 4 integrates the entire system using **object-oriented programming**.

A class called `Drone` is created to represent a drone and its capabilities.

### Drone Attributes

Each drone stores:

```
name
weight
current_energy
maximum_energy
destinations
current_path
```

### Drone Capabilities

The class includes methods to:

* Initialise a drone
* Access and modify attributes (getters/setters)
* Calculate flight energy using the model from **Task 1**
* Estimate travel range
* Load validated destinations from **Task 2**
* Generate routes using the **Task 3 KNN algorithm**
* Check if the drone has enough energy to complete a route

If energy is insufficient, the program identifies **nodes where the drone must recharge**.

---

# Example Workflow

1. Load destination dataset
2. Validate and store valid nodes
3. Create a drone instance
4. Generate a route between locations
5. Calculate energy consumption
6. Determine if the drone can complete the journey

---

# Key Programming Concepts Demonstrated

This project demonstrates several important programming concepts:

* Python functions
* Dictionaries and lists
* Input validation
* Exception handling
* Mathematical modelling
* Algorithmic route planning
* Object-oriented programming
* Modular program design

---

# Running the Project

1. Clone the repository

```
git clone https://github.com/yourusername/drone-simulation
```

2. Navigate into the project folder

```
cd drone-simulation
```

3. Run the scripts

```
python Task1.py
python Task2.py
python Task3.py
python Task4.py
```

---

# Future Improvements

Possible extensions to the project include:

* Implementing more accurate **geographical distance calculations**
* Adding **visualisation of routes**
* Simulating **battery degradation**
* Implementing **advanced path optimisation algorithms**


