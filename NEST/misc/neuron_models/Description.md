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

Adaptive exponential Integrate-and-fire model with alpha-function synaptic conductances.

Parameters | Value | Description
------------------|-------|--------
E_ex |0.0 | Excitatory reversal potential in mV
dg_in | 0.0 |First derivative of g_in in nS/ms
V_reset | -60.0 | Reset membrane potential after a spike in mV
V_peak | 0.0 |Spike detection threshold in mV
V_th |-50.4 | Spike threshold in mV
I_e |0.0 | Constant input current in pA
g_L |30.0 | Leak conductance in nS
t_spike |-1.0 | Point in time of last spike in ms
tau_w | 144.0 | Adaptation time constant in ms
E_L | -70.6 | Resting membrane potential in mV 
dg_ex | 0.0 | First derivative of g_ex in nS/ms
tau_syn_ex | 0.2 | Time constant of postsynaptic excitatory currents in ms
Delta_T | 2.0 | Slope factor in mV
V_m | -70.6 | Membrane potential in mV
beta_Ca |  0.001 | ?? Not declared in NEST documentation
t_ref | 0.0 | Duration of refractory period (V_m = V_reset) in ms
a | 4.0 | Subthreshold adaptation in nS
E_in | -85.0 | Inhibitory reversal potential in mV
b | 80.5 | Spike-triggered adaptation in pA
Ca |  0.0 | ?? Not declared in NEST documentation
C_m | 281.0 | Capacity of the membrane in pF
g_ex | 0.0 | Excitatory synaptic conductance in nS
g_in | 0.0 | Inhibitory synaptic conductance in nS
w | 0.0 | Spike-adaptation current in pA
tau_syn_in | 2.0 | Time constant of postsynaptic inhibitory currents in ms
tau_Ca | 10000.0 | ?? Not declared in NEST documentation

![1] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/aeif_cond_alpha.png)

#### 2. aeif_cond_alpha_RK5

Adaptive exponential integrate-and-fire neuron according to Brette and Gerstner (2005). Synaptic conductances are modelled as alpha-functions.

Parameters | Value| Description
---------|---------|--------
E_ex | 0.0 |Excitatory reversal potential in mV
dg_in | 0.0 | First derivative of g_in in nS/ms
V_reset | -60.0 | Reset membrane potential after a spike in mV
V_peak | 0.0 | Spike detection threshold in mV
V_th | -50.4 | Spike threshold in mV
I_e | 0.0 | Constant input current in pA
g_L |  30.0 | Leak conductance in nS
t_spike | -1.0 | Point in time of last spike in ms
tau_w | 144.0 | Adaptation time constant in ms
MAXERR | 1e-10 | Error estimate tolerance for adaptive stepsize control (steps accepted if err<=MAXERR). In mV. Note that the error refers to the difference between the 4th and 5th order RK terms. Default 1e-10 mV
E_L | -70.6 | Resting membrane potential in mV
dg_ex | 0.0 | First derivative of g_ex in nS/ms
tau_syn_ex | 0.2 | Time constant of postsynaptic excitatory currents in ms
Delta_T | 2.0 | Slope factor in mV
V_m | -70.6 | Membrane potential in mV
beta_Ca | 0.001 | ?? Not declared in NEST documentation
t_ref | 0.0 | Duration of refractory period (V_m = V_reset) in ms
a | 4.0 | Subthreshold adaptation in nS
E_in | -85.0 | Inhibitory reversal potential in mV
b |  80.5 | Spike-triggered adaptation in pA
HMIN | 0.001 |Minimal stepsize for numerical integration in ms
Ca | 0.0 | ?? Not declared in NEST documentation
C_m | 281.0 | Capacity of the membrane in pF
g_ex | 0.0 | Excitatory synaptic conductance in nS
g_in | 0.0 | Inhibitory synaptic conductance in nS
w | 0.0 | Spike-adaptation current in pA
tau_syn_in | 2.0 | Time constant of postsynaptic inhibitory currents in ms
tau_Ca | 10000.0 | ?? Not declared in NEST documentation

