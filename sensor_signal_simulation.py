import numpy as np
import matplotlib.pyplot as plt

# Time
t = np.linspace(0, 10, 100)

# True temperature (smooth signal)
true_temp = 25 + 5*np.sin(t)

# Add noise (simulate sensor error)
noise = np.random.normal(0, 1.5, size=t.shape)
measured_temp = true_temp + noise

# Moving average filter
window = 10
filtered_temp = np.convolve(measured_temp, np.ones(window)/window, mode='same')

# Plot
plt.figure()
plt.plot(t, true_temp, label="True Signal")
plt.plot(t, measured_temp, label="Noisy Sensor Output")
plt.plot(t, filtered_temp, label="Filtered Signal")
plt.legend()
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.title("Sensor Measurement Simulation")
plt.show()

error_before = np.mean(np.abs(true_temp - measured_temp))
error_after = np.mean(np.abs(true_temp - filtered_temp))

print("Error before filtering:", error_before)
print("Error after filtering:", error_after)