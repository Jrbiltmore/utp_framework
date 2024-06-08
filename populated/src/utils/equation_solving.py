
def solve_linear_system(coeff_matrix, const_vector):
    """
    Solve a linear system of equations.
    
    Parameters:
    coeff_matrix (array): Coefficient matrix of the system.
    const_vector (array): Constant vector of the system.
    
    Returns:
    array: Solution vector.
    """
    import numpy as np
    solution = np.linalg.solve(coeff_matrix, const_vector)
    return solution

def solve_nonlinear_system(equations, initial_guess):
    """
    Solve a nonlinear system of equations using Newton-Raphson method.
    
    Parameters:
    equations (callable): Function defining the system of equations.
    initial_guess (array): Initial guess for the solution.
    
    Returns:
    array: Solution vector.
    """
    from scipy.optimize import fsolve
    solution = fsolve(equations, initial_guess)
    return solution
