import nest
import numpy as np

nest.ResetKernel()
nest.SetKernelStatus({'overwrite_files': True,  'local_num_threads': 4, 'resolution': 0.1})

%1$2s