![2] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/aeif_cond_alpha_RK5.png)

#### 3. aeif_cond_exp

Adaptive exponential integrate and fire neuron according to Brette and Gerstner (2005), with post-synaptic conductances in the form of truncated exponentials.

Parameters | Value| Description
-------|-----------|--------
E_ex | 0.0 | Excitatory reversal potential in mV
V_reset | -60.0 | Reset membrane potential after a spike in mV
V_peak | 0.0 | Spike detection threshold in mV
V_th | -50.4 | Spike threshold in mV
I_e | 0.0 | Constant input current in pA
g_L | 30.0 | Leak conductance in nS
t_spike | -1.0 | Point in time of last spike in ms
tau_w | 144.0 | Adaptation time constant in ms
E_L | -70.6 | Resting membrane potential in mV
tau_syn_ex | 0.2 | Time constant of postsynaptic excitatory currents in ms
Delta_T | 2.0 | Slope factor in mV
V_m | -70.6 | Membrane potential in mV
beta_Ca | 0.001 | ?? Not declared in NEST documentation
t_ref | 0.0 | Duration of refractory period (V_m = V_reset) in ms 
a | 4.0 | Subthreshold adaptation in nS
E_in | -85.0 | Inhibitory reversal potential in mV
b | 80.5 | Spike-triggered adaptation in pA
Ca |  0.0 | ?? Not declared in NEST documentation
C_m | 281.0 | Capacity of the membrane in pF
g_ex | 0.0 | Excitatory synaptic conductance in nS
g_in | 0.0 | Inhibitory synaptic conductance in nS
w | 0.0 | Spike-adaptation current in pA
tau_syn_in | 2.0 | Time constant of postsynaptic inhibitory currents in ms
tau_Ca | 10000.0 | ?? Not declared in NEST documentation

![3] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/aeif_cond_exp.png)

#### 4. amat2_psc_exp

Implementation of a leaky integrate-and-fire model with exponential shaped postsynaptic currents (PSCs). Thus, postsynaptic currents have an infinitely short rise time.

Parameters| Value | Description
--------|----------|--------
V_th |  -65.0 | Spike threshold in mV
tau_m | 10.0 | Membrane time constant in ms
I_e | 0.0 | Constant input current in pA
t_spike | -1.0 | Point in time of last spike in ms
V_m | -70.0 | Membrane potential in mV
E_L | -70.0 | Resting membrane potential in mV
tau_syn_ex | 1.0 | Time constant of postsynaptic excitatory currents in ms
beta_Ca | 0.001 | ?? Not declared in NEST documentation
t_ref | 2.0 | Duration of refractory period (V_m = V_reset) in ms
Ca | 0.0 | ?? Not declared in NEST documentation
C_m | 200.0 | Capacity of the membrane in pF
tau_syn_in | 3.0 | Time constant of postsynaptic inhibitory currents in ms
tau_Ca | 10000.0 | ?? Not declared in NEST documentation

![4] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/amat2_psc_exp.png)

#### 5. hh_cond_exp_traub

Implementation of a modified Hodkin-Huxley model 

