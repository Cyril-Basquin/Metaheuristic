## 1/ Introduction

The aim of this project is to solve:  
  -Two Travelling Salesman Problem (TSP) of dimension 38 and 194 (available at http://www.math.uwaterloo.ca/tsp/world/countries.html)  
  -6 functions from the  "Benchmark Functions for the CEC'2018" in dimension 50 and 500 (Shifted Sphere Function, Shifted Schwefel’s Problem 2.21, Shifted Rosenbrock’s Function, Shifted Rastrigin’s Function, Shited Griewank’s Function, Shifted Ackley’s Function). See pdf

To do so, algorithm and function can be implemented manually, but it's more convenient and quick to use python framework. See part 2 'Choice of the framework'

All python scrypts for the continous optimization were run on google collaboratory. System specificity in Mai 2020 (run system_specs.ipynb , from '/miscelaneous' folder to get current specs):
   - Operating System : Ubuntu 18.04.3 LTS
   - CPU              : Intel(R) Xeon(R) CPU @ 2.00GHz, 2 core(s)
   - Memory           : 13.Gb

After some test, I choose to remove any dependancy in my code (much easier to run multiple code in parallel in google colab).  It is sufficient to load a notebook with jupyter notebook/Google colab and run them.  
The python requirements can be found here: https://github.com/Cyril-Basquin/Metaheuristic/tree/master/Metaheuristic_cec2008/tools

Results can be found here: https://github.com/Cyril-Basquin/Metaheuristic/blob/master/Metaheuristic_cec2008/Results.md


## 2/ Discrete Optimization problem : TSP
To solve the TSP problems, I use a tool develop by google: the OR-tools (https://developers.google.com/optimization/routing/tsp#or-tools). The tool is not very well documented (probably on purpose) but I decided to use it as a black box thanks to its efficiency. As a consequence, I don't find a way to get the number of evaluated path. An other problem is the calculated distance calculated by OR-tools was wrong, so i had to recalculate it. I don't find out why, but this problem might require further investigations.


## 3/ Continous optimization problems

### A/ Choice of the 'best' framework
Many framework exist to perform optimization of objective function. SciPy is probably the best known and provide easy to use method such as Nelder-mead or Broyden-Fletcher-Goldfarb-Shanno (BGFS) to solve non-linear problem. When problems became more 'complex', nature inspire algorithm give better result (in computation time). To use these algorithm, many framework exist such as jMetalPy, DEAP, Pygmo, Inspyred, NiaPy, Pymoo, Platypus... More or less rich in benchmark functions, algorithms and more or less customizable.

As computation time can be a crucial parameters, especially for big dimension of 'complex' function, I compare the computation time of 3 framework (jMetalPy, Inspyred and pygmo) to solve the rastrigin problem with a Genetic Algorithm (This function is implemented in the 3 framework).

The code used is available here: framework_computation_time/inspyred_vs_jmetalpy_vs_pygmo.ipynb  
and here framework_computation_time/Homemade_Rastrigin_GA.ipynb  

The summary of the test is presented thereafter:  
GC: code run on Google collaboratory  
Local: my PC (Windows 10, Intel i5-7200U @2.5GHz, Memory: 20Gb)  

Dimension:50, Function: 1M (1 run)
| FRAMEWORK  | GC  | Local  |
|---|---|---|
|Pygmo   | 3s  | - |
|JmetalPy  |  432s | 606s  |
|Inspyred  | 59s  | 93s  |  
|'Homemade'   | 507s  | 540s  |

Dimension: 500, Function: 1M
| FRAMEWORK  | GC  | Local  |
|---|---|---|
|Pygmo   | 27s  | - |
|JmetalPy  |  1462s | 1950s  |
|Inspyred  | 508s  | 843s  |  
|'Homemade'   |  5111s | 5170s  |


Google colab outperfom my local machine to solve the problem. An other advantage of google colab is the possibility to run many instance at the same time (up to 5 with one account) without deterioration of the performance.. And it is possible to create mutliple account.


### B/ Choice of the 'best' algorithm.

Then I have to choose the 'best' algorithm to solve the problem. In this study, I define the 'best' algorithm as the one that give the closer result to the minimum (i.e.: fitness= 0), in a 'reasonable' amount of time (~10 minutes). This definition of best is of course debatable. In addition, further study might be require for fine tuning the algorithm parameters (we didn't do it here).  

#### For the Shifted Sphere problem
Shifted Sphere function is a concave derivable function. To solve it, BFGS was used (because it is in second position in the scipy optimize algorithm documentation, and the 1st one didn't give a good result... I have to admit,  it's not the best reason ever).  

#### For the others continous optimization problem:
For each continous function, the 3 scripts (Step1, Step2, Final) can be found on the folder corresponding to the problem.

#### - Step 1  
For the others function, most of the algorithm implemented in pygmo were tested using the predefined parameters. Tested algorithm are: Artificial Bee Colony, Grey Wolf Optimizer, Differential Evolution, Self-adaptive Differential Evolution (jDE and iDE), a 'pygmo' Self-adaptive Differential Evolution (jDE and iDE), Particle Swarm Optimization and a 'pygmo' Particle Swarm Optimization.
Documentation for those algorithm can be found at: https://esa.github.io/pagmo2/overview.html#list-of-algorithms
Each algorithm was run 1 time using a population size of 100 and 10000 generation (as a consequence, the number of evaluated function may vary from one algorithm to another).  

#### - Step 2  
The 2/3 'best' (closer to the minimum) algorithm were then run 3 times with an higher number of generations (500 000, 100000 for PSO). If many of them reach the solution, the 'best' one is the one that reach it the more often among the 3 runs, then the one that reach the solution the faster (computational time)  

#### - Step 3  (FINAL)
Finally, the 'best' algorithm was run again. Evolution of the fitness was plot and number of evaluated function require to reach the minimum is shown. Note: The run time is not relevant as most of the time, the minimum is reach before 10% of the total evaluated function, and the algorithm is not stopped due to xtol/ftol criterion used 10E-600.. Which can't be reached.   
This last step should be optimize (coherent stopping criterion), but as i already said, my goal was to be as close as the minimum as possible. Running time was not a priority.


### C/ Annotation of the code.
The code is poorly annotated, but quite easy to read. For continous optimization, pygmo and numba have to be install on google colab. The objective function is define outside the class for conveniance: it is easier to use numba (@jit)  that way and Numba is essential, as it decrease computational time by a factor 10.
