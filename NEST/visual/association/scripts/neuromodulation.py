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
    ''' L1 '''
    connect(Cortex[L1][Glu][column], Cortex[L6][Glu][column], syn_type=Glu, weight_coef=3)
    ''' L2 '''
    connect(Cortex[L2][Glu][column], Cortex[L1][Glu][column], syn_type=Glu, weight_coef=3)
    connect(Cortex[L2][Glu][column], Cortex[L2][GABA][column], syn_type=Glu)
    connect(Cortex[L2][GABA][column], Cortex[L1][Glu][column], syn_type=GABA)
    ''' L3 '''
    connect(Cortex[L3][Glu][column], testArea[Glu][k_IDs], syn_type=Glu, weight_coef=2)
    ''' L4 '''
    connect(Cortex[L4][Glu][column], Cortex[L4][GABA][column], syn_type=Glu)
    connect(Cortex[L4][Glu][column], Cortex[L2][Glu][column], syn_type=Glu ,weight_coef=10)
    connect(Cortex[L4][GABA][column], Cortex[L5][Glu][column], syn_type=GABA)
    ''' L5 '''
    connect(Cortex[L5][Glu][column], Cortex[L3][Glu][column], syn_type=Glu)
    ''' L6 '''
    connect(Cortex[L6][Glu][column], Cortex[L5][Glu][column], syn_type=Glu)

''' V4 to center column'''
vt_ex = nest.Create('volume_transmitter')
DOPA_synparams_ex['vt'] = vt_ex[0]
nest.CopyModel('stdp_dopamine_synapse', dopa_synapsel_ex, DOPA_synparams_ex)
nest.Connect(V4[DA][k_IDs], vt_ex)
connect(V4[DA][k_IDs], Cortex[L4][Glu][find_center(Cortex[L1])], syn_type=DA_ex)


logger.debug("* * * Adding neighbors connections")

logger.debug("for L1 layer")
step_L1 = Cortex[L1][area][X_area] / sum(Cortex[L1][step])
for Y in range(0, len(L1_tuple[Glu]) - 1, step_L1):
    for x in range(Y, Y + step_L1, 1):
        for position in availableNeighboursList(x, step_L1, Y, maximum=len(L1_tuple[Glu]) - 1):
            connect(Cortex[L1][Glu][x],  Cortex[L1][Glu][position],  syn_type=Glu)


logger.debug("* * * Creating spike generators")

connect_generator(V4[DA], startTime=200, stopTime=400, rate=90, coef_part=0.2)
#connect_generator(StartV[Glu], startTime=100, stopTime=900, rate=80, coef_part=0.5)


logger.debug("* * * Attaching spikes detectors")
# This detectors need for testing of one column
for col in detector_radius(Cortex[L1], 2):
    connect_detector_layer(Cortex[L1][Glu][col], "column" + str(col))

centerColumn = find_center(Cortex[L1])
connect_detector_layer(Cortex[L1][Glu][centerColumn], str(centerColumn)+" center L1 Glu")
connect_detector_layer(Cortex[L2][Glu][centerColumn], str(centerColumn)+" center L2 Glu")
connect_detector_layer(Cortex[L2][GABA][centerColumn], str(centerColumn)+" center L2 GABA")
connect_detector_layer(Cortex[L3][Glu][centerColumn], str(centerColumn)+" center L3 Glu")
connect_detector_layer(Cortex[L4][Glu][centerColumn], str(centerColumn)+" center L4 Glu")
connect_detector_layer(Cortex[L4][GABA][centerColumn], str(centerColumn)+" center L4 GABA")
connect_detector_layer(Cortex[L5][Glu][centerColumn], str(centerColumn)+" center L5 Glu")
connect_detector_layer(Cortex[L6][Glu][centerColumn], str(centerColumn)+" center L6 Glu")
connect_detector(V4[DA])


del build_model, marking_columns, connect, connect_generator, connect_detector

endbuild = datetime.datetime.now()


simulate()
get_log(startbuild, endbuild)
save(statusGUI)