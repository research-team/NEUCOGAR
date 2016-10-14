"""Main property"""
GlobalColumns = 60 #3000

# keys for layer tuples
Glu  = 0
GABA = 1
area = 2
step = 3

# keys for part there is DA generator
DA = 0
DA_ex = 2

# additional keys for dict elements
Glu_step, GABA_step = range(2)
X_area, Y_area = range(2)
L1, L2, L3, L4, L5, L6 = range(6)

V4_DA = 0

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

# generator delay
pg_delay = 10.

w_Glu = 3.
w_GABA = -w_Glu * 2
w_DA_ex = 4.
dopa_model_ex = 'dopa_ex'

generator_flag = True   # poisson generator with rate set up flag
statusGUI = True        # True - GUI is on | False - is off