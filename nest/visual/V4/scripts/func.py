import os
import sys
import time
import logging
import datetime
import numpy as np
from data import *
from time import clock
from parameters import *
from collections import defaultdict


SAVE_PATH = "" # path to save results
spike_generators = {}   # dict name_part : spikegenerator
spike_detectors = {}    # dict name_part : spikedetector
multimeters = {}        # dict name_part : multimeter
startsimulate = 0
endsimulate = 0
txt_result_path = ""    # path for txt results
all_parts = tuple()     # tuple of all parts
one_collumn = tuple()     # tuple of all parts
MaxSynapses = 4000      # max synapses
SYNAPSES = 0            # synapse number
NEURONS = 0             # neurons number
times = []              # store time simulation

logging.basicConfig(format='%(name)s.%(levelname)s: %(message)s.', level=logging.DEBUG)
logger = logging.getLogger('function')

def getAllParts():
    return all_parts

def generate_neurons(NNumber):
    global NEURONS, all_parts
    logger.debug("* * * Start generate neurons")

    c2 = l2c2 + l3c2 + l4c2 + l5c2 + l6c2
    c3 = l2c3 + l3c3 + l4c3 + l5c3 + l6c3
    c4 = l2c4 + l3c4 + l4c4 + l5c4 + l6c4
    c5 = l2c5 + l3c5 + l4c5 + l5c5 + l6c5
    c6 = l2c6 + l3c6 + l4c6 + l5c6 + l6c6
    c7 = l2c7 + l3c7 + l4c7 + l5c7 + l6c7
    c8 = l2c8 + l3c8 + l4c8 + l5c8 + l6c8
    c9 = l2c9 + l3c9 + l4c9 + l5c9 + l6c9


    parts_no_dopa = l2 + l3 + l4 + l5 + l6 + thalamus
    collumns = c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9


    all_parts = tuple(sorted(parts_no_dopa))
    #all_parts = tuple(sorted(parts_no_dopa + collumns))  FOR ALL PARTS FOR EVERY COLLUMNS

    NN_coef = float(NNumber) / sum(item[k_NN] for item in all_parts)

    for part in all_parts:
        part[k_NN] = NN_minimal if int(part[k_NN] * NN_coef) < NN_minimal else int(part[k_NN] * NN_coef)
    NEURONS = sum(item[k_NN] for item in all_parts)
    for part in collumns:
        part[k_NN] = NN_minimal if int(part[k_NN] * NN_coef) < NN_minimal else int(part[k_NN] * NN_coef)
    NEURONS = sum(item[k_NN] for item in all_parts)

    logger.debug('Initialized: {0} neurons'.format(NEURONS))

    # Init neuron models with our parameters
    nest.SetDefaults('iaf_psc_exp',   iaf_neuronparams)
    nest.SetDefaults('iaf_psc_alpha', iaf_neuronparams)

    # Parts without dopamine
    for part in parts_no_dopa:
        part[k_model] = 'iaf_psc_exp'
    for part in collumns:
        part[k_model] = 'iaf_psc_exp'

    # Creating neurons
    for part in all_parts:
        part[k_IDs] = nest.Create(part[k_model], part[k_NN])
        logger.debug("{0} [{1}, {2}] {3} neurons".format(part[k_name], part[k_IDs][0], part[k_IDs][-1:][0], part[k_NN]))

    for part in collumns:
        part[k_IDs] = nest.Create(part[k_model], part[k_NN])
        logger.debug("{0} [{1}, {2}] {3} neurons".format(part[k_name], part[k_IDs][0], part[k_IDs][-1:][0], part[k_NN]))

def log_connection(pre, post, syn_type, weight):
    global SYNAPSES
    connections = pre[k_NN] * post[k_NN] if post[k_NN] < MaxSynapses else pre[k_NN] * MaxSynapses
    SYNAPSES += connections
    logger.debug("{0} -> {1} ({2}) w[{3}] // "
                 "{4}x{5}={6} synapses".format(pre[k_name], post[k_name], syn_type[:-8], weight, pre[k_NN],
                                               MaxSynapses if post[k_NN] > MaxSynapses else post[k_NN], connections))


def connect(pre, post, syn_type=GABA, weight_coef=1):
    # Set new weight value (weight_coef * basic weight)
    nest.SetDefaults(synapses[syn_type][model], {'weight': weight_coef * synapses[syn_type][basic_weight]})
    # Create dictionary of connection rules
    conn_dict = {'rule': 'fixed_outdegree',
                 'outdegree': MaxSynapses if post[k_NN] > MaxSynapses else post[k_NN],
                 'multapses': True}
    # Connect PRE IDs neurons with POST IDs neurons, add Connection and Synapse specification
    nest.Connect(pre[k_IDs], post[k_IDs], conn_spec=conn_dict, syn_spec=synapses[syn_type][model])
    # Show data of new connection
    log_connection(pre, post, synapses[syn_type][model], nest.GetDefaults(synapses[syn_type][model])['weight'])


