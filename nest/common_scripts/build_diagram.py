import numpy
import pylab
import os

dpi_n = 120

def spike_make_diagram(ts, gids, name, title):
    pylab.figure()
    color_marker = "."
    color_bar = "blue"
    color_edge = "black"
    ylabel = "Neuron ID"

    hist_binwidth = 5.0
    ts1 = ts
    neurons = gids

    ax1 = pylab.axes([0.1, 0.3, 0.85, 0.6])
    pylab.plot(ts1, gids, color_marker)
    pylab.ylabel(ylabel)
    pylab.xticks([])
    xlim = pylab.xlim()

    pylab.axes([0.1, 0.1, 0.85, 0.17])
    t_bins = numpy.arange(numpy.amin(ts), numpy.amax(ts), hist_binwidth)
    n, bins = pylab.histogram(ts, bins=t_bins)
    t_bins = t_bins[:-1]                        # FixMe it must work without cutting the end value
    num_neurons = len(numpy.unique(neurons))
    heights = (1000 * n / (hist_binwidth * num_neurons))
    pylab.bar(t_bins, heights, width=hist_binwidth, color=color_bar, edgecolor=color_edge)
    pylab.yticks([int(a) for a in numpy.linspace(0.0, int(max(heights) * 1.1) + 5, 4)])
    pylab.ylabel("Rate (Hz)")
    pylab.xlabel("Time (ms)")
    pylab.xlim(xlim)
    pylab.axes(ax1)

    pylab.title(title)
    pylab.draw()
    pylab.savefig(path + name + ".png", dpi=dpi_n, format='png')
    pylab.close()


def voltage_make_diagram(times, voltages, name, title):
    timeunit="ms"
    line_style = ""
    if not len(times):
        raise nest.NESTError("No events recorded! Make sure that withtime and withgid are set to True.")
    pylab.plot(times, voltages, line_style, label=title)
    pylab.ylabel("Membrane potential (mV)")
    pylab.xlabel("Time (%s)" % timeunit)
    pylab.legend(loc="best")
    pylab.title(title)
    pylab.draw()
    pylab.savefig(path + name + ".png", dpi=dpi_n, format='png')
    pylab.close()


def start(path):
    for filename in [filename for filename in os.listdir(path) if filename[0] == "@"]:
        if filename.startswith('@spikes'):
            x_vals = []
            y_vals = []
            with open(path + filename, 'r') as f:
                header = f.readline()
                log = list( v.strip() for k, v in (item.split(':') for item in header.split(',')) )
                for line in f:
                    for item in line[line.index("[")+1 : line.index("]")].split(","):
                        x_vals.append(float(line[:6]))
                        y_vals.append(int(item))
            spike_make_diagram(x_vals, y_vals, log[0], log[1])
            del x_vals, y_vals
        else:
            # FixMe doesn't implemented!
            print 'pass this file'
            #with open(path + filename, 'r') as f:
            #    header = f.readline()
            #    log = list( v.strip() for k, v in (item.split(':') for item in header.split(',')) )
            #    for line in f:
            #        x, y = line.split()
            #        x_vals.append(x)
            #        y_vals.append(y)
            #voltage_make_diagram(x_vals, y_vals, log[0], log[1])
        print filename + " diagram created"

if __name__ == '__main__':
    path = raw_input("Enter path to the txt results: ")
    start(path+"/" if path[-1:] != "/" else path)