# -*- coding: utf-8 -*-
# keys for prefrontal cortex
cortex = 0
cortex_Glu0 = 1
cortex_Glu1 = 2
# keys for NAc
nac_Ach = 0
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
tpp_Ach = 1
tpp_Glu = 2

# Quality of graphics
dpi_n = 120

syn_excitory = "excitatory"
syn_inhibitory = "inhibitory"

# dopamine model key
dopa_model_ex = "dopa_ex"
dopa_model_in = "dopa_in"

sd_folder_name = "result/"
sd_filename = "spikes-172-0.gdf"

device_static_synapse = "static_device"
gen_static_syn = "noise_conn"

# dopamine modulation flag
dopa_flag = True

# poisson generator with rate set up flag
poison_generator = True

# True - testing mode | False - real number neurons
test_flag = False

# display graphic
disp_flag = False

# save weight change when vt_flag is True (a graphic and dat file of weigh change of one synapse)
save_weight_flag = False
