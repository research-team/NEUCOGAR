__author__ = "Alexey Panzer"
__version__ = "2.0.1"
__tested___ = "13.11.2017 NEST 2.12.0 Python 3"

import os
import sys
import numpy
import pylab
from collections import defaultdict
from neucogar import api_globals

logger = api_globals.log.getLogger('api_diagrams')


def __create_result_dir(txt_path):
	# Create dir of img results
	if not os.path.exists(txt_path + "/img"):
		os.makedirs(txt_path + "/img")


def BuildSpikeDiagrams(results_folder=None, hist_binwidth=5.0):
	"""
	Function for building spike diagrams

	Args:
		results_folder (str or None): Will str if use api_diagrams as independent script
		hist_binwidth:
	"""

	# Set txt results of simulation from standard data path
	if results_folder is None:
		results_folder = api_globals.NEST.GetKernelStatus()['data_path']
	# Create folder if not exists
	__create_result_dir(results_folder)
	# Get list of .gdf files
	spike_files = sorted([name for name in os.listdir(results_folder) if name.endswith(".gdf")])

	logger.info("scan folder for '.gdf'... {0} {1}".format(len(spike_files),
	                                                       "OK" if spike_files else "No .gdf fiels!"))
	# Exit if no files
	if not spike_files:
		return

	logger.info("results path is '{}/img'".format(results_folder))

	for spike_file in spike_files:
		gids = list()   # Neurons Global ID list
		times = list()  # Spikes time list
		file_path = "{0}/{1}".format(results_folder, spike_file)
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
			err_msg = __make_spikes_diagram(times, gids, spike_file, results_folder, hist_binwidth)
		else:
			err_msg = "ERROR. File is empty (no recorded data)"
		logger.info("{0}... {1}".format(spike_file, err_msg))
	#logger.info("Successfully created {0}/{1}\n".format(successed, len(files_gdf)))


def BuildVoltageDiagrams(results_folder=None):
	"""
	Function for building voltage diagrams

	:param results_folder:
	:return:
	"""

	# Set txt results of simulation from standard data path
	if results_folder is None:
		results_folder = api_globals.NEST.GetKernelStatus()['data_path']
	# Create folder if not exists
	__create_result_dir(results_folder)
	# Get list of .gdf files
	files_dat = sorted([name for name in os.listdir(results_folder) if name.endswith(".dat")])

	logger.info("scan folder for '.gdf'... {0} {1}".format(len(spike_files),
	                                                       "OK" if spike_files else "No .gdf fiels!"))
	# Exit if no files
	if not spike_files:
		return

	logger.info("results path is '{}/img'".format(results_folder))

	for voltage_file in files_dat:
		broken = 0
		meta = voltage_file.split('-')
		times = defaultdict(list)
		voltages = defaultdict(list)
		file_path = "{0}/{1}".format(results_folder, spike_file)
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
			err_msg = __make_voltage_diagram(times, gids, spike_file, results_folder, hist_binwidth)
		else:
			err_msg = "ERROR. File is empty (no recorded data)"
		logger.info("{0}... {1}".format(spike_file, err_msg))
	#logger.info("Successfully created {0}/{1}\n".format(successed, len(files_gdf)))


def Heatmap(txt_path=None):
	"""

	:param txt_path:
	:return:
	"""
	__create_result_dir(txt_path)
	raise NotImplementedError


