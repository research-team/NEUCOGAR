__author__  = "Alexey Panzer"
__version__ = "1.5"
__tested___ = "17.03.2016"

import os
import numpy
import pylab
from collections import defaultdict

# Image quality
dpi_n = 120

def spikes_diagram(ts, gids, name, path):
    """
    Function for making spike diagrams
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
    pylab.savefig("{0}{1}.png".format(path, name), dpi=dpi_n, format='png')
    pylab.close()


def voltage_diagram(times, voltages, name, path):
    """
    Function for making voltage diagrams
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
    pylab.title("Voltage" + name)
    pylab.grid(True)
    pylab.draw()
    pylab.savefig("{0}{1}.png".format(path, name), dpi=dpi_n, format='png')
    pylab.close()


def start(path):
    # Search data and build diagrams for multimeters
    for voltage_file in sorted(set([name[:name.rfind("-")] for name in os.listdir(path) if name.endswith(".dat")])):
        meta = voltage_file.split('-')
        times = defaultdict(list)
        voltages = defaultdict(list)
        # take data of the same files (but another thread)
        for merge_file in [filename for filename in os.listdir(path) if filename.startswith(voltage_file) and filename.endswith(".dat")]:
            with open(path + merge_file, 'r') as f:
                for line in f:
                    # split by whitespace: gid time voltage
                    data = line.split()
                    times[data[0]].append(float(data[1]))
                    voltages[data[0]].append(float(data[2]))

        voltage_diagram(dict(times), dict(voltages), meta[0] + meta[1], path)
        print voltage_file, "diagram created"
        del meta, times, voltages, gid

    # Search data and build diagrams for spike detectors
    for spikes_file in sorted(set([name[:name.rfind("-")] for name in os.listdir(path) if name.endswith(".gdf")])):
        meta = spikes_file.split('-')
        gids = list()
        times = list()
        # take data of the same files (but another thread)
        for merge_file in [filename for filename in os.listdir(path) if filename.startswith(spikes_file) and filename.endswith(".gdf")]:
            # if file is not empty take data
            if os.stat(path+merge_file).st_size > 0:
                with open(path + merge_file, 'r') as f:
                    for line in f:
                        # split by whitespace: gid time
                        data = line.split()
                        gids.append(int(data[0]))
                        times.append(float(data[1]))
        # if no recorded data
        if len(times) == 0:
            print spikes_file, "no recorded data"
        else:
            spikes_diagram(times, gids, meta[0] + meta[1], path)
            print spikes_file, "diagram created"
        del meta, times, gids

if __name__ == '__main__':
    folder = raw_input("Enter path to the txt results: ")
    start(folder + "/" if folder[-1:] != "/" else folder)
