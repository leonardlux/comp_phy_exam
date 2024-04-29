import numpy as np
import config as c

# generate inital values

def inital_values(v_appl = c.v_appl):
    u_0 = (v_appl - c.v_mem) * np.exp(-1*(c.x_g-c.x_0)**2/(2*c.lambda_value**2)) + c.v_mem
    # scale to have correct inital mass in the system, even if part of the distribution is outside
    return u_0

print(inital_values())
