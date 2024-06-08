
def gradient(scalar_field, position, delta=1e-5):
    """
    Calculate the gradient of a scalar field at a given position.
    
    Parameters:
    scalar_field (callable): Function defining the scalar field.
    position (list): Position as [x, y, z].
    delta (float): Small change in position for numerical gradient calculation.
    
    Returns:
    array: Gradient of the scalar field at the given position.
    """
    import numpy as np
    position = np.array(position)
    grad = np.zeros_like(position)
    
    for i in range(len(position)):
        pos_forward = position.copy()
        pos_backward = position.copy()
        pos_forward[i] += delta
        pos_backward[i] -= delta
        grad[i] = (scalar_field(pos_forward) - scalar_field(pos_backward)) / (2 * delta)
    
    return grad

def divergence(vector_field, position, delta=1e-5):
    """
    Calculate the divergence of a vector field at a given position.
    
    Parameters:
    vector_field (callable): Function defining the vector field.
    position (list): Position as [x, y, z].
    delta (float): Small change in position for numerical divergence calculation.
    
    Returns:
    float: Divergence of the vector field at the given position.
    """
    import numpy as np
    position = np.array(position)
    div = 0.0
    
    for i in range(len(position)):
        pos_forward = position.copy()
        pos_backward = position.copy()
        pos_forward[i] += delta
        pos_backward[i] -= delta
        div += (vector_field(pos_forward)[i] - vector_field(pos_backward)[i]) / (2 * delta)
    
    return div

def curl(vector_field, position, delta=1e-5):
    """
    Calculate the curl of a vector field at a given position.
    
    Parameters:
    vector_field (callable): Function defining the vector field.
    position (list): Position as [x, y, z].
    delta (float): Small change in position for numerical curl calculation.
    
    Returns:
    array: Curl of the vector field at the given position.
    """
    import numpy as np
    position = np.array(position)
    curl = np.zeros_like(position)
    
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
                partial_i = (vector_field(pos_forward_i)[j] - vector_field(pos_backward_i)[j]) / (2 * delta)
                partial_j = (vector_field(pos_forward_j)[i] - vector_field(pos_backward_j)[i]) / (2 * delta)
                curl[i] += partial_i - partial_j
    
    return curl
