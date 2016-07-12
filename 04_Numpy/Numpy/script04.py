'''
Lightweight baseball players
100xp
To subset both regular Python lists and Numpy arrays, you can use square brackets:

x = [4 , 9 , 6, 3, 1]
x[1]
import numpy as np
y = np.array(x)
y[1]
For Numpy specifically, you can also use boolean Numpy arrays:

high = y > 5
y[high]
The code that calculates the BMI of all baseball players is already included. Follow the instructions and reveal interesting things from the data!
'''

# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Calculate the BMI: bmi
np_height_m = np.array(height) * 0.0254
np_weight_kg = np.array(weight) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light = np.array(bmi<21)

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[bmi<21])
