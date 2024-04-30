import numpy as np
import config as c

"""
# Here live the function, which generate the matricies, by creating the diagonals
"""

def diags_gen_forward_euler():
    """
    forward euler = explicit
    with A * v^{n+1}  = B * v^n
    
    for forward/explicit A is the unit matrix, but because I had an already working system I just did not remove A.
    """
    
    # generate diagonals
    a_main = np.ones(c.n_x) 
    a_sup  = np.ones(c.n_x) * 0 
    a_sub  = np.ones(c.n_x) * 0 
    a_diags = ( a_main, a_sup, a_sub )
    
    b_main  = np.ones(c.n_x) * (1 - c.b - 2*c.a*c.b )
    b_sup   = np.ones(c.n_x) * (c.a *c.b)
    b_sub   = np.ones(c.n_x) * (c.a *c.b)
    b_diags = ( b_main, b_sup, b_sub )

    return a_diags, b_diags


def diags_gen_backwards_euler():
    """
    backwards euler = implicit
    with A * v^{n+1}  = B * v^n
    
    for backwards/implicit B is the unit matrix, but because I had an already working system I just did not remove B.
    (Multiplication with uni Matrix does not change anything)
    """
    # generate diagonals
    a_main = np.ones(c.n_x) * (2 * c.a * c.b + 1) / (1 - c.b)
    a_sup  = np.ones(c.n_x) * (c.a * c.b) / (c.b - 1)
    a_sub  = np.ones(c.n_x) * (c.a * c.b) / (c.b - 1)
    a_diags = ( a_main, a_sup, a_sub )
    
    b_main  = np.ones(c.n_x) 
    b_sup   = np.ones(c.n_x) * 0
    b_sub   = np.ones(c.n_x) * 0
    b_diags = ( b_main, b_sup, b_sub )

    return a_diags, b_diags


def diags_gen_crank_nicholson():
    """
    crank nicholson
    with A * v^{n+1}  = B * v^n
    """
    # generate diagonals
    a_main = np.ones(c.n_x) * (-1) * (1 + c.a * c.b)
    a_sup  = np.ones(c.n_x) * (c.a * c.b /2)
    a_sub  = np.ones(c.n_x) * (c.a * c.b /2)
    a_diags = ( a_main, a_sup, a_sub )
    
    b_main  = np.ones(c.n_x) * (c.a * c.b + c.b - 1)
    b_sup   = np.ones(c.n_x) * (-1) * (c.a * c.b /2)
    b_sub   = np.ones(c.n_x) * (-1) * (c.a * c.b /2)
    b_diags = ( b_main, b_sup, b_sub )

    return a_diags, b_diags
