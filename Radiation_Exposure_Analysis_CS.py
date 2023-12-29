# Physics Experiment: Radiation Exposure Analysis

# The experiment is to measure the average radiation levels in various environments with high amounts of redioactive waste
# Inputs: rediation measurements for each location
# Insights: the average radiation level and standard deviation for each location

# Define the lists to store locations and their radiation levels

# Import numpy to calculate standard deviation

import numpy


locations = ["City Center", "Industrial Zone", "Residential District", "Rural Outskirts", "Downtown"]
levels = [[],[],[],[],[]]

for i, location in enumerate(locations):
    print(f"Processing {location}.")

# Data entry loop allowing continuous addition of measurements
   
    while True:
        level = (input("Enter radiation level or 'done' to finish : "))
        if level.lower() == 'done':
            break
        
        try:
            
            level = int(level)
            levels[i].append(level)
            print(level)
        except ValueError:
            print("Invalid input, please enter a number.")
    print(location)
    print(levels)

    

# Calculation of the average radiation level by location

for i, location in enumerate(locations):
    total = 0
    print(f"Processing {location}.")
    average = round(sum(levels[i]) / len(levels[i]))
    print(f"{location} average radiation level: {average}")

# Calculation of the standard deviation 
    print(f"Standard deviation of radiation parameters in {location} is % s", round(numpy.std(levels[i])))
    # print(f" The average radiation level in {location}: {average}")



'''
# New data input using a while loop

measurements = []
# Debugging: Inform the user that the data entry process is starting
print("Begin entering new radiation levels. Type 'done' to finish.")

# This loop will run indefinitely until 'done' is entered
while True:
    level = input("Enter radiation level or 'done' to finish: ")
    if level.lower() == 'done':
        # Debugging: Confirm that the loop exit condition has been met
        print("Debug: Exiting input loop.")
        break
    try:
        # Convert the input to an integer and add to the measurements list
        new_level = int(level)
        measurements.append(new_level)
        # Debugging: Confirm that a new level has been added
        print(f"Debug: Added level {new_level}")
    except ValueError:
        # Debugging: Inform the user of an invalid input
        print("Invalid input. Please enter a valid number or 'done'.")

# After exiting the loop, we'll calculate and display the average of the new measurements
if measurements:
    average = sum(measurements) / len(measurements)
    print(f"New Measurements Average Radiation Level: {average}")
else:
    # Debugging: Inform the user that no new measurements were entered
    print("Debug: No new measurements were entered.")
    '''