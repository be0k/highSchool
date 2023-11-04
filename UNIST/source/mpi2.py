from mpi4py import MPI

comm = MPI.COMM_WORLD
myrank = comm.Get_rank()
nproc = comm.Get_size()

print("Hello World! from process {0} of {1} \n".format(myrank, nproc))

