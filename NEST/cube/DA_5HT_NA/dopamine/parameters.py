nrn_parameters = {'t_ref': [2.5, 4.0],	# Refractory period
		  'V_m': -70.,		#
		  'E_L': -70.,		#
		  'E_K': -77.,		#
		  'g_L': 30.,		#
		  'g_Na': 12000.,	#
		  'g_K': 3600.,	#
		  'C_m': 134.,		# Capacity of membrane (pF)
		  'tau_syn_ex': 0.2,	# Time of excitatory action (ms)
		  'tau_syn_in': 2.,	# Time of inhibitory action (ms)
#		  'tau_minus': 100.
}

stdp_glu_params = {'delay': [2, 2.5],	# Synaptic delay
                   'alpha': 1.0,	# Coeficient for inhibitory STDP time (alpha * lambda)
                   'lambda': 0.,	# Time interval for STDP
                   'Wmax': 10.,		# Maximum possible weight
                   'mu_minus': 0.,	# STDP depression step
                   'mu_plus': 0.,	# STDP potential step
#                   'tau_plus': 10000.
}

stdp_gaba_params = {'delay': [2, 2.5],	# Synaptic delay
                    'alpha': 1.0,	# Coeficient for inhibitory STDP time (alpha * lambda)
                    'lambda': 0.,	# Time interval for STDP
                    'Wmax': -10.,	# Maximum possible weight
                    'mu_minus': 0.,	# STDP depression step
                    'mu_plus': 0.,	# STDP potential step
#                    'tau_plus': 10000.
}

stdp_dopa_ex_params = {'delay': [2, 2.5],	# Synaptic delay
                       'Wmin': 1.,		# Minimum possible weight
                       'Wmax': 10.,		# Maximum possible weight
                       'A_plus': 0.,		# Amplitude of weight change for facilitation
                       'A_minus': 0.,         # Amplitude of weight change for depression
}

stdp_dopa_in_params = {'delay': [2, 2.5],	# Synaptic delay
                       'Wmin': -50.,		# Minimum possible weight
                       'Wmax': -1.,		# Maximum possible weight
       	       	       'A_plus': 0.,		# Amplitude of weight change for facilitation 
                       'A_minus': 0.,		# Amplitude of weight change for depression 
}
