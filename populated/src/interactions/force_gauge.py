
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
    potential = gauge_field(position)
    force = -np.gradient(potential)
    return force
