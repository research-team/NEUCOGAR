from api_initialisation import *
from data import *

logger = logging.getLogger('build')

def GenerateStructure(NNumber):
    parts_no_dopa = gpe + gpi + stn + striatum + motor + thalamus + snr
    parts_with_dopa = (vta[vta_DA], snc[snc_DA])

    glob.all_parts = tuple(sorted(parts_no_dopa + parts_with_dopa, key=lambda x: x[glob.k_name]))

    NN_coef = float(NNumber) / sum(item[k_NN] for item in glob.all_parts)

    for part in glob.all_parts:
        SetNeuronNumber(part, min_neurons if int(part[k_NN] * NN_coef) < min_neurons else int(part[k_NN] * NN_coef))

    glob.neuron_number = sum(item[k_NN] for item in glob.all_parts)

    logger.debug('Initialized: {0} neurons'.format(glob.neuron_number))

    # Parts without dopamine
    for part in glob.all_parts:
        Create(part, pyramidal_no_dopa)
