
def calculate_lagrangian(particle, potential_energy, kinetic_energy):
    """
    Calculate the Lagrangian for a particle.
    
    Parameters:
    particle (dict): Properties of the particle.
    potential_energy (float): Potential energy of the particle.
    kinetic_energy (float): Kinetic energy of the particle.
    
    Returns:
    float: Lagrangian of the particle.
    """
    lagrangian = kinetic_energy - potential_energy
    return lagrangian

def kinetic_energy(particle):
    """
    Calculate the kinetic energy of a particle.
    
    Parameters:
    particle (dict): Properties of the particle.
    
    Returns:
    float: Kinetic energy of the particle.
    """
    import numpy as np
    velocity = np.array(particle['velocity'])
    mass = particle['mass']
    ke = 0.5 * mass * np.dot(velocity, velocity)
    return ke

def potential_energy(particle, potential_field):
    """
    Calculate the potential energy of a particle in a given potential field.
    
    Parameters:
    particle (dict): Properties of the particle.
    potential_field (callable): Function defining the potential field.
    
    Returns:
    float: Potential energy of the particle.
    """
    position = particle['position']
    pe = potential_field(position)
    return pe