def BuildWeightDiagrams(txt_path=None):
	"""
	Function for building weight diagrams

	:param txt_path:
	:return:
	"""

	__create_result_dir(txt_path)

	files_csv = sorted([fl for fl in os.listdir(txt_path) if fl.endswith(".csv")])

	logger.info("scan folder for '.csv'... {0} {1}".format(len(files_csv), "OK" if files_csv else "ERROR"))

	if len(files_csv) == 0:
		return

	logger.info("results path '/img'")

	connectome = defaultdict(list)
	# collect all .csv files
	for filename in files_csv:
		with open("{0}/{1}".format(txt_path, filename), 'r') as f:
			for line in f:
				# split data by space. source GID
				data = line.split()
				# (src, dest) : (time, weight)
				connectome[(data[0], data[1])].append((data[2], data[3]))

	if len(connectome) == 0:
		err_msg = "ERROR. No recorded data"
	else:
		err_msg = __make_weight_diagram(connectome, txt_path)
	logger.info("{0}... {1}".format("TEST_CHANGE_ME", err_msg))

	logger.info("Successfully created {} \n".format(sys.getsizeof(connectome), "bytes"))


def __make_weight_diagram(conn_dict, txt_path):
	"""

	:return:
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

	return "OK"


def __make_spikes_diagram(times, gids, file_name, txt_path, hist_binwidth):
	"""
	Draw spike diagram

	:param times: spike times
	:param gids: neuron global IDs
	:param file_name: name of the file with spikes data
	:param txt_path: result folder
	:param hist_binwidth: width of one bin in milliseconds
	:return:
	"""
	color_marker = '.'      # spike marker (dots)
	bar_color = 'green'     # bar color
	border_color = '#0f1c16'  # border color
	simulation_time = api_globals.NEST.GetKernelStatus()['time']
	title = file_name.split(".")[0]

	# Common figure
	pylab.figure()
	location = pylab.axes([0.1, 0.3, 0.85, 0.6])
	# Plotting spikes dots
	pylab.plot(times, gids, color_marker)
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
		return "t_bins for {0} is empty".format(file_name)
	# Get bins
	# n -  is the number of counts in each bin of the histogram
	# bins - is the left hand edge of each bin
	n, bins = pylab.histogram(times, bins=t_bins)
	# Check
	if len(n) == 0:
		pylab.close()
		return "bins for {0} is empty".format(file_name)
	# Get neuron numbers by unique gids
	num_neurons = len(numpy.unique(gids))
	# Recalculate heights of bins to show rate in Hz of spiking
	heights = (1000 * n / (hist_binwidth * num_neurons))
	# Draw the bar
	pylab.bar(bins[:-1], heights, width=hist_binwidth, color=bar_color, edgecolor=border_color)
	yticks = numpy.linspace(start=0, stop=max(heights), num=5)
	pylab.yticks([ int(a) for a in yticks ])
	pylab.ylabel("Rate (Hz)")
	pylab.xlabel("Time (ms)")
	pylab.grid(True)
	pylab.axes(location)
	pylab.title(title)
	pylab.xlim([0, simulation_time])
	pylab.draw()
	pylab.savefig("{0}/img/{1}.png".format(txt_path, title), dpi=120, format='png')
	pylab.close()
	return "OK"


def __make_voltage_diagram(times, voltages, name, path):
	"""
	Draw voltage diagram

	Description:
		Set parameters, include data, draw and save

	Args:
		times   (list, dict): time data of neuron (if list) and neurons (if dict)
		voltages (list, dict): voltage data of neuron (if list) and neurons (if dict)
		name			(str): name of brain part
		path			(str): path to save results
	"""
	global successed

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
	pylab.title(name)
	pylab.grid(True)
	pylab.draw()
	pylab.savefig("{0}/img/{1}.png".format(path, name), dpi=120, format='png')
	pylab.close()

	successed += 1
	return "OK"


# As independent script
if __name__ == '__main__':
	# folder = input("Enter path to the results: ")
	txt_folder = '/home/alex/GitHub/NEUCOGAR/NEST/lib/example/txt/'
	# txt_folder = '/home/alex/350K-126/txt/'
	img_folder = "{}/img".format(txt_folder)
	if not os.path.exists(img_folder):
		os.mkdir(img_folder)

	BuildSpikeDiagrams(txt_folder)
	BuildVoltageDiagrams(txt_folder)
	BuildWeightDiagrams(txt_folder)
