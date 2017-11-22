__author__  = "Alexey Panzer"
__version__ = "2.0.0"
__tested___ = "09.11.2017 NEST 2.12.0 Python 3"

import numpy as numpy
import logging as log
import nest as NEST

log.basicConfig(format='%(name)s::%(funcName)s %(message)s', level=log.INFO)

# Common information
global_syn_number = 0
global_real_nrn_number = 0
global_sim_nrn_number = 0

start_build = 0
end_build = 0

rec_weight_nrn_num = 5

# Neurons number for spike detector
N_detect = 300

# Neurons number for multimeter
N_volt = 5

# Generator delay
pg_delay = 5.

min_neurons = 10
max_syn_per_nrn = 10000

# Global value of memory usage
byte2mb = 1024 ** 2
syn_mem_usage = 0
nrn_mem_usage = 0
dev_mem_usage = 0
