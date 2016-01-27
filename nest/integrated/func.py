import os
import nest
import datetime
import numpy as np
from time import clock
from parameters import *

parts_dict_log = {} # dict part      : name_part
spikedetector = {}  # dict name_part : spikedetector
multimeter = {}     # dict name_part : multimeter
NEURONS = 0


logger = logging.getLogger("function")
log_conn = lambda a, b, syn_type=None: logger.debug('%s -> %s (%s)' % (parts_dict_log[a], parts_dict_log[b],
                                                                       'generator' if syn_type is None else syn_type))

def f_register(item, name):
    global NEURONS
    parts_dict_log[item] = name
    logger.debug("* * * %s interval [%d, %d]" % (name, item[0], item[0] + len(item) - 1))
    NEURONS += len(item)


'''Help method to get neurons_list from iter_all{'name':neurons_list}'''
def get_ids(name, iter_all=None):
    if iter_all is not None:
        get_ids.iter_all = iter_all
    for part in get_ids.iter_all:
        if part[k_name] == name:
            return part[k_ids]
    raise KeyError


'''Help method for SIMPLE connections'''
def connect(part_from, part_to, syn_type=GABA):
    if syn_type == Glu:
        nest.Connect(part_from, part_to, conn_spec=conn_dict, syn_spec=STDP_synparams_Glu)
        log_conn(part_from, part_to, "Glu")
    elif syn_type == ACh:
        nest.Connect(part_from, part_to, conn_spec=conn_dict, syn_spec=STDP_synparams_ACh)
        log_conn(part_from, part_to, "ACh")
    else:
        nest.Connect(part_from, part_to, conn_spec=conn_dict, syn_spec=STDP_synparams_GABA)
        log_conn(part_from, part_to, "GABA")


'''Help method for DOPAMINE connections'''
def connectDA_ex(part_from, part_to):   # read about "conn_dict"
    nest.Connect(part_from, part_to, conn_dict, syn_spec=dopa_model_ex)
    log_conn(part_from, part_to, dopa_model_ex)


'''Help method for DEVICE connections'''
def connect_spikegenerator(typeGenerator, part, startTime, stopTime, weightParam=w_Glu):
    if typeGenerator == 'fast':
        generator_fast = nest.Create("poisson_generator", 1, {"rate": K_fast, 'start': startTime, 'stop': stopTime})
        parts_dict_log[generator_fast[0]] = 'Poisson Generator(fast)'
        nest.Connect(generator_fast, part, syn_spec=gen_static_syn,
                     conn_spec={'rule': 'fixed_outdegree', 'outdegree': len(part) / 4})
        log_conn(generator_fast[0], part)
    else:
        generator_slow = nest.Create("poisson_generator", 1, {"rate": K_slow})
        parts_dict_log[generator_slow[0]] = 'Poisson Generator(slow)'
        nest.CopyModel("static_synapse", gen_static_syn, {'weight': weightParam, 'delay': pg_delay})
        nest.Connect(generator_slow, part, syn_spec=gen_static_syn,
                 conn_spec={'rule': 'fixed_outdegree', 'outdegree': len(part) / 4})
        log_conn(generator_slow[0], part)

def connect_spikedetector(part):
    name = parts_dict_log[part]                                                 # find name of this part
    spikedetector[name] = nest.Create("spike_detector", params=detector_param)  # new detector in dict
    nest.Connect(part[:N_rec], spikedetector[name])                             # connect NUM detector
    logger.debug("spike detector is attached to %s: tracing %d neurons" % (name, N_rec) )

def connect_multimeter(part):
    name = parts_dict_log[part]
    multimeter[name] = nest.Create('multimeter', params=mm_param)
    nest.Connect(multimeter[name], (part[0],) )
    logger.debug("%s - %d", name, part[0])


'''Generates string full name of an image'''
f_name_gen = lambda path, name: path + name + '_'  + ('yes' if dopa_flag else 'no') + '_dopamine_' + \
                                ('noise' if poison_generator_flag else 'static') + '.png'


