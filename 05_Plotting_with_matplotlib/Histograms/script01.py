'''
Build a histogram (1)
100xp
life_exp, the list containing data on the life expectancy for different countries in 2007, is available in your Python shell.

To see how life expectancy in different countries is distributed, let's create a histogram of life_exp.

matplotlib.pyplot is already available as plt.
'''
import matplotlib.pyplot as plt

# Create histogram of life_exp data (do not specify bins, python take it as 10 by default)
plt.hist(life_exp)

# Display histogram
plt.show()
