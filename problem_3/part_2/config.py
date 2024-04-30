import numpy as np

#milli = 1
milli = 10**-3
# given in exam
tau     = 2  * milli
lambda_value = 0.18 * milli

x_max = 10  * milli
x_min = 0
L = x_max-x_min
x_0 = (x_max-x_min)/2

n_x = 301 
n_t = 1000

delta_t = 1e-5

x_g, delta_x = np.linspace(x_min,x_max,n_x,retstep=True,)
t_g = np.arange(0,n_t) * delta_t

# potential values
gamma = 0.5  * milli**-1
v_star = -40  * milli
v_na_nerst = 56  * milli
v_k_nerst = -76 * milli
v_mem = -70 * milli
v_appl = -50  * milli
g_k = 5

# used to define matricies
a = lambda_value**2 / delta_x **2
b = delta_t / tau 