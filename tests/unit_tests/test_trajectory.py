
import unittest
from src.trajectory.update_particle import update_particle
from src.trajectory.simulate_trajectory import simulate_particle_trajectory

class TestTrajectory(unittest.TestCase):
    def test_update_particle(self):
        particle = {'mass': 1.0, 'charge': 1.0, 'spin': 0.5, 'position': [0, 0, 0], 'velocity': [1, 0, 0], 'wavefunction': None}
        force = [0, 0, -9.8]
        time_step = 0.01
        updated_particle = update_particle(particle, force, time_step)
        self.assertEqual(len(updated_particle['position']), 3)
        self.assertEqual(len(updated_particle['velocity']), 3)
    
    def test_simulate_particle_trajectory(self):
        particle = {'mass': 1.0, 'charge': 1.0, 'spin': 0.5, 'position': [0, 0, 0], 'velocity': [1, 0, 0], 'wavefunction': None}
        fields = {
            'gravitational': {'field': None, 'force': lambda p, f: [0, 0, -9.8]},
            'electric': {'field': lambda pos: [1, 0, 0], 'force': lambda p, f: [1, 0, 0]}
        }
        total_time = 1.0
        time_step = 0.01
        trajectory = simulate_particle_trajectory(particle, fields, total_time, time_step)
        self.assertEqual(len(trajectory), int(total_time / time_step))

if __name__ == '__main__':
    unittest.main()
