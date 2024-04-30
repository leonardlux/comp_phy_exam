import config as c
import numpy as np
from ipywidgets import interact
import matplotlib.animation as animation
from matplotlib import pyplot as plt
from matplotlib import cm


# Plots (simpel)

t_diff_times = [0, 1, 5, 10, 25,50, 99]
t_diff_times = list(range(5,15))
def plot_diff_times(
        U,
        title="",
        t=c.t_g,
        t_diff_times = t_diff_times,
        log = False,
        legend = False,
        func_t = None,
        ):
    fig = plt.figure()
    plt.title(title)
    for t in t_diff_times:
        plt.plot(c.x_g,U[t], label=f"t={c.delta_t*t}")
        if func_t != None:
            plt.plot(c.x_g, func_t(c.delta_t*t),color="grey")
    if legend:
        plt.legend()
    plt.xlabel("x")
    plt.ylabel("u(x)")
    if log:
        plt.yscale("log")
    plt.show()
