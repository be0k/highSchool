#!/bin/bash
#PBS -N jun
#PBS -V
#PBS -q eduf
#PBS -A inhouse
#PBS -l select=4:ncpus=68:mpiprocs=68:ompthreads=1
#PBS -l walltime=00:30:00
#PBS -M abc@abc.com
#PBS -m abe

cd $PBS_O_WORKDIR
source ~/.bashrc
conda activate mpi

mpirun python ./width_divide.py -x -0.38 -y 0.665 –W 1024 –H 1024 -s 0.05 -m 1000 -o img001.png

