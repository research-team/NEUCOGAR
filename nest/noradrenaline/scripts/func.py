import os
import nest
import logging
import datetime
from time import clock
from parameters import *
from data import *

times = []
spikegenerators = {}  # dict name_part : spikegenerator
spikedetectors = {}  # dict name_part : spikedetector
multimeters = {}  # dict name_part : multimeter

SYNAPSES = 0

FORMAT = '%(name)s.%(levelname)s: %(message)s.'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
logger = logging.getLogger('function')


def generate_neurons():
    global NEURONS, all_parts
    logger.debug("* * * Start generate neurons")
    parts_no_nora = pgi + prh + (lc[lc_D1], lc[lc_D2], ldt[laterodorsal_tegmentum], vta[ventral_tegmental_area])

    parts_with_nora = pf + motor + nts + (lc[locus_coeruleus], ldt[LDT_a1], ldt[LDT_a2], vta[vta_a1]) + striatum + \
                      bnst + rn

    all_parts = tuple(sorted(parts_no_nora + parts_with_nora))

    if test_flag:
        # TEST NUMBER
        motor[motor_cortex][k_NN] = 60

        striatum[striatumR][k_NN] = 30

        vta[ventral_tegmental_area][k_NN] = 30
        vta[vta_a1][k_NN] = 30

        lc[locus_coeruleus][k_NN] = 30
        lc[lc_D1][k_NN] = 30
        lc[lc_D2][k_NN] = 30

        prh[perirhinal_cortex][k_NN] = 30

        pgi[nucleus_paragigantocellularis_lateralis][k_NN] = 30

        rn[rn_a1][k_NN] = 30
        rn[rn_a2][k_NN] = 30

        bnst[bed_nucleus_of_the_stria_terminalis][k_NN] = 30

        nts[nts_a1][k_NN] = 30
        nts[nts_a2][k_NN] = 30

        ldt[laterodorsal_tegmentum][k_NN] = 30
        ldt[LDT_a1][k_NN] = 30
        ldt[LDT_a2][k_NN] = 30

        pf[prefrontal_cortex][k_NN] = 30

    else:
        # REAL NUMBER
        #TODO
        motor[motor_cortex][k_NN] = 60

        striatum[striatumR][k_NN] = 30

        vta[ventral_tegmental_area][k_NN] = 30
        vta[vta_a1][k_NN] = 30

        lc[locus_coeruleus][k_NN] = 30
        lc[lc_D1][k_NN] = 30
        lc[lc_D2][k_NN] = 30

        prh[perirhinal_cortex][k_NN] = 30

        pgi[nucleus_paragigantocellularis_lateralis][k_NN] = 30

        rn[rn_a1][k_NN] = 30
        rn[rn_a2][k_NN] = 30

        bnst[bed_nucleus_of_the_stria_terminalis][k_NN] = 30

        nts[nts_a1][k_NN] = 30
        nts[nts_a2][k_NN] = 30

        ldt[laterodorsal_tegmentum][k_NN] = 30
        ldt[LDT_a1][k_NN] = 30
        ldt[LDT_a2][k_NN] = 30

        pf[prefrontal_cortex][k_NN] = 30

        for part in all_parts:
            part[k_NN] = NN_minimal if int(part[k_NN] * NN_coef) < NN_minimal else int(part[k_NN] * NN_coef)

    NEURONS = sum(item[k_NN] for item in all_parts)
    logger.debug('Initialised: {0} neurons'.format(NEURONS))

    # assign neuron params to every part
    nest.SetDefaults('iaf_psc_exp', iaf_neuronparams)
    nest.SetDefaults('iaf_psc_alpha', iaf_neuronparams)

    # without dopamine
    for part in parts_no_nora:
        part[k_model] = 'iaf_psc_exp'
    # with dopamine
    for part in parts_with_nora:
        part[k_model] = 'iaf_psc_alpha'

    for part in all_parts:
        part[k_IDs] = nest.Create(part[k_model], part[k_NN])
        logger.debug("{0} [{1}, {2}] {3} neurons".format(part[k_name], part[k_IDs][0],
                                                         part[k_IDs][0] + part[k_NN] - 1,
                                                         part[k_NN]))


