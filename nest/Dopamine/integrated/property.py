GABA = 0            # keys for connection type
Glu = 1
ACh = 2
DA_ex = 3
DA_in = 4

motivation = 0      # keys for motor cortex
action = 1

pfc_Glu0 = 0        # keys for prefrontal cortex
pfc_Glu1 = 1

D1 = 0              # keys for striatum
D2 = 1
tan = 2             # Tonically active neurons

snc_GABA = 0        # keys for SNc
snc_DA = 1

gpe_GABA = 0        # key for GPe
gpi_GABA = 0        # key for GPi
snr_GABA = 0        # key for SNr
stn_Glu = 0         # key for STN
thalamus_Glu = 0    # key for thalamus
amygdala_Glu = 0    # key for amygdala

nac_ACh = 0         # keys for NAc
nac_GABA0 = 1
nac_GABA1 = 2

vta_GABA0 = 0       # keys for VTA
vta_DA0 = 1
vta_GABA1 = 2
vta_DA1 = 3
vta_GABA2 = 4

tpp_GABA = 0        # keys for TPP
tpp_ACh = 1
tpp_Glu = 2

dpi_n = 120         # Quality of graphics

# dopamine model key
dopa_model_ex = 'dopa_ex'
dopa_model_in = 'dopa_in'
gen_static_syn = 'noise_conn'

dopa_flag = True                # dopamine modulation flag
generator_flag = True    # poisson generator with rate set up flag
test_flag = False                # True - testing mode | False - real number neurons
statusGUI = True                # True - GUI is on | False - is off