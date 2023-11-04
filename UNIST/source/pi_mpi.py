from mpi4py import MPI
import math

comm = MPI.COMM_WORLD
size  = comm.Get_size()
rank = comm.Get_rank()

#This is a comment
#starting value of x
x=-1

#step size  CHANGE THIS
dx=0.0000001

iters=int(2/dx)
N = iters // size + (iters % size > rank)
start = comm.scan(N)-N

print (rank, start, N)

#the sum of all the areas - start at 0
A=0.
x=x+dx*start
#now for a loop to go through and add up all the 
#tiny rectangle areas
for i in range(N):
  #each area is sqrt(1-x**2)*dx
  #add this area to the existing area
	A=A+math.sqrt(1-x**2)*dx
  #now move x forward by an amount dx
	x=x+dx
A = comm.reduce(A, op=MPI.SUM, root=0)

#end the loop
#pi is twice the area
if rank==0:
    tpi=2*A
    error = abs(tpi - math.pi)
    print ("pi is approximately %.16f, "
                "error is %.16f" % (tpi, error))

