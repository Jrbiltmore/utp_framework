
def force_gravitational(particle, metric_tensor):
    """
    Calculate the gravitational force on a particle in a given metric tensor.
    
    Parameters:
    particle (dict): Properties of the particle.
    metric_tensor (array): Metric tensor of the spacetime.
    
    Returns:
    array: Gravitational force acting on the particle.
    """
    import numpy as np
    position = particle['position']
    mass = particle['mass']
    # Placeholder for actual gravitational force calculation
    F_grav = -mass * np.array([0, 0, 9.8])  # Assuming a constant gravitational field
    return F_grav
