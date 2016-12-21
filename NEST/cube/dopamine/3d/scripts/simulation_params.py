import argparse

parser = argparse.ArgumentParser(description='Run simulation for dopa w 3d layers')
parser.add_argument('t', metavar='threads', type=int,
                    default=1,
                    help='number of nest threads')
parser.add_argument('n', metavar='nn',
                    default=3000,
                    help='desired number of neurons')

args = parser.parse_args()


# Quality of graphics
dpi_n = 120

number_of_threads = args.t

# Number of neurons
NN = args.n

# T - simulation time | dt - simulation pause step
T = 1000.
dt = 10.

# Neurons number for spike detector
N_detect = 100

# Neurons number for multimeter
N_volt = 3

# Generator delay
pg_delay = 10.

# Synapse weights
w_Glu = 3.
w_GABA = -w_Glu * 2
w_ACh = 8.
w_DA_ex = 13.
w_DA_in = -w_DA_ex

# Minimal number of neurons
NN_minimal = 10

# Additional settings
dopamine_flag = True     # dopamine modulation flag
create_images = True

MaxSynapses = 4000      # max synapses

BOUND = 0.2  # outer bound of rectangular 3d layer
R = .25      # radius of connectivity sphere of a neuron
