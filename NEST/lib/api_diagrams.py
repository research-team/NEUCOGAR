__author__  = "Alexey Panzer"
__version__ = "2.0.0"
__tested___ = "07.11.2017 NEST 2.12.0 Python 3"

import os
import sys
import numpy
import pylab
import logging
import api_globals as glob
from collections import defaultdict

logging.basicConfig(format='%(name)s::%(funcName)s %(message)s', level=logging.INFO)
logger = logging.getLogger('api_diagrams')
successed = 0


def __create_dirs(txt_path=None):
    """
    AAAAAAAAAa

    Description:
        AAAAAAAAa

    Args:
        txt_path (str): path for txt_OLD results
    """
    # Determine current work path
    if not txt_path:
        txt_path = glob.current_path
    # Create dirs for txt_OLD and img results
    if not os.path.exists(txt_path):
        os.makedirs(txt_path + "/img")


def BuildSpikeDiagrams(txt_path=None):
    """
    Function for building spike diagrams
    
    Description:
        Init save path, get data from files and invoke method for drawing

    Args:
        txt_path (str): path for txt_OLD results
    """
    __create_dirs(txt_path)

    files_gdf = sorted(set([name[:name.rfind("-")] for name in os.listdir(txt_path) if name.endswith(".gdf")]))

    logger.info("scan folder for '.gdf'... {0} {1}".format(len(files_gdf), "OK" if files_gdf else "ERROR"))

    if len(files_gdf) == 0:
        return

    logger.info("results path '/img'")

    for spikes_file in files_gdf:
        meta = spikes_file.split('-')
        gids = list()
        times = list()
        # take data of the same files (but another thread)
        for merge_file in [filename for filename in os.listdir(txt_path) if filename.startswith(spikes_file) and filename.endswith(".gdf")]:
            # if file is not empty take data
            if os.stat("{0}/{1}".format(txt_path, merge_file)).st_size > 0:
                with open("{0}/{1}".format(txt_path, merge_file), 'r') as f:
                    for line in f:
                        # split by whitespace: gid time
                        data = line.split()
                        if len(data) == 2:
                            gids.append(int(data[0]))
                            times.append(float(data[1]))
        if len(times) == 0:
            err_msg = "ERROR. No recorded data"
        else:
            err_msg = __make_spikes_diagram(times, gids, "{0} {1}".format(meta[0], meta[1]), txt_path)

        logger.info("{0}... {1}".format(spikes_file, err_msg))

    logger.info("Successfully created {0}/{1}\n".format(successed, len(files_gdf)))


def BuildVoltageDiagrams(txt_path=None):
    """
    Function for building voltage diagrams

    Description:
        Init save path, get data from files and invoke method for drawing

    Args:
        txt_path (str): path for txt_OLD results
    """
    __create_dirs(txt_path)

    files_dat = sorted(set([name[:name.rfind("-")] for name in os.listdir(txt_path) if name.endswith(".dat")]))

    logger.info("scan folder for '.dat'... {0} {1}".format(len(files_dat), "OK" if files_dat else "ERROR"))

    if len(files_dat) == 0:
        return

    logger.info("results path '/img'")

    for voltage_file in files_dat:
        broken = 0
        meta = voltage_file.split('-')
        times = defaultdict(list)
        voltages = defaultdict(list)
        # take data of the same files (but another thread)
        for merge_file in [filename for filename in os.listdir(txt_path) if filename.startswith(voltage_file) and filename.endswith(".dat")]:
            with open("{0}/{1}".format(txt_path, merge_file), 'r') as f:
                for line in f:
                    # split by whitespace: gid time voltage
                    data = line.split()
                    if len(data) == 3:
                        times[data[0]].append(float(data[1]))
                        voltages[data[0]].append(float(data[2]))
                    else:
                        broken+=1

        if len(times) == 0:
            err_msg = "ERROR. No recorded data"
        else:
            err_msg = __make_voltage_diagram(dict(times), dict(voltages), "{0} {1}".format(meta[0], meta[1]), txt_path)
        logger.info("{0}... {1} (broken lines {2})".format(voltage_file, err_msg, broken))
    logger.info("Successfully created {0}/{1}\n".format(successed, len(files_dat)))


def Heatmap(txt_path=None):
    """
    aaaaaa

    Description:
        aaaaaaa

    Args:
        txt_path (str): path for txt_OLD results
    """
    __create_dirs(txt_path)
    pass


