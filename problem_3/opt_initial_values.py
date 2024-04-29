import numpy as np
import config as c

# generate inital values

def inital_values_gauss(mu=c.x_0,sigma=c.simga_inital):
    u_0 = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (c.x_g - mu)**2 / (2 * sigma**2)) *c.v_0
    # scale to have correct inital mass in the system, even if part of the distribution is outside
    return u_0


