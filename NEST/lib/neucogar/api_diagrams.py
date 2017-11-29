__author__ = "Alexey Panzer"
__version__ = "2.0.3"
__tested___ = "27.11.2017 NEST 2.12.0 Python 3"

import os
import sys
import time
import numpy
import pylab
from collections import defaultdict
import neucogar.api_kernel as api

logger = api.log.getLogger('api_diagrams')

def __create_result_dir(results_dir):
	# Create dir of img results
	if not os.path.exists(results_dir + "/img"):
		os.makedirs(results_dir + "/img")


def BuildSpikeDiagrams(results_dir=None, hist_binwidth=5.0):
	"""
	Function for building spike diagrams

	Args:
		results_dir (str or None): Will str if use api_diagrams as independent script
		hist_binwidth:
	"""
	# Set txt results of simulation from standard data path
	if results_dir is None:
		results_dir = api.NEST.GetKernelStatus()['data_path']
	# Create folder if not exists
	__create_result_dir(results_dir)
	# Get list of *.gdf files
	spike_files = sorted([name for name in os.listdir(results_dir) if name.endswith(".gdf")])
	# Show info about number of founded files
	logger.info("scan folder for '.gdf'... {0} {1}".format(
		len(spike_files),
		"OK" if spike_files else "No *.gdf files!"))
	# Exit if no files
	if not spike_files:
		return
	logger.info("results path is '{}/img'".format(results_dir))
	# Draw all spike files
	for spike_file in spike_files:
		gids = list()   # Neurons Global ID list
		times = list()  # Spikes time list
		file_path = "{0}/{1}".format(results_dir, spike_file)
		# if file is not empty take data
		if os.stat(file_path).st_size > 0:
			with open(file_path, 'r') as f:
				for line in f:
					# Split data by whitespace (GID, time)
					data = line.split()
					# If line is not broken by threads
					if len(data) == 2:
						gids.append(int(data[0]))
						times.append(float(data[1]))
			# Run diagram builder with these data
			out_msg = __make_spikes_diagram(times, gids, spike_file, results_dir, hist_binwidth)
		else:
			out_msg = "File is empty (no recorded data)"

		logger.info("{0}...{1}".format(spike_file, out_msg))
	logger.info("FINISHED")


def BuildVoltageDiagrams(results_dir=None):
	"""
	Function for building voltage diagrams

	Args:
		results_dir (str or None): path to the result follder
	"""
	# Set txt results of simulation from standard data path
	if results_dir is None:
		results_dir = api.NEST.GetKernelStatus()['data_path']
	# Create folder if not exists
	__create_result_dir(results_dir)
	# Get list of *.dat files
	files_dat = sorted([name for name in os.listdir(results_dir) if name.endswith(".dat")])
	# Show info about number of founded files
	logger.info("scan folder for '.gdf'... {0} {1}".format(
		len(files_dat),
	    "OK" if files_dat else "No .dat fiels!"))
	# Exit if no files
	if not files_dat:
		return
	logger.info("results path is '{}/img'".format(results_dir))
	for voltage_file in files_dat:
		broken = 0
		times = defaultdict(list)
		voltages = defaultdict(list)
		file_path = "{0}/{1}".format(results_dir, voltage_file)
		# if file is not empty take data
		if os.stat(file_path).st_size > 0:
			with open(file_path, 'r') as f:
				for line in f:
					# split by whitespace: gid time voltage
					data = line.split()
					if len(data) == 3:
						times[data[0]].append(float(data[1]))
						voltages[data[0]].append(float(data[2]))
					else:
						broken += 1
			# Run diagram builder with these data
			out_msg = __make_voltage_diagram(dict(times), dict(voltages), voltage_file, results_dir)
		else:
			out_msg = "File is empty (no recorded data)"
		logger.info("{0}... {1}".format(voltage_file, out_msg))
	logger.info("FINISHED")


def Heatmap(results_dir=None):
	"""
	Args:
		results_dir:
	"""
	# Set txt results of simulation from standard data path
	if results_dir is None:
		results_dir = api.NEST.GetKernelStatus()['data_path']
	# Create folder if not exists
	__create_result_dir(results_dir)

	raise NotImplementedError


def BuildWeightDiagrams(results_dir=None):
	"""
	Function for building weight diagrams

	Args:
		results_dir:
	"""
	# Set txt results of simulation from standard data path
	if results_dir is None:
		results_dir = api.NEST.GetKernelStatus()['data_path']
	# Create folder if not exists
	__create_result_dir(results_dir)
	# Get list of *.csv files
	files_csv = sorted([name for name in os.listdir(results_dir) if name.endswith(".csv")])
	# Show info about number of founded files
	logger.info("scan folder for '.csv'... {0} {1}".format(
		len(files_csv),
		"OK" if files_csv else "ERROR"))
	# Exit if no files
	if not files_csv:
		return 'ERROR'
	logger.info("results path is '{}/img'".format(results_dir))

	connectome = defaultdict(list)
	# collect all .csv files
	# if file is not empty take data
	for weight_file in files_csv:
		file_path = "{0}/{1}".format(results_dir, voltage_file)
		if os.stat(file_path).st_size > 0:
			with open("{0}/{1}".format(results_dir, weight_file), 'r') as file:
				for line in file:
					# split data by space. source GID
					data = line.split()
					# (src, dest) : (time, weight)
					connectome[(data[0], data[1])].append((data[2], data[3]))
			if len(connectome) == 0:
				logger.info("ERROR. No recorded data")
			else:
				__make_weight_diagram(connectome, results_dir)
		else:
			logger.info("ERROR. File is empty (no recorded data)")
		logger.info("{0}... ".format(weight_file))