'''Method for dt simulation and geting info from sensors'''
def start_simulation():
    global startsimulate, endsimulate
    startsimulate = clock()
    nest.PrintNetwork()

    times = []
    resources = []

    iter_dt = 0
    begin = 0
    for t in np.arange(0, T + dt, dt):
        print str(iter_dt)
        nest.Simulate(dt)
        end = clock()
        times.append(str('%10.1f %8.1f %10.1f   %4d ' % (begin, end - begin, end, t)) + str(datetime.datetime.now().time()) + '\n')
        iter_dt+=1
        begin = end
        tRes = open('timeResources.txt', 'w')
        tSim = open('timeSimulation.txt', 'w')
        for item in resources:
            tRes.write(item)
        for item in times:
            tSim.write(item)
        tSim.close()
        tRes.close()

    endsimulate = clock()


'''Log informations about simulating'''
def get_information(startbuild, endbuild, *args):
    build_time = endbuild - startbuild
    sim_time = endsimulate - endbuild
    # logger.info("Number of neurons : {0}".format(len(thalamus)))
    # logger.info("Number of synapses: {0}".format(num_synapses))
    logger.info("Building time: %8.2f s" % build_time)
    logger.info("Simulation time: %8.2f s" % sim_time)
    for key in spikedetector:
        logger.info("%18s rate: %8.2f Hz" % (key, nest.GetStatus(spikedetector[key], "n_events")[0] / sim_time * 1000.0 / N_rec))

    logger.info('Dopamine: ' + ('YES' if dopa_flag else 'NO'))
    logger.info('Noise: ' + ('YES' if poison_generator_flag else 'NO'))


'''Saving resuts method'''
def save_results(GUI):
    global SAVE_PATH
    if GUI:
        import nest.raster_plot
        import nest.voltage_trace
        import pylab as pl

        SAVE_PATH = "output-%d (png)/" % NEURONS
        logger.debug('Saving IMAGES into %s' % SAVE_PATH)
        if not os.path.exists(SAVE_PATH):
            os.mkdir(SAVE_PATH)
        for key in spikedetector:
            nest.raster_plot.from_device((spikedetector[key][0],), hist=True)
            pl.savefig(f_name_gen(SAVE_PATH, "spikes_" + key.lower()), dpi=dpi_n, format='png')
            pl.close()
        for key in multimeter:
            nest.voltage_trace.from_device(multimeter[key])
            pl.savefig(f_name_gen(SAVE_PATH, "volt_" + key.lower()), dpi=dpi_n, format='png')
            pl.close()
    else:
        SAVE_PATH = "output-%d (txt)/" % NEURONS
        logger.debug('Saving TEXT into %s' % SAVE_PATH)
        if not os.path.exists(SAVE_PATH):
            os.mkdir(SAVE_PATH)
        for key in spikedetector:
            save_spikes(spikedetector[key], name=key)           #, hist=True)
        for key in multimeter:
            save_voltage(multimeter[key], name=key)

'''Saving spikes into txt file '''
def save_spikes(detec, name, hist=False):
    ev = nest.GetStatus(detec, "events")[0]
    ts = ev["times"]
    gids = ev["senders"]
    title = "Raster plot from device '%i'" % detec[0]
    flag = "True" if hist else "False"
    output = open(SAVE_PATH + "@spikes_" + name + ".txt", 'wb')
    for elem in ts:
        output.write(str(elem) + " ")
    output.write("@@@")
    for elem in gids:
        output.write(str(elem) + " ")
    output.write("@@@" + title + "@@@" + flag)
    output.close()

'''Saving membrne potential into txt file '''
def save_voltage(detec, name):
    ev = nest.GetStatus(detec, "events")[0]
    output = open(SAVE_PATH + "@voltage_" + name + ".txt", 'wb')
    times = ev["times"]
    voltages = ev["V_m"]
    for elem in times:
        output.write(str(elem) + " ")
    output.write("@@@")
    for elem in voltages:
        output.write(str(elem) + " ")
        #todo add neuron title
    output.close()

'''
import psutil

import time
from threading import Thread

class writeRes(Thread):
    def run(self):
        resources.append(str('%5d MB %7.1f MHz ' % (psutil.virtual_memory()[3] / MEGA, psutil.cpu_times()[0] ) + str(datetime.datetime.now().time())) + '\n')

class timer(Thread):
    def run(self):
        while timerFlag:
            writeRes().start()
            sleep
'''