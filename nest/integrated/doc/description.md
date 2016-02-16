
#### 1. Initializing neurons
#### 2. Connection of neurons
#### 3. Connection of devices
#### 4. Simulating


### Initializing neurons

text text text


### Connection of neurons
```python
# standard connection is GABA and weight coefficient is 1
def connect(part_from, part_to, syn_type=GABA, weight_coef=1):
	# from synases dict handle to 'syn_type' tuple, then to 'synparams' and 'weight' 
	# include result of multiplying standard synapse weight and coefficient
	types[syn_type][0]['weight'] = weight_coef * types[syn_type][1]
	# variable with parameters of synapse (another for dopamine)
	syn = types[syn_type][3] if syn_type in (DA_ex, DA_in) else types[syn_type][0]
	# connect two parts, include rules of connections and parameters of synapse
	nest.Connect(part_from, part_to, conn_spec=conn_dict, syn_spec=syn)
	# logging actions (from, to, type, weight)
	log_conn(part_from, part_to, types[syn_type][2], types[syn_type][0]['weight'])  
```
Dict of synapses
```python
#		 key	 synapse parameters   weight    name
types = {GABA:  (STDP_synparams_GABA, w_GABA,  'GABA'),
		 ACh:   (STDP_synparams_ACh,  w_ACh,   'Ach'),
		 Glu:   (STDP_synparams_Glu,  w_Glu,   'Glu'),
		 DA_ex: (DOPA_synparams_ex,   w_DA_ex, 'DA_ex', dopa_model_ex),
		 DA_in: (DOPA_synparams_in,   w_DA_in, 'DA_in', dopa_model_in)}
```
Keys of synapse types
```
GABA = 0
Glu = 1
ACh = 2
DA_ex = 3
DA_in = 4
```
---

### Connection of devices
#### 1. Spike detector
```python
def connect_detector(part):
	# took name of this part
    name = parts_dict[part]
    # if neuron number smaller than N_rec use all neurons 
    # in standard N_rec = 100
    number = len(part) if len(part) < N_rec else N_rec
    # append new detector to the dict (Name:Device) with parameters
    spikedetectors[name] = nest.Create('spike_detector', params=detector_param)
    # attaching spikedetector to the first N_rec neurons
    nest.Connect(part[:number], spikedetectors[name])
    # logging action
    logger.debug("Detector => {0}. Tracing {1} neurons".format(name, number))
```
Detecrtor parameters
```python
detector_param = {'label': 'spikes', 		# add label name
				  'withtime': True, 		# add time 
				  'withgid': True, 			# add spike gid
				  'to_file': False, 		# not save to file
				  'to_memory': True,		# write to memory
				  'scientific': True}		# ???
```
---
#### 2. Multimeter
```python
def connect_multimeter(part):
	# took name of this part
	name = parts_dict[part]
	# append new multimeter to the dict (Name:Device) with parameters
    multimeters[name] = nest.Create('multimeter', params=mm_param)
    # attaching multimeter to the first neuron
    nest.Connect(multimeters[name], (part[0],))
    logger.debug("Multimeter => {0}. On {1}".format(name, part[0]))
```
Multimeter parameters
```python
mm_param = {'to_memory': True,			# save to memory
			'to_file': False, 			# save not to file
            'withtime': True, 			# add time
            'interval': 0.1,			# use interval 0.1ms
            'record_from': ['V_m'], 	# record voltage [mV]
            'withgid': True}			# add gid
```
---
#### 3. Generator
```python
def connect_generator(part, startTime=1, stopTime=T, rate=250, coef_part=1):
    # took name of this part
    name = parts_dict[part]
    # copy to the 'gen_static_syn' standard parameters of 'static_synapse' and add new property
    nest.CopyModel('static_synapse',    # origin model
                    gen_static_syn,     # new model
                    {'weight': weight,	# weight of the synapse
                    'delay': pg_delay})	# delay of transmiting a signal
    # append new generator to the dict (Name:Device) with parameters
    # in this experiment was used 'poisson_generator'
    spikegenerators[name] = nest.Create('poisson_generator', 		  # type of generator
                                        1,                            # number of generators
                                        {'rate': float(rate),         # rate of spiking
                                         'start': float(startTime),   # start spiking(ms)
                                         'stop': float(stopTime)})    # stop spiking(ms)
    # attaching generator to the every neuron in  part
    nest.Connect(spikegenerators[name],                               # generator
                 part,                                                # part to connect
                 syn_spec=gener_static_syn,                           # synapse parameters
                 conn_spec={'rule': 'fixed_outdegree',                # connection rules
                            'outdegree': int(len(part) * coef_part)}) # number of connections
    logger.debug("Generator => {0}. Element #{1}".format(name, spikegenerators[name][0]))
```
The following devices generate sequences of spikes which can be send to a neuron. These devices act like populations of neurons and connected to their targets like a neuron.
##### 3.1 poisson_generator 
> Simulate neuron firing with Poisson processes statistics.

The poisson_generator simulates a neuron that is firing with Poisson statistics, i.e. exponentially distributed interspike intervals. It will generate a *unique* spike train for each of it's targets |Generates spike-events from an array.|Device to produce Gaussian spike-trains.
*Parameters*

| parameter | type 		| description 											|
|-----------|-----------|-------------------------------------------------------|
|rate 		|(double)	|mean firing rate in Hz  								|
|origin		|(double)	|Time origin for device timer in ms						|
|star		|(double)	|begin of device application with resp. to origin in ms |
|stop		|(double)	|end of device application with resp. to origin in ms	|

 
##### 3.2 spike_generator
> A device which generates spikes from an array with spike-times.

##### 3.3 noise_generator
> Device to generate Gaussian white noise current.

##### 3.3 pulsepacket_generator
> Generate sequence of Gaussian pulse packets.

---