def __make_weight_diagram(conn_dict, txt_path):
	"""
	Args:
		conn_dict (dict):
		txt_path (str):
	"""

	fig = pylab.figure()
	fig.suptitle("STDP")
	pylab.xlabel("Time (ms)")
	pylab.ylabel("Weight")

	for conn in list(conn_dict)[:10]:
		times = [data[0] for data in conn_dict[conn]]
		weights = [data[1] for data in conn_dict[conn]]
		pylab.plot(times, weights, label="{}".format(conn))
		pylab.draw()

	pylab.legend(loc='upper left')
	pylab.savefig("{0}/img/{1}.png".format(txt_path, "STDP_weights"), figsize=(10, 6), dpi=120, format='png')
	pylab.close()



def __make_spikes_diagram(times, gids, file_name, results_dir, hist_binwidth):
	"""
	Draw spike diagram

	Args:
		times (list): spike times
		gids (list): neuron global IDs
		file_name (str): name of the file with spikes data
		results_dir (str): result folder
		hist_binwidth (float): width of one bin in milliseconds
	"""
	bar_color = 'green'         # bar color
	border_color = '#0f1c16'    # border color
	simulation_time = api.NEST.GetKernelStatus()['time']
	title = file_name.split(".")[0]

	# create big-expensive-figure
	pylab.ioff()  # turn updates off
	pylab.figure()
	time.sleep(1.5)
	location = pylab.axes([0.1, 0.3, 0.85, 0.6])
	# Plotting spikes dots
	pylab.plot(times, gids, '.')
	pylab.ylabel("Neuron ID")
	pylab.xticks([])
	pylab.axes([0.1, 0.1, 0.85, 0.17])
	pylab.xlim([0, simulation_time])
	# Figure of spikes
	t_bins = numpy.arange(start=numpy.amin(times),
	                      stop=numpy.amax(times) + 2 * hist_binwidth,
	                      step=hist_binwidth)
	if len(t_bins) == 0:
		pylab.close()
		return 'len(t_bins) = 0'
	# Get bins
	# n -  is the number of counts in each bin of the histogram
	# bins - is the left hand edge of each bin
	n, bins = pylab.histogram(times, bins=t_bins)
	# Check
	if len(n) == 0:
		pylab.close()
		return 'len(n) = 0'
	# Get neuron numbers by unique gids
	num_neurons = len(numpy.unique(gids))
	# Recalculate heights of bins to show rate in Hz of spiking
	heights = (1000 * n / (hist_binwidth * num_neurons))
	# Draw the bar
	pylab.bar(bins[:-1], heights, width=hist_binwidth, color=bar_color, edgecolor=border_color)
	yticks = numpy.linspace(start=0, stop=max(heights), num=5)
	pylab.yticks([int(a) for a in yticks])
	pylab.ylabel("Rate (Hz)")
	pylab.xlabel("Time (ms)")
	pylab.grid(True)
	pylab.axes(location)
	pylab.title(title)
	pylab.xlim([0, simulation_time])
	pylab.draw()
	pylab.savefig("{0}/img/spikes_{1}.png".format(results_dir, title), dpi=120, format='png')
	return 'OK'

def __make_voltage_diagram(times, voltages, name, path):
	"""
	Draw voltage diagram

	Args:
		times (dict): time data of neuron (if list) and neurons (if dict)
		voltages (dict): voltage data of neuron (if list) and neurons (if dict)
		name (str): name of brain part
		path (str): path to save results
	"""
	title = file_name.split(".")[0]

	pylab.ioff()  # turn updates off
	pylab.figure()
	time.sleep(1.5)
	for key in times:
		pylab.plot(times[key], voltages[key], "", label=key)
	pylab.ylabel("Membrane potential (mV)")
	pylab.xlabel("Time (ms)")
	pylab.legend(loc="best")
	pylab.title(name)
	pylab.grid(True)
	pylab.draw()
	pylab.savefig("{0}/img/voltage_{1}.png".format(path, name), dpi=120, format='png')
	return 'OK'

# As independent script
if __name__ == '__main__':
	folder = input("Enter path to the results: ")
	img_folder = "{}/img".format(folder)

	if not os.path.exists(img_folder):
		os.mkdir(img_folder)

	BuildSpikeDiagrams(folder)
	BuildVoltageDiagrams(folder)
	BuildWeightDiagrams(folder)
