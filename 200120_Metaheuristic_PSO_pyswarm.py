''' python code to test easily and automatically different omega, phig (= c1) and phip (=c2) parameter
 with particle swarm optimization algorithm (see GitHub)'''

# Importing package : !!! Take care if you need another package that math for your function !!!
from pyswarm import pso
import numpy as np
import math

# Define your Objective Function (Rosenbrock is implemented by default)
def objective_function(x):
    ''' Rosenbrock function'''
    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)

''' Define your parameters here'''
# Defining parameters
D = 4                               # number of variable for the Objective function
lower_bound = -10                   # lower_bound value
upper_bound = 10                    # upper_bound value

omega_, phip_, phig_ = 0, 1, 1  # omega, phip and phig starting value
i_, j_, k_ = 5, 5, 1                # number omega, phip and phig tested
step_size_omega, step_size_phip, step_size_phig = 0.25, 0.5, 0.5 # Step size evolution of omega, phip and phig

replicate = 10                      # How much replicate per condition (Minimum = 1)
swarm_size = 20                     # Size of the swarm
max_iteration = 100                 # Maximum iteration per run

mini_step = 1e-8        # stop if velocity become too small at each step
mini_fct = 1e-8         # stop if function progress is too small ate each step

# Function to start the algorithm
def pso_automatic_fct():
    def lb_ub(D, lb_ = lower_bound, ub_ = upper_bound):
        lb, ub = [], []
        lb_value, ub_value = lb_ , ub_
        for i in range(D):
            lb.append(lb_value)
            ub.append(ub_value)
        return lb, ub

    lb, ub = lb_ub(D)                     # Lower bound and upper bound list construction
    result_pso = np.zeros((i_*j_*k_,D+4)) # Result array initialisation
    l = 0                                 # Iterator initialisation for response

    for i in range(i_):   # nb of step for omega
        for j in range(j_):   # nb of step for phip (=c1)
            for k in range(k_):   # nb of step for phig (=c2)
                xopt_ , fopt_ = 0, 0 # (Re)Initialisation of variable for iterations
                for w in range(replicate):
                    xopt, fopt = pso(objective_function, lb, ub, omega=(omega_ + i*step_size_omega), phip=(phip_ + j*step_size_phip), phig=(phig_ + k*step_size_phig), maxiter=max_iteration,
                        swarmsize=swarm_size, minstep= mini_step, minfunc=mini_fct)
                    xopt_ += xopt
                    fopt_ += fopt
                result_pso[l, 0] = fopt_/replicate
                result_pso[l, D+1] = (omega_ + i*step_size_omega)
                result_pso[l, D+2] = (phig_ + j*step_size_phig)
                result_pso[l, D+3] = (phip_ + k*step_size_phip)
                for z in range(D):
                    result_pso[l, z+1] = xopt_[z]/replicate
                l += 1
                print('Iteration : ', l, '/', i_*j_*k_)
    return result_pso

# Function to visualize the result
def get_best_result_minimization(x):
    # Sorting the result by fopt from smaller to greater
    sorted_by_fopt = result[np.lexsort(np.fliplr(result).T[[7]])]

    # Print the 10 best results (Minimization)
    for i in range(x):
        print('#', i+1, np.round(sorted_by_fopt[i], decimals=2))
def get_best_result_maximization(x):
    # Sorting the result by fopt from smaller to greater
    sorted_by_fopt = result[np.lexsort(np.fliplr(result).T[[7]])]

    # Print the 10 best results (Maximization)
    for i in range(10):
        print(i+1, np.round(sorted_by_fopt[-(i+1)], decimals=2))

''' Launch the function and see the 'best' results quickly'''
result = pso_automatic_fct()
get_best_result_minimization(5)
