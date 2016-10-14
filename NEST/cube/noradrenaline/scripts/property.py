# keys for connection type
GABA = 0
Glu = 1
ACh = 2
DA_ex = 3
DA_in = 4
NA = 5
#DA = 6

# Quality of graphics
dpi_n = 120

k_IDs = 'IDs'
k_name = 'Name'
k_NN = 'NN'
k_model = 'Model'

# general settings
T = 1000.
dt = 10.

# neurons number for spike detector
N_detect = 100

# neurons number for multimeter
N_volt = 3

# generator delay
pg_delay = 10.

w_Glu = 3.
w_GABA = -w_Glu * 2
w_ACh = 8.

# Volume transmission
w_NR_ex = 13.
w_NR_in = -w_NR_ex

NN_minimal = 10

NN_coef = 0.0001

# dopamine model key
nora_model_ex = 'dopa_ex'
gen_static_syn = 'noise_conn'
#nora_model_ex = 'dopa_ex'
nora_model_in = 'dopa_in'

nora_flag = True        # dopamine modulation flag
#nora_flag = True
generator_flag = True   # poisson generator with rate set up flag
test_flag = True       # True - testing mode | False - real number neurons
statusGUI = True        # True - GUI is on | False - is off