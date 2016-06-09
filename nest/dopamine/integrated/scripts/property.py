# Keys for connection type
GABA = 0
Glu = 1
ACh = 2
DA_ex = 3
DA_in = 4

# Keys for synapse models
model = 0
basic_weight = 1

# Quality of graphics
dpi_n = 120

# Keys for parts dictionary
k_IDs   = 'IDs'
k_name  = 'Name'
k_NN    = 'NN'
k_model = 'Model'

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

# Synapse models
glu_synapse      = 'glu_synapse'
gaba_synapse     = 'gaba_synapse'
ach_synapse      = 'ach_synapse'
dopa_synapse_ex  = 'dopa_synapse_ex'
dopa_synapse_in  = 'dopa_synapse_in'
gen_static_syn   = 'noise_conn'

# Additional setings
dopamine_flag = True     # dopamine modulation flag
status_gui = True        # True - GUI is on | False - is off