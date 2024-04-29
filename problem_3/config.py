import numpy as np
# given in exam
tau     = 1
lambda_value = 1

x_max = 1
x_min = 0
L = x_max -x_min

x_0 = 0.5

n_x = 101
n_t = 100

delta_t = 0.01

x_g, delta_x = np.linspace(x_min,x_max,n_x,retstep=True,)
t_g = np.arange(0,n_t) * delta_t

# integral over complete gauss
v_0 = 1

# used to define matricies
a = lambda_value**2 / delta_x **2
b = delta_t / tau 