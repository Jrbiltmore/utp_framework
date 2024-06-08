
def calculate_gauge_potential(gauge_field, position):
    """
    Calculate the gauge potential at a given position.
    
    Parameters:
    gauge_field (callable): Function defining the gauge field.
    position (list): Position as [x, y, z].
    
    Returns:
    array: Gauge potential at the given position.
    """
    return gauge_field(position)

def force_gauge(particle, gauge_field):
    """
    Calculate the force on a particle due to a gauge field.
    
    Parameters:
    particle (dict): Properties of the particle.
    gauge_field (callable): Function defining the gauge field.
    
    Returns:
    array: Force on the particle due to the gauge field.
    """
    import numpy as np
    position = np.array(particle['position'])
    delta = 1e-5  # small change in position for numerical gradient calculation
    gradient = np.zeros_like(position)
    
    for i in range(len(position)):
        pos_forward = position.copy()
        pos_backward = position.copy()
        pos_forward[i] += delta
        pos_backward[i] -= delta
        gradient[i] = (gauge_field(pos_forward)[i] - gauge_field(pos_backward)[i]) / (2 * delta)
    
    return -gradient
