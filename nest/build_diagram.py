import numpy
import pylab
import os

#TODO change directory
path = "/home/alex/Desktop/test/"
dpi_n = 120



def spike_make_diagram(ts, gids, name, title, hist):
    pylab.figure()
    color_marker = "."
    color_bar = "blue"
    color_edge = "black"
    ylabel = "Neuron ID"

    if hist == "True":
        #TODO this part doesn't work! Trying to fix
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
        num_neurons = len(numpy.unique(neurons))
        print "num_neurons " + str(num_neurons)
        heights = 1000 * n / (hist_binwidth * num_neurons)
        print "t_bins " + str(len(t_bins)) + "\n" + str(t_bins) + "\n" + \
               "height " + str(len(heights)) + "\n" + str(heights) + "\n"
        #bar(left,height, width=0.8, bottom=None, hold=None, **kwargs):
        pylab.bar(t_bins, heights, width=hist_binwidth, color=color_bar, edgecolor=color_edge)
        pylab.yticks([int(a) for a in numpy.linspace(0.0, int(max(heights) * 1.1) + 5, 4)])
        pylab.ylabel("Rate (Hz)")
        pylab.xlabel("Time (ms)")
        pylab.xlim(xlim)
        pylab.axes(ax1)
    else:
        pylab.plot(ts, gids, color_marker)
        pylab.xlabel("Time (ms)")
        pylab.ylabel(ylabel)

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



block = [filename for filename in os.listdir(path) if filename[0] == "@"]

listing = []


def plotting():
    from pyqtgraph.Qt import QtGui, QtCore
    import pyqtgraph as pg

    ts = listing[0]
    gids = listing[1]

    #QtGui.QApplication.setGraphicsSystem('raster')
    app = QtGui.QApplication([])
    #mw = QtGui.QMainWindow()
    #mw.resize(800,800)
    # Enable antialiasing for prettier plots
    pg.setConfigOptions(antialias=True)

    win = pg.GraphicsWindow(title="Basic plotting examples")
    win.resize(1000,600)
    win.setWindowTitle('pyqtgraph example: Plotting')

    p4 = win.addPlot(title="Parametric, grid enabled")
    p4.plot(ts, gids)
    p4.showGrid(x=True, y=True)

    ## Start Qt event loop unless running in interactive mode or using pyside.
    if __name__ == '__main__':
        import sys
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            QtGui.QApplication.instance().exec_()


for filename in block:
    x_vals = []
    y_vals = []

    if filename.startswith('@spikes'):
        with open(path + filename, 'r') as f:
            header = f.readline()
            log = list( v.strip() for k, v in (item.split(':') for item in header.split(',')) )
            for line in f:
                x, y = line.split()
                x_vals.append(x)
                y_vals.append(y)
        spike_make_diagram(x_vals, y_vals, log[0], log[1], log[2])
    else:
        with open(path + filename, 'r') as f:
            header = f.readline()
            log = list( v.strip() for k, v in (item.split(':') for item in header.split(',')) )
            for line in f:
                x, y = line.split()
                x_vals.append(x)
                y_vals.append(y)
        voltage_make_diagram(x_vals, y_vals, log[0], log[1])

    print filename + " diagram created"
