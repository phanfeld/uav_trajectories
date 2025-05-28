import numpy as np


t = np.linspace(0, 2 * np.pi, 30)
x = 0.5 * np.sin(2 * t)  # Horizontal figure 8
y = 1.5 * np.sin(t)  # Vertical figure 8
z = np.ones_like(t)  # Constant height at 1
yaw = np.zeros_like(t)  # Constant yaw
# self.target_trajectory = np.column_stack((x, y, z, yaw))


with open("figure8.csv", "w") as f:
    # f.write("t,x,y,z,yaw\n")
    for i in range(len(t)):
        f.write("{},{},{}\n".format(x[i], y[i], z[i]))