Parameters| Value | Description
---------|---------|--------
V_T | -63.0 | Voltage offset that controls dynamics. For default parameters V_T = -63mV results in a threshold around -50mV
E_ex | 0.0 | Excitatory reversal potential in mV
I_e | 0.0 | Constant input current in pA
g_L | 10.0 | Leak conductance in nS
t_spike | -1.0 | Point in time of last spike in ms
g_K |6000.0 | Potassium peak conductance in nS
E_K | -90.0 | Potassium reversal potential in mV
V_m | -60.0 | Membrane potential in mV
E_L | -60.0 | Resting membrane potential in mV
Act_m | 9.89556309675e-09 | Activation variable m
Act_h | 0.999999999106 | Activation variable h
tau_syn_ex | 5.0 | Time constant of postsynaptic excitatory currents in ms
Inact_n | 2.5515770516e-07 | Inactivation variable n
beta_Ca | 0.001 | ?? Not declared in NEST documentation
E_Na | 50.0 | Sodium reversal potential in mV
E_in | -80.0 | Inhibitory reversal potential in mV
Ca | 0.0 |  ?? Not declared in NEST documentation
C_m | 200.0 | Capacity of the membrane in pF
g_Na | 20000.0 | Sodium peak conductance in nS
tau_syn_in | 10.0 |Time constant of postsynaptic inhibitory currents in ms
tau_Ca | 10000.0 | ?? Not declared in NEST documentation

![5] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/hh_cond_exp_traub.png)

#### 6. hh_psc_alpha

Hodgkin-Huxley model with alpha-function post-synaptic currents.

Parameters| Value | Description
---------|---------|--------
I_e | 0.0 | Constant input current in pA
g_L | 30.0 | Leak conductance in nS
t_spike | -1.0 | Point in time of last spike in ms
g_K | 3600.0 | Potassium peak conductance in nS
E_K | -77.0 | Potassium reversal potential in mV
V_m | -65.0 | Membrane potential in mV
t_ref | 2.0 | Duration of refractory period (V_m = V_reset) in ms
E_L | -54.402 | Resting membrane potential in mV
Act_m | 0.0529324852572 | Activation variable m
Act_h | 0.596120753508 | Activation variable h
tau_syn_ex | 0.2 | Time constant of postsynaptic excitatory currents in ms
Inact_n | 0.317676914061 | Inactivation variable n
beta_Ca | 0.001 | ?? Not declared in NEST documentation
E_Na | 50.0 | Sodium reversal potential in mV
Ca | 0.0 | ?? Not declared in NEST documentation
C_m | 100.0 | Capacity of the membrane in pF
g_Na | 12000.0 | Sodium peak conductance in nS
tau_syn_in | 2.0 | Time constant of postsynaptic inhibitory currents in ms
tau_Ca | 10000.0 | ?? Not declared in NEST documentation

![6] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/hh_psc_alpha.png)

#### 7. hh_psc_alpha_gap

Implementation of a spiking neuron using the Hodkin-Huxley formalism. In contrast to hh_psc_alpha the implementation additionally supports gap junctions.

Parameters | Value | Description
---------|---------|--------
I_e | 0.0 | Constant input current in pA
g_L | 10.0 | Leak conductance in nS
t_spike | -1.0 | Point in time of last spike in ms
E_K | -90.0 | Potassium reversal potential in mV
V_m | -69.6040119163 | Membrane potential in mV
t_ref | 2.0 | Duration of refractory period (V_m = V_reset) in ms
E_L | -70.0 | Resting membrane potential in mV
Act_m | 0.0191987669851 | Activation variable m
Act_h | 0.868462041294 | Activation variable h
tau_syn_ex | 0.2 | Time constant of postsynaptic excitatory currents in ms
Inact_n | 0.000574157622836 | Inactivation variable n
beta_Ca | 0.001 | ?? Not declared in NEST documentation
E_Na | 74.0 | Sodium reversal potential in mV
Ca | 0.0 | ?? Not declared in NEST documentation
C_m | 40.0 | Capacity of the membrane in pF
g_Na | 4500.0 | Sodium peak conductance in nS
tau_syn_in | 2.0 | Time constant of postsynaptic inhibitory currents in ms
tau_Ca | 10000.0 | ?? Not declared in NEST documentation

![7] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/hh_psc_alpha_gap.png)

#### 8. iaf_chs_2007

Spike-response model used in Carandini et al 2007.

