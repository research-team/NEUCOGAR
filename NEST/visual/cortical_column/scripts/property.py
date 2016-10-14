"""Main property"""
GlobalColumns = 100 #3000


Glu = 0
GABA = 1
column = 0

# keys for layer tuples
L2_GABA0, L2_GABA1 = range(2)
L3_Glu, L3_GABA0, L3_GABA1 = range(3)
L4_Glu0, L4_Glu1, L4_GABA = range(3)
L5_Glu = 0
L6_Glu = 0

area = 3
step = 4
model = 5

# additional keys for dict elements
Glu_step  = 0
GABA_step = 1
X_area = 0
Y_area = 1

L2, L3, L4, L5, L6 = range(5)

Glu_generator = 0
Glu_result = 1

V1_Glu = 0
V2_Glu = 0
V5_Glu = 0

# quality of graphics
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

# weight synapse
w_Glu = 3.
w_GABA = -w_Glu * 2

# additional flags
generator_flag = True   # poisson generator with rate set up flag
statusGUI = True        # True - GUI is on | False - is off