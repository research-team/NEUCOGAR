import os
import nest
import datetime
import numpy as np
from time import clock
from parameters import *

times = []
parts_dict = {}         # dict part      : name_part
spikegenerators = {}    # dict name_part : spikegenerator
spikedetectors = {}     # dict name_part : spikedetector
multimeters = {}        # dict name_part : multimeter

SYNAPSES = 0
NEURONS = 0

logger = logging.getLogger('function')


def log_conn (pre, post, syn_type, weight):
    global SYNAPSES
    SYNAPSES += len(pre) * len(post)
    logger.debug("{0} -> {1} ({2}) w[{3}] // {4} synapses".format(parts_dict[pre], parts_dict[post],
                                                                  syn_type, weight, len(pre) * len(post)))


def f_register(item, name):
    global NEURONS
    parts_dict[item] = name
    logger.debug("{0} [{1}, {2}] {3} neurons".format(name, item[0], item[0] + len(item) - 1, len(item)))
    NEURONS += len(item)


'''Help method to get neurons_list from iter_all{'name' : neurons_list}'''
def get_ids(name, iter_all=None):
    if iter_all is not None:
        get_ids.iter_all = iter_all
    for part in get_ids.iter_all:
        if part[k_name] == name:
            return part[k_ids]
    raise KeyError


def connect(pre, post, syn_type=GABA, weight_coef=1):
    types[syn_type][0]['weight'] = weight_coef * types[syn_type][1]                 # edit weight in syn_param
    syn = types[syn_type][3] if syn_type in (DA_ex, DA_in) else types[syn_type][0]  # help variable
    nest.Connect(pre, post, conn_spec=conn_dict, syn_spec=syn)
    log_conn(pre, post, types[syn_type][2], types[syn_type][0]['weight'])


def connect_generator(part, startTime=1, stopTime=T, rate=250, coef_part=1):
    name = parts_dict[part]
    spikegenerators[name] = nest.Create('poisson_generator', 1, {'rate': float(rate),
                                                                 'start': float(startTime),
                                                                 'stop': float(stopTime)})
    nest.Connect(spikegenerators[name], part,
                 syn_spec=gen_static_syn,
                 conn_spec={'rule': 'fixed_outdegree',
                            'outdegree': int(len(part) * coef_part)})
    logger.debug("Generator => {0}. Element #{1}".format(name, spikegenerators[name][0]))


def connect_detector(part):
    name = parts_dict[part]
    number = len(part) if len(part) < N_rec else N_rec
    spikedetectors[name] = nest.Create('spike_detector', params=detector_param)
    nest.Connect(part[:number], spikedetectors[name])
    logger.debug("Detector => {0}. Tracing {1} neurons".format(name, number))


def connect_multimeter(part):
    name = parts_dict[part]
    multimeters[name] = nest.Create('multimeter', params=mm_param)                  # ToDo add count of multimeters
    nest.Connect(multimeters[name], (part[0],))
    logger.debug("Multimeter => {0}. On {1}".format(name, part[0]) )


'''Generates string full name of an image'''
def f_name_gen(path, name):
    return "{0}{1}_{2}_dopamine_{3}.png".format(path, name, 'yes' if dopa_flag else 'no',
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
        print "COMPLETED {0}%\n".format(t/dt)
    endsimulate = datetime.datetime.now()
    logger.debug('* * * Simulation completed successfully')


def get_log(startbuild, endbuild):
    logger.info("Number of neurons  : {}".format(NEURONS))
    logger.info("Number of synapses : {}".format(SYNAPSES))
    logger.info("Building time      : {}".format(endbuild - startbuild))
    logger.info("Simulation time    : {}".format(endsimulate - startsimulate))
    for key in spikedetectors:
        logger.info("{0:>18} rate: {1:.2f}Hz".format(key, nest.GetStatus(spikedetectors[key], 'n_events')[0] / T * 1000.0 / N_rec))
    logger.info("Dopamine           : {}".format('YES' if dopa_flag else 'NO'))
    logger.info("Noise              : {}".format('YES' if generator_flag else 'NO'))


def save(GUI):
    global SAVE_PATH
    if GUI:
        import pylab as pl
        import nest.raster_plot
        import nest.voltage_trace

        SAVE_PATH = "output-{0}(png)/".format(NEURONS)
        logger.debug("Saving IMAGES into {0}".format(SAVE_PATH))
        if not os.path.exists(SAVE_PATH):
            os.mkdir(SAVE_PATH)
        for key in spikedetectors:
            try:
                nest.raster_plot.from_device((spikedetectors[key][0],), hist=True)
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

    SAVE_PATH = "output-{0}(txt)/".format(NEURONS)
    logger.debug("Saving TEXT into {0}".format(SAVE_PATH))
    if not os.path.exists(SAVE_PATH):
        os.mkdir(SAVE_PATH)
    for key in spikedetectors:
        save_spikes(spikedetectors[key], name=key)           #, hist=True)
    for key in multimeters:
        save_voltage(multimeters[key], name=key)

    with open(SAVE_PATH + 'timeSimulation.txt', 'w') as f:
        for item in times:
            f.write(item)


def save_spikes(detec, name, hist=False):
    title = "Raster plot from device '%i'" % detec[0]
    ev = nest.GetStatus(detec, "events")[0]
    ts = ev["times"]
    gids = ev["senders"]

    with open("{0}@spikes_{1}.txt".format(SAVE_PATH, name), 'w') as f:
        f.write("Name: {0}, Title: {1}, Hist: {2}\n".format(name, title, "True" if hist else "False"))
        for num in range(0, len(ts)):
            f.write("{0} {1}\n".format(str(ts[num]), str(gids[num])))


def save_voltage(detec, name):
    title = "Membrane potential"
    ev = nest.GetStatus(detec, "events")[0]
    ts = ev["times"]
    voltages = ev["V_m"]

    with open("{0}@voltage_{1}.txt".format(SAVE_PATH, name), 'w') as f:
        f.write("Name: {0}, Title: {1}\n".format(name, title))
        for num in range(0, len(ts)):
            f.write("{0} {1}\n".format(str(ts[num]), str(voltages[num])))


# ToDo => params={'spike_times': np.arange(1, T, 20.) in generator