Parameters | Value| Description
---------|---------|--------
V_reset |  2.31 | Reset membrane potential after a spike in mV
t_spike | -1.0 | Point in time of last spike in ms
V_m | 0.0 | Membrane potential in mV
beta_Ca | 0.001 | ?? Not declared in NEST documentation
Ca | 0.0 | ?? Not declared in NEST documentation
tau_Ca | 10000.0 | ?? Not declared in NEST documentation

![8] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/iaf_chs_2007.png)

#### 9. iaf_chxk_2008

Implementation of a spiking neuron using IAF dynamics with conductance-based synapses. It is modeled after iaf_cond_alpha with the addition of after hyper-polarization current instead of a membrane potential reset. Incoming spike events induce a post-synaptic change of conductance modeled by an alpha function. The alpha function is normalized such that an event of weight 1.0 results in a peak current of 1 nS at t = tau_syn.

Parameters| Value | Description
--------|----------|--------
E_ex | 20.0 | Excitatory reversal potential in mV
V_th | -45.0 | Spike threshold in mV
I_e | 0.0 | Constant input current in pA
g_L | 100.0 | Leak conductance in nS
t_spike | -1.0 | Point in time of last spike in ms
V_m | -60.0 | Membrane potential in mV
E_L | -60.0 | Resting membrane potential in mV
tau_syn_ex | 51.0 | Time constant of postsynaptic excitatory currents in ms
beta_Ca | 0.001 | ?? Not declared in NEST documentation
E_in | -90.0 | Inhibitory reversal potential in mV
Ca |  0.0 | ?? Not declared in NEST documentation
C_m | 1000.0 | Capacity of the membrane in pF
tau_syn_in | 1.0 | Time constant of postsynaptic inhibitory currents in ms
g_ahp | 443.8 | AHP conductance
tau_Ca | 10000.0 | ?? Not declared in NEST documentation

![9] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/iaf_chxk_2008.png)

#### 10. iaf_cond_alpha

Implementation of a spiking neuron using IAF dynamics with conductance-based synapses. Incoming spike events induce a post-synaptic change of conductance modelled by an alpha function. The alpha function is normalised such that an event of weight 1.0 results in a peak current of 1 nS

Parameters| Value | Description
--------|----------|--------
E_ex |  0.0 | Excitatory reversal potential in mV
V_reset | -60.0 | Reset membrane potential after a spike in mV
V_th | -55.0 | Spike threshold in mV
I_e |  0.0 | Constant input current in pA
g_L | 16.6667 | Leak conductance in nS
t_spike | -1.0 | Point in time of last spike in ms
V_m | -70.0 | Membrane potential in mV
E_L | -70.0 | Resting membrane potential in mV
tau_syn_ex | 0.2 | Time constant of postsynaptic excitatory currents in ms
beta_Ca | 0.001 | ?? Not declared in NEST documentation
t_ref | 2.0 | Duration of refractory period (V_m = V_reset) in ms
E_in | -85.0 | Inhibitory reversal potential in mV
Ca | 0.0 | ?? Not declared in NEST documentation 
C_m | 250.0 | Capacity of the membrane in pF
tau_syn_in | 2.0 | Time constant of postsynaptic inhibitory currents in ms
tau_Ca | 10000.0 | ?? Not declared in NEST documentation

![10] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/iaf_cond_alpha.png)

#### 11. iaf_cond_exp

Integrate-and-fire model with exponential synaptic conductances.

Parameters| Value | Description
----------|--------|--------
E_ex | 0.0 | Excitatory reversal potential in mV
V_reset | -60.0 | Reset membrane potential after a spike in mV
V_th | -55.0 | Spike threshold in mV
I_e | 0.0 | Constant input current in pA
g_L | 16.6667 | Leak conductance in nS
t_spike | -1.0 | Point in time of last spike in ms
V_m | -70.0 | Membrane potential in mV
E_L | -70.0 | Resting membrane potential in mV
tau_syn_ex | 0.2 | Time constant of postsynaptic excitatory currents in ms
beta_Ca | 0.001 | ?? Not declared in NEST documentation
t_ref |  2.0 | Duration of refractory period (V_m = V_reset) in ms
E_in | -85.0 | Inhibitory reversal potential in mV
Ca | 0.0 | ?? Not declared in NEST documentation
C_m | 250.0 | Capacity of the membrane in pF
tau_syn_in | 2.0 |Time constant of postsynaptic inhibitory currents in ms
tau_Ca | 10000.0 | ?? Not declared in NEST documentation

