# Must be the first
import neucogar.api_kernel as api
import neucogar.api_diagrams as diagrams

# Set new settings
api.SetKernelStatus(local_num_threads=4,
                    data_path='txt',
                    resolution=0.1)

# Import connectomes
from serotonin.connectomes import *

api.Simulate(1000.)

diagrams.BuildSpikeDiagrams()
diagrams.BuildVoltageDiagrams()

