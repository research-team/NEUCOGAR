#!/bin/bash

# Check if no arguments
if [ $# -eq 0 ]
  then
    echo "Choose neuromodulator module as argument [DA/5HT/NA/DA3d/DA+5HT]!"
    exit 1
fi


# Save parameters
read -p "1. Job name       : " job
read -p "2. Neuron number  : " neurons
read -p "3. MPI tasks: " tasks

# Create work directory
today=$(date "+%d-%m_%H:%M")
script_path="$HOME/scripts/$1/run8.py"
new_dir="results/$1/%J_${job}_${today}"
mkdir ${new_dir} && cd ${new_dir}
echo "Created and moved to $new_dir"
echo

err="$HOME/log/$1/%J($job).err"
out="$HOME/log/$1/%J($job).out"

export OMP_NUM_THREADS=1
bsub -J ${job} -o ${out} -e ${err} -n ${tasks} -m cluster-manager /shared/NEST-2.12.0/bin/python3.6 ${script_path} ${neurons} ${tasks}

# Delete broken clone of directory
cd "$HOME/results/$1/"
rm -rf "$HOME/$new_dir"
