import numpy as np
"""
## Boundary conditions
This is a mathematical sound way to compute the boundary conditions, regardless what the values of the matrix are. 
I derived this term for assignment 1 and will therefore not go into detail on why this works.
This is also rather trivial.
"""

def boundary_conditions_neumann(diags_list):
    # split up diags (the side diags come in one to long)
    main_diag, sup_diag, sub_diag, = diags_list
    # change correct values of matr
    # we need to add the first value of sub to sup and then remove it from sub
    sup_diag[ 0] = sup_diag[0] + sub_diag[0]
    sub_diag     = sub_diag[1:]
    # same for the last index and the sub diag
    sub_diag[-1] = sup_diag[-1] + sub_diag[-1]
    sup_diag     = sup_diag[:-1]

    return (main_diag, sup_diag, sub_diag)