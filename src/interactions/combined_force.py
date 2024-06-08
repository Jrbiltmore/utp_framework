
def combined_force(particle, fields):
    """
    Calculate the combined force on a particle due to multiple fields.
    
    Parameters:
    particle (dict): Properties of the particle.
    fields (dict): Dictionary containing different fields and their respective functions.
    
    Returns:
    array: Combined force acting on the particle.
    """
    import numpy as np
    total_force = np.zeros(3)
    
    for field_type, field_function in fields.items():
        field = field_function['field']
        force_function = field_function['force']
        total_force += force_function(particle, field)
    
    return total_force
