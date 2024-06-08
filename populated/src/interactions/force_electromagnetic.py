
def force_electromagnetic(particle, electric_field, magnetic_field):
    """
    Calculate the electromagnetic force on a particle due to electric and magnetic fields.
    
    Parameters:
    particle (dict): Properties of the particle.
    electric_field (callable): Function defining the electric field.
    magnetic_field (callable): Function defining the magnetic field.
    
    Returns:
    array: Electromagnetic force acting on the particle.
    """
    import numpy as np
    charge = particle['charge']
    velocity = np.array(particle['velocity'])
    position = np.array(particle['position'])
    
    E = np.array(electric_field(position))
    B = np.array(magnetic_field(position))
    
    F_electric = charge * E
    F_magnetic = charge * np.cross(velocity, B)
    
    F_em = F_electric + F_magnetic
    return F_em
