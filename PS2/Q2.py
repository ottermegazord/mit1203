import numpy as np
import matplotlib.pyplot as plt


def graph(formula, x_range):
    x = np.array(x_range)
    y = eval(formula)
    plt.plot(x, y)
    plt.ylabel("Mean waiting time / minute")
    plt.xlabel("Pertubation term / minute")
    plt.show()

# Constants
pert = 1
x_range = np.linspace(0,100, 101)
T = np.full((len(x_range),1), 20)

print T

mean_timeA = (T/2) - pert
plt.plot(x_range, mean_timeA)
plt.show()
