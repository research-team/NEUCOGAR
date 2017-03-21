__author__  = "Alexey Panzer"
__version__ = "1.2"
__tested___ = "22.03.2017"

import os
import numpy
import pylab
import logging
from collections import defaultdict

logging.basicConfig(format='%(name)s::%(funcName)s %(message)s', level=logging.INFO)
logger = logging.getLogger('api_diagrams')

def BuildSpikeDiagrams(txt_path=None):
    """
    Function for making spike diagrams
    :return:
    """
    img_path = "img"

    if not txt_path:
        import api_globals as glob
        txt_path = glob.current_path

    if txt_path and not os.path.exists(txt_path):
        os.makedirs(txt_path)

    if not os.path.exists(img_path):
        os.makedirs(img_path)

    for spikes_file in sorted(set([name[:name.rfind("-")] for name in os.listdir(txt_path) if name.endswith(".gdf")])):
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
        # if no recorded data
        if len(times) == 0:
            print spikes_file, "no recorded data"
        else:
            __make_spikes_diagram(times, gids, "{0} {1}".format(meta[0], meta[1]), img_path)
            print spikes_file, "diagram created"
        del meta, times, gids


def BuildVoltageDiagrams(txt_path=None):
    """
    Function for making voltage diagrams
    :return:
    """

    img_path = "img"

    if not txt_path:
        import api_globals as glob
        txt_path = glob.current_path

    if txt_path and not os.path.exists(txt_path):
        os.makedirs(txt_path)

    if not os.path.exists(img_path):
        os.makedirs(img_path)

    for voltage_file in sorted(set([name[:name.rfind("-")] for name in os.listdir(txt_path) if name.endswith(".dat")])):
        meta = voltage_file.split('-')
        times = defaultdict(list)
        voltages = defaultdict(list)
        # take data of the same files (but another thread)
        for merge_file in [filename for filename in os.listdir(txt_path) if filename.startswith(voltage_file) and filename.endswith(".dat")]:
            with open("{0}/{1}".format(txt_path, merge_file), 'r') as f:
                for line in f:
                    # split by whitespace: gid time voltage
                    data = line.split()
                    times[data[0]].append(float(data[1]))
                    voltages[data[0]].append(float(data[2]))
        __make_voltage_diagram(dict(times), dict(voltages), "{0} {1}".format(meta[0], meta[1]), img_path)
        print voltage_file, "diagram created"
        del meta, times, voltages


def Heatmap():
    pass


def __make_spikes_diagram(ts, gids, name, path):
    """
    Build diagram
    :param ts:   (list) times
    :param gids: (list) global IDs of neurons
    :param name: (str) name of brain part
    :param path: (str) path to save results
    :return: None
    """
    pylab.figure()
    color_marker = "."
    color_bar = "blue"
    color_edge = "black"
    ylabel = "Neuron ID"
    hist_binwidth = 5.0
    location = pylab.axes([0.1, 0.3, 0.85, 0.6])
    pylab.plot(ts, gids, color_marker)
    pylab.ylabel(ylabel)
    xlim = pylab.xlim()
    pylab.xticks([])
    pylab.axes([0.1, 0.1, 0.85, 0.17])
    t_bins = numpy.arange(numpy.amin(ts), numpy.amax(ts), hist_binwidth)
    n, bins = pylab.histogram(ts, bins=t_bins)
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


def __make_voltage_diagram(times, voltages, name, path):
    """
    Build diagram
    :param times:    (dict) times
    :param voltages: (dict) voltages
    :param name:     (str) name of brain part
    :param path:     (str) path to save diagram
    :return: None
    """
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
    pylab.title("Voltage " + name)
    pylab.grid(True)
    pylab.draw()
    pylab.savefig("{0}/{1}.png".format(path, name), dpi=120, format='png')
    pylab.close()

'''
START POINT, WHERE I CAN FIND PATH
'''

# As independent script
if __name__ == '__main__':
    folder = raw_input("Enter path to the results: ")
    BuildSpikeDiagrams(folder)
    BuildVoltageDiagrams(folder)