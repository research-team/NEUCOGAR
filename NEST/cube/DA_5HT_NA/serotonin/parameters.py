nrn_parameters = {'t_ref': [2.5, 4.0],	# Refractory period
		  'V_m': -70.0,		#
		  'E_L': -70.0,		#
		  'E_K': -77.0,		#
		  'g_L': 30.0,		#
		  'g_Na': 12000.0,	#
		  'g_K': 3600.0,	#
		  'C_m': 134.0,		# Capacity of membrane (pF)
		  'tau_syn_ex': 0.2,	# Time of excitatory action (ms)
		  'tau_syn_in': 2.0,	# Time of inhibitory action (ms)
#		  'tau_minus': 100.
}

stdp_glu_params = {'delay': [2, 2.5],	# Synaptic delay
                   'alpha': 1.0,	# Coeficient for inhibitory STDP time (alpha * lambda)
                   'lambda': 0.,	# Time interval for STDP
                   'Wmax': 10,		# Maximum possible weight
                   'mu_minus': 0.0,	# STDP depression step
                   'mu_plus': 0.0,	# STDP potential step
#                   'tau_plus': 10000.
}

stdp_gaba_params = {'delay': [2, 2.5],	# Synaptic delay
                    'alpha': 1.0,	# Coeficient for inhibitory STDP time (alpha * lambda)
                    'lambda': 0.,	# Time interval for STDP
                    'Wmax': -10.0,	# Maximum possible weight
                    'mu_minus': 0.0,	# STDP depression step
                    'mu_plus': 0.0,	# STDP potential step
#                    'tau_plus': 10000.
}

stdp_sero_ex_params = {'delay': [2, 2.5],	# Synaptic delay
                       'Wmin': 1.,		# Minimum possible weight
                       'Wmax': 100.,		# Maximum possible weight
       	       	       'A_plus': 0.0,		# Amplitude of weight change for facilitation 
                       'A_minus': 0.0,		# Amplitude of weight change for depression
}

stdp_sero_in_params = {'delay': [2, 2.5],	# Synaptic delay
                       'Wmin': -100.,		# Minimum possible weight
                       'Wmax': -20.,		# Maximum possible weight
                       'A_plus': 0.0,		# Amplitude of weight change for facilitation 
                       'A_minus': 0.0,		# Amplitude of weight change for depression 
}
