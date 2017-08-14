__author__  = "Alexey Panzer"
__version__ = "1.3.1"
__tested___ = "14.08.2017 NEST 2.12.0 Python 3"

import os
import numpy
import pylab
import logging
import api_globals as glob
from collections import defaultdict

logging.basicConfig(format='%(name)s::%(funcName)s %(message)s', level=logging.INFO)
logger = logging.getLogger('api_diagrams')
successed = 0

def BuildSpikeDiagrams(txt_path=None):
    """
    Function for building spike diagrams
    
    Description:
        Init save path, get data from files and invoke method for drawing

    Args:
        txt_path (str): path for txt results
    """

    if not txt_path:
        txt_path = glob.current_path

    if txt_path and not os.path.exists(txt_path):
        os.makedirs(txt_path)

    logger.info("results path '{0}/img'".format(txt_path))

    files_gdf = sorted(set([name[:name.rfind("-")] for name in os.listdir(txt_path) if name.endswith(".gdf")]))

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
                        gids.append(int(data[0]))
                        times.append(float(data[1]))
        if len(times) == 0:
            err_msg = "ERROR. No recorded data"
        else:
            err_msg = __make_spikes_diagram(times, gids, "{0} {1}".format(meta[0], meta[1]), txt_path)

        logger.info("{0}... {1}".format(spikes_file, err_msg))
        del meta, times, gids

    logger.info("Successfully created {0}/{1}\n".format(successed, len(files_gdf)))


def BuildVoltageDiagrams(txt_path=None):
    """
    Function for building voltage diagrams

    Description:
        Init save path, get data from files and invoke method for drawing

    Args:
        txt_path (str): path for txt results
    """

    if not txt_path:
        txt_path = glob.current_path

    if txt_path and not os.path.exists(txt_path):
        os.makedirs(txt_path)

    for voltage_file in sorted(set([name[:name.rfind("-")] for name in os.listdir(txt_path) if name.endswith(".dat")])):
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
        __make_voltage_diagram(dict(times), dict(voltages), "{0} {1}".format(meta[0], meta[1]), txt_path)
        logger.info("{0}. Broken lines {1}".format(voltage_file, broken))
        del meta, times, voltages


def Heatmap():
    pass


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

    path += "/img"

    if not os.path.exists(path):
        os.makedirs(path)

    pylab.figure()
    color_marker = "."
    color_bar = "blue"
    color_edge = "black"
    ylabel = "Neuron ID"
    hist_binwidth = 5.0
    location = pylab.axes([0.1, 0.3, 0.85, 0.6])
    pylab.plot(times, gids, color_marker)
    pylab.ylabel(ylabel)
    xlim = pylab.xlim()
    pylab.xticks([])
    pylab.axes([0.1, 0.1, 0.85, 0.17])
    t_bins = numpy.arange(numpy.amin(times), numpy.amax(times), hist_binwidth)
    if len(t_bins) == 0:
        pylab.close()
        return "t_bins for {0} is empty".format(name)
    n, bins = pylab.histogram(times, bins=t_bins)
    num_neurons = len(numpy.unique(gids))
    heights = (1000 * n / (hist_binwidth * num_neurons))
    # FixMe t_bins[:-1] should work without cutting the end value
    pylab.bar(t_bins[:-1], heights, width=hist_binwidth, color=color_bar, edgecolor=color_edge)
    pylab.yticks([int(a) for a in numpy.linspace(0.0, int(max(heights) * 1.1) + 5, 4)])
    pylab.ylabel("Rate (Hz)")
    pylab.xlabel("Time (ms)")
    pylab.grid(True)
    pylab.axes(location)
    pylab.title(name)
    pylab.xlim(xlim)
    pylab.draw()
    pylab.savefig("{0}/{1}.png".format(path, name), dpi=120, format='png')
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

    path += "/img"

    if not os.path.exists(path):
        os.makedirs(path)

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
    pylab.savefig("{0}/{1}.png".format(path, name), dpi=120, format='png')
    pylab.close()


# As independent script
if __name__ == '__main__':
    folder = input("Enter path to the results: ")
    BuildSpikeDiagrams(folder)
    BuildVoltageDiagrams(folder)