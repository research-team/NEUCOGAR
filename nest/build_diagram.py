import numpy
import pylab
import os

#TODO change directory
path = "/home/panzer/Desktop/"

def spike_make_diagram(ts, gids, hist, title, xlabel, name):
    dpi_n = 120
    ts1 = ts
    neurons = gids
    hist_binwidth = 5.0
    pylab.figure()
    color_marker = "."
    color_bar = "blue"
    color_edge = "black"
    ylabel = "Neuron ID"

    if hist == "True":
        #TODO this part doesn't work! Trying to fix
        ax1 = pylab.axes([0.1, 0.3, 0.85, 0.6])
        pylab.plot(ts1, gids, color_marker)
        pylab.ylabel(ylabel)
        pylab.xticks([])
        xlim = pylab.xlim()

        pylab.axes([0.1, 0.1, 0.85, 0.17])
        t_bins = numpy.arange(numpy.amin(ts), numpy.amax(ts), hist_binwidth)
        n, bins = pylab.histogram(ts, bins=t_bins)
        num_neurons = len(numpy.unique(neurons))
        print "num_neurons " + str(num_neurons)
        heights = 1000 * n / (hist_binwidth * num_neurons)
        print "t_bins " + str(len(t_bins)) + "\n" + str(t_bins) + "\n" + \
               "height " + str(len(heights)) + "\n" + str(heights) + "\n"
        #bar(left,height, width=0.8, bottom=None, hold=None, **kwargs):
        pylab.bar(t_bins, heights, width=hist_binwidth, color=color_bar, edgecolor=color_edge)
        pylab.yticks([int(a) for a in numpy.linspace(0.0, int(max(heights) * 1.1) + 5, 4)])
        pylab.ylabel("Rate (Hz)")
        pylab.xlabel(xlabel)
        pylab.xlim(xlim)
        pylab.axes(ax1)
    else:
        pylab.plot(ts1, gids, color_marker)
        pylab.xlabel(xlabel)
        pylab.ylabel(ylabel)

    pylab.title(title)
    pylab.draw()
    pylab.savefig(path + name + ".png", dpi=dpi_n, format='png')
    pylab.close()

def voltage_make_diagram(times, voltages, name):
    title = "Membrane potential"
    dpi_n = 120
    timeunit="ms"
    line_style = ""
    if not len(times):
        raise nest.NESTError("No events recorded! Make sure that withtime and withgid are set to True.")
    pylab.plot(times, voltages, line_style, label="Neuron %s" % "test(null)")
    pylab.ylabel("Membrane potential (mV)")
    pylab.xlabel("Time (%s)" % timeunit)
    pylab.legend(loc="best")
    pylab.title(title)
    pylab.draw()
    pylab.savefig(path + name + ".png", dpi=dpi_n, format='png')
    pylab.close()



block = [filename for filename in os.listdir(path) if filename[0] == "@"]

for filename in block:
    if filename.find("spikes") != -1:
        inFile = open(path + filename, 'rb')
        mas = inFile.read().split("@@@")
        inFile.close()

        x_vals = [float(x) for x in mas[0].split()]
        y_vals = [int(y) for y in mas[1].split()]
        clearName = filename[1:filename.find(".txt")]
        #make_diagram(ts, gids, hist, title, xlabel, name):
        spike_make_diagram(x_vals, y_vals, mas[4], mas[2], mas[3], clearName)
    else:
        inFile = open(path + filename, 'rb')
        mas = inFile.read().split("@@@")
        inFile.close()

        x_vals = [float(x) for x in mas[0].split()]
        y_vals = [float(y) for y in mas[1].split()]
        clearName = filename[1:filename.find(".txt")]
        voltage_make_diagram(x_vals, y_vals, clearName)
    print filename + " diagram created"