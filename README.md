# General Information

I added a new notebook for every task that needs solving using some programming. This is done to stop code from one task from cluttering other tasks (Kepp the namespace clean). To enable the sharing of code between these subtask, all the function are defined in pure python files (`.py` ending). The names of the files should give a clear indication of what functions are inside. I used so many files to make functions easy to find. In most cases one does not need to scroll through the file to see all of it. The approach allows for a bigger amout of modularity. 

For a computational paradigma, I tried to go for a function orientated style with less objects. Instead every choice can be made by passing a function a parameter, which can also be a funciton.

I decided against writing function for plotting because there a higher degree of freedom and a simple way to change is benefecial. Especially because a maybe broken plot can not negativley influence other parts of the programm.

# General note on programming style in this exam

During this exam I tried to follow the KISS priniciple.
This includes using and adapting the allready working and tested parts from Assignment 1 and the working parts from the [github of this lecture](https://github.com/nordam/ComputationalPhysics/blob/master/Notebooks/02%20-%20Numerical%20precision.ipynb).

Moreover this is also the exact reason I decided against using numba. 
Numba would increase the performance of the code, but at the expense of time needed to adapt everything to be able to work with numba.
The code itself is not that slow (nothing needs more than a minute on my laptop from late 2013), therefore more optimization would just waste time and increase the probability of adding errors.
