
def calculate_scalar_potential(scalar_field, position):
    """
    Calculate the scalar potential at a given position.
    
    Parameters:
    scalar_field (callable): Function defining the scalar field.
    position (list): Position as [x, y, z].
    
    Returns:
    float: Scalar potential at the given position.
    """
    return scalar_field(position)

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
    delta = 1e-5  # small change in position for numerical gradient calculation
    gradient = np.zeros_like(position)
    
    for i in range(len(position)):
        pos_forward = position.copy()
        pos_backward = position.copy()
        pos_forward[i] += delta
        pos_backward[i] -= delta
        gradient[i] = (scalar_field(pos_forward) - scalar_field(pos_backward)) / (2 * delta)
    
    return -gradient
