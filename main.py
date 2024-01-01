from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np


fig = plt.figure()
plt.style.use('default')


ax = fig.add_subplot(111, projection='3d')
plt.title("Figure 5.3: 3D Regression of Square of Velocity, Angle of Attack, and Lift Force using Figure 5.1 and 5.2")


ax.set_xlabel('Square of Velocity/m^2s^-2')
ax.set_ylabel('Angle of Attack/°')
ax.set_zlabel('Lift Force/N')
# actual surface
for count in range(-10, 181):
    x1 = np.linspace(0, 20, 20)


    y1 = np.linspace(count / 10, count / 10, 20)


    z1 = 3.11 * (0.02193 * x1 - 0.02658) * (0.01412 * y1 + 0.06561)


    if count % 50 == 0:
        ax.plot(x1, y1, z1, color="white", alpha=1)
    else:
        ax.plot(x1, y1, z1, color="blue", alpha=0.3)


for count in range(0, 20):
    if count % 5 == 0:
        x1 = np.linspace(count, count, 20)


        y1 = np.linspace(-1, 18, 20)


        z1 = 3.11 * (0.02193 * x1 - 0.02658) * (0.01412 * y1 + 0.06561)
        ax.plot(x1, y1, z1, color="white", alpha=1)


for count in range(-180, -10):
    x1 = np.linspace(0, 20, 20)


    y1 = np.linspace(count / 10, count / 10, 20)


    z1 = 3.11 * (0.02193 * x1 - 0.02658) * (0.000237 * y1 ** 2 + 0.01356 * y1 + 0.06655)


    if count % 50 == 0:
        ax.plot(x1, y1, z1, color="white", alpha=1)
    else:
        ax.plot(x1, y1, z1, color="blue", alpha=0.3)


for count in range(0, 20):
    if count % 5 == 0:
        x1 = np.linspace(count, count, 20)


        y1 = np.linspace(-18, -1, 20)


        z1 = 3.11 * (0.02193 * x1 - 0.02658) * (0.000237 * y1 ** 2 + 0.01356 * y1 + 0.06655)
        ax.plot(x1, y1, z1, color="white", alpha=1)


# x = 20
for count in range(-90, -5):
    x1 = 20
    x2 = np.linspace(x1, x1, 20)


    y1 = count/5
    y2 = np.linspace(y1, y1, 20)


    z2 = np.linspace(0, 3.11 * (0.02193 * x1 - 0.02658) * (0.000237 * y1 ** 2 + 0.01356 * y1 + 0.06655), 20)


    if count % 25 == 0:
        ax.plot(x2, y2, z2, color="white", alpha=0.3)
    else:
        ax.plot(x2, y2, z2, color="blue", alpha=0.2)


for count in range(-5, 90):
    x1 = 20
    x2 = np.linspace(x1, x1, 20)


    y1 = count/5
    y2 = np.linspace(y1, y1, 20)


    z2 = np.linspace(0, 3.11 * (0.02193 * x1 - 0.02658) * (0.01412 * y1 + 0.06561), 20)
    if count % 25 == 0:
        ax.plot(x2, y2, z2, color="white", alpha=0.3)
    else:
        ax.plot(x2, y2, z2, color="blue", alpha=0.2)






# y = 18
for count in range(0, 200):
    x1 = count/10
    x2 = np.linspace(x1, x1, 20)


    y1 = 18
    y2 = np.linspace(y1, y1, 20)


    z2 = np.linspace(0, 3.11 * (0.02193 * x1 - 0.02658) * (0.01412 * y1 + 0.06561), 20)


    if count % 50 == 0:
        ax.plot(x2, y2, z2, color="white", alpha=0.3)
    else:
        ax.plot(x2, y2, z2, color="blue", alpha=0.2)


# y = -18
for count in range(0, 200):
    x1 = count/10
    x2 = np.linspace(x1, x1, 20)


    y1 = -18
    y2 = np.linspace(y1, y1, 20)


    z2 = np.linspace(0, 3.11 * (0.02193 * x1 - 0.02658) * (0.000237 * y1 ** 2 + 0.01356 * y1 + 0.06655), 20)


    if count % 50 == 0:
        ax.plot(x2, y2, z2, color="white", alpha=0.3)
    else:
        ax.plot(x2, y2, z2, color="blue", alpha=0.2)


# z = 0
for count in range(0, 100):
    x2 = np.linspace(count/5, count/5, 20)


    y2 = np.linspace(-18, 18, 20)


    z2 = np.linspace(0, 0, 20)


    ax.plot(x2, y2, z2, color="black", alpha=0.5)


ax.set_xlim3d(0, 20)
ax.set_ylim3d(-18, 18)
ax.set_zlim3d(-0.2, 0.5)


# plot data point for theta and f
v = np.linspace(16, 16, 19)


theta = [-18.0,
-16.0,
-14.0,
-12.0,
-10.0,
-8.0,
-6.0,
-4.0,
-2.0,
0.0,
2.0,
4.0,
6.0,
8.0,
10.0,
12.0,
14.0,
16.0,
18.0,]


F = [-0.101,
-0.088,
-0.079,
-0.064,
-0.039,
-0.031,
-0.005,
0.015,
0.041,
0.062,
0.089,
0.115,
0.144,
0.174,
0.201,
0.226,
0.249,
0.292,
0.323]
for count in range(0,19):
    ax.plot(v[count], theta[count], F[count], color="orange", alpha=1, marker="x")


v = [17.36,
13.69,
11.11,
6.08,
9.00,
16.00,
3.87]


theta = np.linspace(18, 18, 7)


F = [0.364,
0.263,
0.202,
0.126,
0.174,
0.323,
0.049]


for count in range(0,7):
    ax.plot(v[count], theta[count], F[count], color="orange", alpha=1, marker="x")


plt.show()

