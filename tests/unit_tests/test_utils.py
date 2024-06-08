
import unittest
from src.utils.differential_operations import gradient, divergence, curl
from src.utils.tensor_calculations import calculate_metric_tensor, calculate_ricci_tensor, calculate_stress_energy_tensor
from src.utils.lagrangian_formulation import calculate_lagrangian, kinetic_energy, potential_energy
from src.utils.equation_solving import solve_linear_system, solve_nonlinear_system

class TestUtils(unittest.TestCase):
    def test_gradient(self):
        scalar_field = lambda x: x[0]**2 + x[1]**2 + x[2]**2
        position = [1, 1, 1]
        grad = gradient(scalar_field, position)
        self.assertEqual(len(grad), 3)
    
    def test_divergence(self):
        vector_field = lambda x: [x[0], x[1], x[2]]
        position = [1, 1, 1]
        div = divergence(vector_field, position)
        self.assertIsInstance(div, float)
    
    def test_curl(self):
        vector_field = lambda x: [x[0], x[1], x[2]]
        position = [1, 1, 1]
        crl = curl(vector_field, position)
        self.assertEqual(len(crl), 3)
    
    def test_calculate_metric_tensor(self):
        position = [1, 1, 1]
        metric_tensor = calculate_metric_tensor(position)
        self.assertEqual(metric_tensor.shape, (4, 4))
    
    def test_calculate_ricci_tensor(self):
        metric_tensor = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        ricci_tensor = calculate_ricci_tensor(metric_tensor)
        self.assertEqual(ricci_tensor.shape, (4, 4))
    
    def test_calculate_stress_energy_tensor(self):
        matter_fields = {}
        stress_energy_tensor = calculate_stress_energy_tensor(matter_fields)
        self.assertEqual(stress_energy_tensor.shape, (4, 4))
    
    def test_calculate_lagrangian(self):
        particle = {'mass': 1.0, 'position': [0, 0, 0], 'velocity': [1, 0, 0]}
        ke = kinetic_energy(particle)
        pe = potential_energy(particle, lambda x: x[0])
        lagrangian = calculate_lagrangian(particle, pe, ke)
        self.assertIsInstance(lagrangian, float)
    
    def test_solve_linear_system(self):
        coeff_matrix = [[3, 2], [1, 2]]
        const_vector = [1, 1]
        solution = solve_linear_system(coeff_matrix, const_vector)
        self.assertEqual(len(solution), 2)
    
    def test_solve_nonlinear_system(self):
        equations = lambda x: [x[0]**2 - 2 * x[0] - x[1] + 0.5, x[0]**2 + 4 * x[1]**2 - 4]
        initial_guess = [1, 1]
        solution = solve_nonlinear_system(equations, initial_guess)
        self.assertEqual(len(solution), 2)

if __name__ == '__main__':
    unittest.main()