![11] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/iaf_cond_exp.png)

#### 12. iaf_cond_exp_sfa_rr

Implementation of a spiking neuron using IAF dynamics with conductance-based synapses, with additional spike-frequency adaptation and relative refractory mechanisms as described in Dayan+Abbott, 2001, page 166. As for the iaf_cond_exp_sfa_rr, Incoming spike events induce a post-synaptic change of conductance modelled by an exponential function. The exponential function is normalised such that an event of weight 1.0 results in a peak current of 1 nS.

Parameters | Value | Description
------------|------|--------
E_ex | 0.0 | Excitatory reversal potential in mV
V_reset | 110.0 | Reset membrane potential after a spike in mV
I_e | 0.0 | Constant input current in pA
g_L | 28.95 | Leak conductance in nS
V_th | -57.0 | Spike threshold in mV
t_spike | -1.0 | Point in time of last spike in ms
E_L | -70.0 | Resting membrane potential in mV
tau_syn_ex | 1.5 | Time constant of postsynaptic excitatory currents in ms
V_m | -70.0 | Membrane potential in mV
beta_Ca | 0.001 | ?? Not declared in NEST documentation
t_ref | 0.5 | Duration of refractory period (V_m = V_reset) in ms
E_in |-75.0 | Inhibitory reversal potential in mV
Ca | 0.0 | ?? Not declared in NEST documentation
C_m | 289.5 | Capacity of the membrane in pF
g_ex | 0.0 | Excitatory synaptic conductance in nS
g_in | 0.0 | Inhibitory synaptic conductance in nS
tau_syn_in | 10.0 | Time constant of postsynaptic inhibitory currents in ms
tau_Ca | 10000.0 | ?? Not declared in NEST documentation

![12] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/iaf_cond_exp_sfa_rr.png)

#### 13. iaf_neuron

Default integrate-and-fire model with alpha-function post-synaptic currents.

Parameters| Value | Description
----------|--------|--------
V_reset | -70.0 | Reset membrane potential after a spike in mV
beta_Ca | 0.001 | ?? Not declared in NEST documentation
tau_m | 10.0 | Membrane time constant in ms
I_e | 0.0 | Constant input current in pA
t_spike | -1.0 | Point in time of last spike in ms
V_m | -70.0 | Membrane potential in mV
E_L | -70.0 | Resting membrane potential in mV
V_th | -55.0 | Spike threshold in mV
t_ref | 2.0 | Duration of refractory period (V_m = V_reset) in ms
Ca |  0.0 | ?? Not declared in NEST documentation
C_m | 250.0 | Capacity of the membrane in pF
tau_Ca | 10000.0 | ?? Not declared in NEST documentation

![13] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/iaf_neuron.png)

#### 14. iaf_psc_alpha

Implementation of a leaky integrate-and-fire model with alpha-function shaped synaptic currents. Thus, synaptic currents and the resulting post-synaptic potentials have a finite rise time.

