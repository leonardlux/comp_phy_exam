import numpy as np
import config as c

# generate inital values following the given constraints

def inital_values_gauss(mu=c.x_0,sigma=c.simga_inital):
    v_0 = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (c.x_g - mu)**2 / (2 * sigma**2)) *c.v_0
    return v_0


