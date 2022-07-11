import numpy as np
import matplotlib.pyplot as plt
seedx = 0.25
seedy = 0.95
total_num = 10000
period = 1e100
print(period)
a = 5214
c = 8689
random_num1 = []
random_num1.append(seedx / period)
N_i = []
N_i.append(seedx)
for i in range(total_num):
    N_i.append(np.mod(a * N_i[i - 1] + c, period))
    random_num1.append(N_i[i] / period)
random_num1 = np.array(random_num1, dtype=float)
random_num2 = []
random_num2.append(seedy / period)
N_i = []
N_i.append(seedy)
for i in range(total_num):
    N_i.append(np.mod(a * N_i[i - 1] + c, period))
    random_num2.append(N_i[i] / period)
random_num2 = np.array(random_num2, dtype=float)
no_inside_circle = 0
no_inside_circle_numpy = 0
x_numpy = np.random.random([total_num])
y_numpy = np.random.random([total_num])
for i in range(total_num):
    if np.power(random_num1[i], 2) + np.power(random_num2[i], 2) < 1.:
        no_inside_circle = no_inside_circle + 1
    if np.power(x_numpy[i], 2) + np.power(y_numpy[i], 2) < 1.:
        no_inside_circle_numpy = no_inside_circle_numpy + 1
monte_carlo_pi = 4 * (no_inside_circle / total_num)
numpy_rand_num_pi = 4 * (no_inside_circle_numpy / total_num)
print("Monter-Carlo value of pi using linear congruential generator: ", np.array(monte_carlo_pi, dtype=float),
      "\nMonter-Carlo value of pi using numpy random generator: ", np.array(numpy_rand_num_pi, dtype=float))
theta = np.linspace(0, np.pi / 2, 1000)
a = np.cos(theta)
b = np.sin(theta)

plt.scatter(random_num1, random_num2, marker='.', label='pseudo-random-points', color='yellow', linewidths=0.05)
plt.plot(a, b, label='circle', color='blue')
plt.legend()
plt.show()
plt.scatter(x_numpy, y_numpy, marker='.', label='numpy-random-points', color='orange', linewidths=0.05)
plt.plot(a, b, label='circle', color='red')
plt.legend()
plt.show()