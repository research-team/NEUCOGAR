
#### 1. Initializing neurons
#### 2. Connection of neurons
#### 3. Connection of devices
#### 4. Simulating


### Initializing neurons

text text text



[one-to-one]: http://www.nest-simulator.org/wp-content/uploads/2014/12/One_to_one.png
[all-to-all]: http://www.nest-simulator.org/wp-content/uploads/2014/12/All_to_all.png
[fixed-indegree]: http://www.nest-simulator.org/wp-content/uploads/2014/12/Fixed_indegree.png
[fixed-outdegree]: http://www.nest-simulator.org/wp-content/uploads/2014/12/Fixed_outdegree.png
[receptor-type]: http://www.nest-simulator.org/wp-content/uploads/2014/12/Receptor_types.png

### Connection of neurons

Connection rules are specified using the conn_spec parameter, which can be a string naming a connection rule or a dictionary containing a rule specification. Only connection rules requiring no parameters can be given as strings, for all other rules, a dictionary specifying the rule and its parameters, such as in- or out-degrees, is required.

Type 				|  Example 				|  Description 											
--------------------|-----------------------|-------------------------------------------------------
one-to-one 			|![1][one-to-one]		|The ith node in pre is connected to the ith node in post. The node lists pre and post have to be of the same length.
all-to-all			|![2][all-to-all]		|Each node in *pre* is connected to every node in *post*. 
fixed-indegree		|![3][fixed-indegree]	|The nodes in *pre* are randomly connected with the nodes in *post* such that each node in *post* has a fixed indegree.
fixed-outdegree		|![4][fixed-outdegree]	|The nodes in *pre* are randomly connected with the nodes in *post* such that each node in *pre* has a fixed outdegree.	
receptor-type		|![5][receptor-type] 	|Each connection in NEST targets a specific receptor type on the post-synaptic node. The meaning of the receptor type depends on the model.	
fixed-total-number  |						|The nodes in *pre* are randomly connected with the nodes in *post* such that the total number of connections equals N
pairwise-bernoulli	|						|For each possible pair of nodes from *pre* and *post*, a connection is created with probability p.

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
**Dict of synapses**
```python
#		 key	 synapse parameters   weight    name
types = {GABA:  (STDP_synparams_GABA, w_GABA,  'GABA'),
		 ACh:   (STDP_synparams_ACh,  w_ACh,   'Ach'),
		 Glu:   (STDP_synparams_Glu,  w_Glu,   'Glu'),
		 DA_ex: (DOPA_synparams_ex,   w_DA_ex, 'DA_ex', dopa_model_ex),
		 DA_in: (DOPA_synparams_in,   w_DA_in, 'DA_in', dopa_model_in)}
```
**Keys of synapse types**  
(using for make code easier for reading and lighter)
```
GABA = 0
Glu = 1
ACh = 2
DA_ex = 3
DA_in = 4
```

**Synapse Specification**

The synapse properties can be given as a string or a dictionary. The string can be the name of a pre-defined synapse which can be found in the synapsedict (see [Synapse Types](http://www.nest-simulator.org/connection_management/#Synapse_Types)) or a manually defined synapse via CopyModel().

**Parameters of synapses**

static_synapse	| stdp_synapse	| stdp_dopamine_synapse	|	Description
----------------|---------------|-----------------------|--------------
weight			|weight			|weight					|Weight (power) of synapse
receptor_type	|receptor_type	|receptor_type			|Type of receptor
delay			|delay			|delay					|Distribution of delay values for connections.
				|tau_plus		|tau_plus				|STDP time constant for facilitation in ms
				|Wmax			|Wmax					|Maximum allowed synaptic weight
				|mu_plus		|						|Weight dependence exponent, potentiation
				|mu_minus		|						|Weight dependence exponent, depression
				|alpha			|						|Asymmetry parameter (scales depressing increments as alpha*lambda)
				|lambda			|						|Step size
				|				|Wmin					|Minimal synaptic weight
				|				|tau_n					|Time constant of dopaminergic trace in ms
				|				|b						|Dopaminergic baseline concentration
				|				|c						|eligibility trace
				|				|A_plus					|Amplitude of weight change for facilitation
				|				|A_minus				|Amplitude of weight change for depression
				|				|tau_c					|Time constant of eligibility trace in ms
				|				|n						|neuromodulator concentration

Standard weight of synapses:  
```python
w_Glu = 3.  
w_GABA = -w_Glu * 2  
w_ACh = 8.  
w_DA_ex = 13.  
w_DA_in = -w_DA_ex
```

* static_synapse  
This type os synapse uses in **spike generators**
```python
nest.CopyModel('static_synapse',    	# origin model
            	gen_static_syn,     	# new model
                {'weight': w_Glu * 5,
                'delay': 10.}) 
```
* stdp_synapse  
This type os synapse uses in **non dopaminergic** connections
```python
# Common parameters for 'stdp_synapse'
STDP_synapseparams = {
    'model': 'stdp_synapse',
    'tau_m': {'distribution': 'uniform', 'low': 15., 'high': 25.},
    'alpha': {'distribution': 'normal_clipped', 'low': 0.5, 'mu': 5.0, 'sigma': 1.0},
    'delay': {'distribution': 'uniform', 'low': 0.8, 'high': 2.5},
    'lambda': 0.5
}
# Unique parameters for GLUTAMATE
STDP_synparams_Glu = dict({'delay': {'distribution': 'uniform', 'low': 0.7, 'high': 1.3},
                           'weight': w_Glu,
                           'Wmax': 70.}, **STDP_synapseparams)
#Unique parameters for GABA
STDP_synparams_GABA = dict({'delay': {'distribution': 'uniform', 'low': 1., 'high': 1.9},
                            'weight': w_GABA,
                            'Wmax': -60.}, **STDP_synapseparams)
#Unique parameters for ACETYLCHOLINE
STDP_synparams_ACh = dict({'delay': {'distribution': 'uniform', 'low': 0.7, 'high': 1.3},
                           'weight': w_ACh,
                           'Wmax': 70.}, **STDP_synapseparams)
                           
```

* stdp_dopamine_synapse  
This type os synapse uses in **dopaminergic** connections
```python
DOPA_synparams = {'delay': 1.}
DOPA_synparams_ex = dict({'weight': w_DA_ex,
                          'Wmax': 100.,
                          'Wmin': 85.}, **DOPA_synparams)

DOPA_synparams_in = dict({'weight': w_DA_in,
                          'Wmax': -100.,
                          'Wmin': -85.}, **DOPA_synparams)
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


For the creation of custom synapse types from already existing synapse types, the command CopyModel is used. It has an optional argument params to directly customize it during the copy operation.

```python
def connect_generator(part, startTime=1, stopTime=T, rate=250, coef_part=1):
    # took name of this part
    name = parts_dict[part]
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