def connect_generator(part, startTime=1, stopTime=T, rate=250, coef_part=1):
    name = part[k_name]
    # Add to spikeGenerators dict a new generator
    spike_generators[name] = nest.Create('poisson_generator', 1, {'rate' : float(rate),
                                                                  'start': float(startTime),
                                                                  'stop' : float(stopTime)})
    # Create dictionary of connection rules
    conn_dict = {'rule': 'fixed_outdegree',
                 'outdegree': int(part[k_NN] * coef_part)}
    # Connect generator and part IDs with connection specification and synapse specification
    nest.Connect(spike_generators[name], part[k_IDs], conn_spec=conn_dict, syn_spec=static_syn)
    # Show data of new generator
    logger.debug("Generator => {0}. Element #{1}".format(name, spike_generators[name][0]))


def connect_detector(part):
    name = part[k_name]
    # Init number of neurons which will be under detector watching
    number = part[k_NN] if part[k_NN] < N_detect else N_detect
    # Add to spikeDetectors a new detector
    spike_detectors[name] = nest.Create('spike_detector', params=detector_param)
    # Connect N first neurons ID of part with detector
    nest.Connect(part[k_IDs][:number], spike_detectors[name])
    # Show data of new detector
    logger.debug("Detector => {0}. Tracing {1} neurons".format(name, number))


'''Generates string full name of an image'''
def f_name_gen(path, name):
    return "{0}{1}{2}.png".format(path, name, "+dopa" if dopamine_flag else "")


def simulate():
    global startsimulate, endsimulate
    begin = 0
    save_path = "../results/output-{0}/".format(NEURONS)
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    nest.PrintNetwork()
    logger.debug('* * * Simulating')
    startsimulate = datetime.datetime.now()
    for t in np.arange(0, T, dt):
        print "SIMULATING [{0}, {1}]".format(t, t + dt)
        nest.Simulate(dt)
        end = clock()
        times.append("{0:10.1f} {1:8.1f} "
                     "{2:10.1f} {3:4.1f} {4}\n".format(begin, end - begin, end, t, datetime.datetime.now().time()))
        begin = end
        print "COMPLETED {0}%\n".format(t/dt)
    endsimulate = datetime.datetime.now()
    logger.debug('* * * Simulation completed successfully')


def get_log(startbuild, endbuild):
    logger.info("Number of neurons  : {}".format(NEURONS))
    logger.info("Number of synapses : {}".format(SYNAPSES))
    logger.info("Building time      : {}".format(endbuild - startbuild))
    logger.info("Simulation time    : {}".format(endsimulate - startsimulate))
    logger.info("Dopamine           : {}".format('YES' if dopamine_flag else 'NO'))
    logger.info("Noise              : {}".format('YES' if generator_flag else 'NO'))


def save(GUI):
    global txt_result_path
    if GUI:
        import pylab as pl
        import nest.raster_plot
        import nest.voltage_trace
        logger.debug("Saving IMAGES into {0}".format(SAVE_PATH))
        N_events_gen = len(spike_generators)
        for key in spike_detectors:
            try:
                nest.raster_plot.from_device(spike_detectors[key], hist=True)
                pl.savefig(f_name_gen(SAVE_PATH, "spikes_" + key.lower()), dpi=dpi_n, format='png')
                pl.close()
            except Exception:
                print("From {0} is NOTHING".format(key))
                N_events_gen -= 1
        for key in multimeters:
            try:
                nest.voltage_trace.from_device(multimeters[key])
                pl.savefig(f_name_gen(SAVE_PATH, "volt_" + key.lower()), dpi=dpi_n, format='png')
                pl.close()
            except Exception:
                print("From {0} is NOTHING".format(key))
        print "Results {0}/{1}".format(N_events_gen, len(spike_detectors))
        print "Results {0}/{1}".format(N_events_gen, len(spike_detectors))


    txt_result_path = SAVE_PATH + 'txt/'
    logger.debug("Saving TEXT into {0}".format(txt_result_path))
    if not os.path.exists(txt_result_path):
        os.mkdir(txt_result_path)
    for key in spike_detectors:
        save_spikes(spike_detectors[key], name=key)
    #for key in multimeters:
    #    save_voltage(multimeters[key], name=key)

    with open(txt_result_path + 'timeSimulation.txt', 'w') as f:
        for item in times:
            f.write(item)


def save_spikes(detec, name, hist=False):
    title = "Raster plot from device '%i'" % detec[0]
    ev = nest.GetStatus(detec, "events")[0]
    ts = ev["times"]
    gids = ev["senders"]
    data = defaultdict(list)

    if len(ts):
        with open("{0}@spikes_{1}.txt".format(txt_result_path, name), 'w') as f:
            f.write("Name: {0}, Title: {1}, Hist: {2}\n".format(name, title, "True" if hist else "False"))
            for num in range(0, len(ev["times"])):
                data[round(ts[num], 1)].append(gids[num])
            for key in sorted(data.iterkeys()):
                f.write("{0:>5} : {1:>4} : {2}\n".format(key, len(data[key]), sorted(data[key])))
    else:
        print "Spikes in {0} is NULL".format(name)
