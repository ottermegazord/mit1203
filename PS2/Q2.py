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
# A
pert = 1
x_range = np.linspace(0,20, 21)
T = np.full((len(x_range),1), 20)
pert_range = np.linspace(0,10., 21)

# B
N_0 = 20.
ld_l = 0
ld_r = 0
W_b = np.linspace(0,20., 21)

print T

# mean_timeA = (T/2) - pert
# plt.plot(x_range, mean_timeA)
# plt.title('Plot of mean waiting time against number of pedestrians with constant P')
# plt.xlabel("Number of Pedestrians / minute")
# plt.ylabel("Mean waiting time / minute""Number of Pedestrians / minute")
# plt.show()

for i in range(2):
    ld_r = ld_r + 0.1
    for j in range(2):
        ld_l = ld_l + 0.1
        P = ((N_0 - 1.) / (2.*(ld_l + ld_r))) - W_b
        #plt.legend(ld_l, ld_r)
        plt.plot(W_b, P, label='ld_l: %.1f, ld_r: %.1f' % (ld_l, ld_r))
plt.legend(loc='best')
plt.title('Plot of Perturbation time against waiting time (System B)')
plt.ylabel("Perturbation / minute")
#plt.ylim([0 , 30])
plt.xlabel("Waiting time / minute")
plt.show()


