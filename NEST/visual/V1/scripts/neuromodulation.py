from func import *

startbuild = datetime.datetime.now()

nest.ResetKernel()
nest.SetKernelStatus({'overwrite_files': True,
                      'local_num_threads': 4,
                      'resolution': 0.1})
logger = logging.getLogger('neuromodulation')


logger.debug("* * * Building layers")
build_model()


logger.debug("* * * Marking columns")
marking_columns()


# Initialize connections
logger.debug("* * * Connecting layers in columns")
for column in range(GlobalColumns):
    if column % 100 == 0:
        logger.debug("Connecting in columns #{0} ... {1}".format(column, column + 100))
    ''' L2 '''
    # GABA 0
    connect(Cortex[L2][L2_GABA0][column], Cortex[L4][L4_Glu0][column], syn_type=GABA)

    ''' L3 '''
    # Glu

    connect(Cortex[L3][L3_Glu][column], V1[V1_Glu][k_IDs], syn_type=Glu)

    # GABA 0
    connect(Cortex[L3][L3_GABA0][column], Cortex[L3][L3_Glu][column], syn_type=GABA)
    # GABA 1
    connect(Cortex[L3][L3_GABA1][column], Cortex[L3][L3_Glu][column], syn_type=GABA)

    ''' L4 '''
    # Glu 0
    connect(Cortex[L4][L4_Glu0][column], Cortex[L2][L2_GABA0][column], syn_type=Glu)
    # Glu 1
    connect(Cortex[L4][L4_Glu0][column], Cortex[L3][L3_Glu][column], syn_type=Glu)
    # GABA
    connect(Cortex[L4][L4_GABA][column], Cortex[L3][L3_GABA0][column], syn_type=GABA)
    connect(Cortex[L4][L4_GABA][column], Cortex[L3][L3_GABA1][column], syn_type=GABA)
    connect(Cortex[L4][L4_GABA][column], Cortex[L2][L2_GABA0][column], syn_type=GABA)
    connect(Cortex[L4][L4_GABA][column], Cortex[L2][L2_GABA1][column], syn_type=GABA)

    connect_detector_layer(Cortex[L4][L4_Glu1][column], "L4_Glu1_" + str(column))


    ''' L5 '''
    # Glu
    connect(Cortex[L5][L5_Glu][column], Cortex[L4][L4_Glu1][column], syn_type=Glu)
    connect(Cortex[L5][L5_Glu][column], Cortex[L3][L3_GABA0][column], syn_type=Glu)
    connect(Cortex[L5][L5_Glu][column], Cortex[L3][L3_GABA0][column], syn_type=Glu)
    connect(Cortex[L5][L5_Glu][column], Cortex[L3][L3_Glu][column], syn_type=Glu)
    connect(Cortex[L5][L5_Glu][column], Cortex[L2][L2_GABA1][column], syn_type=Glu)

    ''' L6 '''
    # Glu
    connect(Cortex[L6][L6_Glu][column], Cortex[L4][L4_Glu1][column], syn_type=Glu)
    connect(Cortex[L6][L6_Glu][column], Thalamus[Glu_result][k_IDs], syn_type=Glu)

    ''' Thalamus '''
    connect(Thalamus[Glu_generator][k_IDs], Cortex[L6][L6_Glu][column], syn_type=Glu)
    connect(Thalamus[Glu_generator][k_IDs], Cortex[L5][L5_Glu][column], syn_type=Glu)
    connect(Thalamus[Glu_generator][k_IDs], Cortex[L4][L4_Glu0][column], syn_type=Glu)
    connect(Thalamus[Glu_generator][k_IDs], Cortex[L4][L4_Glu1][column], syn_type=Glu)
    connect(Thalamus[Glu_generator][k_IDs], Cortex[L4][L4_GABA][column], syn_type=Glu)
    connect(Thalamus[Glu_generator][k_IDs], Cortex[L3][L3_Glu][column], syn_type=Glu)
    connect(Thalamus[Glu_generator][k_IDs], Cortex[L3][L3_GABA1][column], syn_type=Glu)


logger.debug("* * * Adding neighbors connections")

logger.debug("for L2 layer")
step_L2 = Cortex[L2][area][X_area] / sum(Cortex[L2][step])
for Y in range(0, len(L2_tuple[L2_GABA0]) - 1, step_L2):
    for x in range(Y, Y + step_L2, 1):
        for position in availableNeighboursList(x, step_L2, Y, maximum=len(L2_tuple[L2_GABA0]) - 1):
            connect(Cortex[L2][L2_GABA0][x],  Cortex[L2][L2_GABA0][position],  syn_type=GABA)

logger.debug("for L3 layer")
step_L3 = Cortex[L3][area][X_area] / sum(Cortex[L3][step])
for Y in range(0, len(L3_tuple[L3_Glu]) - 1, step_L3):
    for x in range(Y, Y + step_L3, 1):
        for position in availableNeighboursList(x, step_L3, Y, maximum=len(L3_tuple[L3_Glu]) - 1):
            connect(Cortex[L3][L3_Glu][x],  Cortex[L3][L3_Glu][position],  syn_type=Glu)

logger.debug("for L4 layer")
step_L4 = Cortex[L4][area][X_area] / sum(Cortex[L4][step])
for Y in range(0, len(L4_tuple[L4_Glu0]) - 1, step_L4):
    for x in range(Y, Y + step_L4, 1):
        for position in availableNeighboursList(x, step_L4, Y, maximum=len(L4_tuple[L4_Glu0]) - 1):
            connect(Cortex[L4][L4_Glu0][x],  Cortex[L4][L4_Glu0][position],  syn_type=Glu)

logger.debug("for L6 layer")
step_L6 = Cortex[L6][area][X_area] / sum(Cortex[L6][step])
for Y in range(0, len(L6_tuple[L6_Glu]) - 1, step_L6):
    for x in range(Y, Y + step_L6, 1):
        for position in availableNeighboursList(x, step_L6, Y, maximum=len(L6_tuple[L6_Glu]) - 1):
            connect(Cortex[L6][L6_Glu][x],  Cortex[L6][L6_Glu][position],  syn_type=Glu)


logger.debug("* * * Creating spike generators")

connect_generator(Thalamus[Glu_generator], rate=200, startTime=100, stopTime=300)
connect_generator(Thalamus[Glu_generator], rate=200, startTime=600, stopTime=800)


logger.debug("* * * Attaching spikes detectors")

del build_model, marking_columns, connect, connect_generator, connect_detector

endbuild = datetime.datetime.now()


simulate()
get_log(startbuild, endbuild)
save(statusGUI)