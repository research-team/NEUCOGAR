# -*- coding: utf-8 -*-
GABA = 0
Glu = 1
ACh = 2

# keys for cerebral_cortex
motivation = 0
action = 1

pfc_Glu0 = 0
pfc_Glu1 = 1

# keys for striatum
D1 = 0
D2 = 1
tan = 2  # Tonically active neurons

snc_GABA = 0
snc_DA = 1

gpe_Glu = 0
gpi_GABA = 0
stn_Glu = 0
snr_GABA = 0
thalamus_Glu = 0

# keys for NAc
nac_ACh = 0
nac_GABA0 = 1
nac_GABA1 = 2

# keys for VTA
vta_GABA0 = 0
vta_DA0 = 1
vta_GABA1 = 2
vta_DA1 = 3
vta_GABA2 = 4

# keys for TPP
tpp_GABA = 0
tpp_ACh = 1
tpp_Glu = 2

# Quality of graphics
dpi_n = 120

# dopamine model key
dopa_model_ex = "dopa_ex"
dopa_model_in = "dopa_in"

sd_folder_name = "output"

gen_static_syn = "noise_conn"

# dopamine modulation flag
dopa_flag = True

# poisson generator with rate set up flag
poison_generator_flag = True

# True - testing mode | False - real number neurons
test_flag = True

#info about GUI
withoutGUI = False

#save weight change when vt_flag is True (a graphic and dat file of weight change of one synapse)
save_weight_flag = True