Parameters| Value | Description
-------|-----------|--------
V_reset | -70.0 |  Reset membrane potential after a spike in mV
V_th | -55.0 | Spike threshold in mV
tau_m | 10.0 | Membrane time constant in ms
I_e | 0.0 | Constant input current in pA
t_spike | -1.0 | Point in time of last spike in ms
V_m | -70.0 | Membrane potential in mV
E_L | -70.0 | Resting membrane potential in mV
tau_syn_ex | 2.0 | Rise time of the excitatory synaptic alpha function in ms
beta_Ca | 0.001 | ?? Not declared in NEST documentation
t_ref |  2.0 | Duration of refractory period (V_m = V_reset) in ms
Ca | 0.0 | ?? Not declared in NEST documentation
C_m | 250.0 | Capacity of the membrane in pF
tau_syn_in |  2.0 | Rise time of the inhibitory synaptic alpha function in ms
V_min | -inf | Absolute lower value for the membrane potential
tau_Ca |  10000.0 | ?? Not declared in NEST documentation

![14] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/iaf_psc_alpha.png)

#### 15. iaf_psc_alpha_canon

Like iaf_neuron, but with separate time-constants for excitatory and inhibitory synapses.

Parameters| Value | Description
---------|---------|--------
V_reset | -70.0 | Reset membrane potential after a spike in mV
V_th | -55.0 | Spike threshold in mV
tau_m | 10.0 | Membrane time constant in ms
I_e | 0.0 | Constant input current in pA
t_spike | -1.0 | Point in time of last spike in ms
V_m | -70.0 | Membrane potential in mV
E_L | -70.0 | Resting membrane potential in mV
beta_Ca | 0.001 | ?? Not declared in NEST documentation
t_ref | 2.0 | Duration of refractory period (V_m = V_reset) in ms
Ca | 0.0 | ?? Not declared in NEST documentation
C_m | 250.0 | Capacity of the membrane in pF
V_min | -inf | Absolute lower value for the membrane potential
tau_Ca | 10000.0 | ?? Not declared in NEST documentation

![15] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/iaf_psc_alpha_canon.png)

#### 16. iaf_psc_alpha_presc

Leaky iaf neuron, alpha PSC synapses, canonical implementation.

Parameters| Value | Description
---------|---------|--------
V_reset | -70.0 | Reset membrane potential after a spike in mV
beta_Ca | 0.001 | ?? Not declared in NEST documentation
tau_m | 10.0 | Membrane time constant in ms
I_e | 0.0 | Constant input current in pA
t_spike | -1.0 | Point in time of last spike in ms
V_m | -70.0 | Membrane potential in mV
E_L | -70.0 | Resting membrane potential in mV
V_th | -55.0 | Spike threshold in mV
t_ref | 2.0 | Duration of refractory period (V_m = V_reset) in ms
Ca | 0.0 |?? Not declared in NEST documentation
C_m | 250.0 | Capacity of the membrane in pF
V_min | -inf | Absolute lower value for the membrane potential
tau_Ca | 10000.0 | ?? Not declared in NEST documentation

![16] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/iaf_psc_alpha_presc.png)

#### 17. iaf_psc_delta

Integrate-and-fire model with delta-function post-synaptic currents.

Parameters | Value| Description
---------|---------|--------
V_reset | -70.0 | Reset membrane potential after a spike in mV
tau_m |  10.0 | Membrane time constant in ms
refractory_input | False | If true do not discard input during refractory period. Default: false.
t_spike | -1.0 | Point in time of last spike in ms
V_m | -70.0 | Membrane potential in mV
E_L | -70.0 | Resting membrane potential in mV
V_th | -55.0 | Spike threshold in mV
beta_Ca | 0.001 | ?? Not declared in NEST documentation
t_ref | 2.0 | Duration of refractory period (V_m = V_reset) in ms
Ca | 0.0 | ?? Not declared in NEST documentation
C_m | 250.0 | Capacity of the membrane in pF
I_e | 0.0 | Constant input current in pA
V_min | -1.79769313486e+308 | Absolute lower value for the membrane potential
tau_Ca | 10000.0 | ?? Not declared in NEST documentation

![17] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/iaf_psc_delta.png)

#### 18. iaf_psc_delta_canon

Leaky integrate-and-fire neuron model.

