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
        filename="",
        alpha=1,
        ls = "-",
        differential = False,
        ):
    fig = plt.figure(figsize=(5,4))
    plt.title(title)
    analy_label = False
    for t in t_diff_times:
        if differential:
            U[t] = U[t] - func_t(c.delta_t*t)
        plt.plot(c.x_g,U[t],label=f"$t={c.delta_t*t*10**3:.1f}$ms",alpha=alpha,ls=ls,lw=1,marker=".")
        if func_t != None and not differential:
            if not analy_label:
                plt.plot(c.x_g, func_t(c.delta_t*t),color="black",alpha=0.5,label="analy. sol.")
                analy_label = True
            else:
                plt.plot(c.x_g, func_t(c.delta_t*t),color="black",alpha=0.5)

    if legend:
        plt.legend()
    plt.xlabel("$x$ in m")
    if not differential:
        plt.ylabel("$V(x,t)$ in V")
    else: 
        plt.ylabel("$V(x,t)-V_{analy.}(x,t)$ in V")
    if log:
        plt.yscale("log")
    if filename!="":
        plt.savefig(f"images/{filename}.pdf")
    plt.show()
