import numpy as np
import config as c

"""
# Here live the function, which generate the matricies, by creating the diagonals
"""

def diags_gen_backwards_euler():
    """
    backwards euler = implicit
    with A * v^{n+1}  = F(v^n)
    
    the function F, is calculated in the simulation function, which lives in a different file (simluation.py)

    """
    # generate diagonals
    a_main = np.ones(c.n_x) * (-1) * (2*c.lambda_value**2/c.delta_x**2 + c.tau/c.delta_t)
    a_sup  = np.ones(c.n_x) * c.lambda_value**2/c.delta_x**2
    a_sub  = np.ones(c.n_x) * c.lambda_value**2/c.delta_x**2
    a_diags = ( a_main, a_sup, a_sub )
    

    return a_diags

