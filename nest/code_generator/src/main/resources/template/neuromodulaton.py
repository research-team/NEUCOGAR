from func import *

logger = logging.getLogger('neuromodulation')
startbuild = datetime.datetime.now()


# Connect the volume transmitter to the parts
vt_dopa_ex = nest.Create('volume_transmitter')
vt_dopa_in = nest.Create('volume_transmitter')
vt_sero_ex = nest.Create('volume_transmitter')
vt_sero_in = nest.Create('volume_transmitter')
DOPA_synparams_ex['vt'] = vt_dopa_ex[0]
DOPA_synparams_in['vt'] = vt_dopa_in[0]
SERO_synparams_ex['vt'] = vt_sero_ex[0]
SERO_synparams_in['vt'] = vt_sero_in[0]


nest.CopyModel('stdp_dopamine_synapse', dopa_model_ex, DOPA_synparams_ex)
nest.CopyModel('stdp_dopamine_synapse', dopa_model_in, DOPA_synparams_in)
nest.CopyModel('stdp_serotonine_synapse', sero_model_in, SERO_synparams_in)
nest.CopyModel('stdp_serotonine_synapse', sero_model_ex, SERO_synparams_ex)

%1$2s

logger.debug("* * * Creating spike generators...")
%2$2s

logger.debug("* * * Attaching spikes detector")
logger.debug("* * * Attaching multimeters")
%3$2s

endbuild = datetime.datetime.now()

simulate()
get_log(startbuild, endbuild)
save(GUI=statusGUI)