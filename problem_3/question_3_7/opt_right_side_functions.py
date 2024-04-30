import numpy as np
import config as c
# following functions (F(v))were added to describe the right hand side of: A * v^{n+1}  = F(v^n)

def g_na_g_k(v_vec):
    return ((100/(1+ np.exp(c.gamma*(c.v_star - v_vec)))) + 1/5)/c.g_k

def right_side_function(v_vec):
    return (1-c.tau/c.delta_t) * v_vec + g_na_g_k(v_vec) * (v_vec - c.v_na_nerst) - c.v_k_nerst

# and a different function, where the sodium ion channels are not present in certain parts

def g_na_g_k_cutoff(v_vec):
    vec = ((100/(1+ np.exp(c.gamma*(c.v_star - v_vec)))) + 1/5)/c.g_k
    vec[:c.i_cutoff] = np.zeros(c.i_cutoff)
    return vec

def right_side_function_cutoff(v_vec):
    return (1-c.tau/c.delta_t) * v_vec + g_na_g_k_cutoff(v_vec) * (v_vec - c.v_na_nerst) - c.v_k_nerst