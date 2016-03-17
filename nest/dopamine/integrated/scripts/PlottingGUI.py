import numpy
import pylab
import os

import pyqtgraph.examples
pyqtgraph.examples.run()

#TODO change directory
path = "/home/alex/Desktop/test/"

block = [filename for filename in os.listdir(path) if filename[0] == "@"]

listing = []
title = []

def plotting():
    from pyqtgraph.Qt import QtGui, QtCore
    import pyqtgraph as pg

    app = QtGui.QApplication([])

    pg.setConfigOptions(antialias=True)

    win = pg.GraphicsWindow(title="examples")
    win.resize(1000,600)
    win.setWindowTitle('Plotting')

    a = win.addPlot(title=title[0][6:title[0].find(',')])
    a.plot(listing[0], listing[1])
    a.showGrid(x=True, y=True)

    for i in range(2, len(listing), 2):
        print i
        if i % 3 == 0:
            win.nextRow()
        p1 = win.addPlot(title=title[i/ 2][6:title[i/2].find(',')])
        p1.plot(listing[i], listing[i + 1])
        p1.showGrid(x=True, y=True)
        p1.setXLink(a)
        p1.setYLink(a)

    if __name__ == '__main__':
        import sys
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            QtGui.QApplication.instance().exec_()

for filename in block:
    x = []
    y = []

    if filename.startswith('@spikes'):           #find("spikes") != -1:
        inFile = open(path + filename, 'rb')
        inFile.close()
        '''
        x_vals = [float(x) for x in mas[0].split()]
        y_vals = [int(y) for y in mas[1].split()]
        #clearName = filename[1:filename.find(".txt")]
        #make_diagram(ts, gids, hist, title, xlabel, name):
        #spike_make_diagram(x_vals, y_vals, mas[4], mas[2], clearName)'''
    else:
        with open(path + filename, 'r') as f:
            title.append(f.readline())
            for line in f:
                x_val, y_val = line.split()
                x.append(float(x_val))
                y.append(float(y_val))
            listing.append(x)
            listing.append(y)
plotting()