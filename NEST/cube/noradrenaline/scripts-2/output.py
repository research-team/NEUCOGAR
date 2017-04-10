import logging
import os
from collections import defaultdict

import datetime

from keys import *
from simulation_params import *
import globals as g

import nest

txt_result_path = "/home/tobias/Desktop/"    # path for txt results
save_path = "/home/tobias/Desktop/"

logging.basicConfig(format='%(name)s.%(levelname)s: %(message)s.', level=logging.DEBUG)
logger = logging.getLogger('function')


def set_paths(new_save_path):
    global txt_result_path, save_path

    save_path = new_save_path
    txt_result_path = os.path.join(save_path, 'txt', '')

    if not os.path.exists(txt_result_path):
        os.makedirs(txt_result_path)


def image_name(path, name):
    """
    Generates string full name of an image
    """
    return "{0}{1}{2}.png".format(path, name, "+nora" if noradrenaline_flag else "")


def log_connection(pre, post, syn_type, weight, count):
    logger.debug("{0} -> {1} ({2}) w[{3}] // "
                 "{4}x{5}={6} synapses".format(pre[k_name], post[k_name], syn_type[:-8], weight, pre[k_NN],
                                               MaxSynapses if post[k_NN] > MaxSynapses else post[k_NN], count))


def get_log(startbuild, endbuild):
    logger.info("Number of neurons  : {}".format(g.NEURONS))
    logger.info("Number of synapses : {}".format(g.SYNAPSES))
    logger.info("Building time      : {}".format(endbuild - startbuild))
    logger.info("Simulation time    : {}".format(g.endsimulate - g.startsimulate))
    logger.info("Noradrenaline           : {}".format('YES' if noradrenaline_flag else 'NO'))


def save(images):
    """
    Save simulation results to txt_result_path folder
    Args:
        images: if True, png images will be created
    Returns: None
    """
    if images:
        import pylab as pl
        import nest.raster_plot
        import nest.voltage_trace
        N_events_gen = len(g.spike_generators)
        for key in g.spike_detectors:
            try:
                nest.raster_plot.from_device(g.spike_detectors[key], hist=True)
                pl.savefig(image_name(save_path, "spikes_" + key.lower()), dpi=dpi_n, format='png')
                pl.close()
            except Exception:
                print("From {0} is NOTHING".format(key))
                N_events_gen -= 1
        for key in g.multimeters:
            try:
                nest.voltage_trace.from_device(g.multimeters[key])
                pl.savefig(image_name(save_path, "volt_" + key.lower()), dpi=dpi_n, format='png')
                pl.close()
            except Exception:
                print("From {0} is NOTHING".format(key))
        print "Results {0}/{1}".format(N_events_gen, len(g.spike_detectors))

    logger.debug("Saving TEXT into {0}".format(txt_result_path))

    for key in g.spike_detectors:
        save_spikes(g.spike_detectors[key], name=key)

    # save_voltage(multimeters)

    with open(txt_result_path + 'timeSimulation.txt', 'w') as f:
        for item in g.times:
            f.write(item)


def save_spikes(detec, name, hist=False):
    """
    Save spikes from specified detector to file
    Args:
        detec: detector
        name: file name (will be prefixed)
        hist: include histogram?
    Returns: None
    """
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


def save_voltage(multimeters):
    import h5py

    print "Write to HDF5 file"
    filename = "voltage.hdf5"
    timestamp = datetime.datetime.now()

    with h5py.File(filename, "w") as f:
        f.attrs['default'] = 'entry'
        f.attrs['file_name'] = filename
        f.attrs['file_time'] = str(timestamp)

        f.create_dataset(key, data=nest.GetStatus(multimeters[key], "events")[0]["V_m"])
        f.close()
    print "wrote file:", filename
    # title = "Membrane potential"
    # ev = nest.GetStatus(detec, "events")[0]
    # with open("{0}@voltage_{1}.txt".format(txt_result_path, name), 'w') as f:
    #    f.write("Name: {0}, Title: {1}\n".format(name, title))
    #    print int(T / multimeter_param['interval'])
    #    for line in range(0, int(T / multimeter_param['interval'])):
    #        for index in range(0, N_volt):
    #            print "{0} {1} ".format(ev["times"][line], ev["V_m"][line])
    #        #f.write("\n")
    #        print "\n"


def print_connections(f):
    f.write('edgedef> node, node2')
    for conn in nest.GetConnections():
        f.write("%d, %d\n" % (conn[0], conn[1]))


def print_gdf(f):
    """
    Print network as a graph in GDF format
    Args:
        f: file
    Returns: None
    """

    f.write("nodedef> label\n")
    for node in nest.GetNodes((0,))[0]:
        f.write("%d\n" % node)

    print_connections(f)
