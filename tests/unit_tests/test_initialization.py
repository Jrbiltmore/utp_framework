
import unittest
from src.initialization.initialize_particle import initialize_particle
from src.initialization.initialize_fields import initialize_electric_field, initialize_magnetic_field

class TestInitialization(unittest.TestCase):
    def test_initialize_particle(self):
        particle = initialize_particle(mass=1.0, charge=1.0, spin=0.5, position=[0, 0, 0], velocity=[1, 0, 0], wavefunction=None)
        self.assertEqual(particle['mass'], 1.0)
        self.assertEqual(particle['charge'], 1.0)
        self.assertEqual(particle['spin'], 0.5)
        self.assertEqual(particle['position'], [0, 0, 0])
        self.assertEqual(particle['velocity'], [1, 0, 0])
    
    def test_initialize_electric_field(self):
        electric_field = initialize_electric_field(strength=1.0, direction=[1, 0, 0])
        self.assertEqual(electric_field['strength'], 1.0)
        self.assertEqual(electric_field['direction'], [1, 0, 0])
    
    def test_initialize_magnetic_field(self):
        magnetic_field = initialize_magnetic_field(strength=1.0, direction=[0, 1, 0])
        self.assertEqual(magnetic_field['strength'], 1.0)
        self.assertEqual(magnetic_field['direction'], [0, 1, 0])

if __name__ == '__main__':
    unittest.main()
