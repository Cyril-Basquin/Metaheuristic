# 1/ Introduction

The aim of this project is to solve:
  -Two Travelling Salesman Problem (TSP) of dimension 38 and 194
  -6 functions from the  "Benchmark Functions for the CEC'2018" in dimension 50 and 500 (Shifted Sphere Function, Shifted Schwefel’s Problem 2.21, Shifted Rosenbrock’s Function, Shifted Rastrigin’s Function, Shited Griewank’s Function, Shifted Ackley’s Function)

To do so, algorithm and function can be implemented manually, but it's more convenient and quick to use python framework. See part 2 'Choice of the framework'

All python scrypts were run on google collaboratory. System specificity in Mai 2020 (run system_specs.ipynb , from '/miscelaneous' folder to get current specs):
   - Operating System : Ubuntu 18.04.3 LTS
   - CPU              : Intel(R) Xeon(R) CPU @ 2.00GHz, 2 core(s)
   - Memory           : 13.Gb




# 2/ Choice of the framework
Many framework exist to perform mimization (or maximization) of objective function using different kind of solver. SciPy is probably the best known and provide easy to use method such as Nelder-mead or Broyden-Fletcher-Goldfarb-Shanno to solve non-linear problem. When problems became more 'complex', nature inspire algorithm give better result in computation time. To use these algorithm, many framework exist such as jMetalPy, DEAP, Pygmo, Inspyred, NiaPy, Pymoo, Platypus... More or less rich in benchmark functions, algorithms and more or less customizable.

As computation time can be a crucial parameters, especially for big dimension of 'complex' function, I compare the computation time of 3 framework (jMetalPy, Inspyred and pygmo) to solve the rastrigin problem with a Genetic Algorithm (This function is implemented in the 3 framework).

The code used is available here: framework_computation_time/inspyred_vs_jmetalpy_vs_pygmo.ipynb
and here framework_computation_time/Homemade_Rastrigin_GA.ipynb

The summary of the test is presented thereafter:
GC: code run on Goocl collaboratory
Local: my PC (Windows 10, Intel i5-7200U @2.5GHz, Memory: 20Gb)

Dimension:50, Function: 1M (1 run)
| FRAMEWORK  | GC  | Local  |
|---|---|---|
|Pygmo   | 3s  | - |
|JmetalPy  |  432s | 606s  |
|Inspyred  | 59s  | 93s  |  
|'Homemade'   | 507  | 540s  |

Dimension: 500, Function: 1M
| FRAMEWORK  | GC  | Local  |
|---|---|---|
|Pygmo   | 27s  | - |
|JmetalPy  |  1462s | 1950s  |
|Inspyred  | 508s  | 843s  |  
|'Homemade'   |  5111s | 5170s  |
