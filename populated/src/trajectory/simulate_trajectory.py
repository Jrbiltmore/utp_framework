
def simulate_particle_trajectory(particle, fields, total_time, time_step):
    """
    Simulate the trajectory of a particle under the influence of various fields.
    
    Parameters:
    particle (dict): Properties of the particle.
    fields (dict): Dictionary containing different fields and their respective functions.
    total_time (float): Total simulation time.
    time_step (float): Time step for numerical integration.
    
    Returns:
    list: List of particle positions at each time step.
    """
    import numpy as np
    from src.trajectory.update_particle import update_particle
    
    num_steps = int(total_time / time_step)
    trajectory = []
    
    for _ in range(num_steps):
        combined_force = combined_force(particle, fields)
        particle = update_particle(particle, combined_force, time_step)
        trajectory.append(particle['position'])
    
    return trajectory
