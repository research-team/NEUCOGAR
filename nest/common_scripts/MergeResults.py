import os
import re
import sys
from collections import defaultdict

path = sys.argv(0)
print path
block = [filename for filename in os.listdir(path) if filename[0] == "@"]

for filename in block:
    print filename
    data = defaultdict(list)
    header = ""
    if filename.startswith('@spikes'):
        with open(path + filename, 'r') as f:
            header = f.readline()
            for line in f:
                if re.match(" *\d", line):
                    time = float(re.search('\d+\.\d', line).group(0))
                    neurons = re.search("\[[\d, ]+\]", line).group(0).translate(None, ''.join(['[',']']))
                    for s in neurons.split(','):
                        data[time].append(int(s))
        with open(path + filename, 'w') as f:
            f.write(header)
            for key in data:
                f.write("{0:>5} {1:>4} : {2}\n".format(key, len(data[key]), sorted(data[key])))
    else:
        print "@voltage not implemented"