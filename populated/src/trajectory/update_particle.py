
def update_particle(particle, force, time_step):
    """
    Update the particle's position and velocity based on the applied force and time step.
    
    Parameters:
    particle (dict): Properties of the particle.
    force (array): Force acting on the particle.
    time_step (float): Time step for the update.
    
    Returns:
    dict: Updated particle properties.
    """
    import numpy as np
    position = np.array(particle['position'])
    velocity = np.array(particle['velocity'])
    mass = particle['mass']
    
    acceleration = force / mass
    new_velocity = velocity + acceleration * time_step
    new_position = position + new_velocity * time_step
    
    particle['position'] = new_position.tolist()
    particle['velocity'] = new_velocity.tolist()
    
    return particle
