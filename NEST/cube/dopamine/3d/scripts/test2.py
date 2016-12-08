from func import *
import datetime

logger = logging.getLogger('neuromodulation')
startbuild = datetime.datetime.now()

nest.ResetKernel()
nest.SetKernelStatus({'overwrite_files': True,
                      'local_num_threads': 1,
                      'resolution': 0.1})

nest.CopyModel('static_synapse', gen_static_syn, static_syn)
nest.CopyModel('stdp_synapse', glu_synapse, STDP_synparams_Glu)
nest.CopyModel('stdp_synapse', gaba_synapse, STDP_synparams_GABA)
nest.CopyModel('stdp_synapse', ach_synapse, STDP_synparams_ACh)
nest.CopyModel('stdp_dopamine_synapse', dopa_synapse_ex, DOPA_synparams_ex)
nest.CopyModel('stdp_dopamine_synapse', dopa_synapse_in, DOPA_synparams_in)


generate_neurons(3000)

add_connection(pptg[pptg_Glu], pptg[pptg_GABA])

connect_all()
print "3d connected"
