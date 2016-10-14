import os
import re
import sys
import numpy as np
import matplotlib.pyplot as plt


path = "/home/artem/PycharmProjects/untitled/txt/"
time_simulation = 1000.
heatmap = []
temp = []
test = []


files = sorted([filename for filename in os.listdir(path) if filename.startswith("@spikes_")])

for filename in files:
    data_file = {}
    with open(path + filename, 'r') as f:
        f.readline()
        for line in f:
            temp = line.split(":")
            time = int(float(temp[0]))
            num = int(temp[1])
            if data_file.get(time) is None:
                data_file[time] = num
            else:
                data_file[time] += num

    for i in np.arange(0, int(time_simulation), 1):
        if data_file.get(i) is None:
            data_file[i] = 0
    heatmap.append(data_file)

data = [part.values() for part in heatmap]
plt.xlabel("Time in ms")
plt.ylabel("Part of brain")
ax = plt.gca()
ax.set_yticks(range(len(files)))

for item in files:
    test.append(item[8:-4])

ax.set_yticklabels(test)

#ax.set_yticklabels(item[8:-4] for item in files)
plt.imshow(data, aspect='auto', interpolation='none', cmap="hot")
plt.colorbar()
plt.show()