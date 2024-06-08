
def gradient(scalar_field, position):
    """
    Calculate the gradient of a scalar field at a given position.
    
    Parameters:
    scalar_field (callable): Function defining the scalar field.
    position (list): Position as [x, y, z].
    
    Returns:
    array: Gradient of the scalar field at the given position.
    """
    import numpy as np
    delta = 1e-5  # small change in position for numerical gradient calculation
    gradient = np.zeros(len(position))
    
    for i in range(len(position)):
        pos_forward = position.copy()
        pos_backward = position.copy()
        pos_forward[i] += delta
        pos_backward[i] -= delta
        gradient[i] = (scalar_field(pos_forward) - scalar_field(pos_backward)) / (2 * delta)
    
    return gradient

def divergence(vector_field, position):
    """
    Calculate the divergence of a vector field at a given position.
    
    Parameters:
    vector_field (callable): Function defining the vector field.
    position (list): Position as [x, y, z].
    
    Returns:
    float: Divergence of the vector field at the given position.
    """
    import numpy as np
    delta = 1e-5  # small change in position for numerical divergence calculation
    divergence = 0.0
    
    for i in range(len(position)):
        pos_forward = position.copy()
        pos_backward = position.copy()
        pos_forward[i] += delta
        pos_backward[i] -= delta
        divergence += (vector_field(pos_forward)[i] - vector_field(pos_backward)[i]) / (2 * delta)
    
    return divergence

def curl(vector_field, position):
    """
    Calculate the curl of a vector field at a given position.
    
    Parameters:
    vector_field (callable): Function defining the vector field.
    position (list): Position as [x, y, z].
    
    Returns:
    array: Curl of the vector field at the given position.
    """
    import numpy as np
    delta = 1e-5  # small change in position for numerical curl calculation
    curl = np.zeros(len(position))
    
    for i in range(len(position)):
        for j in range(len(position)):
            if i != j:
                pos_forward_i = position.copy()
                pos_backward_i = position.copy()
                pos_forward_j = position.copy()
                pos_backward_j = position.copy()
                pos_forward_i[i] += delta
                pos_backward_i[i] -= delta
                pos_forward_j[j] += delta
                pos_backward_j[j] -= delta
                curl[i] += (vector_field(pos_forward_j)[j] - vector_field(pos_backward_j)[j]) - (vector_field(pos_forward_i)[i] - vector_field(pos_backward_i)[i]) / (2 * delta)
    
    return curl
