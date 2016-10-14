from func import *

startbuild = datetime.datetime.now()

nest.ResetKernel()
nest.SetKernelStatus({'overwrite_files': True,
                      'local_num_threads': 4,
                      'resolution': 0.1})

logger = logging.getLogger('neuromodulation')
logger.debug("* * * Building layers")
build_model()

logger.debug("* * * Marking column")
marking_column()

# Initialize connections
logger.debug("* * * Connecting layers in column")
column = 0
''' L2 '''
connect(Cortex[L2][L2_GABA0][column], Cortex[L4][L4_Glu0][column], syn_type=GABA)

''' L3 '''
connect(Cortex[L3][L3_GABA0][column], Cortex[L3][L3_Glu][column], syn_type=GABA)
connect(Cortex[L3][L3_GABA1][column], Cortex[L3][L3_Glu][column], syn_type=GABA)

''' L4 '''
connect(Cortex[L4][L4_Glu0][column], Cortex[L2][L2_GABA0][column], syn_type=Glu)
connect(Cortex[L4][L4_Glu0][column], Cortex[L3][L3_Glu][column], syn_type=Glu)
connect(Cortex[L4][L4_GABA][column], Cortex[L3][L3_GABA0][column], syn_type=GABA)
connect(Cortex[L4][L4_GABA][column], Cortex[L3][L3_GABA1][column], syn_type=GABA)
connect(Cortex[L4][L4_GABA][column], Cortex[L2][L2_GABA0][column], syn_type=GABA)
connect(Cortex[L4][L4_GABA][column], Cortex[L2][L2_GABA1][column], syn_type=GABA)

''' L5 '''
connect(Cortex[L5][L5_Glu][column], Cortex[L4][L4_Glu1][column], syn_type=Glu)
connect(Cortex[L5][L5_Glu][column], Cortex[L3][L3_GABA0][column], syn_type=Glu)
connect(Cortex[L5][L5_Glu][column], Cortex[L3][L3_GABA0][column], syn_type=Glu)
connect(Cortex[L5][L5_Glu][column], Cortex[L3][L3_Glu][column], syn_type=Glu)
connect(Cortex[L5][L5_Glu][column], Cortex[L2][L2_GABA1][column], syn_type=Glu)

''' L6 '''
connect(Cortex[L6][L6_Glu][column], Cortex[L4][L4_Glu1][column], syn_type=Glu)

''' Thalamus '''
connect(Thalamus[Glu_generator][k_IDs], Cortex[L6][L6_Glu][column], syn_type=Glu)
connect(Thalamus[Glu_generator][k_IDs], Cortex[L5][L5_Glu][column], syn_type=Glu)
connect(Thalamus[Glu_generator][k_IDs], Cortex[L4][L4_Glu0][column], syn_type=Glu)
connect(Thalamus[Glu_generator][k_IDs], Cortex[L4][L4_Glu1][column], syn_type=Glu)
connect(Thalamus[Glu_generator][k_IDs], Cortex[L4][L4_GABA][column], syn_type=Glu)
connect(Thalamus[Glu_generator][k_IDs], Cortex[L3][L3_Glu][column], syn_type=Glu)
connect(Thalamus[Glu_generator][k_IDs], Cortex[L3][L3_GABA1][column], syn_type=Glu)

logger.debug("* * * Creating spike generators")
connect_generator(Thalamus[Glu_generator], startTime=200, stopTime=500, coef_part=0.5)

logger.debug("* * * Attaching spikes detectors")
for layer in Cortex:
    for part in range(3):
        connect_detector(layer[part])
connect_detector_Thalamus(Thalamus[Glu_generator])
del build_model, marking_column, connect, connect_generator, connect_detector

endbuild = datetime.datetime.now()

simulate()
get_log(startbuild, endbuild)
save(statusGUI)