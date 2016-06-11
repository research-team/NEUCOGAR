# TODO check num_threads before testing / 8 for Cisco Server
# TODO ATTTENTION! Maybe there are some mistakes in neuron parameters! Write to alexey.panzer@gmail.com.

from func import *

logger = logging.getLogger('neuromodulation')
startbuild = datetime.datetime.now()

nest.ResetKernel()
nest.SetKernelStatus({'overwrite_files': True,
                      'local_num_threads': 4,
                      'resolution': 0.1})
generate_neurons(12000)

logger.debug("* * * Start connection initialisation")
# * * * NIGROSTRIATAL * * *
connect(motor[Cortex], thalamus[thalamus_Glu], syn_type=Glu, weight_coef=0.7)
connect(motor[Cortex], striatum[D1], syn_type=Glu)
connect(motor[Cortex], striatum[D2], syn_type=Glu)

connect(striatum[D1], snr[snr_GABA], weight_coef=0.01)
connect(striatum[D1], gpi[gpi_GABA], weight_coef=0.01)

connect(striatum[D1], gpe[gpe_GABA], weight_coef=0.001)
connect(striatum[D2], gpe[gpe_GABA], weight_coef=5)

connect(gpe[gpe_GABA], stn[stn_Glu], weight_coef=0.05)

connect(stn[stn_Glu], snr[snr_GABA], syn_type=Glu, weight_coef=30)
connect(stn[stn_Glu], gpi[gpi_GABA], syn_type=Glu, weight_coef=30)

connect(gpi[gpi_GABA], thalamus[thalamus_Glu], weight_coef=1)
connect(snr[snr_GABA], thalamus[thalamus_Glu], weight_coef=1)

connect(thalamus[thalamus_Glu], motor[FrontalCortex], syn_type=Glu)


if dopa_flag:
    logger.debug("* * * Making neuromodulating connections...")
    # Connect the volume transmitter to the parts
    vt_ex = nest.Create('volume_transmitter')
    vt_in = nest.Create('volume_transmitter')
    DOPA_synparams_ex['vt'] = vt_ex[0]
    DOPA_synparams_in['vt'] = vt_in[0]
    nest.CopyModel('stdp_dopamine_synapse', dopa_synapse_ex, DOPA_synparams_ex)
    nest.CopyModel('stdp_dopamine_synapse', dopa_synapse_in, DOPA_synparams_in)

    nest.Connect(snc[snc_DA][k_IDs], vt_ex)
    nest.Connect(snc[snc_DA][k_IDs], vt_in)
    nest.Connect(vta[vta_DA0][k_IDs], vt_ex)
    nest.Connect(vta[vta_DA0][k_IDs], vt_ex)

    connect(snc[snc_DA], striatum[D1], syn_type=DA_ex)
    connect(snc[snc_DA], striatum[D2], syn_type=DA_in)

    connect(vta[vta_DA0], striatum[D1], syn_type=DA_ex)
    connect(vta[vta_DA0], striatum[D2], syn_type=DA_in)


logger.debug("* * * Creating spike generators...")
if generator_flag:
    connect_generator(motor[Cortex], 0.1, T, rate=300, coef_part=1)


    delta = [1.0, 1.5, 0.38, 0.8, 0.33]

    k = 10
    iter = 0

    for i in range(5) :
        connect_generator(snc[snc_DA], k, k + 3.3, rate = delta[iter], coef_part=1)
        connect_generator(vta[vta_DA0], k, k + 3.3, rate = delta[iter],  coef_part=1)
        iter += 1
        k += 3.3

logger.debug("* * * Attaching spikes detector")
connect_detector(gpi[gpi_GABA])
connect_detector(snr[snr_GABA])
connect_detector(gpe[gpe_GABA])
connect_detector(stn[stn_Glu])
connect_detector(snc[snc_DA])
connect_detector(thalamus[thalamus_Glu])
connect_detector(striatum[tan])
connect_detector(striatum[D1])
connect_detector(striatum[D2])
connect_detector(motor[Cortex])
connect_detector(motor[FrontalCortex])
connect_detector(vta[vta_DA0])
connect_detector(snc[snc_DA])


logger.debug("* * * Attaching multimeters")
connect_multimeter(gpi[gpi_GABA])
connect_multimeter(snr[snr_GABA])
connect_multimeter(gpe[gpe_GABA])
connect_multimeter(stn[stn_Glu])
connect_multimeter(snc[snc_DA])
connect_multimeter(thalamus[thalamus_Glu])
connect_multimeter(striatum[tan])
connect_multimeter(striatum[D1])
connect_multimeter(striatum[D2])
connect_multimeter(motor[Cortex])
connect_multimeter(motor[FrontalCortex])
connect_multimeter(vta[vta_DA0])
connect_multimeter(snc[snc_DA])

del generate_neurons, connect, connect_generator, connect_detector, connect_multimeter

endbuild = datetime.datetime.now()

simulate()
get_log(startbuild, endbuild)
save(GUI=statusGUI)