def log_connection(pre, post, syn_type, weight):
    global SYNAPSES
    SYNAPSES += pre[k_NN] * post[k_NN]
    logger.debug("{0} -> {1} ({2}) w[{3}] // {4} synapses".format(pre[k_name], post[k_name],
                                                                  syn_type, weight, pre[k_NN] * post[k_NN]))


def connect(pre, post, syn_type=GABA, weight_coef=1):
    types[syn_type][0]['weight'] = weight_coef * types[syn_type][1]
    nest.Connect(pre[k_IDs],
                 post[k_IDs],
                 conn_spec=conn_dict,
                 syn_spec=types[syn_type][3] if syn_type in (DA_ex, DA_in) else types[syn_type][0])
    log_connection(pre, post, types[syn_type][2], types[syn_type][0]['weight'])


def connect_generator(part, startTime=1, stopTime=T, rate=250, coef_part=1):
    name = part[k_name]
    spikegenerators[name] = nest.Create('poisson_generator', 1, {'rate': float(rate),
                                                                 'start': float(startTime),
                                                                 'stop': float(stopTime)})
    nest.Connect(spikegenerators[name], part[k_IDs],
                 syn_spec=static_syn,
                 conn_spec={'rule': 'fixed_outdegree',
                            'outdegree': int(part[k_NN] * coef_part)})
    logger.debug("Generator => {0}. Element #{1}".format(name, spikegenerators[name][0]))


def connect_detector(part):
    name = part[k_name]
    number = part[k_NN] if part[k_NN] < N_detect else N_detect
    spikedetectors[name] = nest.Create('spike_detector', params=detector_param)
    nest.Connect(part[k_IDs][:number], spikedetectors[name])
    logger.debug("Detector => {0}. Tracing {1} neurons".format(name, number))


def connect_multimeter(part):
    name = part[k_name]
    multimeters[name] = nest.Create('multimeter', params=multimeter_param)  # ToDo add count of multimeters
    nest.Connect(multimeters[name], (part[k_IDs][:N_volt]))
    logger.debug("Multimeter => {0}. On {1}".format(name, part[k_IDs][:N_volt]))


'''Generates string full name of an image'''


def f_name_gen(path, name):
    return "{0}{1}_{2}_dopamine_{3}.png".format(path, name, 'yes' if nora_flag else 'no',
                                                'noise' if generator_flag else 'static')


def simulate():
    global startsimulate, endsimulate
    begin = 0
    nest.PrintNetwork()
    logger.debug('* * * Simulating')
    startsimulate = datetime.datetime.now()
    for t in np.arange(0, T, dt):
        print "SIMULATING [{0}, {1}]".format(t, t + dt)
        nest.Simulate(dt)
        end = clock()
        times.append("{0:10.1f} {1:8.1f} {2:10.1f} {3:4.1f} {4}\n".format(begin, end - begin, end,
                                                                          t, datetime.datetime.now().time()))
        begin = end
        print "COMPLETED {0}%\n".format(t / dt)
    endsimulate = datetime.datetime.now()
    logger.debug('* * * Simulation completed successfully')


def get_log(startbuild, endbuild):
    logger.info("Number of neurons  : {}".format(NEURONS))
    logger.info("Number of synapses : {}".format(SYNAPSES))
    logger.info("Building time      : {}".format(endbuild - startbuild))
    logger.info("Simulation time    : {}".format(endsimulate - startsimulate))
    for key in spikedetectors:  # FixMe bug in '1000.0 / N_rec' in some case N_rec can be equal part[k_IDs]
        print "***************"
        print nest.GetStatus(spikedetectors[key])[0]
        logger.info("{0:>18} rate: {1:.2f}Hz".format(key, nest.GetStatus(spikedetectors[key], 'n_events')[
            0] / T * 1000.0 / N_detect))
    logger.info("Dopamine           : {}".format('YES' if nora_flag else 'NO'))
    logger.info("Noise              : {}".format('YES' if generator_flag else 'NO'))


