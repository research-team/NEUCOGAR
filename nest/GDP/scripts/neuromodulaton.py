# TODO check num_threads before testing / 8 for Cisco Server
# TODO ATTTENTION! Maybe there are some mistakes in neuron parameters!

from func import *

logger = logging.getLogger('neuromodulation')
startbuild = datetime.datetime.now()

nest.ResetKernel()
nest.SetKernelStatus({'overwrite_files': True,  'local_num_threads': 4, 'resolution': 0.1})

generate_neurons()

logger.debug("* * * Start connection initialisation")
# * * * NIGROSTRIATAL * * *
connect(enterial[enterial_Glu0], dentate[dentate_ACh], syn_type=Glu, weight_coef=0.005)
connect(enterial[enterial_GABA], dentate[dentate_ACh],  weight_coef=0.000005)  
connect(enterial[enterial_NA0], CA3[CA3_GABA], weight_coef=0.005)

connect(dentate[dentate_ACh], CA3[CA3_GABA])

connect(CA3[CA3_GABA], CA3[CA3_GABA])

'''
if dopa_flag:
    logger.debug("* * * Making neuromodulating connections...")
    # Connect the volume transmitter to the parts
    vt_ex = nest.Create('volume_transmitter')
    vt_in = nest.Create('volume_transmitter')
    DOPA_synparams_ex['vt'] = vt_ex[0]
    DOPA_synparams_in['vt'] = vt_in[0]
    nest.CopyModel('stdp_dopamine_synapse', dopa_model_ex, DOPA_synparams_ex)
    nest.CopyModel('stdp_dopamine_synapse', dopa_model_in, DOPA_synparams_in)

    nest.Connect(snc[snc_DA][k_IDs], vt_ex)
    nest.Connect(snc[snc_DA][k_IDs], vt_in)
    nest.Connect(vta[vta_DA0][k_IDs], vt_ex)
    nest.Connect(vta[vta_DA1][k_IDs], vt_ex)

    # NIGROSTRIATAL
    connect(snc[snc_DA], striatum[D1], syn_type=DA_ex)
    connect(snc[snc_DA], gpe[gpe_GABA], syn_type=DA_ex)
    connect(snc[snc_DA], stn[stn_Glu], syn_type=DA_ex)
    connect(snc[snc_DA], nac[nac_GABA0], syn_type=DA_ex)
    connect(snc[snc_DA], nac[nac_GABA1], syn_type=DA_ex)
    connect(snc[snc_DA], striatum[D2], syn_type=DA_in)
    connect(snc[snc_DA], striatum[tan], syn_type=DA_in)

    # MESOCORTICOLIMBIC
    connect(vta[vta_DA0], striatum[D1], syn_type=DA_ex)
    connect(vta[vta_DA0], striatum[D2], syn_type=DA_in)
    connect(vta[vta_DA0], prefrontal[pfc_Glu0], syn_type=DA_ex)
    connect(vta[vta_DA0], prefrontal[pfc_Glu1], syn_type=DA_ex)
    connect(vta[vta_DA1], nac[nac_GABA0], syn_type=DA_ex)
    connect(vta[vta_DA1], nac[nac_GABA1], syn_type=DA_ex)
'''

logger.debug("* * * Creating spike generators...")
if generator_flag:
    connect_generator(enterial[enterial_Glu0], rate=300, coef_part=1)
    connect_generator(enterial[enterial_GABA], rate=300, coef_part=1)
    connect_generator(enterial[enterial_NA0], rate=300, coef_part=1)
    connect_generator(dentate[dentate_ACh], 400., 600., rate=250, coef_part=1)
    connect_generator(CA3[CA3_GABA], 400., 600., rate=250, coef_part=1)


logger.debug("* * * Attaching spikes detector")
connect_detector(dentate[dentate_ACh])
connect_detector(enterial[enterial_Glu0])
connect_detector(enterial[enterial_NA0])
connect_detector(enterial[enterial_GABA])
connect_detector(CA3[CA3_GABA])


logger.debug("* * * Attaching multimeters")
connect_multimeter(dentate[dentate_ACh])
connect_multimeter(enterial[enterial_Glu0])
connect_multimeter(enterial[enterial_GABA])
connect_multimeter(enterial[enterial_NA0])
connect_multimeter(CA3[CA3_GABA])


del generate_neurons, connect, connect_generator, connect_detector, connect_multimeter

endbuild = datetime.datetime.now()

simulate()
get_log(startbuild, endbuild)
save(GUI=status_gui)