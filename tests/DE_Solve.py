import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Gravitacijski pospešek [m/s^2]
g = 9.80665
# Masa uteži [kg]
m = 1
# Koeficient dušenja [kg/s]
b = 0.1
# Dolžina niahala [m]
l = 10
# Čas pri katerme želimo odčitati odmik nihala [s]
t_final = 100
# Število razdelitev na območju [0,t]
n_points = 10000


# Začetni pogoji
initial_position = 0.8  # začetni odmik nihala [rad]
initial_velocity = 0.0   # začetna kotna hitrost nihala [rad/s]

# Sistem diferencialnih enačb
def damped_pendulum(t, y):
    theta, omega = y
    dydt = [omega, - (b/m) * omega - (g/l) * np.sin(theta)]
    return dydt

# Časovni trak
t_eval = np.linspace(0, t_final, n_points)

# Definicija začetnih pogojev
y0 = [initial_position, initial_velocity]

# Reševanje diferencialne enačbe
solution = solve_ivp(damped_pendulum, [0, t_final], y0, t_eval=t_eval, method='RK45')

# Rezultati
t = solution.t
theta = solution.y[0]
theta_100 = theta[-1]
print(f"Odmik nitnega nihala ob času t = 100 sekund je {theta_100} rad.")




#---------------------------------------------------------------------------------------------------



# Koeficient vzmeti [N/m]
k = 10
# Masa uteži [kg]
m = 10
# Koeficient dušenja [kg/s]
b = 2
# Čas pri katerme želimo odčitati odmik nihala [s]
t_final = 100
# Število razdelitev na območju [0,t]
n_points = 10000

# Začetni pogoji
initial_position = 10  # začetni odmik nihala [m]
initial_velocity = 0.0   # začetna kotna hitrost nihala [m/s]


# Sistem difencialnih enačb
def damped_harmonic_oscillator(t, y):
    theta, omega = y
    dydt = [omega, - (b/m) * omega - (k/m) * theta]
    return dydt

# Časocni trak
t_eval = np.linspace(0, t_final, n_points)

# Definicija začetnih pogojev
y0 = [initial_position, initial_velocity]

# Reševanje diferencialne enačbe
solution = solve_ivp(damped_harmonic_oscillator, [0, t_final], y0, t_eval=t_eval, method='RK45')

# Rezultati
t = solution.t
theta = solution.y[0]
theta_100 = theta[-1]
print(f"Odmik vzmetnega nihala ob času t = 100 0sekund je {theta_100} m.")
