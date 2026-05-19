import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
time = np.arange(0, 100, 1)

# Desired temperature
setpoint = 25

# Initial room temperature
room_temp = 18

# Lists for plotting
temperature_history = []
heater_history = []

# Heater state
heater_on = False

for t in time:

    # Control logic
    if room_temp < setpoint:
        heater_on = True
    else:
        heater_on = False

    # Temperature dynamics
    if heater_on:
        room_temp += 0.3
    else:
        room_temp -= 0.1

    # Store values
    temperature_history.append(room_temp)
    heater_history.append(int(heater_on))

# Plot temperature
plt.figure(figsize=(10,5))
plt.plot(time, temperature_history, label="Room Temperature")
plt.axhline(setpoint, color='r', linestyle='--', label="Setpoint")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.title("Smart Temperature Control Simulation")
plt.legend()
plt.grid()

plt.show()