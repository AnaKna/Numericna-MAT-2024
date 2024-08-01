import unittest
import sys

sys.path.append('.')
from src.Nihala import nitno_nihalo, duseno_harmonicno_nihalo, duseno_nitno_nihalo, harmonično_nihalo




#--------------------------------TEST - NITNO NIHALO BREZ DUŠENJA----------------------------------------------------------

class TestNitnoNihalo(unittest.TestCase):

    def test_nitno_nihalo(self):
        """Testiranje funkcije za izračun sistema nihanja nitnega nihala brez dušenja"""
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
        initial_speed = 0  # Začetna kotna hitrsot [rad/s] 

        displacement = nitno_nihalo(l, t, initial_angle, initial_speed, n, False)
        predviden_rezultat = -0.29986 # displacement  -> theta(t) = initial_angle * cos( sqrt(g/l) * t)
        self.assertAlmostEqual(displacement[0], predviden_rezultat, places=2)




#--------------------------------TEST - HARMONIČNO VZMETNO NIHALO BREZ DUŠENJA----------------------------------------------------------

class TestVzmetnoNihalo(unittest.TestCase):

    def test_vzmetno_nihalo(self):
        """Testiranje funkcije za izračun sistema nihanja vzmetnega nihala brez dušenja"""
        # Koeficient vzmeti [N/m]
        k = 0.5
        # Masa uteži [kg]
        m = 1.0
        # Čas pri katerme želimo odčitati odmik nihala [s]
        t = 100
        # Število razdelitev na območju [0,t]
        n = 1000

        # Začetni pogoji
        initial_position = 1.0  # začetni odmik nihala [m]
        initial_velocity = 0.0  # začetna kotna hitrost nihala [m/s]

        displacement = harmonično_nihalo(m, k, t, initial_position, initial_velocity, n, False)
        predviden_rezultat = -0.02484 # displacement  -> theta(t) = initial_position*cos( sqrt(k/m) * t)
        self.assertAlmostEqual(displacement[0], predviden_rezultat, places=4)





#--------------------------------TEST - NITNO NIHALO Z DUŠENJEM----------------------------------------------------------

class TestNitnoNihalo_dusenje(unittest.TestCase):

    def test_nitno_nihalo_dusenje(self):
        """Testiranje funkcije za izračun sistema nihanja nitnega nihala z dušenjem"""
        # Gravitacijski pospešek [m/s^2]
        g = 9.80665
        # Masa uteži [kg]
        m = 1
        # Koeficient dušenja [kg/s]
        b = 0.1
        # Dolžina niahala [m]
        l = 10
        # Čas pri katerme želimo odčitati odmik nihala [s]
        t = 100
        # Število razdelitev na območju [0,t]
        n = 10000

        # Začetni pogoji
        initial_position = 0.8  # začetni odmik nihala [rad]
        initial_velocity = 0.0   # začetna kotna hitrost nihala [rad/s]

        displacement, oscilation_time = duseno_nitno_nihalo(m, l, g, b, t, initial_position, initial_velocity, n, False)

        predviden_rezultat = -0.0023750194917456302 # Rezultat pridobljen iz DE_Solve.py
        self.assertAlmostEqual(displacement[0], predviden_rezultat, places=2)






#--------------------------------TEST - HARMONIČNO VZMETNO NIHALO Z DUŠENJEM----------------------------------------------------------

class TestVzmetnoNihalo_dusenje(unittest.TestCase):

    def test_vzmetno_nihalo_dusenje(self):
        """Testiranje funkcije za izračun sistema nihanja vzmetnega nihala z dušenjem"""
        # Koeficient vzmeti [N/m]
        k = 10
        # Masa uteži [kg]
        m = 10
        # Koeficient dušenja [kg/s]
        b = 2
        # Čas pri katerme želimo odčitati odmik nihala [s]
        t = 100
        # Število razdelitev na območju [0,t]
        n = 10000

        # Začetni pogoji
        initial_position = 10  # začetni odmik nihala [m]
        initial_velocity = 0.0   # začetna kotna hitrost nihala [m/s]

        displacement, oscilation_time = duseno_harmonicno_nihalo(m, k, b, t, initial_position, initial_velocity, n, False)
        predviden_rezultat = 0.00020064861611826393 # Rezultat pridobljen iz DE_Solve.py
        self.assertAlmostEqual(displacement[0], predviden_rezultat, places=4)



if __name__ == "__main__":
    unittest.main()
