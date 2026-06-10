import numpy as np
import matplotlib.pyplot as plt

# 1. constants
q = 1.0            # charge
m = 1.0            #mass
B = np.array([0, 0, 1])   #uniform magnetic field(z direction)

# 2. time 
dt = 0.01        
steps = 2000       

# 3. initial conditions
v = np.array([1.0, 0.0, 1.0])   
r = np.array([0.0, 0.0, 0.0])

#4 
positions = []

# 5. 
for _ in range(steps):
    F = q * np.cross(v, B)      # محاسبه نیروی لورنتس
    a = F / m                   # شتاب
    v = v + a * dt               # به‌روزرسانی سرعت
    r = r + v * dt               # به‌روزرسانی موقعیت
    positions.append(r.copy())   # ذخیره موقعیت جدید

# 6. 
positions = np.array(positions)

# 7. plot trajectory
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')


ax.plot(positions[:, 0], positions[:, 1], positions[:, 2], label='Particle Path')


ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Charged Particle Motion in Uniform Magnetic Field")

plt.legend()
plt.show()