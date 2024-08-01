import numpy as np 
import matplotlib.pyplot as plt 

g = 9.80665

# Linearna predstavitev diferencialne enačbe druge stopnje, ki opisuje nihanje brez dušenja
# t -> čas [s]
# y -> linerane kombinacija sistema
# l -> dolžina nihala [m]
# g -> gravitacijski pospešek [m/s^2]
def f(t, y, l, g):
    theta, omega = y
    return np.array([omega, - (g / l) * np.sin(theta)])


# Linearna predstavitev diferencialne enačbe druge stopnje, ki opisuje harmonično nihanje
# t -> čas [s]
# y -> linerane kombinacija sistema
# k -> koeficient vzmeti [N/m]
# m -> masa nihala [kg]
def f_harmonic(t, y, k, m):
    theta, omega = y
    return np.array([omega, - (k / m) * theta])


# Linearna predstavitev diferencialne enačbe druge stopnje, ki opisuje nihanje vumeti z dušenjem
# t -> čas [s]
# y -> linerane kombinacija sistema
# b -> koeficient dušenja [kg/s]
# k -> koeficient vzmeti [N/m]
# m -> masa nihala [kg]
def f_damped(t, y, b, k, m):
    theta, omega = y
    return np.array([omega, - (b / m) * omega - (k/m)*theta])


# Linearna predstavitev diferencialne enačbe druge stopnje, ki opisuje nihanje nitnega nihala z dušenjem
# t -> čas [s]
# y -> linerane kombinacija sistema
# m -> masa nihala [kg]
# l -> dolžina nihala [m]
# g -> gravitacijski pospešek [m/s^2]
# b -> koeficient dušenja [kg/s
def f_damped_pendulum(t, y, m, l, g, b):
    theta, omega = y
    return np.array([omega, - (g / l) * np.sin(theta) - (b/m)*omega])



