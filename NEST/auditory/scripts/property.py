"""Main property"""
GlobalColumns = 40 #3000
# keys for layer tuples
Glu  = 0
GABA = 1
area = 2
step = 3

# additional keys for dict elements
Glu_step, GABA_step = range(2)
X_area, Y_area = range(2)
L1, L2, L3, L4, L5, L6 = range(6)

MGB_generator, MGB_result = range(2)
IC_glu = 0

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

generator_flag = True   # poisson generator with rate set up flag
statusGUI = True        # True - GUI is on | False - is off