def save(GUI):
    global txtResultPath
    SAVE_PATH = "../results/output-{0}/".format(NEURONS)
    if GUI:
        import pylab as pl
        import nest.raster_plot
        import nest.voltage_trace
        logger.debug("Saving IMAGES into {0}".format(SAVE_PATH))
        if not os.path.exists(SAVE_PATH):
            os.mkdir(SAVE_PATH)
        for key in spikedetectors:
            try:
                nest.raster_plot.from_device(spikedetectors[key], hist=True)
                pl.savefig(f_name_gen(SAVE_PATH, "spikes_" + key.lower()), dpi=dpi_n, format='png')
                pl.close()
            except Exception:
                print(" * * * from {0} is NOTHING".format(key))
        for key in multimeters:
            try:
                nest.voltage_trace.from_device(multimeters[key])
                pl.savefig(f_name_gen(SAVE_PATH, "volt_" + key.lower()), dpi=dpi_n, format='png')
                pl.close()
            except Exception:
                print(" * * * from {0} is NOTHING".format(key))

    txtResultPath = SAVE_PATH + 'txt/'
    logger.debug("Saving TEXT into {0}".format(txtResultPath))
    if not os.path.exists(txtResultPath):
        os.mkdir(txtResultPath)
    for key in spikedetectors:
        save_spikes(spikedetectors[key], name=key)  # , hist=True)
    # for key in multimeters:
    #    save_voltage(multimeters[key], name=key)

    with open(txtResultPath + 'timeSimulation.txt', 'w') as f:
        for item in times:
            f.write(item)


from collections import defaultdict

GlobalDICT = {}


def save_spikes(detec, name, hist=False):
    title = "Raster plot from device '%i'" % detec[0]
    ev = nest.GetStatus(detec, "events")[0]
    ts = ev["times"]
    gids = ev["senders"]
    data = defaultdict(list)
    temp_dict = {}

    if len(ts):
        with open("{0}@spikes_{1}.txt".format(txtResultPath, name), 'w') as f:
            f.write("Name: {0}, Title: {1}, Hist: {2}\n".format(name, title, "True" if hist else "False"))
            for num in range(0, len(ev["times"])):
                data[round(ts[num], 1)].append(gids[num])
            for key in sorted(data.iterkeys()):
                f.write("{0:>5} {1:>4} : {2}\n".format(key, len(data[key]), sorted(data[key])))
                temp_dict[key] = len(data[key])
    else:
        print "Spikes in {0} is NULL".format(name)

    result_list = []
    '''
        if len(ts):
            for i in np.arange(0, int(min(key for key in temp_dict)), 1):
                result_list.append(0)
            for i in np.arange(int(min(key for key in temp_dict)), int(max(key for key in temp_dict)) + 1, 1):
                result_list.append( sum(temp_dict[key] for key in temp_dict if int(key) == i) )
            for i in np.arange(max(key for key in temp_dict) + 1, int(T), 1):
                result_list.append(0)
        else:
            for i in np.arange(0, T, 1):
                result_list.append(0)

        GlobalDICT[name] = result_list
    '''


def save_voltage(detec, name):
    title = "Membrane potential"
    ev = nest.GetStatus(detec, "events")[0]
    with open("{0}@voltage_{1}.txt".format(txtResultPath, name), 'w') as f:
        f.write("Name: {0}, Title: {1}\n".format(name, title))
        print int(T / multimeter_param['interval'])
        for line in range(0, int(T / multimeter_param['interval'])):
            for index in range(0, N_volt):
                print "{0} {1} ".format(ev["times"][line], ev["V_m"][line])
            # f.write("\n")
            print "\n"


# ToDo => params={'spike_times': np.arange(1, T, 20.) in generator

def testUnit():
    import matplotlib.pyplot as plt

    data = [GlobalDICT[key][:999] for key in GlobalDICT]

    plt.xlabel("Time in ms")
    plt.ylabel("Part of brain")

    # ax.set_xticklabels(np.arange(len(data[0])))
    # ax.set_yticklabels('kek', 'lol', 'tot')

    plt.imshow(data, aspect='auto', interpolation='none', cmap="hot")
    plt.show()
    # plt.savefig("TESTPIC.png",dpi=360, format='png')
