import nest

save_path = "output-text/"

def save_spikes(detec, name, hist=False):
    if not nest.GetStatus(detec)[0]["model"] == "spike_detector":
        raise nest.NESTError("Please provide a spike_detector.")
    if nest.GetStatus(detec, "to_memory")[0]:
        ev = nest.GetStatus(detec, "events")[0]
        ts = ev["times"]
        gids = ev["senders"]
        if not len(ts):
            raise nest.NESTError("No events recorded!")
        title = "Raster plot from device '%i'" % detec[0]
        xlabel = "Time (ms)"

        #write to file
        flag = "True" if hist else "False"
        output = open(save_path + "@spikes_" + name + ".txt", 'wb')
        for elem in ts:
            output.write(str(elem) + " ")
        output.write("@@@")
        for elem in gids:
            output.write(str(elem) + " ")
        output.write("@@@" + title + "@@@" + xlabel + "@@@" + flag)
        output.close()
    else:
        raise nest.NESTError("No data to plot. Make sure that either to_memory or to_file are set.")

def save_voltage(detec, name):
    if len(detec) > 1:
        raise nest.NESTError("Please provide a single voltmeter.")
    if not nest.GetStatus(detec)[0]['model'] in ('voltmeter', 'multimeter'):
        raise nest.NESTError("Please provide a voltmeter or a multimeter measuring V_m.")
    elif nest.GetStatus(detec)[0]['model'] == 'multimeter':
        if not "V_m" in nest.GetStatus(detec, "record_from")[0]:
            raise nest.NESTError("Please provide a multimeter measuring V_m.")
        elif (not nest.GetStatus(detec, "to_memory")[0] and
              len(nest.GetStatus(detec, "record_from")[0]) > 1):
            raise nest.NESTError("Please provide a multimeter measuring only V_m or record to memory!")
    if nest.GetStatus(detec, "to_memory")[0]:
        ev = nest.GetStatus(detec)[0]
        output = open(save_path + "@voltage_" + name + ".txt", 'wb')
        times = ev["events"]["times"]
        voltages = ev["events"]["V_m"]
        for elem in times:
            output.write(str(elem) + " ")
        output.write("@@@")
        for elem in voltages:
            output.write(str(elem) + " ")
        output.close()
    else:
        raise nest.NESTError("Provided devices neither records to file, nor to memory.")
