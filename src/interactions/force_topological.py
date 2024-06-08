
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
    topological_value = topological_field(position)
    force = -np.gradient(topological_value)
    return force
