
def initialize_particle(mass, charge, spin, position, velocity, wavefunction):
    """
    Initialize a quantum particle with given properties.
    
    Parameters:
    mass (float): Mass of the particle.
    charge (float): Charge of the particle.
    spin (float): Spin of the particle.
    position (list): Initial position of the particle as [x, y, z].
    velocity (list): Initial velocity of the particle as [vx, vy, vz].
    wavefunction (callable): Wavefunction of the particle.
    
    Returns:
    dict: Dictionary containing particle properties.
    """
    particle = {
        'mass': mass,
        'charge': charge,
        'spin': spin,
        'position': position,
        'velocity': velocity,
        'wavefunction': wavefunction
    }
    return particle

def example_wavefunction(position):
    """
    Example wavefunction for a quantum particle.
    
    Parameters:
    position (list): Position of the particle as [x, y, z].
    
    Returns:
    complex: Value of the wavefunction at the given position.
    """
    import numpy as np
    x, y, z = position
    return np.exp(-0.5 * (x**2 + y**2 + z**2)) + 1j * np.exp(-0.5 * (x**2 + y**2 + z**2))
