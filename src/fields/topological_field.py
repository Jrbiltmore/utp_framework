
def calculate_topological_charge(topological_field, position):
    """
    Calculate the topological charge at a given position.
    
    Parameters:
    topological_field (callable): Function defining the topological field.
    position (list): Position as [x, y, z].
    
    Returns:
    float: Topological charge at the given position.
    """
    return topological_field(position)

def force_topological(particle, topological_field):
    """
    Calculate the force on a particle due to a topological field.
    
    Parameters:
    particle (dict): Properties of the particle.
    topological_field (callable): Function defining the topological field.
    
    Returns:
    array: Force on the particle due to the topological field.
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
        gradient[i] = (topological_field(pos_forward) - topological_field(pos_backward)) / (2 * delta)
    
    return -gradient
