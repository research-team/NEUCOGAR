# Must be the first
import neucogar.api_kernel as api

import sys
sys.path.append("/gpfs/GLOBAL_JOB_REPO_KPFU/openlab/scripts/DA_5HT")

# Set new settings
api.SetKernelStatus(total_num_virtual_procs=70,
                    data_path='txt',
                    resolution=0.1)

# Import connectomes
from serotonin.connectomes import *


api.Simulate(21000.)

