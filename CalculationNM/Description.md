## Neuron models
  1. [aeif_cond_alpha](#1-aeif_cond_alpha)
  2. [aeif_cond_alpha_RK5](#2-aeif_cond_alpha_RK5)
  3. [aeif_cond_exp](#3-aeif_cond_exp)
  4. [amat2_psc_exp](#4-amat2_psc_exp)
  5. [hh_cond_exp_traub](#5-hh_cond_exp_traub)
  6. [hh_psc_alpha](#6-hh_psc_alpha)
  7. [hh_psc_alpha_gap](#7-hh_psc_alpha_gap)
  8. [iaf_chs_2007](#8-iaf_chs_2007)
  9. [iaf_chxk_2008](#9-iaf_chxk_2008)
  10. [iaf_cond_alpha](#10-iaf_cond_alpha)
  11. [iaf_cond_exp](#11-iaf_cond_exp)
  12. [iaf_cond_exp_sfa_rr](#12-iaf_cond_exp_sfa_rr)
  13. [iaf_neuron](#13-iaf_neuron)
  14. [iaf_psc_alpha](#14-iaf_psc_alpha)
  15. [iaf_psc_alpha_canon](#15-iaf_psc_alpha_canon)
  16. [iaf_psc_alpha_presc](#16-iaf_psc_alpha_presc)
  17. [iaf_psc_delta](#17-iaf_psc_delta)
  18. [iaf_psc_delta_canon](#18-iaf_psc_delta_canon)
  19. [iaf_psc_exp](#19-iaf_psc_exp)
  20. [iaf_psc_exp_ps](#20-iaf_psc_exp_ps)
  21. [iaf_tum_2000](#21-iaf_tum_2000)
  22. [izhikevich](#22-izhikevich)
  23. [mat2_psc_exp](#23-mat2_psc_exp)
  24. [pp_pop_psc_delta](#24-pp_pop_psc_delta)
  25. [pp_psc_delta](#25-pp_psc_delta)


#### 1. aeif_cond_alpha

Parameters | Description
------------------|--------
E_ex | Excitatory reversal potential in mV
dg_in | First derivative of g_in in nS/ms
V_reset | Reset membrane potential after a spike in mV
V_peak | Spike detection threshold in mV
V_th | Spike threshold in mV
I_e | Constant input current in pA
g_L | Leak conductance in nS
t_spike | Point in time of last spike in ms
tau_w | Adaptation time constant in ms
E_L | Resting membrane potential in mV 
dg_ex | First derivative of g_ex in nS/ms
tau_syn_ex | Time constant of postsynaptic excitatory currents in ms
Delta_T | Slope factor in mV
V_m | Membrane potential in mV
beta_Ca | ?? Not declared in NEST documentation
t_ref | Duration of refractory period (V_m = V_reset) in ms
a | Subthreshold adaptation in nS
E_in | Inhibitory reversal potential in mV
b | Spike-triggered adaptation in pA
Ca | ?? Not declared in NEST documentation
C_m | Capacity of the membrane in pF
g_ex | Excitatory synaptic conductance in nS
g_in | Inhibitory synaptic conductance in nS
w | Spike-adaptation current in pA
tau_syn_in | Time constant of postsynaptic inhibitory currents in ms
tau_Ca | ?? Not declared in NEST documentation

![1] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/aeif_cond_alpha.png)

#### 2. aeif_cond_alpha_RK5

Parameters | Description
------------------|--------
E_ex | Excitatory reversal potential in mV
dg_in | First derivative of g_in in nS/ms
V_reset | Reset membrane potential after a spike in mV
V_peak | Spike detection threshold in mV
V_th | Spike threshold in mV
I_e | Constant input current in pA
g_L | Leak conductance in nS
t_spike | Point in time of last spike in ms
tau_w | Adaptation time constant in ms
MAXERR | Error estimate tolerance for adaptive stepsize control (steps accepted if err<=MAXERR). In mV. Note that the error refers to the difference between the 4th and 5th order RK terms. Default 1e-10 mV
E_L | Resting membrane potential in mV
dg_ex | First derivative of g_ex in nS/ms
tau_syn_ex | Time constant of postsynaptic excitatory currents in ms
Delta_T | Slope factor in mV
V_m | Membrane potential in mV
beta_Ca | ?? Not declared in NEST documentation
t_ref | Duration of refractory period (V_m = V_reset) in ms
a | Subthreshold adaptation in nS
E_in | Inhibitory reversal potential in mV
b | Spike-triggered adaptation in pA
HMIN | Minimal stepsize for numerical integration in ms (default 0.001ms)
Ca | ?? Not declared in NEST documentation
C_m | Capacity of the membrane in pF
g_ex | Excitatory synaptic conductance in nS
g_in | Inhibitory synaptic conductance in nS
w | Spike-adaptation current in pA
tau_syn_in | Time constant of postsynaptic inhibitory currents in ms
tau_Ca | ?? Not declared in NEST documentation

![2] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/aeif_cond_alpha_RK5.png)

#### 3. aeif_cond_exp

Parameters | Description
------------------|--------
E_ex | Excitatory reversal potential in mV
V_reset | Reset membrane potential after a spike in mV
V_peak | Spike detection threshold in mV
V_th | Spike threshold in mV
I_e | Constant input current in pA
g_L | Leak conductance in nS
t_spike | Point in time of last spike in ms
tau_w | Adaptation time constant in ms
E_L | Resting membrane potential in mV
tau_syn_ex | Time constant of postsynaptic excitatory currents in ms
Delta_T | Slope factor in mV
V_m | Membrane potential in mV
beta_Ca | ?? Not declared in NEST documentation
t_ref | Duration of refractory period (V_m = V_reset) in ms 
a | Subthreshold adaptation in nS
E_in | Inhibitory reversal potential in mV
b | Spike-triggered adaptation in pA
Ca | ?? Not declared in NEST documentation
C_m | Capacity of the membrane in pF
g_ex | Excitatory synaptic conductance in nS
g_in | Inhibitory synaptic conductance in nS
w | Spike-adaptation current in pA
tau_syn_in | Time constant of postsynaptic inhibitory currents in ms
tau_Ca | ?? Not declared in NEST documentation

![3] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/aeif_cond_exp.png)

#### 4. amat2_psc_exp

Parameters | Description
------------------|--------
V_th | Spike threshold in mV
tau_m | Membrane time constant in ms
I_e | Constant input current in pA
t_spike | Point in time of last spike in ms
V_m | Membrane potential in mV
E_L | Resting membrane potential in mV
tau_syn_ex | Time constant of postsynaptic excitatory currents in ms
beta_Ca | ?? Not declared in NEST documentation
t_ref | Duration of refractory period (V_m = V_reset) in ms
Ca | ?? Not declared in NEST documentation
C_m | Capacity of the membrane in pF
tau_syn_in | Time constant of postsynaptic inhibitory currents in ms
tau_Ca | ?? Not declared in NEST documentation

![4] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/amat2_psc_exp.png)

#### 5. hh_cond_exp_traub

Parameters | Description
------------------|--------
V_T | Voltage offset that controls dynamics. For default parameters V_T = -63mV results in a threshold around -50mV
E_ex | Excitatory reversal potential in mV
I_e | Constant input current in pA
g_L | Leak conductance in nS
t_spike | Point in time of last spike in ms
g_K | Potassium peak conductance in nS
E_K | Potassium reversal potential in mV
V_m | Membrane potential in mV
E_L | Resting membrane potential in mV
Act_m | Activation variable m
Act_h | Activation variable h
tau_syn_ex | Time constant of postsynaptic excitatory currents in ms
Inact_n | Inactivation variable n
beta_Ca | ?? Not declared in NEST documentation
E_Na | Sodium reversal potential in mV
E_in | Inhibitory reversal potential in mV
Ca | ?? Not declared in NEST documentation
C_m | Capacity of the membrane in pF
g_Na | Sodium peak conductance in nS
tau_syn_in | Time constant of postsynaptic inhibitory currents in ms
tau_Ca | ?? Not declared in NEST documentation

![5] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/hh_cond_exp_traub.png)

#### 6. hh_psc_alpha

Parameters | Description
------------------|--------
I_e | Constant input current in pA
g_L | Leak conductance in nS
t_spike | Point in time of last spike in ms
g_K | Potassium peak conductance in nS
E_K | Potassium reversal potential in mV
V_m | Membrane potential in mV
t_ref | Duration of refractory period (V_m = V_reset) in ms
E_L | Resting membrane potential in mV
Act_m | Activation variable m
Act_h | Activation variable h
tau_syn_ex | Time constant of postsynaptic excitatory currents in ms
Inact_n | Inactivation variable n
beta_Ca | ?? Not declared in NEST documentation
E_Na | Sodium reversal potential in mV
Ca | ?? Not declared in NEST documentation
C_m | Capacity of the membrane in pF
g_Na | Sodium peak conductance in nS
tau_syn_in | Time constant of postsynaptic inhibitory currents in ms
tau_Ca | ?? Not declared in NEST documentation

![6] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/hh_psc_alpha.png)

#### 7. hh_psc_alpha_gap

Parameters | Description
------------------|--------
I_e | Constant input current in pA
g_L | Leak conductance in nS
t_spike | Point in time of last spike in ms
E_K | Potassium reversal potential in mV
V_m | Membrane potential in mV
t_ref | Duration of refractory period (V_m = V_reset) in ms
E_L | Resting membrane potential in mV
Act_m | Activation variable m
Act_h | Activation variable h
tau_syn_ex | Time constant of postsynaptic excitatory currents in ms
Inact_n | Inactivation variable n
beta_Ca | ?? Not declared in NEST documentation
E_Na | Sodium reversal potential in mV
Ca | ?? Not declared in NEST documentation
C_m | Capacity of the membrane in pF
g_Na | Sodium peak conductance in nS
tau_syn_in | Time constant of postsynaptic inhibitory currents in ms
tau_Ca | ?? Not declared in NEST documentation

![7] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/hh_psc_alpha_gap.png)

#### 8. iaf_chs_2007

Parameters | Description
------------------|--------
V_reset | Reset membrane potential after a spike in mV
t_spike | Point in time of last spike in ms
V_m | Membrane potential in mV
beta_Ca | ?? Not declared in NEST documentation
Ca | ?? Not declared in NEST documentation
tau_Ca | ?? Not declared in NEST documentation

![8] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/iaf_chs_2007.png)

#### 9. iaf_chxk_2008

Parameters | Description
------------------|--------
E_ex | Excitatory reversal potential in mV
V_th | Spike threshold in mV
I_e | Constant input current in pA
g_L | Leak conductance in nS
t_spike | Point in time of last spike in ms
V_m | Membrane potential in mV
E_L | Resting membrane potential in mV
tau_syn_ex | Time constant of postsynaptic excitatory currents in ms
beta_Ca | ?? Not declared in NEST documentation
E_in | Inhibitory reversal potential in mV
Ca | ?? Not declared in NEST documentation
C_m | Capacity of the membrane in pF
tau_syn_in | Time constant of postsynaptic inhibitory currents in ms
g_ahp | AHP conductance
tau_Ca | ?? Not declared in NEST documentation

![9] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/iaf_chxk_2008.png)

#### 10. iaf_cond_alpha

Parameters | Description
------------------|--------
E_ex | Excitatory reversal potential in mV
V_reset | Reset membrane potential after a spike in mV
V_th | Spike threshold in mV
I_e | Constant input current in pA
g_L | Leak conductance in nS
t_spike | Point in time of last spike in ms
V_m | Membrane potential in mV
E_L | Resting membrane potential in mV
tau_syn_ex | Time constant of postsynaptic excitatory currents in ms
beta_Ca | ?? Not declared in NEST documentation
t_ref | Duration of refractory period (V_m = V_reset) in ms
E_in | Inhibitory reversal potential in mV
Ca | ?? Not declared in NEST documentation 
C_m | Capacity of the membrane in pF
tau_syn_in | Time constant of postsynaptic inhibitory currents in ms
tau_Ca | ?? Not declared in NEST documentation

![10] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/iaf_cond_alpha.png)

#### 11. iaf_cond_exp

Parameters | Description
------------------|--------
E_ex | Excitatory reversal potential in mV
V_reset | Reset membrane potential after a spike in mV
V_th | Spike threshold in mV
I_e | Constant input current in pA
g_L | Leak conductance in nS
t_spike | Point in time of last spike in ms
V_m | Membrane potential in mV
E_L | Resting membrane potential in mV
tau_syn_ex | Time constant of postsynaptic excitatory currents in ms
beta_Ca | ?? Not declared in NEST documentation
t_ref | Duration of refractory period (V_m = V_reset) in ms
E_in | Inhibitory reversal potential in mV
Ca | ?? Not declared in NEST documentation
C_m | Capacity of the membrane in pF
tau_syn_in | Time constant of postsynaptic inhibitory currents in ms
tau_Ca | ?? Not declared in NEST documentation

![11] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/iaf_cond_exp.png)

#### 12. iaf_cond_exp_sfa_rr

Parameters | Description
------------------|--------
E_ex | Excitatory reversal potential in mV
V_reset | Reset membrane potential after a spike in mV
I_e | Constant input current in pA
g_L | Leak conductance in nS
V_th | Spike threshold in mV
t_spike | Point in time of last spike in ms
E_L | Resting membrane potential in mV
tau_syn_ex | Time constant of postsynaptic excitatory currents in ms
V_m | Membrane potential in mV
beta_Ca | ?? Not declared in NEST documentation
t_ref | Duration of refractory period (V_m = V_reset) in ms
E_in | Inhibitory reversal potential in mV
Ca | ?? Not declared in NEST documentation
C_m | Capacity of the membrane in pF
g_ex | Excitatory synaptic conductance in nS
g_in | Inhibitory synaptic conductance in nS
tau_syn_in | Time constant of postsynaptic inhibitory currents in ms
tau_Ca | ?? Not declared in NEST documentation

![12] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/iaf_cond_exp_sfa_rr.png)

#### 13. iaf_neuron

Parameters | Description
------------------|--------
V_reset | Reset membrane potential after a spike in mV
beta_Ca | ?? Not declared in NEST documentation
tau_m | Membrane time constant in ms
I_e | Constant input current in pA
t_spike | Point in time of last spike in ms
V_m | Membrane potential in mV
E_L | Resting membrane potential in mV
V_th | Spike threshold in mV
t_ref | Duration of refractory period (V_m = V_reset) in ms
Ca | ?? Not declared in NEST documentation
C_m | Capacity of the membrane in pF
tau_Ca | ?? Not declared in NEST documentation

![13] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/iaf_neuron.png)

#### 14. iaf_psc_alpha

Parameters | Description
------------------|--------
V_reset | Reset membrane potential after a spike in mV
V_th | Spike threshold in mV
tau_m | Membrane time constant in ms
I_e | Constant input current in pA
t_spike | Point in time of last spike in ms
V_m | Membrane potential in mV
E_L | Resting membrane potential in mV
tau_syn_ex | Rise time of the excitatory synaptic alpha function in ms
beta_Ca | ?? Not declared in NEST documentation
t_ref | Duration of refractory period (V_m = V_reset) in ms
Ca | ?? Not declared in NEST documentation
C_m | Capacity of the membrane in pF
tau_syn_in | Rise time of the inhibitory synaptic alpha function in ms
V_min | Absolute lower value for the membrane potential
tau_Ca | ?? Not declared in NEST documentation

![14] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/iaf_psc_alpha.png)

#### 15. iaf_psc_alpha_canon

Parameters | Description
------------------|--------
V_reset | Reset membrane potential after a spike in mV
tau_syn |
V_th | Spike threshold in mV
tau_m | Membrane time constant in ms
I_e | Constant input current in pA
t_spike | Point in time of last spike in ms
V_m | Membrane potential in mV
E_L | Resting membrane potential in mV
is_refractory | Neuron is in refractory period (debugging
beta_Ca | ?? Not declared in NEST documentation
t_ref | Duration of refractory period (V_m = V_reset) in ms
Ca | ?? Not declared in NEST documentation
C_m | Capacity of the membrane in pF
V_min | Absolute lower value for the membrane potential
tau_Ca | ?? Not declared in NEST documentation

![15] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/iaf_psc_alpha_canon.png)

#### 16. iaf_psc_alpha_presc

Parameters | Description
------------------|--------
V_reset | Reset membrane potential after a spike in mV
beta_Ca | ?? Not declared in NEST documentation
tau_m | Membrane time constant in ms
I_e | Constant input current in pA
t_spike | Point in time of last spike in ms
V_m | Membrane potential in mV
E_L | Resting membrane potential in mV
V_th | Spike threshold in mV
t_ref | Duration of refractory period (V_m = V_reset) in ms
Ca | ?? Not declared in NEST documentation
C_m | Capacity of the membrane in pF
V_min | Absolute lower value for the membrane potential
tau_Ca | ?? Not declared in NEST documentation

![16] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/iaf_psc_alpha_presc.png)

#### 17. iaf_psc_delta

Parameters | Description
------------------|--------
V_reset | Reset membrane potential after a spike in mV
tau_m | Membrane time constant in ms
refractory_input | If true do not discard input during refractory period. Default: false.
t_spike | Point in time of last spike in ms
V_m | Membrane potential in mV
E_L | Resting membrane potential in mV
V_th | Spike threshold in mV
beta_Ca | ?? Not declared in NEST documentation
t_ref | Duration of refractory period (V_m = V_reset) in ms
Ca | ?? Not declared in NEST documentation
C_m | Capacity of the membrane in pF
I_e | Constant input current in pA
V_min | Absolute lower value for the membrane potential
tau_Ca | ?? Not declared in NEST documentation

![17] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/iaf_psc_delta.png)

#### 18. iaf_psc_delta_canon

Parameters | Description
------------------|--------
V_reset | Reset membrane potential after a spike in mV
V_th | Spike threshold in mV
tau_m | Membrane time constant in ms
refractory_input | If true do not discard input during refractory period. Default: false.
t_spike | Point in time of last spike in ms
V_m | Membrane potential in mV
E_L | Resting membrane potential in mV
is_refractory | Neuron is in refractory period (debugging)
beta_Ca | ?? Not declared in NEST documentation
t_ref | Duration of refractory period (V_m = V_reset) in ms
Ca | ?? Not declared in NEST documentation
C_m | Capacity of the membrane in pF
I_e | Constant input current in pA
V_min | Absolute lower value for the membrane potential
tau_Ca | ?? Not declared in NEST documentation

![18] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/iaf_psc_delta_canon.png)

#### 19. iaf_psc_exp

Parameters | Description
------------------|--------
V_reset | Reset membrane potential after a spike in mV
V_th | Spike threshold in mV
tau_m | Membrane time constant in ms
I_e | Constant input current in pA
t_spike | Point in time of last spike in ms
V_m | Membrane potential in mV
E_L | Resting membrane potential in mV
tau_syn_ex | Time constant of postsynaptic excitatory currents in ms
beta_Ca | ?? Not declared in NEST documentation
t_ref | Duration of refractory period (V_m = V_reset) in ms
Ca | ?? Not declared in NEST documentation
C_m | Capacity of the membrane in pF
tau_syn_in | Time constant of postsynaptic inhibitory currents in ms
tau_Ca | ?? Not declared in NEST documentation

![19] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/iaf_psc_exp.png)

#### 20. iaf_psc_exp_ps

Parameters | Description
------------------|--------
V_reset | Reset membrane potential after a spike in mV
tau_syn_ex | Time constant of postsynaptic excitatory currents in ms
tau_m | Membrane time constant in ms
I_e | Constant input current in pA
t_spike | Point in time of last spike in ms
V_m | Membrane potential in mV
E_L | Resting membrane potential in mV
is_refractory | Neuron is in refractory period (debugging)
tau_minus_triplet |
V_th | Spike threshold in mV
beta_Ca | ?? Not declared in NEST documentation
t_ref | Duration of refractory period (V_m = V_reset) in ms
Ca | ?? Not declared in NEST documentation
C_m | Capacity of the membrane in pF
tau_syn_in | Time constant of postsynaptic inhibitory currents in ms
V_min | Absolute lower value for the membrane potential
tau_Ca | ?? Not declared in NEST documentation

![20] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/iaf_psc_exp_ps.png)

#### 21. iaf_tum_2000

Parameters | Description
------------------|--------
t_ref_tot | Duration of total refractory period (no spiking) in ms
V_reset | Reset membrane potential after a spike in mV
V_th | Spike threshold in mV
tau_m | Membrane time constant in ms
I_e | Constant input current in pA
t_spike | Point in time of last spike in ms
V_m | Membrane potential in mV
E_L | Resting membrane potential in mV
tau_syn_ex | Time constant of postsynaptic excitatory currents in ms
t_ref_abs | Duration of absolute refractory period (V_m = V_reset) in ms
beta_Ca | ?? Not declared in NEST documentation
Ca | ?? Not declared in NEST documentation
C_m | Capacity of the membrane in pF
tau_syn_in | Time constant of postsynaptic inhibitory currents in ms
tau_Ca | ?? Not declared in NEST documentation

![21] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/iaf_tum_2000.png)

#### 22. izhikevich

Parameters | Description
------------------|--------
I_e | Constant input current in pA
t_spike | Point in time of last spike in ms
V_m | Membrane potential in mV
V_th | Spike threshold in mV
U_m | Membrane potential recovery variable
beta_Ca | ?? Not declared in NEST documentation
a | describes time scale of recovery variable
c | after-spike reset value of V_m
b | sensitivity of recovery variable
d | after-spike reset value of U_m
Ca | ?? Not declared in NEST documentation
V_min | Absolute lower value for the membrane potential
tau_Ca | ?? Not declared in NEST documentation

![22] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/izhikevich.png)

#### 23. mat2_psc_exp

Parameters | Description
------------------|--------
V_th | Spike threshold in mV
tau_m | Membrane time constant in ms
I_e | Constant input current in pA
t_spike | Point in time of last spike in ms
V_m | Membrane potential in mV
E_L | Resting membrane potential in mV
tau_syn_ex | Time constant of postsynaptic excitatory currents in ms
beta_Ca | ?? Not declared in NEST documentation
t_ref | Duration of refractory period (V_m = V_reset) in ms
Ca | ?? Not declared in NEST documentation
C_m | Capacity of the membrane in pF
tau_syn_in | Time constant of postsynaptic inhibitory currents in ms
tau_Ca | ?? Not declared in NEST documentation

![23] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/mat2_psc_exp.png)

#### 24. pp_pop_psc_delta

Parameters | Description
------------------|--------
tau_m | Membrane time constant in ms
I_e | Constant input current in pA
V_m | Membrane potential in mV
C_m | Capacity of the membrane in pF

![24] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/pp_pop_psc_delta.png)

#### 25. pp_psc_delta

Parameters | Description
------------------|--------
tau_m | Membrane time constant in ms
I_e | Constant input current in pA
t_spike | Point in time of last spike in ms
V_m | Membrane potential in mV
t_ref_remaining | Time remaining till end of refractory state.(ms)
beta_Ca | ?? Not declared in NEST documentation
Ca | ?? Not declared in NEST documentation
C_m | Capacity of the membrane in pF
tau_Ca | ?? Not declared in NEST documentation

![25] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/pp_psc_delta.png)
