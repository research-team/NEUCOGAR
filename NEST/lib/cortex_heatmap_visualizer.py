__author__  = "Alexey Panzer"
__version__ = "1.1.1"
__tested___ = "14.08.2017 NEST 2.12.0 Python 3"

import os
import re
import sys
import string
import numpy as np
import os.path as fs
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backend_bases import NavigationToolbar2

time_simulation = 1000
delta_t = 10
total_interval_num = time_simulation / delta_t

iteration = 0
heatmap_full_data = {}
max_spike_num = 0
fig = None

forward = NavigationToolbar2.forward
back = NavigationToolbar2.back


def forward_btn(self):
    """
    aaaa

    Description:
        aaaa

    Args:
        self
    """
    global iteration
    if 0 <= iteration < total_interval_num:
        iteration += 1
        print(iteration)
        forward(self)
        plt.gcf().clear()
        heatmap_builder(iteration, width_x=5)


def back_btn(self):
    """
    aaaa

    Description:
        aaaa

    Args:
        self
    """
    global iteration
    if 0 <= iteration < total_interval_num:
        iteration -= 1
        print(iteration)
        back(self)
        plt.gcf().clear()
        heatmap_builder(iteration, width_x=5)


def init_heatmap_data(dt=10):
    """

    :param dt:
    :return:
    """
    global heatmap_full_data

    result_path = "/home/alex/GitHub/NEUCOGAR/NEST/cube/dopamine/integrated/results/300K/txt/"

    # merge results
    for spikes_file_name in sorted(set([name[:name.rfind("-")] for name in os.listdir(result_path) if name.endswith(".gdf")])):
        # spikes - name - column - thread .gdf
        column_index = spikes_file_name.split('-')[1]
        # list of times when was a spike
        spike_times = []
        # take data of the same files of the brain part, but another thread
        for file_to_merge in [filename for filename in os.listdir(result_path) if
                              filename.startswith(spikes_file_name) and filename.endswith(".gdf")]:
            # if file is not empty then take the data
            if os.stat("{0}/{1}".format(result_path, file_to_merge)).st_size > 0:
                with open("{0}/{1}".format(result_path, file_to_merge), 'r') as f:
                    for line in f:
                        spike_times.append(int(float(line.split("\t")[1]) * 10))
        # if no recorded data
        if len(spike_times) == 0:
            heatmap_full_data[column_index] = 0
        else:
            heatmap_full_data[column_index] = sorted(spike_times)
        del spike_times
    __collapse_data(dt)


def __collapse_data(dt):
    """

    :param dt:
    :param width:
    :return:
    """
    global max_spike_num

    dt *= 10    # correlate dt (without floating comma)
    print("==================================")
    for column_number, data in heatmap_full_data.items():
        print(column_number, data)

        # If data is empty (equal 0) then fill by zeros
        if type(data) is int:
            heatmap_full_data[column_number] = [0 for _ in range(total_interval_num)]
        # Else fill list by interval
        else:
            spikes_for_interval = [0 for _ in range(total_interval_num)]
            end_interval_value = dt - 1
            interval_index = 0
            data_index = 0

            while interval_index < total_interval_num - 1 and data_index != len(data):
                if data[data_index] <= end_interval_value:
                    spikes_for_interval[interval_index] += 1
                    data_index += 1
                else:
                    end_interval_value += dt
                    interval_index += 1
            heatmap_full_data[column_number] = spikes_for_interval

            # Find maximum number of spikes
            local_max_spike_num = max(spikes_for_interval)
            if local_max_spike_num > max_spike_num:
                max_spike_num = local_max_spike_num
            # Delete
            del spikes_for_interval

    print("============= A F T E R =====================")
    print('      ', end='')
    for i in range(total_interval_num):
        print("{0:<4}".format(i), end=' ')
    print()

    # After collapsing
    for column_number, data in sorted(heatmap_full_data.items()):
        print (column_number, end=' ')
        for elem in data:
            print("{0:<4}".format(elem), end=' ')
        print()


colorbar = None
one = True
def heatmap_builder(interval_index, width_x=5):
    """

    :param folder:
    :param value:
    :param dt:
    :param isColumn:
    :return:
    """
    global max_spike_num
    global colorbar
    global fig
    global one
    line_values = []  # one line of heatmap
    heatmap_for_gui = []

    # Gather data from all columns by specific interval
    for i, column in enumerate(heatmap_full_data):
        # Add element at interval_index position
        line_values.append(heatmap_full_data[column][interval_index])
        # If next index element is bigger than width
        if (i+1) % width_x == 0:
            # Add this one for the heatmap list of lists
            heatmap_for_gui.append(line_values)
            # Clear list
            line_values = []
    print(heatmap_for_gui)

    # Init the figure
    sns.set()
    # Set titles in figure
    plt.title("Interval [{0}, {1}]. The {2} of {3}".format(interval_index * delta_t,
                                                           delta_t * (interval_index + 1),
                                                           interval_index + 1,
                                                           total_interval_num))
    # Create the figure
    af = sns.heatmap(heatmap_for_gui, annot=True, yticklabels='ABC', fmt="d", cmap='hot', vmin=0, vmax=max_spike_num)
    af.set_yticklabels('ABCDEFG', rotation=0)


    # Set a 11 values (with zero) to the colorbar
    full_bar_ticks = range(max_spike_num + 1)
    bar_ticks = len(full_bar_ticks) / 10

    # Add the ONE colorbar if it isn't exists
    if colorbar is None:
        colorbar = af.collections[0].colorbar
        colorbar.set_ticks(full_bar_ticks[::2] if bar_ticks <= 1 else full_bar_ticks[::bar_ticks])
    # Draw the picture
    fig.canvas.draw()
    # Delete
    del full_bar_ticks, af



if __name__ == '__main__':
    # Set event listener
    NavigationToolbar2.forward = forward_btn
    NavigationToolbar2.back = back_btn

    # Create figure
    fig = plt.figure()
    #plt.ion()

    # Init heatmap
    init_heatmap_data(dt=delta_t)
    heatmap_builder(0, width_x=5)

    # Show plot
    plt.show(block=True)
