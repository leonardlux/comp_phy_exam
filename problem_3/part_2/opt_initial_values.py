import numpy as np
import config as c

"""
Here we define the inital value function.
This function is also defined on the exam sheat
"""

def inital_values(v_appl):
    v_0 = (v_appl - c.v_mem) * np.exp(-1*(c.x_g-c.x_0)**2/(2*c.lambda_value**2)) + c.v_mem
    # scale to have correct inital mass in the system, even if part of the distribution is outside
    return v_0
