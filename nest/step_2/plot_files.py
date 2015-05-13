import nest.tests.test_connect_all_patterns


setattr(io,'HAVE_TABLEIO', False)
data_file = signals.NestFile(sd_folder_name + sd_filename, with_time=True)
# dims - dimension, it is 1 because there is no topology in connection.
spikes = signals.load_spikelist(data_file, dims=1, id_list=list(cortex))
spikes.raster_plot()  # read help spikes.raster_plot
spikes.mean_rates()