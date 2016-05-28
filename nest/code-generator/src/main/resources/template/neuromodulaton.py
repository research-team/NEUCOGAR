from func import *

logger = logging.getLogger('neuromodulation')
startbuild = datetime.datetime.now()



# Connect the volume transmitter to the parts
vt_ex = nest.Create('volume_transmitter')
vt_in = nest.Create('volume_transmitter')
DOPA_synparams_ex['vt'] = vt_ex[0]
DOPA_synparams_in['vt'] = vt_in[0]
nest.CopyModel('stdp_dopamine_synapse', dopa_model_ex, DOPA_synparams_ex)
nest.CopyModel('stdp_dopamine_synapse', dopa_model_in, DOPA_synparams_in)

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