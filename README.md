## PhD course: Advanced Scientific Programming with Python (3 hp) - Answers to exercises 

### Day 1 

- Readme file `LinneaGG.md` is in the uu-python/participants repository
- Jupyter notebook with answers to questions is in `minimal_done.ipynb`

### Day 2
- The animals package is in the animals folder
- A working, bug-free dice game is in the no_bugs folder
- Questions about performance:

a. Investigate the performance of the matmult.py script
In which line(s) of the script would you start optimizing for speed?

- I would start at line 26 where there are 3 nested loops. 

b. Investigate the performance of the euler72.py script
In which line(s) of the script would you start optimizing for speed? (This is one problem from the euler project: https://projecteuler.net/problem=72)

- I would start with the `factorize` function, at line 26 where there is a while-loop nesten within a for-loop. 

c. Improve the performance of the matmult.py script
What is the best performance that you achieved with N=250?

- By using NumPy's function for dot multiplication I got a total time of 0.0197328 s. 

### Day 3 
- The `classroom` package with `Person`, `Student`, and `Teacher` classes are in the classroom folder
- Answers to NumPy exercises are in `numpy_exercises.py`
- An optimised matmult script using NumPy is in `matmult_opt.py`
- For MPI scripts see `mpi_ranks.py` and `mpi_sum.py`
- For GPU computing script see `GPUcomputing.ipynb`
