# Keys for connection type
GABA = 0
Glu = 1
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
dt = 100.
KN = 2. # collumn number
k = []

# Neurons number for spike detector
N_detect = 100


# Generator delay
pg_delay = 10.

# Synapse weights
w_Glu = 3.
w_GABA = -w_Glu * 2
# Minimal number of neurons
NN_minimal = 10

# Synapse models
glu_synapse      = 'glu_synapse'
gaba_synapse     = 'gaba_synapse'


# Additional setings
dopamine_flag = False     # dopamine modulation flag
generator_flag = True
status_gui = True        # True - GUI is on | False - is off