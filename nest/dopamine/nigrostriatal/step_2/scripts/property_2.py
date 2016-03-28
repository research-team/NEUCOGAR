# -*- coding: utf-8 -*-
# static final names
dopa = 0
nodopa = 1
D1 = 0
D2 = 1
tan = 2  # Tonically active neurons

# static final values
dpi_n = 120

syn_excitory = "excitatory"
syn_inhibitory = "inhibitory"

# dopamine model key
dopa_model_ex = "dopa_ex"
dopa_model_in = "dopa_in"

sd_folder_name = "output/"
sd_filename = "spikes-172-0.gdf"

device_static_synapse = "static_device"
gen_static_syn = "noise_conn"
# dopamine modulation flag
vt_flag = True
# poisson generator with rate set up flag
pg_flag = True
# testing mode or real number neurons
test_flag = True
#save weight change when vt_flag is True
save_weight_flag = False