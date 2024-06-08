
def force_scalar(particle, scalar_field):
    """
    Calculate the force on a particle due to a scalar field.
    
    Parameters:
    particle (dict): Properties of the particle.
    scalar_field (callable): Function defining the scalar field.
    
    Returns:
    array: Force on the particle due to the scalar field.
    """
    import numpy as np
    position = np.array(particle['position'])
    gradient = np.gradient(scalar_field(position))
    force = -gradient
    return force
