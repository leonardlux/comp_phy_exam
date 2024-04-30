import config as c
import numpy as np
# This file contains all the equations and fuctions that are need for analyitcal parts
def sigma(t):
    return np.sqrt(2 * (c.lambda_value**2 * t /c.tau))

# this is the analytical function from 3.5b)
def analytical_function(t):
    return c.v_analytical_0 / (np.sqrt(2*np.pi) * sigma(t)) * np.exp(-1*(c.x_g-c.x_0)**2/(2*sigma(t)**2) - t/c.tau)

# this is the analytical function from 3.5d) assuming that 3 simga intervall is a good approximation
def t_good_approx():
    # good approx. until the 3 sigma distance from center reaches the boundary
    return (c.L/c.lambda_value)**2 * c.tau/(2**3*3**2)