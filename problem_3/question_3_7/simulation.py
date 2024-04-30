import numpy as np
from scipy.sparse import diags   
#from numba import jit

import config as c
import opt_boundary_conditions  as opt_bc
import opt_right_side_functions as opt_rsf

"""
General note/commentary on computation and simulation: 
During this exam I tried to follow the KISS priniciple.
This includes using and adapting the allready working and tested parts from Assignment 1 and the working parts from the github of this lecture:
https://github.com/nordam/ComputationalPhysics/blob/master/Notebooks/02%20-%20Numerical%20precision.ipynb 

Moreover this is also the exact reason I decided against using numba. 
Numba would increase the performance of the code, but at the expense of time needed to adapt everything to be able to work with numba.
The could itself is not that slow (nothing needs more than a minute), therefore more optimization would just waste time and increase the probability of adding errors.
"""



# As mentioned early the following part is nearly completly adapted from my assignment 1 and the github repo.

def build_matrix_from_diag(diags_list):
    # unpack list
    main_diag, sup_diag, sub_diag, = diags_list
    # build a banded matrix using the different diagonals
    M = diags((sub_diag, main_diag, sup_diag), offsets = (-1, 0, 1),)# .toarray()
    return M

def gen_matricies(diags_gen, boundary_condition):
    # this function is not necessarily needed, but is a bit of legacy code, which does not need a lot of power
    # therefore it is allowed to stay. (And it makes this simulation.py more comparible to the previous one and the one in Assignment 1)
    # generate diags
    a_diags = diags_gen()
    # apply boundary conditons
    a_diags = boundary_condition(a_diags)
    # build Matrix
    A = build_matrix_from_diag(a_diags)
    return A


# taken from github of this course, after scipy did not work :( 
#@jit(nopython = True)
def tdma_solver(a, b, c, d):
    # Solves Ax = d,
    # where layout of matrix A is
    # b1 c1 ......... 0
    # a2 b2 c2 ........
    # .. a3 b3 c3 .....
    # .................
    # .............. cN-1
    # 0 ..........aN bN
    # Note index offset of a
    N = len(d)
    # Make to extra arrays to avoid overwriting input
    c_ = np.zeros(N-1)
    d_ = np.zeros(N)
    x  = np.zeros(N)
    c_[0] = c[0]/b[0]
    d_[0] = d[0]/b[0]
    for i in range(1, N-1):
        q = (b[i] - a[i-1]*c_[i-1])
        c_[i] = c[i]/q
        d_[i] = (d[i] - a[i-1]*d_[i-1])/q
    d_[N-1] = (d[N-1] - a[N-2]*d_[N-2])/(b[N-1] - a[N-2]*c_[N-2])
    x[-1] = d_[-1]
    for i in range(N-2, -1, -1):
        x[i] = d_[i] - c_[i]*x[i+1]
    return x

def tdma(A, b):
    # Solves Ax = b to find x
    # This is a wrapper function, which unpacks
    # A from a sparse array structure into separate diagonals,
    # and passes them to the numba-compiled solver defined above.
    x = tdma_solver(A.diagonal(-1), A.diagonal(0), A.diagonal(1), b)
    return x

# solve_simulation
def solve_simulation(starting_distr, diags_gen, cutoff = False):
    """
    starting_distr is now a vector
    """

    # initalize U
    U  = np.zeros((c.n_t,c.n_x),)
    U[0] = starting_distr

    # generate Matricies

    boundary_condition = opt_bc.boundary_conditions_neumann
    # boundary conditions are hardcoded, because we do not need to change them
    A = gen_matricies(diags_gen, boundary_condition)
    
    for n in range(0, c.n_t-1):
        # Calculate the function: F(u^n) = _u (right hand side)
        if cutoff:
            _u = opt_rsf.right_side_function_cutoff(U[n,:])
        else:
            _u = opt_rsf.right_side_function(U[n,:])
        # Then, solve equation A * u^(n+1) = _u
        U[n+1,:] = tdma(A,_u)
    return U
