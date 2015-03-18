neuron_models =[
'aeif_cond_alpha',
'aeif_cond_alpha_RK5' ,
'aeif_cond_alpha_multisynapse' ,
'aeif_cond_exp' ,
'amat2_psc_exp'  ,
'ginzburg_neuron' ,
'hh_cond_exp_traub' ,
'hh_psc_alpha' ,
'ht_neuron' ,
'iaf_chs_2007' ,
'iaf_chxk_2008' ,
'iaf_cond_alpha' ,
'iaf_cond_alpha_mc' ,
'iaf_cond_exp' ,
'iaf_cond_exp_sfa_rr' ,
'iaf_neuron' ,
'iaf_psc_alpha' ,
'iaf_psc_alpha_canon' ,
'iaf_psc_alpha_multisynapse' ,
'iaf_psc_alpha_presc' ,
'iaf_psc_delta' ,
'iaf_psc_delta_canon' ,
'iaf_psc_exp' ,
'iaf_psc_exp_multisynapse' ,
'iaf_psc_exp_ps' ,
'iaf_tum_2000' ,
'izhikevich' ,
'mat2_psc_exp' ,
'mcculloch_pitts_neuron'  ,
'multimeter' ,
'parrot_neuron' ,
'parrot_neuron_ps' ,
'pp_pop_psc_delta' ,
'pp_psc_delta' ,
'sli_neuron']

import nest
found = []
for mod in neuron_models:
    try:
        found.append([mod for a in nest.GetDefaults(mod).keys() if 'recep' in  a])
    except:
        print 'Opps'

print found