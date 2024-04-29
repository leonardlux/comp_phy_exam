import config as c
import numpy as np

def sigma(t):
    return np.sqrt(2 * (c.lambda_value**2 * t /c.tau))

def analytical_function(t):
    return c.v_analytical_0 / (np.sqrt(2*np.pi) * sigma(t)) * np.exp(-1*(c.x_g-c.x_0)**2/(2*sigma(t)**2) - t/c.tau)


def t_good_approx():
    # good approx. until the 3 sigma distance from center reaches the boundary
    return (c.L/c.lambda_value)**2 * c.tau/(2**3*3**2)