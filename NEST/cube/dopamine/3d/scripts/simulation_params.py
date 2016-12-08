# Quality of graphics
dpi_n = 120

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
gui_enabled = True

MaxSynapses = 4000      # max synapses

BOUND = 0.2  # outer bound of rectangular 3d layer
R = .25      # radius of connectivity sphere of a neuron