def nitno_nihalo(l, t, initial_angle, initial_speed, n, izris_grafa):
    '''
    l -> dolžina nihala [m]
    t -> čas pri katerem želimo odčitati odmik nihala [s]
    inital_angle -> začetni odmik nihala [rad]
    initial_speed -> začetna kotna hitrost nihala [rad/s]
    n -> število podintervalu na območnu [0,t]
    izris_grafa -> True or False
    '''
    h = t / (n - 1)  # Velikost koraka
    time = np.linspace(0, t, n)  # Časovna os


    y = np.zeros((n, 2))
    y[0] = [initial_angle, initial_speed]  # Dodajanje začetnih pogojev

    # Runge-Kutta metoda 4. reda
    for i in range(n-1): 
        k1 = h * f(time[i], y[i], l, g)
        k2 = h * f(time[i] + h/2, y[i] + k1/2, l, g)
        k3 = h * f(time[i] + h/2, y[i] + k2/2, l, g)
        k4 = h * f(time[i] + h, y[i] + k3, l, g)

        # Posodovitev vrednosti y
        y[i+1] = y[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6.0 

    theta_values = y[:, 0]  # Vrednsoti - odmik [rad]
    omega_values = y[:, 1]  # Vrednsoti - kotna hitrost [rad/s]

    if(izris_grafa == True):
        plt.plot(time, theta_values)
        plt.title('Odmik nitnega nihala brez dušenja')
        plt.xlabel('Čas [s]')
        plt.ylabel('Odmik [rad]')
        plt.grid(True)
        plt.show()

    return y[-1]




def harmonično_nihalo(m, k, t, initial_position, initial_speed, n, izris_grafa):
    '''
    m -> masa nihala [kg]
    k -> koeficient vzmeti [N/m]
    t -> čas pri katerem želimo odčitati odmik nihala [s]
    initial_position -> začetni odmik nihala [m]
    initial_speed -> začetna kotna hitrost nihala [m/s]
    n -> število podintervalu na območnu [0,t]
    izris_grafa -> True or False
    '''

    h = t / (n - 1)  # Velikost koraka
    time = np.linspace(0, t, n)  # Časovna os


    y = np.zeros((n, 2))
    y[0] = [initial_position, initial_speed]  # Dodajanje začetnih pogojev

    # Runge-Kutta metoda 4. reda
    for i in range(n-1): 
        k1 = h * f_harmonic(time[i], y[i], k, m)
        k2 = h * f_harmonic(time[i] + h/2, y[i] + k1/2, k, m)
        k3 = h * f_harmonic(time[i] + h/2, y[i] + k2/2, k, m)
        k4 = h * f_harmonic(time[i] + h, y[i] + k3, k, m)

        # Posodovitev vrednosti y
        y[i+1] = y[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6.0 

    theta_values = y[:, 0]   # Vrednsoti - odmik [m]
    omega_values = y[:, 1]   # Vrednsoti - hitrost [m/s]

    if(izris_grafa == True):
        plt.plot(time, theta_values)
        plt.title('Odmik harmoničnega nihala brez dušenja')
        plt.xlabel('Čas [s]')
        plt.ylabel('Odmik [m]')
        plt.grid(True)
        plt.show()

    return y[-1]




def duseno_harmonicno_nihalo(m, k, b, t, initial_position, initial_speed, n, izris_grafov):
    '''
    m -> masa nihala [kg]
    k -> koeficient vzmeti 
    b -> koeficient dušenja
    t -> čas pri katerem želimo odčitati odmik nihala [s]
    inital_angle -> začetni odmik nihala [rad]
    initial_speed -> začetna kotna hitrost nihala [rad/s]
    n -> število podintervalu na območnu [0,t]
    '''
    h = t / (n - 1)  # Velikost koraka
    time = np.linspace(0, t, n)  # Časovna os


    y = np.zeros((n, 2))
    y[0] = [initial_position, initial_speed]  # Dodajanje začetnih pogojev

    # Runge-Kutta metoda 4. reda
    for i in range(n-1): 
        k1 = h * f_damped(time[i], y[i], b,  k, m)
        k2 = h * f_damped(time[i] + h/2, y[i] + k1/2, b, k, m)
        k3 = h * f_damped(time[i] + h/2, y[i] + k2/2, b, k, m)
        k4 = h * f_damped(time[i] + h, y[i] + k3, b, k, m)

        # Update next value of y 
        y[i+1] = y[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6.0 

    theta_values = y[:, 0]  # Vrednsoti - odmik [m]
    omega_values = y[:, 1]  # Vrednsoti - hitrost [m/s]

    
    w0 = np.sqrt(k/m) # Začetna frekvenca nihanja

    theta_values_energy = np.zeros(len(theta_values))
    omega_values_energy = np.zeros(len(omega_values))
    energy = np.zeros(len(omega_values))

    for i in range(0,len(theta_values)):
        # Računanje vrednosti potencialne energija [J]
        # odmik^2 * osnovna_frekvenca^2 * masa * 0.5
        theta_values_energy[i] = theta_values[i] * theta_values[i] * 0.5 * m * w0*w0

    for i in range(0,len(omega_values)):
        # Računanje vrednosti kinetične energija [J]
        # hitrost^2 * masa * 0.5
        omega_values_energy[i] = omega_values[i] * omega_values[i] * 0.5 * m

    for i in range(0,len(energy)):
        energy[i] = theta_values_energy[i] + omega_values_energy[i]


    peaks = np.zeros(len(omega_values))
    peaks[0] = theta_values[0]
    parameter = 0

    # Iz izračunanega niza odmikov izluščimo "vrhove" - maksimume
    for i in range(1,len(theta_values)-1):
        if(theta_values[i] > 0 ):
            if(theta_values[i] > theta_values[i+1]):
                if(parameter == 0):
                    peaks[i] = theta_values[i]
            else:
                peaks[i] = 0
                parameter = 0
        else:
            peaks[i] = 0
        
        if(peaks[i-1] > 0):
            peaks[i] = 0
            parameter = 1


    period = []
    time_Table = []
    energy_table = []

    # Glede na ploožaj vrhovov odčitamo čas in velikost energije ko so se pojavili 
    for i in range(len(peaks)):
        if(peaks[i] > 0):
            period.append(peaks[i])
            time_Table.append(time[i])
            energy_table.append(energy[i])


    # Iz izluščenih maksimimov in časov ko so se pojavili izračunamo nihanji čas vsake periode nihanja
    oscillation_time = np.zeros(len(period))
    for i in range(len(period)-1):
        oscillation_time[i] = time_Table[i+1] - time_Table[i]
        if(i == len(period)-2):
            oscillation_time[i+1] = oscillation_time[i]


    if(izris_grafov == True):
        plt.plot(time, theta_values, color = 'blue')
        plt.title('Odmik nihanja vzmetnega nihala z dušenjem')
        plt.xlabel('Čas [s]')
        plt.ylabel('Odmik [m]')
        plt.grid(True)
        plt.show()

        plt.plot(time, omega_values,  color = 'teal')
        plt.title('Hitrost vzmetnega nihala z dušenjem')
        plt.xlabel('Čas [s]')
        plt.ylabel('Hitrost [s/m]')
        plt.grid(True)
        plt.show()


        plt.plot(time, theta_values_energy, color = 'lightskyblue', label='Potencialna energija')
        plt.plot(time, omega_values_energy, color = 'lightpink', label = "Kinetična energija")
        plt.plot(time, energy, color = 'red', linewidth = 3.0, label = "Skupna energija")
        plt.title('Energija vzmetnega nihala')
        plt.xlabel('Čas [s]')
        plt.ylabel('Energija [J]')
        plt.grid(True)
        leg = plt.legend()
        plt.show()


        plt.plot(time_Table, oscillation_time, color = 'lightskyblue')
        plt.title('Nihajni čas vzmetnega nihala v odvisnosti od časa')
        plt.xlabel('Čas [s]')
        plt.ylabel('Nihanji čas [s]')
        plt.grid(True)
        plt.margins(0, 700)
        plt.show()


    return y[-1], oscillation_time[0]




def duseno_nitno_nihalo(m, l, g, b, t, initial_position, initial_speed, n, izris_grafov):
    '''
    # m -> masa nihala [kg]
    # l -> dolžina nihala [m]
    # g -> gravitacijski pospešek [m/s^2]
    # b -> koeficient dušenja
    t -> čas pri katerem želimo odčitati odmik nihala [s]
    inital_angle -> začetni odmik nihala [rad]
    initial_speed -> začetna kotna hitrost nihala [rad/s]
    n -> število podintervalu na območnu [0,t]
    '''
    h = t / (n - 1)  # Velikost koraka
    time = np.linspace(0, t, n)  # Časovna os


    y = np.zeros((n, 2))
    y[0] = [initial_position, initial_speed]  # Dodajanje začetnih pogojev

    # Runge-Kutta metoda 4. reda
    for i in range(n-1): 
        k1 = h * f_damped_pendulum(time[i], y[i], m,  l, g, b)
        k2 = h * f_damped_pendulum(time[i] + h/2, y[i] + k1/2, m,  l, g, b)
        k3 = h * f_damped_pendulum(time[i] + h/2, y[i] + k2/2, m,  l, g, b)
        k4 = h * f_damped_pendulum(time[i] + h, y[i] + k3, m,  l, g, b)

        # Update next value of y 
        y[i+1] = y[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6.0 

    theta_values = y[:, 0]  # Vrednsoti - odmik [m]
    omega_values = y[:, 1]  # Vrednsoti - hitrost [m/s]

    
    w0 = np.sqrt(g/l) # Začetna frekvenca nihanja

    theta_values_energy = np.zeros(len(theta_values))
    omega_values_energy = np.zeros(len(omega_values))
    energy = np.zeros(len(omega_values))

    for i in range(0,len(theta_values)):
        # Računanje vrednosti potencialne energija [J]
        # odmik^2 * osnovna_frekvenca^2 * masa * 0.5
        theta_values_energy[i] = theta_values[i] * theta_values[i] * 0.5 * m * w0*w0

    for i in range(0,len(omega_values)):
        # Računanje vrednosti kinetične energija [J]
        # hitrost^2 * masa * 0.5
        omega_values_energy[i] = omega_values[i] * omega_values[i] * 0.5 * m

    for i in range(0,len(energy)):
        energy[i] = theta_values_energy[i] + omega_values_energy[i]



    peaks = np.zeros(len(omega_values))
    peaks[0] = theta_values[0]
    parameter = 0

    # Iz izračunanega niza odmikov izluščimo "vrhove" - maksimume
    for i in range(1,len(theta_values)-1):
        if(theta_values[i] > 0 ):
            if(theta_values[i] > theta_values[i+1]):
                if(parameter == 0):
                    peaks[i] = theta_values[i]
            else:
                peaks[i] = 0
                parameter = 0
        else:
            peaks[i] = 0
        
        if(peaks[i-1] > 0):
            peaks[i] = 0
            parameter = 1


    period = []
    time_Table = []
    energy_table = []

    # Glede na ploožaj vrhovov odčitamo čas in velikost energije ko so se pojavili 
    for i in range(len(peaks)):
        if(peaks[i] > 0):
            period.append(peaks[i])
            time_Table.append(time[i])
            energy_table.append(energy[i])

    print(energy_table)
    # Iz izluščenih maksimimov in časov ko so se pojavili izračunamo nihanji čas vsake periode nihanja
    oscillation_time = np.zeros(len(period))
    for i in range(len(period)-1):
        oscillation_time[i] = time_Table[i+1] - time_Table[i]
        if(i == len(period)-2):
            oscillation_time[i+1] = oscillation_time[i]



    if(izris_grafov == True):
        plt.plot(time, theta_values, color = 'blue')
        plt.title('Odmik nihanja nitnega nihala z dušenjem')
        plt.xlabel('Čas [s]')
        plt.ylabel('Odmik [rad]')
        plt.grid(True)
        plt.show()

        plt.plot(time, omega_values,  color = 'teal')
        plt.title('Hitrost nihanja nitenga nihala z dušenjem')
        plt.xlabel('Čas [s]')
        plt.ylabel('Hitrost [rad/s]')
        plt.grid(True)
        plt.show()


        plt.plot(time, theta_values_energy, color = 'lightskyblue', label='Potencialna energija')
        plt.plot(time, omega_values_energy, color = 'lightpink', label = "Kinetična energija")
        plt.plot(time, energy, color = 'red', linewidth = 3.0, label = "Skupna energija")
        plt.title('Energija nitenga nihala')
        plt.xlabel('Čas [s]')
        plt.ylabel('Energija [J]')
        plt.grid(True)
        leg = plt.legend()
        plt.show()

        plt.plot(energy_table, oscillation_time, color = 'lightskyblue')
        plt.title('Nihajni čas nitenga nihala v odvisnosti od energije sistema')
        plt.xlabel('Energija sistema [J]')
        plt.ylabel('Nihanji čas [s]')
        plt.grid(True)
        plt.show()


    return y[-1], oscillation_time[0]