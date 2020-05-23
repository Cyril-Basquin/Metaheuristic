# 1/ Introduction

The aim of this project is to solve:  
  -Two Travelling Salesman Problem (TSP) of dimension 38 and 194  
  -6 functions from the  "Benchmark Functions for the CEC'2018" in dimension 50 and 500 (Shifted Sphere Function, Shifted Schwefel’s Problem 2.21, Shifted Rosenbrock’s Function, Shifted Rastrigin’s Function, Shited Griewank’s Function, Shifted Ackley’s Function)  

To do so, algorithm and function can be implemented manually, but it more convenient and quick to use python framework. Since many framework exist, the choosen ones for this project are details in part 2: Choice of the framework.

All python scrypts were run on google collaboratory. System specificity in Mai 2020 (run system_specs.ipynb , from '/miscelaneous' folder to get current specs):  
   - Operating System : Ubuntu 18.04.3 LTS  
   - CPU              : Intel(R) Xeon(R) CPU @ 2.00GHz, 2 core(s)  
   - Memory           : 13.Gb  

To copy this result:  
From an empty new notebook on google colab (https://colab.research.google.com/)  
Clone the git repository 



# 2/ Choice of the framework  
Many framework exist to perform mimization (or maximization) of objective function using different kind of solver. SciPy is probably the best known and provide easy to use method such as Nelder-mead or Broyden-Fletcher-Goldfarb-Shanno to solve non-linear problem. When problems became more 'complex', nature inspire algorithm give better result in computation time. To use these algorithm, many framework exist such as jMetalPy, DEAP, Pygmo, Inspyred, NiaPy, Pymoo, Platypus... More or less rich in benchmark functions, algorithms and more or less customizable.  

As computation time can be a crucial parameters, especially for big dimension of 'complex' function, I compare the computation time of 3 framework (jMetalPy, Inspyred and pygmo) to solve the rastrigin problem with a Genetic Algorithm (This function is implemented in the 3 framework).  

The code is available here: framework_computation_time/inspyred_vs_jmetalpy_vs_pygmo.ipynb  

Result shows a clear advantage for pygmo in both 50 and 500 dimensions:  
pygmo dim 50 =  
