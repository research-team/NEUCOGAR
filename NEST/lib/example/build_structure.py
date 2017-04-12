from api_initialisation import *
from data import *

logger = logging.getLogger('build')

def GenerateStructure(NNumber):
    parts_no_dopa = gpe + gpi + stn + amygdala + (vta[vta_GABA0], vta[vta_GABA1], vta[vta_GABA2], snc[snc_GABA]) + \
                    striatum + motor + prefrontal + nac + pptg + thalamus + snr
    parts_with_dopa = (vta[vta_DA0], vta[vta_DA1], snc[snc_DA])

    glob.all_parts = tuple(sorted(parts_no_dopa + parts_with_dopa))

    NN_coef = float(NNumber) / sum(item[k_NN] for item in glob.all_parts)

    for part in glob.all_parts:
        SetNeuronNumber(part, min_neurons if int(part[k_NN] * NN_coef) < min_neurons else int(part[k_NN] * NN_coef))

    glob.neuron_number = sum(item[k_NN] for item in glob.all_parts)

    logger.debug('Initialized: {0} neurons'.format(glob.neuron_number))

    # Parts without dopamine
    for part in parts_no_dopa:
        Create(part, pyramidal_no_dopa)
    # Parts with dopamine
    for part in parts_with_dopa:
        Create(part, pyramidal_with_dopa)
