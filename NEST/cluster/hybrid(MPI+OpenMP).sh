#!/bin/bash

# Check if no arguments
if [ $# -eq 0 ]
  then
    echo "Choose neuromodulator module as argument [DA/5HT/NA/DA3d/DA+5HT]!"
    exit 1
fi

# Save parameters
echo "CHECK 'HOSTS' and 'HOSTFILE' BEFORE STARTING THE TASK!"
read -p "1. Job name                    : " job
read -p "2. Neuron number               : " neurons
read -p "3. Node number (MPI per node)  : " nodes
read -p "4. OpenMP threads number       : " omp

# Create work directory
today=$(date "+%d-%m_%H:%M")
script_path="$HOME/scripts/$1/neuromodulation.py"
new_dir="results/$1/%J_${job}_${today}"
mkdir ${new_dir} && cd ${new_dir}

echo "Created and moved to $new_dir"
echo

err="$HOME/log/$1/%J($job).err"
out="$HOME/log/$1/%J($job).out"
res=$(($omp * $nodes))

bsub -J ${job} -e ${err} -o ${out} -n ${res} -R "span[ptile=$omp]" -a openmp -m "$(cat "$HOME/hostfile")" mpirun -np ${nodes} -rr -f $HOME/hosts -print-rank-map /shared/NEST-2.12.0/bin/python3.6 ${script_path} ${neurons}

# Delete broken clone of directory
cd "$HOME/results/$1/"
rm -rf "$HOME/$new_dir"