def BuildWeightDiagrams(txt_path=None):
    """
    Function for building weight diagrams

    Description:
        aaaaaaa

    Args:
        txt_path (str): path for txt_OLD results
    """
    global successed

    __create_dirs(txt_path)

    files_csv = sorted([fl for fl in os.listdir(txt_path) if fl.endswith(".csv")])

    logger.info("scan folder for '.csv'... {0} {1}".format(len(files_csv), "OK" if files_csv else "ERROR"))

    if len(files_csv) == 0:
        return

    logger.info("results path '/img'")

    connectome = defaultdict(list)
    # collect all .csv files
    for filename in files_csv:
        with open("{0}/{1}".format(txt_path, filename), 'r') as f:
            for line in f:
                # split data by space. source GID
                data = line.split()
                # (src, dest) : (time, weight)
                connectome[(data[0], data[1])].append( (data[2], data[3]) )
            successed += 1

    if len(connectome) == 0:
        err_msg = "ERROR. No recorded data"
    else:
        err_msg = __make_weight_diagram(connectome, txt_path)
    logger.info("{0}... {1}".format("TEST_CHANGE_ME", err_msg))

    logger.info("Successfully created {} \n".format(sys.getsizeof(connectome), "bytes"))


def __make_weight_diagram(conn_dict, txt_path):
    """

    :return:
    """
    pylab.figure()
    pylab.title("STDP")
    pylab.xlabel("Time (ms)")
    pylab.ylabel("Weight")

    for conn in list(conn_dict)[:10]:
        times = [data[0] for data in conn_dict[conn]]
        weights = [data[1] for data in conn_dict[conn]]
        pylab.plot(times, weights, label="{}".format(conn))
        pylab.draw()
    pylab.legend(loc='upper left')
    pylab.savefig("{0}/img/{1}.png".format(txt_path, "STDP_weights"), figsize=(10, 6), dpi=120, format='png')
    pylab.close()

    return "OK"


def __make_spikes_diagram(times, gids, name, path):
    """
    Draw spike diagram
    
    Description:
        Set parameters, include data, draw and save
        
    Args:
        times (list): times
        gids  (list): global IDs of neurons
        name   (str): name of brain part
        path   (str): path to save results
    """
    global successed
    pylab.figure()
    color_marker = "."
    color_bar = "blue"
    color_edge = "black"
    ylabel = "Neuron ID"
    hist_binwidth = 5.0
    location = pylab.axes([0.1, 0.3, 0.85, 0.6])
    pylab.plot(times, gids, color_marker)
    pylab.ylabel(ylabel)
    pylab.xticks([])
    pylab.axes([0.1, 0.1, 0.85, 0.17])
    pylab.xlim([0, 1000])
    t_bins = numpy.arange(numpy.amin(times), numpy.amax(times), hist_binwidth)
    if len(t_bins) == 0:
        pylab.close()
        return "t_bins for {0} is empty".format(name)
    n, bins = pylab.histogram(times, bins=t_bins)
    num_neurons = len(numpy.unique(gids))
    heights = (1000 * n / (hist_binwidth * num_neurons))
    if len(heights) == 0:
        pylab.close()
        return "heights for {0} is empty".format(name)
    # FixMe t_bins[:-1] should work without cutting the end value
    pylab.bar(t_bins[:-1], heights, width=hist_binwidth, color=color_bar, edgecolor=color_edge)
    pylab.yticks([int(a) for a in numpy.linspace(0.0, int(max(heights) * 1.1) + 5, 4)])
    pylab.ylabel("Rate (Hz)")
    pylab.xlabel("Time (ms)")
    pylab.grid(True)
    pylab.axes(location)
    pylab.title(name)
    pylab.xlim([0, 1000])
    pylab.draw()
    pylab.savefig("{0}/img/{1}.png".format(path, name), dpi=120, format='png')
    pylab.close()

    successed += 1
    return "OK"


def __make_voltage_diagram(times, voltages, name, path):
    """
    Draw voltage diagram

    Description:
        Set parameters, include data, draw and save

    Args:
        times    (list, dict): time data of neuron (if list) and neurons (if dict)
        voltages (list, dict): voltage data of neuron (if list) and neurons (if dict)
        name            (str): name of brain part
        path            (str): path to save results
    """
    global successed

    pylab.figure()
    line_style = ""

    if type(times) is dict:
        # for each neuron plot
        for key in times:
            pylab.plot(times[key], voltages[key], line_style, label=key)
    else:
        raise ValueError("Unsupported value")

    pylab.ylabel("Membrane potential (mV)")
    pylab.xlabel("Time (ms)")
    pylab.legend(loc="best")
    pylab.title(name)
    pylab.grid(True)
    pylab.draw()
    pylab.savefig("{0}/img/{1}.png".format(path, name), dpi=120, format='png')
    pylab.close()

    successed += 1
    return "OK"


# As independent script
if __name__ == '__main__':
    #folder = input("Enter path to the results: ")
    txt_folder = '/home/alex/350K-124/txt/'
    img_folder = "{}/img".format(txt_folder)
    if not os.path.exists(img_folder):
        os.mkdir(img_folder)

    BuildSpikeDiagrams(txt_folder)
    BuildVoltageDiagrams(txt_folder)
    BuildWeightDiagrams(txt_folder)
