
def initialize_electric_field(strength, direction):
    """
    Initialize an electric field with given strength and direction.
    
    Parameters:
    strength (float): Strength of the electric field.
    direction (list): Direction of the electric field as [dx, dy, dz].
    
    Returns:
    dict: Dictionary containing electric field properties.
    """
    electric_field = {
        'strength': strength,
        'direction': direction
    }
    return electric_field

def initialize_magnetic_field(strength, direction):
    """
    Initialize a magnetic field with given strength and direction.
    
    Parameters:
    strength (float): Strength of the magnetic field.
    direction (list): Direction of the magnetic field as [dx, dy, dz].
    
    Returns:
    dict: Dictionary containing magnetic field properties.
    """
    magnetic_field = {
        'strength': strength,
        'direction': direction
    }
    return magnetic_field

def initialize_scalar_field(potential_function):
    """
    Initialize a scalar field with a given potential function.
    
    Parameters:
    potential_function (callable): Potential function of the scalar field.
    
    Returns:
    dict: Dictionary containing scalar field properties.
    """
    scalar_field = {
        'potential_function': potential_function
    }
    return scalar_field

def initialize_gauge_field(gauge_potential):
    """
    Initialize a gauge field with a given gauge potential.
    
    Parameters:
    gauge_potential (callable): Gauge potential of the field.
    
    Returns:
    dict: Dictionary containing gauge field properties.
    """
    gauge_field = {
        'gauge_potential': gauge_potential
    }
    return gauge_field

def example_potential_function(position):
    """
    Example potential function for a scalar field.
    
    Parameters:
    position (list): Position as [x, y, z].
    
    Returns:
    float: Value of the potential at the given position.
    """
    x, y, z = position
    return x**2 + y**2 + z**2

def example_gauge_potential(position):
    """
    Example gauge potential for a gauge field.
    
    Parameters:
    position (list): Position as [x, y, z].
    
    Returns:
    list: Value of the gauge potential at the given position as [Ax, Ay, Az].
    """
    x, y, z = position
    return [x, y, z]
