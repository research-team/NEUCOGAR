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
    # for Glu
    connect(Cortex[L2][Glu][column], Cortex[L2][GABA][column], syn_type=Glu)
    connect(Cortex[L2][Glu][column], Cortex[L5][Glu][column], syn_type=Glu)
    # for GABA
    connect(Cortex[L2][GABA][column], Cortex[L3][Glu][column], syn_type=GABA)
    connect(Cortex[L2][GABA][column], Cortex[L5][Glu][column], syn_type=GABA)

    ''' L3 '''
    # for Glu
    connect(Cortex[L3][Glu][column], Cortex[L2][Glu][column], syn_type=Glu)
    connect(Cortex[L3][Glu][column], Cortex[L4][GABA][column], syn_type=Glu)
    connect(Cortex[L3][Glu][column], V5[Glu][k_IDs], syn_type=Glu)

    ''' L4 '''
    # for Glu
    connect(Cortex[L4][Glu][column], Cortex[L3][Glu][column], syn_type=Glu)
    connect(Cortex[L4][Glu][column], Cortex[L5][Glu][column], syn_type=Glu)
    connect(Cortex[L4][Glu][column], Cortex[L4][GABA][column], syn_type=Glu)
    # for GABA
    connect(Cortex[L4][GABA][column], Cortex[L4][Glu][column], syn_type=GABA)
    connect(Cortex[L4][GABA][column], Cortex[L3][Glu][column], syn_type=GABA)
    connect(Cortex[L4][GABA][column], Cortex[L2][GABA][column], syn_type=GABA)

    ''' L5 '''
    # for Glu
    connect(Cortex[L5][Glu][column], Cortex[L6][Glu][column], syn_type=Glu)
    connect(Cortex[L5][Glu][column], Cortex[L5][GABA][column], syn_type=Glu)
    connect(Cortex[L5][Glu][column], Thalamus[Glu_result][k_IDs], syn_type=Glu)
    # for GABA
    connect(Cortex[L5][GABA][column], Cortex[L5][GABA][column], syn_type=GABA)

    ''' L6 '''
    # for Glu
    connect(Cortex[L6][Glu][column], Cortex[L6][GABA][column], syn_type=Glu)
    connect(Cortex[L6][Glu][column], Cortex[L4][GABA][column], syn_type=Glu)
    connect(Cortex[L6][Glu][column], Cortex[L4][Glu][column], syn_type=Glu)
    connect(Cortex[L6][Glu][column], Thalamus[Glu_result][k_IDs], syn_type=Glu)
    connect(Cortex[L6][Glu][column], V2[V2_Glu][k_IDs], syn_type=Glu)
    connect(Cortex[L6][Glu][column], V1[V1_Glu][k_IDs], syn_type=Glu)
    # for GABA
    connect(Cortex[L6][GABA][column], Cortex[L6][Glu][column], syn_type=Glu)

    ''' Thalamus '''
    connect(Thalamus[Glu_generator][k_IDs], Cortex[L4][Glu][column], syn_type=Glu)
    connect(Thalamus[Glu_generator][k_IDs], Cortex[L6][Glu][column], syn_type=Glu)

    ''' V1 '''
    connect(V1[V1_Glu][k_IDs], Cortex[L4][Glu][column], syn_type=Glu)

    ''' V2 '''
    connect(V2[V2_Glu][k_IDs], Cortex[L4][Glu][column], syn_type=Glu)


logger.debug("* * * Adding neighbors connections")

logger.debug("for L2 layer")
step_L2 = Cortex[L2][area][X_area] / sum(Cortex[L2][step])
for Y in range(0, len(L2_tuple[Glu]) - 1, step_L2):
    for x in range(Y, Y + step_L2, 1):
        for position in availableNeighboursList(x, step_L2, Y, maximum=len(L2_tuple[Glu]) - 1):
            connect(Cortex[L2][Glu][x],  Cortex[L2][Glu][position],  syn_type=Glu)
            connect(Cortex[L2][GABA][x], Cortex[L2][GABA][position], syn_type=Glu)

logger.debug("for L4 layer")
step_L4 = Cortex[L4][area][X_area] / sum(Cortex[L4][step])
for Y in range(0, len(L4_tuple[Glu]) - 1, step_L4):
    for x in range(Y, Y + step_L4, 1):
        for position in availableNeighboursList(x, step_L4, Y, maximum=len(L4_tuple[Glu]) - 1):
            connect(Cortex[L4][Glu][x],  Cortex[L4][Glu][position],  syn_type=Glu)
            connect(Cortex[L4][GABA][x], Cortex[L4][GABA][position], syn_type=Glu)


logger.debug("* * * Creating spike generators")

connect_generator(Thalamus[Glu_generator], rate=200, startTime=100, stopTime=300)
connect_generator(Thalamus[Glu_generator], rate=200, startTime=600, stopTime=800)


logger.debug("* * * Attaching spikes detectors")

connect_detector_layer(Cortex[L2][Glu][20],  "L2_20_Glu")
connect_detector_layer(Cortex[L2][GABA][20], "L2_20_GABA")
connect_detector_layer(Cortex[L3][Glu][20],  "L3_20_Glu")
connect_detector_layer(Cortex[L4][Glu][20],  "L4_20_Glu")
connect_detector_layer(Cortex[L4][GABA][20], "L4_20_GABA")
connect_detector_layer(Cortex[L5][Glu][20],  "L5_20_Glu")
connect_detector_layer(Cortex[L5][GABA][20], "L5_20_GABA")
connect_detector_layer(Cortex[L6][Glu][20],  "L6_20_Glu")
connect_detector_layer(Cortex[L6][GABA][20], "L6_20_GABA")

connect_detector(V1[V1_Glu])
connect_detector(V2[V2_Glu])
connect_detector(V5[V5_Glu])
connect_detector(Thalamus[Glu_result])
connect_detector(Thalamus[Glu_generator])

del build_model, marking_columns, connect, connect_generator, connect_detector

endbuild = datetime.datetime.now()


simulate()
get_log(startbuild, endbuild)
save(statusGUI)