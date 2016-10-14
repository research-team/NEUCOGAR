from func import *

logger.debug("* * * Building layers")
build_model()


logger.debug("* * * Marking columns")
marking_columns()


# Initialize connections
logger.debug("* * * Connecting layers in columns")
for column in range(GlobalColumns):
    if column % 100 == 0:
        logger.debug("Connecting in columns #{0} ... {1}".format(column, column + 100))

    ''' L1 '''
    connect(Cortex[L1][Glu][column], Cortex[L2][Glu][column], syn_type=Glu)

    ''' L2 '''
    connect(Cortex[L2][Glu][column], Cortex[L2][GABA][column], syn_type=Glu)
    connect(Cortex[L2][Glu][column], Cortex[L5][Glu][column], syn_type=Glu)
    connect(Cortex[L2][Glu][column], Cortex[L6][Glu][column], syn_type=Glu)

    connect(Cortex[L2][GABA][column], Cortex[L1][Glu][column], syn_type=GABA)

    ''' L3 '''
    connect(Cortex[L3][Glu][column], Cortex[L2][Glu][column], syn_type=Glu)

    connect(Cortex[L3][Glu][column], Cortex[L3][GABA][column], syn_type=Glu)
    connect(Cortex[L3][Glu][column], Cortex[L5][Glu][column], syn_type=Glu)

    connect(Cortex[L3][GABA][column], Cortex[L4][Glu][column], syn_type=Glu)

    ''' L4 '''
    connect(Cortex[L4][Glu][column], Cortex[L3][Glu][column], syn_type=Glu)

    ''' L5 '''
    connect(Cortex[L5][Glu][column], Cortex[L6][GABA][column], syn_type=Glu)
    connect(Cortex[L5][Glu][column], MGB[MGB_result][k_IDs], syn_type=Glu)
    connect(Cortex[L5][Glu][column], IC[IC_glu][k_IDs], syn_type=Glu)

    ''' L6 '''
    connect(Cortex[L6][Glu][column], Cortex[L4][Glu][column], syn_type=Glu)
    connect(Cortex[L6][Glu][column], MGB[MGB_result][k_IDs], syn_type=Glu)

    connect(Cortex[L6][GABA][column], Cortex[L6][Glu][column], syn_type=GABA)

    ''' MGB generator'''
    connect(MGB[MGB_generator][k_IDs], Cortex[L1][Glu][column], syn_type=Glu)
    connect(MGB[MGB_generator][k_IDs], Cortex[L3][Glu][column], syn_type=Glu)
    connect(MGB[MGB_generator][k_IDs], Cortex[L4][Glu][column], syn_type=Glu)


logger.debug("* * * Adding neighbors connections")

logger.debug("for L2 layer")
step_L2 = Cortex[L2][area][X_area] / sum(Cortex[L2][step])
for Y in range(0, len(L2_tuple[Glu]) - 1, step_L2):
    for x in range(Y, Y + step_L2, 1):
        for position in availableNeighboursList(x, step_L2, Y, maximum=len(L2_tuple[Glu]) - 1):
            connect(Cortex[L2][Glu][x],  Cortex[L2][Glu][position],  syn_type=Glu)
            connect(Cortex[L2][GABA][x], Cortex[L2][GABA][position], syn_type=Glu)

logger.debug("for L3 layer")
step_L3 = Cortex[L3][area][X_area] / sum(Cortex[L3][step])
for Y in range(0, len(L3_tuple[Glu]) - 1, step_L3):
    for x in range(Y, Y + step_L3, 1):
        for position in availableNeighboursList(x, step_L3, Y, maximum=len(L3_tuple[Glu]) - 1):
            connect(Cortex[L3][Glu][x],  Cortex[L3][Glu][position],  syn_type=Glu)
            connect(Cortex[L3][GABA][x], Cortex[L3][GABA][position], syn_type=Glu)

logger.debug("* * * Creating spike generators")

connect_generator(MGB[MGB_generator], rate=200, startTime=200, stopTime=600)

logger.debug("* * * Attaching spikes detectors")
connect_detector_layer(Cortex[L1][Glu][20], "L1_20_GABA")
connect_detector_layer(Cortex[L2][Glu][20],  "L2_20_Glu")
connect_detector_layer(Cortex[L2][GABA][20], "L2_20_GABA")
connect_detector_layer(Cortex[L3][Glu][20],  "L3_20_Glu")
connect_detector_layer(Cortex[L3][GABA][20], "L3_20_GABA")
connect_detector_layer(Cortex[L4][Glu][20],  "L4_20_Glu")
connect_detector_layer(Cortex[L5][Glu][20],  "L5_20_Glu")
connect_detector_layer(Cortex[L6][Glu][20],  "L6_20_Glu")
connect_detector_layer(Cortex[L6][GABA][20], "L6_20_GABA")

connect_detector(IC[Glu])
connect_detector(MGB[MGB_result])
connect_detector(MGB[MGB_generator])

del build_model, marking_columns, connect, connect_generator, connect_detector

endbuild = datetime.datetime.now()


simulate()
get_log(startbuild, endbuild)
save(statusGUI)
