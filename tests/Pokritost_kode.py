import sys
sys.path.append('.')
from src.Nihala import nitno_nihalo, duseno_harmonicno_nihalo, harmonično_nihalo, duseno_nitno_nihalo

# Gravitacijski pospešek [m/s^2]
g = 9.80665
# Dolžina niahala [m]
l = 1.0
# Čas pri katerme želimo odčitati odmik nihala [s]
t = 3
# Število razdelitev na območju [0,t]
n = 1000

# Začetni pogoji
initial_angle = 0.3 # Začetni odmik [rad]
initial_speed = 0   # Začetna kotna hitrsot [rad/s] 

displacement = nitno_nihalo(l, t, initial_angle, initial_speed, n, True)
print("Odmik nitenga nihala ob času t=" + str(t) + "s je " + str(round(displacement[0],5)) + " rad")



# Koeficient vzmeti [N/m]
k = 0.5
# Masa uteži [kg]
m = 1.0
# Čas pri katerme želimo odčitati odmik nihala [s]
t = 100
# Število razdelitev na območju [0,t]
n = 1000

# Initial conditions
initial_position = 1.0  # začetni odmik nihala [m]
initial_velocity = 0.0  # začetna kotna hitrost nihala [m/s]

displacement = harmonično_nihalo(m, k, t, initial_position, initial_velocity, n, True)
print("Odmik harmoničnega vzmetnega nihala ob času t=" + str(t) + "s je " + str(round(displacement[0],5)) + " m")



# Koeficient vzmeti [N/m]
k = 10
# Masa uteži [kg]
m = 10
# Koeficient dušenja [kg/s]
b = 0.6
# Čas pri katerme želimo odčitati odmik nihala [s]
t = 100
# Število razdelitev na območju [0,t]
n = 10000

# Initial conditions
initial_position = 2  # začetni odmik nihala [m]
initial_velocity = 0.0   # začetna kotna hitrost nihala [m/s]

displacement, oscilation_time = duseno_harmonicno_nihalo(m, k, b, t, initial_position, initial_velocity, n, True)
print("Odmik dušenega harmoničnega vzmetnega nihala ob času t=" + str(t) + "s je  " + str(round(displacement[0],5)) + " m")




# Gravitacijski pospešek [m/s^2]
g = 9.80665
# Masa uteži [kg]
m = 1
# Koeficient dušenja [kg/s]
b = 0.3
# Dolžina niahala [m]
l = 10
# Čas pri katerme želimo odčitati odmik nihala [s]
t = 100
# Število razdelitev na območju [0,t]
n = 10000

# Initial conditions
initial_position = 0.8  # začetni odmik nihala [rad]
initial_velocity = 0.0   # začetna kotna hitrost nihala [rad/s]

displacement, oscilation_time = duseno_nitno_nihalo(m, l, g, b, t, initial_position, initial_velocity, n, True)
print("Odmik dušenega nitenga nihala ob času t=" + str(t) + "s je  " + str(round(displacement[0],5)) + " rad")