Parameters | Value| Description
--------|----------|--------
V_reset | -70.0 | Reset membrane potential after a spike in mV
V_th | -55.0 | Spike threshold in mV
tau_m | 10.0 | Membrane time constant in ms
refractory_input | False | If true do not discard input during refractory period. Default: false.
t_spike | -1.0 | Point in time of last spike in ms
V_m | -70.0 | Membrane potential in mV
E_L | -70.0 | Resting membrane potential in mV
beta_Ca | 0.001 | ?? Not declared in NEST documentation
t_ref | 2.0 | Duration of refractory period (V_m = V_reset) in ms
Ca | 0.0 | ?? Not declared in NEST documentation
C_m | 250.0 | Capacity of the membrane in pF
I_e | 0.0 | Constant input current in pA
V_min | -1.79769313486e+308 | Absolute lower value for the membrane potential
tau_Ca |  10000.0 | ?? Not declared in NEST documentation

![18] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/iaf_psc_delta_canon.png)

#### 19. iaf_psc_exp

Leaky integrate-and-fire neuron model with exponential PSCs.

Parameters | Value | Description
-----------|-------|--------
V_reset | -70.0 | Reset membrane potential after a spike in mV
V_th | -55.0 | Spike threshold in mV
tau_m | 10.0 | Membrane time constant in ms
I_e |  0.0 | Constant input current in pA
t_spike | -1.0 | Point in time of last spike in ms
V_m | -70.0 | Membrane potential in mV
E_L | -70.0 | Resting membrane potential in mV
tau_syn_ex | 2.0 | Time constant of postsynaptic excitatory currents in ms
beta_Ca | 0.001 | ?? Not declared in NEST documentation
t_ref | 2.0 | Duration of refractory period (V_m = V_reset) in ms
Ca | 0.0 | ?? Not declared in NEST documentation
C_m | 250.0 | Capacity of the membrane in pF
tau_syn_in | 2.0 | Time constant of postsynaptic inhibitory currents in ms
tau_Ca | 10000.0 | ?? Not declared in NEST documentation

![19] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/iaf_psc_exp.png)

#### 20. iaf_psc_exp_ps

Integrate-and-fire neuron model with exponential PSCs and adaptive threshold.

Parameters | Value| Description
-----------|-------|--------
V_reset | -70.0 | Reset membrane potential after a spike in mV
tau_syn_ex | 2.0 | Time constant of postsynaptic excitatory currents in ms
tau_m | 10.0 | Membrane time constant in ms
I_e | 0.0 | Constant input current in pA
t_spike | -1.0 | Point in time of last spike in ms
V_m | -70.0 | Membrane potential in mV
E_L | -70.0 | Resting membrane potential in mV
V_th | -55.0 | Spike threshold in mV
beta_Ca | 0.001 | ?? Not declared in NEST documentation
t_ref | 2.0 | Duration of refractory period (V_m = V_reset) in ms
Ca | 0.0 | ?? Not declared in NEST documentation
C_m | 250.0 | Capacity of the membrane in pF
tau_syn_in | 2.0 | Time constant of postsynaptic inhibitory currents in ms
V_min | -inf | Absolute lower value for the membrane potential
tau_Ca | 10000.0 | ?? Not declared in NEST documentation

![20] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/iaf_psc_exp_ps.png)

#### 21. iaf_tum_2000

Implementation of a leaky integrate-and-fire model with exponential shaped postsynaptic currents (PSCs)

Parameters | Value| Description
--------|----------|--------
t_ref_tot | 2.0 | Duration of total refractory period (no spiking) in ms
V_reset | -70.0 | Reset membrane potential after a spike in mV
V_th | -55.0 | Spike threshold in mV
tau_m | 10.0 | Membrane time constant in ms
I_e | 0.0 | Constant input current in pA
t_spike | -1.0 | Point in time of last spike in ms
V_m | -70.0 | Membrane potential in mV
E_L | -70.0 | Resting membrane potential in mV
tau_syn_ex | 2.0 | Time constant of postsynaptic excitatory currents in ms
t_ref_abs | 2.0 | Duration of absolute refractory period (V_m = V_reset) in ms
beta_Ca | 0.001 | ?? Not declared in NEST documentation
Ca | 0.0 | ?? Not declared in NEST documentation
C_m | 250.0 | Capacity of the membrane in pF
tau_syn_in | 2.0 | Time constant of postsynaptic inhibitory currents in ms
tau_Ca | 10000.0 | ?? Not declared in NEST documentation

