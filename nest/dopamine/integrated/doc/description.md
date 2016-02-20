<<<<<<< 58f33498b151e8ab636ef59e37f8aa68d4f0672c
[one-to-one]: http://www.nest-simulator.org/wp-content/uploads/2014/12/One_to_one.png
[all-to-all]: http://www.nest-simulator.org/wp-content/uploads/2014/12/All_to_all.png
[fixed-indegree]: http://www.nest-simulator.org/wp-content/uploads/2014/12/Fixed_indegree.png
[fixed-outdegree]: http://www.nest-simulator.org/wp-content/uploads/2014/12/Fixed_outdegree.png
[receptor-type]: http://www.nest-simulator.org/wp-content/uploads/2014/12/Receptor_types.png

=======
[fixed-outdegree]: http://www.nest-simulator.org/wp-content/uploads/2014/12/Fixed_outdegree.png
[fixed-indegree]: http://www.nest-simulator.org/wp-content/uploads/2014/12/Fixed_indegree.png
[receptor-type]: http://www.nest-simulator.org/wp-content/uploads/2014/12/Receptor_types.png
[one-to-one]: http://www.nest-simulator.org/wp-content/uploads/2014/12/One_to_one.png
[all-to-all]: http://www.nest-simulator.org/wp-content/uploads/2014/12/All_to_all.png
>>>>>>> 2596e7d0791224ac464d07587de66e88de2cd288


[neuromodulation]: https://github.com/research-team/NEUCOGAR/blob/master/nest/dopamine/integrated/neuromodulation.py
[parameters]: https://github.com/research-team/NEUCOGAR/blob/master/nest/dopamine/integrated/parameters.py
[property]: https://github.com/research-team/NEUCOGAR/blob/master/nest/dopamine/integrated/property.py
[func]: https://github.com/research-team/NEUCOGAR/blob/master/nest/dopamine/integrated/func.py
[data]: https://github.com/research-team/NEUCOGAR/blob/master/nest/dopamine/integrated/data.py


#### 1. [Structure](https://github.com/research-team/NEUCOGAR/blob/master/nest/dopamine/integrated/doc/description.md#structure)
#### 2. [Initializing neurons](https://github.com/research-team/NEUCOGAR/blob/master/nest/dopamine/integrated/doc/description.md#initializing-neurons)
#### 3. [Connection of neurons](https://github.com/research-team/NEUCOGAR/blob/master/nest/dopamine/integrated/doc/description.md#connection-of-neurons)
#### 4. [Connection of devices](https://github.com/research-team/NEUCOGAR/blob/master/nest/dopamine/integrated/doc/description.md#connection-of-devices)
#### 5. [Simulation](https://github.com/research-team/NEUCOGAR/blob/master/nest/dopamine/integrated/doc/description.md#simulation)

### 1. Structure

