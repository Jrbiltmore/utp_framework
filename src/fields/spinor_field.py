
def calculate_spinor_field(spinor_field, position):
    """
    Calculate the spinor field at a given position.
    
    Parameters:
    spinor_field (callable): Function defining the spinor field.
    position (list): Position as [x, y, z].
    
    Returns:
    array: Spinor field at the given position.
    """
    return spinor_field(position)

def force_spinor(particle, spinor_field):
    """
    Calculate the force on a particle due to a spinor field.
    
    Parameters:
    particle (dict): Properties of the particle.
    spinor_field (callable): Function defining the spinor field.
    
    Returns:
    array: Force on the particle due to the spinor field.
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
        gradient[i] = (spinor_field(pos_forward)[i] - spinor_field(pos_backward)[i]) / (2 * delta)
    
    return -np.real(gradient)