![21] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/iaf_tum_2000.png)

#### 22. izhikevich

Model combines the biologically plausibility of Hodgkin-Huxley-type dynamics and the computational efficiency of integrate-and-fire neurons.

Parameters | Value| Description
---------|---------|--------
I_e | 0.0 | Constant input current in pA
t_spike | -1.0 | Point in time of last spike in ms
V_m | -65.0 | Membrane potential in mV
V_th | 30.0 | Spike threshold in mV
U_m | 0.0 | Membrane potential recovery variable
beta_Ca | 0.001 | ?? Not declared in NEST documentation
a | 0.02 | describes time scale of recovery variable
c | -65.0 | after-spike reset value of V_m
b | 0.2 | sensitivity of recovery variable
d | 8.0 | after-spike reset value of U_m
Ca | 0.0 | ?? Not declared in NEST documentation
V_min | -1.79769313486e+308 | Absolute lower value for the membrane potential
tau_Ca | 10000.0 | ?? Not declared in NEST documentation

![22] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/izhikevich.png)

#### 23. mat2_psc_exp

Integrate-and-fire neuron model with exponential PSCs and adaptive threshold.

Parameters | Value| Description
-----|-------------|--------
V_th | -51.0 | Spike threshold in mV
tau_m | 5.0 | Membrane time constant in ms
I_e | 0.0 | Constant input current in pA
t_spike | -1.0 | Point in time of last spike in ms
V_m | -70.0 | Membrane potential in mV
E_L | -70.0 | Resting membrane potential in mV
tau_syn_ex | 1.0 | Time constant of postsynaptic excitatory currents in ms
beta_Ca | 0.001 | ?? Not declared in NEST documentation
t_ref | 2.0 | Duration of refractory period (V_m = V_reset) in ms
Ca | 0.0 | ?? Not declared in NEST documentation
C_m | 100.0 | Capacity of the membrane in pF
tau_syn_in | 3.0 | Time constant of postsynaptic inhibitory currents in ms
tau_Ca | 10000.0 | ?? Not declared in NEST documentation

![23] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/mat2_psc_exp.png)

#### 24. pp_pop_psc_delta

(nest stops working when using inhibitory neurons in this model)

Population of point process neurons with leaky integration of delta-shaped PSCs.

Parameters | Value | Description
----------|--------|--------
tau_m | 10.0 | Membrane time constant in ms
I_e | 0.0 | Constant input current in pA
V_m | 0.0 | Membrane potential in mV
C_m | 250.0 | Capacity of the membrane in pF

![24] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/pp_pop_psc_delta.png)

#### 25. pp_psc_delta

Point process neuron with leaky integration of delta-shaped PSCs.

Parameters | Value | Description
--------|----------|--------
tau_m | 10.0 | Membrane time constant in ms
I_e | 0.0 | Constant input current in pA
t_spike | -1.0 | Point in time of last spike in ms
V_m | 0.0 | Membrane potential in mV
t_ref_remaining | 0.0 | Time remaining till end of refractory state.(ms)
beta_Ca | 0.001 | ?? Not declared in NEST documentation
Ca | 0.0 | ?? Not declared in NEST documentation
C_m | 250.0 | Capacity of the membrane in pF
tau_Ca | 10000.0 | ?? Not declared in NEST documentation

![25] (https://github.com/research-team/NEUCOGAR/blob/master/CalculationNM/Results/pp_psc_delta.png)