![13](https://github.com/research-team/NEUCOGAR/blob/master/nest/dopamine/integrated/doc/structure.png)

Dopamine project has this hierarchy of files.
* [property.py][property] contains main settings and definition of keys for readability;
* [data.py][data] is responsible for initial dicts of the parts and keys for them. It makes the code more readable and light;
* [parameters.py][parameters] provides sets of settings for various types of neurons, synapses and generators;
* [func.py][func] keeps functions which doing routine work and doesn't return anything;
* [neuromodulation.py][neuromodulation] is using for logical job such as assembly process.


### Initializing neurons
In our model 'iaf_neuron_exp' uses in non-dopaminergic neurons. 'iaf_psc_alpha' for dopaminergic neurons and 'izhikevich' for thalamo-cortical circuit.

iaf_neuron_exp	|iaf_psc_alpha	|izhikevich	| Description
----------------|---------------|-----------|------------------------
V_m          	|V_m			|V_m		|Membrane potential in mV
V_th         	|V_th 			|V_th		|Spike threshold in mV.
I_e          	|I_e 			|I_e		|Constant input current in pA.
E_L          	|E_L			|			|Resting membrane potential in mV.
C_m          	|C_m 			|			|Capacity of the membrane in pF
tau_m        	|tau_m 			|			|Membrane time constant in ms.
t_ref        	|t_ref			|			|Duration of refractory period (V_m = V_reset) in ms.
V_reset      	|V_reset 		|			|Reset membrane potential after a spike in mV.
				|V_min			|V_min		|Absolute lower value for the membrane potential.
tau_syn_ex   	| 				|			|Time constant of postsynaptic excitatory currents in ms
tau_syn_in   	| 				|			|Time constant of postsynaptic inhibitory currents in ms
t_spike      	| 				|			|Point in time of last spike in ms.
				|tau_syn_ex		|			|Rise time of the excitatory synaptic alpha function in ms.
				|tau_syn_in		|			|Rise time of the inhibitory synaptic alpha function in ms.
				|				|U_m		|Membrane potential recovery variable
         		|				|a			|describes time scale of recovery variable
         		|				|b			|sensitivity of recovery variable
         		|				|c			|after-spike reset value of V_m
         		|				|d			|after-spike reset value of U_m

---

### Connection of neurons

Connection rules are specified using the conn_spec parameter, which can be a string naming a connection rule or a dictionary containing a rule specification. Only connection rules requiring no parameters can be given as strings, for all other rules, a dictionary specifying the rule and its parameters, such as in- or out-degrees, is required. In our model we use rule *'all-to-all'* (**must be explored**)


Type 				|  Example 				|  Description 	
--------------------|-----------------------|---------------
one-to-one 			|![1][one-to-one]		|The ith node in pre is connected to the ith node in post. The node lists pre and post have to be of the same length.
all-to-all			|![2][all-to-all]		|Each node in *pre* is connected to every node in *post*. 
fixed-indegree		|![3][fixed-indegree]	|The nodes in *pre* are randomly connected with the nodes in *post* such that each node in *post* has a fixed indegree.
fixed-outdegree		|![4][fixed-outdegree]	|The nodes in *pre* are randomly connected with the nodes in *post* such that each node in *pre* has a fixed outdegree.	
receptor-type		|![5][receptor-type] 	|Each connection in NEST targets a specific receptor type on the post-synaptic node. The meaning of the receptor type depends on the model.	
fixed-total-number  |						|The nodes in *pre* are randomly connected with the nodes in *post* such that the total number of connections equals N
pairwise-bernoulli	|						|For each possible pair of nodes from *pre* and *post*, a connection is created with probability p.

Implemented help function for connecting parts with each other (see in [func.py](https://github.com/research-team/NEUCOGAR/blob/master/nest/dopamine/integrated/func.py))
```python
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

**Dict of synapses** (help structure)
```python
#		 key	 synapse parameters   weight    name
types = {GABA:  (STDP_synparams_GABA, w_GABA,  'GABA'),
		 ACh:   (STDP_synparams_ACh,  w_ACh,   'Ach'),
		 Glu:   (STDP_synparams_Glu,  w_Glu,   'Glu'),
		 DA_ex: (DOPA_synparams_ex,   w_DA_ex, 'DA_ex', dopa_model_ex),
		 DA_in: (DOPA_synparams_in,   w_DA_in, 'DA_in', dopa_model_in)}
```
**Keys of synapse types**  (see [property.py](https://github.com/research-team/NEUCOGAR/blob/master/nest/dopamine/integrated/property.py))
(using for make code lighter and easier for reading)
```
GABA = 0
Glu = 1
ACh = 2
DA_ex = 3
DA_in = 4
```

**Synapse Specification**  
The synapse properties can be given as a string or a dictionary. The string can be the name of a pre-defined synapse which can be found in the synapsedict (see [Synapse Types](http://www.nest-simulator.org/connection_management/#Synapse_Types)) or a manually defined synapse via CopyModel().

static_synapse	| stdp_synapse	| stdp_dopamine_synapse	|	Description
----------------|---------------|-----------------------|--------------
weight			|weight			|weight					|Weight (power) of synapse
receptor_type	|receptor_type	|receptor_type			|Type of receptor
delay			|delay			|delay					|Distribution of delay values for connections.
				|tau_plus		|tau_plus				|STDP time constant for facilitation in ms
				|Wmax			|Wmax					|Maximum allowed weight
				|mu_plus		|						|Weight dependence exponent, potentiation
				|mu_minus		|						|Weight dependence exponent, depression
				|alpha			|						|Asymmetry parameter (scales depressing increments as alpha*lambda)
				|lambda			|						|Step size
				|				|Wmin					|Minimal synaptic weight
				|				|tau_n					|Time constant of dopaminergic trace in ms
				|				|b					 	|Dopaminergic baseline concentration
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


**Distributing synapse parameters**  
The synapse parameters are specified in the synapse dictionary which is passed to the Connect-function. If the parameter is set to a scalar all connections will be drawn using the same parameter. Parameters can be randomly distributed by assigning a dictionary to the parameter. The dictionary has to contain the key distribution setting the target distribution of the parameters (for example normal). Optionally parameters associated with the distribution can be set (for example mu).

<table>
	<tr align="center">
		<td width=10%>
			<b>Distributions
		<td width=60%>
			<b>Keys
		<td width=30%>
			<b>Formula
	<tr>
		<td>
			normal
		<td>
			 <li>mu  - mean of the underlying normal distribution 
			 <li>sigma - standard deviation of the underlying normal distribution 
		<td>
			<img src="https://upload.wikimedia.org/math/5/6/4/564914214ead956aceccd30b78d2f6ee.png"/>
	<tr>
		<td>
			lognormal
		<td>
			<li>mu  - mean
			<li>sigma - standard deviation
		<td>
			<img src="https://upload.wikimedia.org/math/9/e/2/9e2b928f871663bc2ab9e7478735f4e2.png"/>
	<tr>
		<td>
			uniform
		<td>
			<li>low  - lower interval boundary, included
  			<li>high - upper interval boudnary, excluded
		<td>
			- - -
  	<tr>
  		<td>
  			uniform_int
  		<td>
  			<li>low - smallest allowed random number 
  			<li> high - largest allowed random number
  		<td>
  			p(n) = 1 / (high - low + 1),   n = low, low+1, ..., high
  	<tr>
  		<td>
  			binomial
  		<td>
  			<li>p - probability of success in a single trial (double)
			<li>n - number of trials (positive integer)
  		<td>
  			<img src="https://upload.wikimedia.org/math/f/1/d/f1d6646783a852d50c363c1928e8a99e.png"/>
			, where
			<img src="https://upload.wikimedia.org/math/3/7/4/3747421657b1dea010fdb4fc09de8319.png"/>
  	<tr>
  		<td>
  			exponential
  		<td>
  			lambda - rate parameter
  		<td>
  			<img src="https://upload.wikimedia.org/math/a/a/4/aa4903b858058a7ceba1271512a86e08.png"/>
  	<tr>
  		<td>
  			gamma
  		<td>
  			<li>k - order of the gamma distribution
   			<li>θ - scale parameter
  		<td>
			<img src="https://upload.wikimedia.org/math/9/a/2/9a277651cacd3a06158a9d7800415972.png"/>
			, where
			<img src="https://upload.wikimedia.org/math/e/5/9/e59fe250c57082f60e35fa96379afd2f.png"/>
  	<tr>
  		<td>
  			poisson
  		<td>
  			lambda - distribution parameter, lambda
  		<td>
  			<img src="https://upload.wikimedia.org/math/7/9/d/79de1417e943a2f4e25868afbc9dc783.png"/>
</table>

Example:
```python
syn_dict = {"model": "stdp_synapse", 
            "alpha": {"distribution": "uniform", "low": Min_alpha, "high": Max_alpha},
            "weight": {"distribution": "uniform", "low": Wmin, "high": Wmax},
            "delay": 1.0 }
```

---

### Connection of devices
#### 1. Spike detector

Define a help function with one parameter 'part' — list of neuron ID's
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

### Simulation


---

