# 1. DOMAČA NALOGA: Matematiˇcno nihalo

# Ana Knafelc, avgust 2024

## Opis

V projektu je podana implementacija funkcij za izračun odmika nihala ob poljubnem času.

<br/>


## Mapa src

V mapi "**src**", v skripti **Nihala.py** se nahajajo glavne funkcije za izračun:
- kotnega odmika nitnega nihala pri nedušenem nihanju (funkcija nitno_nihalo),
- odmika harmoničnega vzmetnega nihala pri nedušenem nihanju (funkcija harmonično_nihalo), 
- kotnega odmika nitnega nihala pri dušenem nihanju (funkcija duseno_nitno_nihalo),
- odmika harmoničnega vzmetnega nihala pri dušenem nihanju (funkcija duseno_harmonicno_nihalo).

<br/>

Primer uporabe funkcije **nitno_nihalo**:

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


<br/>


Primer uporabe funkcije **harmonično_nihalo**:

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



<br/>



Primer uporabe funkcije **duseno_nitno_nihalo**:

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



<br/>


Primer uporabe funkcije **duseno_harmonicno_nihalo**:

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


<br/>


Vse zgoraj navedene primere lahko preizkusite v skript **Pokritost_kode.py**.

<br/>
<br/>

## Mapa tests

V mapi "**tests**", v skripti **Test_algoritmov** se nahajajo naslednji testi:
- Test računanja kotnega odmika nihanja nitnega nihala brez dušenja,
- Test računanja odmika harmoničnega nihanja vzmetnega nihala brez dušenja,
- Test računanja kotnega odmika nihanja nitnega nihala z dušenjem,
- Test računanja odmika harmoničnega nihanja vzmetnega nihala z dušenjem.


<br/>
Za natančen izračun odmika nihanja vzmetnega in nitnega nihala z dušenjem, je bila uporabljena koda v skripti **DE_Solve.py**.
Vsi testi so uspešni z natančnostjo na najmanj 2 decimalki.
<br/>
<br/>
<br/>
<br/>

V skripti **Pokritost_kode.py** se izvedejo vse funkcije in njihove metode z namenom testiranja delovanja celotnega programa.\
Test pokritosti kode izvedemo v terminalu z naslednjimi zaporednimi ukazi:
```shell
python -m coverage run tests\00_Pokritost_kode.py report
```
in
```shell
coverage report -m
```
<br/>

Pokritost kode je 100%.
<br/>
