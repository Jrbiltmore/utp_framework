
def calculate_electric_field(vector_field, position):
    """
    Calculate the electric field at a given position.
    
    Parameters:
    vector_field (callable): Function defining the vector field.
    position (list): Position as [x, y, z].
    
    Returns:
    array: Electric field vector at the given position.
    """
    import numpy as np
    # Calculate the electric field at the given position using the provided vector field function
    electric_field = vector_field(position)
    return np.array(electric_field)

def calculate_magnetic_field(vector_field, position):
    """
    Calculate the magnetic field at a given position.
    
    Parameters:
    vector_field (callable): Function defining the vector field.
    position (list): Position as [x, y, z].
    
    Returns:
    array: Magnetic field vector at the given position.
    """
    import numpy as np
    # Calculate the magnetic field at the given position using the provided vector field function
    magnetic_field = vector_field(position)
    return np.array(magnetic_field)
