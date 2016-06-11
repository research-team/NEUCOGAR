rate = 100

first_generator  = 1.0 * rate
second_generator = 1.5 * rate
third_generator  = 2.0 * rate
print first_generator, second_generator, third_generator

# keys for connection type
GABA = 0
Glu = 1
ACh = 2
DA_ex = 3
DA_in = 4

# Quality of graphics
dpi_n = 120

k_IDs = 'IDs'
k_name = 'Name'
k_NN = 'NN'
k_model = 'Model'

# general settings
T = 40.
dt = T

# neurons number for spike detector
N_detect = 100

# neurons number for multimeter
N_volt = 3

w_Glu = 3.
w_GABA = -w_Glu * 2
w_ACh = 8.

# Volume transmission
w_DA_ex = 13.
w_DA_in = -w_DA_ex

NN_minimal = 10

# dopamine model key
dopa_synapse_ex = 'dopa_ex'
dopa_synapse_in = 'dopa_in'
gen_static_syn = 'noise_conn'

dopa_flag = True        # dopamine modulation flag
generator_flag = True   # poisson generator with rate set up flag
test_flag = False       # True - testing mode | False - real number neurons
statusGUI = True        # True - GUI is on | False - is off