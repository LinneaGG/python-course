from mpi4py import MPI
import sys
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n = 5
x = numpy.linspace(start=float(rank)/size, stop=float(1+rank)/size, num=n//size, endpoint=False)
cosx = numpy.cos(x)

integral = numpy.zeros(1)
total = numpy.zeros(1)

integral[0] = numpy.sum(cosx)*1.0/n

comm.Reduce(integral, total, op=MPI.SUM, root=0)

# root process prints results 
if comm.rank == 0:
	print("Sum:", total)
