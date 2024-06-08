
import unittest
from src.interactions.force_gravitational import force_gravitational
from src.interactions.force_electromagnetic import force_electromagnetic
from src.interactions.force_scalar import force_scalar
from src.interactions.force_gauge import force_gauge
from src.interactions.force_spinor import force_spinor
from src.interactions.force_topological import force_topological
from src.interactions.combined_force import combined_force

class TestInteractions(unittest.TestCase):
    def test_force_gravitational(self):
        particle = {'mass': 1.0, 'position': [0, 0, 0]}
        metric_tensor = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        force = force_gravitational(particle, metric_tensor)
        self.assertEqual(len(force), 3)
    
    def test_force_electromagnetic(self):
        particle = {'charge': 1.0, 'velocity': [1, 0, 0], 'position': [0, 0, 0]}
        electric_field = lambda pos: [1, 0, 0]
        magnetic_field = lambda pos: [0, 1, 0]
        force = force_electromagnetic(particle, electric_field, magnetic_field)
        self.assertEqual(len(force), 3)
    
    def test_force_scalar(self):
        particle = {'position': [0, 0, 0]}
        force = force_scalar(particle, lambda x: x[0])
        self.assertEqual(len(force), 3)
    
    def test_force_gauge(self):
        particle = {'position': [0, 0, 0]}
        force = force_gauge(particle, lambda x: [x[0], x[1], x[2]])
        self.assertEqual(len(force), 3)
    
    def test_force_spinor(self):
        particle = {'position': [0, 0, 0]}
        force = force_spinor(particle, lambda x: [x[0], x[1], x[2]])
        self.assertEqual(len(force), 3)
    
    def test_force_topological(self):
        particle = {'position': [0, 0, 0]}
        force = force_topological(particle, lambda x: x[0])
        self.assertEqual(len(force), 3)
    
    def test_combined_force(self):
        particle = {'mass': 1.0, 'charge': 1.0, 'spin': 0.5, 'position': [0, 0, 0], 'velocity': [1, 0, 0], 'wavefunction': None}
        fields = {
            'gravitational': {'field': None, 'force': force_gravitational},
            'electric': {'field': lambda pos: [1, 0, 0], 'force': lambda p, f: force_electromagnetic(p, f, lambda pos: [0, 1, 0])}
        }
        force = combined_force(particle, fields)
        self.assertEqual(len(force), 3)

if __name__ == '__main__':
    unittest.main()
