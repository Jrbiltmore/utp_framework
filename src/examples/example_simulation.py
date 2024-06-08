
from src.initialization.initialize_particle import initialize_particle
from src.initialization.initialize_fields import initialize_electric_field, initialize_magnetic_field
from src.trajectory.simulate_trajectory import simulate_particle_trajectory

# Initialize particle
particle = initialize_particle(mass=1.0, charge=1.0, spin=0.5, position=[0, 0, 0], velocity=[1, 0, 0], wavefunction=None)

# Initialize fields
electric_field = initialize_electric_field(strength=1.0, direction=[1, 0, 0])
magnetic_field = initialize_magnetic_field(strength=1.0, direction=[0, 1, 0])

fields = {
    'electric': {'field': electric_field, 'force': lambda p, f: f['strength'] * f['direction']},
    'magnetic': {'field': magnetic_field, 'force': lambda p, f: f['strength'] * f['direction']}
}

# Simulate trajectory
total_time = 10.0
time_step = 0.01
trajectory = simulate_particle_trajectory(particle, fields, total_time, time_step)

# Print trajectory
for position in trajectory:
    print(position)
