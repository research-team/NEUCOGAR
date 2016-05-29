import os
import re
import sys
import numpy as np
path = "/home/alex/merged/"
block = sorted([filename for filename in os.listdir(path) if filename.startswith("@spikes_")])
heatmap = []
T = 1000.
for filename in block:
    data = {}
    with open(path + filename, 'r') as f:
        f.readline()
        for line in f:
            temp = line.split(":")
            time = int(float(temp[0]))
            num = int(temp[1])
            if data.get(time) is None:
                data[time] = num
            else:
                data[time] += num

    for i in np.arange(0, int(T), 1):
        if data.get(i) is None:
            data[i] = 0
    heatmap.append(data)

import matplotlib.pyplot as plt

data = [part.values() for part in heatmap]

plt.xlabel("Time in ms")
plt.ylabel("Part of brain")

ax = plt.gca()
ax.set_yticks(range(len(block)))
ax.set_yticklabels(item[8:-4] for item in block)

plt.imshow(data, aspect='auto', interpolation='none', cmap="hot")
plt.show()