[fixed-outdegree]: http://www.nest-simulator.org/wp-content/uploads/2014/12/Fixed_outdegree.png
[fixed-indegree]: http://www.nest-simulator.org/wp-content/uploads/2014/12/Fixed_indegree.png
[receptor-type]: http://www.nest-simulator.org/wp-content/uploads/2014/12/Receptor_types.png
[one-to-one]: http://www.nest-simulator.org/wp-content/uploads/2014/12/One_to_one.png
[all-to-all]: http://www.nest-simulator.org/wp-content/uploads/2014/12/All_to_all.png

[neuromodulation]: https://github.com/research-team/NEUCOGAR/blob/master/nest/dopamine/integrated/neuromodulation.py
[parameters]: https://github.com/research-team/NEUCOGAR/blob/master/nest/dopamine/integrated/parameters.py
[property]: https://github.com/research-team/NEUCOGAR/blob/master/nest/dopamine/integrated/property.py
[func]: https://github.com/research-team/NEUCOGAR/blob/master/nest/dopamine/integrated/func.py
[data]: https://github.com/research-team/NEUCOGAR/blob/master/nest/dopamine/integrated/data.py


1. **[Structure](#1-structure)**
2. **[Initialization of neurons](#2-initialization-of-neurons)**
	1. [Main dictionary](#21-main-dictionary)
	2. [Table of neurons](#22-table-of-neuron-parameters)
	3. [Generating neurons](#23-generating-neurons)
3. **[Connection of neurons](#3-connection-of-neurons)**
	1. [Table of connections](#31-table-of-connections)
	2. [Synapse specification](#32-synapse-specification)
	3. [Distributing synapse parameters](#33-distributing-synapse-parameters)
	4. [Neuromodulating connections](#34-neuromodulating-connections)
4. **[Connection of devices](#4-connection-of-devices)**
	1. [Spike detector](#41-spike-detector)
	2. [Multimeter](#42-multimeter)
	3. [Generator](#43-generator)
5. **[Simulation](#5-simulation)**
6. **[Save results](#6-save-results)**


## 1. Structure

![13](https://github.com/research-team/NEUCOGAR/blob/master/nest/dopamine/integrated/doc/structure.png)
* [property.py][property] contains main settings and definition of keys for readability;
* [data.py][data] is responsible for initial dicts of the parts and keys for them. It makes the code more readable and light;
* [parameters.py][parameters] provides sets of settings for various types of neurons, synapses and generators;
* [func.py][func] keeps functions which doing routine work and doesn't return anything;
* [neuromodulation.py][neuromodulation] is using for logical job such as assembly process.


============================


## 2. Initialization of neurons

#### 2.1 Main dictionary 
*data.py* include the primal dictionary of parts and the keys for them. Later this dictionary will grow.
```python
# write name of the parts
motor = ({k_name: 'Motor cortex [Glu0]'},
         {k_name: 'Motor cortex [Glu1]'})
# and add keys to refer to this parts by using np.arrange()
# in output we get motor_Glu0 = 0 and motor_Glu1 = 1
motor_Glu0, motor_Glu1 = np.arange(2)		
. . . . . .
. . . . . .
thalamus = ({k_name: 'Thalamus [Glu]'}, )
thalamus_Glu = 0
```

#### 2.2 Table of neuron parameters
In our model, the *iaf_neuron_exp* uses in non-dopaminergic neurons. The *iaf_psc_alpha* for dopaminergic neurons and the *izhikevich* for thalamo-cortical circuit.

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

#### 2.3 Generating neurons
Function ```generate_neurons()``` assemble parameters into the main dictionary.  
At first we group neurons by type of their future model.
```python
# group without dopamine neurons (tuple)
parts_no_dopa = gpe + gpi + ... + thalamus +  snr
# with dopamine neurons (tuple)
parts_with_dopa = (vta[vta_DA0], vta[vta_DA1], snc[snc_DA])
# also create group of all parts, sort them (for readability) and convert to the tuple
all_parts = tuple(sorted(parts_no_dopa + parts_with_dopa))
```

Then specify the neuron number.
```python
#object[part][key of neuron number]
gpe[gpe_GABA][k_NN] = 84100
gpi[gpi_GABA][k_NN] = 12600
. . . . . . . . .
pptg[pptg_Glu][k_NN] = 2300

# multiply number value with NN_coef, also check neuron number with NN_minimal
for part in all_parts:
    part[k_NN] = NN_minimal if int(part[k_NN] * NN_coef) < NN_minimal else int(part[k_NN] * NN_coef)

# variable which contains information about global neuron number
NEURONS = sum(item[k_NN] for item in all_parts)
```

Define neuron parameters.
```python
iaf_neuronparams = {'E_L': -70.,
                    'V_th': -50.,
                    'V_reset': -67.,
                    'C_m': 2.,
                    't_ref': 2.,
                    'V_m': -60.,
                    'tau_syn_ex': 1.,
                    'tau_syn_in': 1.33}
```

Write neuron models into the dictionary.
```python
# default values of a synapse type can be modified with SetDefaults(), 
# which takes the name of the synapse type and a parameter dictionary as arguments
nest.SetDefaults('iaf_psc_exp', iaf_neuronparams)
nest.SetDefaults('iaf_psc_alpha', iaf_neuronparams)

# write to the dictionary parts without dopamine the 'iaf_psc_exp' model 
for part in parts_no_dopa:
    part[k_model] = 'iaf_psc_exp'
# write to the dictionary parts with dopamine the 'iaf_psc_alpha' model 
for part in parts_with_dopa:
    part[k_model] = 'iaf_psc_alpha'
# create neurons and write their ID into dictionary with key k_IDs
for part in all_parts:
    part[k_IDs] = nest.Create(part[k_model], part[k_NN])
```

In result we get tuple of all parts with necessary parameters:
```python
# example
({'Model': 'iaf_psc_exp', 'Name': 'Amygdala [Glu]', 'NN': 40, 'IDs': (1, ... , 40)},
 {'Model': 'iaf_psc_exp', 'Name': 'GPe [GABA]', 'NN': 30, 'IDs': (41, ... , 70)},
	. . . . . .
 {'Model': 'iaf_psc_alpha', 'Name': 'VTA [DA1]', 'NN': 20, 'IDs': (1157, ... , 1176)})
```


========================


### 3. Connection of neurons

Connection rules are specified using the conn_spec parameter, which can be a string naming a connection rule or a dictionary containing a rule specification. Only connection rules requiring no parameters can be given as strings, for all other rules, a dictionary specifying the rule and its parameters, such as in- or out-degrees, is required. In our model we use rule *'all-to-all'* (**must be explored**)

#### 3.1 Table of connections

Type 				|  Example 				|  Description 	
--------------------|-----------------------|---------------
one-to-one 			|![1][one-to-one]		|The ith node in pre is connected to the ith node in post. The node lists pre and post have to be of the same length.
all-to-all			|![2][all-to-all]		|Each node in *pre* is connected to every node in *post*. 
fixed-indegree		|![3][fixed-indegree]	|The nodes in *pre* are randomly connected with the nodes in *post* such that each node in *post* has a fixed indegree.
fixed-outdegree		|![4][fixed-outdegree]	|The nodes in *pre* are randomly connected with the nodes in *post* such that each node in *pre* has a fixed outdegree.	
receptor-type		|![5][receptor-type] 	|Each connection in NEST targets a specific receptor type on the post-synaptic node. The meaning of the receptor type depends on the model.	
fixed-total-number  |						|The nodes in *pre* are randomly connected with the nodes in *post* such that the total number of connections equals N
pairwise-bernoulli	|						|For each possible pair of nodes from *pre* and *post*, a connection is created with probability p.


Implemented help function for connecting parts with each other (see [func.py](https://github.com/research-team/NEUCOGAR/blob/master/nest/dopamine/integrated/func.py))
```python
def connect(pre, post, syn_type=GABA, weight_coef=1):
	# include result of multiplying standard synapse weight and coefficient
	# into weight parameter of the synapse
	types[syn_type][0]['weight'] = weight_coef * types[syn_type][1]
	# connect two parts, include rules of connections
	# in syn_spec include synapse parameters (another type for dopamine)
    nest.Connect(pre[k_IDs], 
                 post[k_IDs], 
                 conn_spec=conn_dict, 
                 syn_spec=types[syn_type][3] if syn_type in (DA_ex, DA_in) else types[syn_type][0])
	# logging action (from, to, type, weight)
	log_conn(pre, post, types[syn_type][2], types[syn_type][0]['weight'])  
```
Where
```python
conn_dict = {'rule': 'all_to_all',
             'multapses': True}
```
and
```python
def log_connection(pre, post, syn_type, weight):
	# global variable of synapse number
    global SYNAPSES
    # this formula is working if we use rule 'all-to-all'
    SYNAPSES += pre[k_NN] * post[k_NN]
    # logging action
    logger.debug("{0} -> {1} ({2}) w[{3}] // {4} synapses".format(pre[k_name], post[k_name],
                                                                  syn_type, weight, 
                                                                  pre[k_NN]*post[k_NN]))
```

'Another part' is implemented bacause nest.Connect doesn't support the direct specification of the volume transmitter of stdp_dopamine_synapse in syn_spec. So need use SetDefaults() or CopyModel().
```python
# dictionary of synapses (help structure)
#		 key	 synapse parameters   weight    name 	 another type
types = {GABA:  (STDP_synparams_GABA, w_GABA,  'GABA'),
		 ACh:   (STDP_synparams_ACh,  w_ACh,   'Ach'),
		 Glu:   (STDP_synparams_Glu,  w_Glu,   'Gl
),
		 DA_ex: (DOPA_synparams_ex,   w_DA_ex, 'DA_ex', dopa_model_ex),
		 DA_in: (DOPA_synparams_in,   w_DA_in, 'DA_in', dopa_model_in)}
```


#### 3.2 Synapse Specification
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
	
**Standard weight of synapses:**  (must be explored)
```python
w_Glu = 3.  
w_GABA = -w_Glu * 2  
w_ACh = 8.  
w_DA_ex = 13.  
w_DA_in = -w_DA_ex
```

**Keys of synapse types** (using for make code lighter and easier for reading)
```
GABA = 0
Glu = 1
ACh = 2
DA_ex = 3
DA_in = 4
```


#### 3.3 Distributing synapse parameters
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
			<ul>
				<li>mu  - mean of the underlying normal distribution 
				<li>sigma - standard deviation of the underlying normal distribution 
			</ul>
		<td>
			<img src="https://upload.wikimedia.org/math/5/6/4/564914214ead956aceccd30b78d2f6ee.png"/>
	<tr>
		<td>
			lognormal
		<td>
			<ul>
				<li>mu  - mean
				<li>sigma - standard deviation
			</ul>
		<td>
			<img src="https://upload.wikimedia.org/math/9/e/2/9e2b928f871663bc2ab9e7478735f4e2.png"/>
	<tr>
		<td>
			uniform
		<td>
			<ul>
				<li>low  - lower interval boundary, included
  				<li>high - upper interval boudnary, excluded
  			</ul>
		<td>
			- - -
  	<tr>
  		<td>
  			uniform_int
  		<td>
  			<ul>
  				<li>low - smallest allowed random number 
  				<li> high - largest allowed random number
  			</ul>
  		<td>
  			p(n) = 1 / (high - low + 1),   n = low, low+1, ..., high
  	<tr>
  		<td>
  			binomial
  		<td>
  			<ul>
  				<li>p - probability of success in a single trial (double)
				<li>n - number of trials (positive integer)
			</ul>
  		<td>
  			<img src="https://upload.wikimedia.org/math/f/1/d/f1d6646783a852d50c363c1928e8a99e.png"/>
			, where
			<img src="https://upload.wikimedia.org/math/3/7/4/3747421657b1dea010fdb4fc09de8319.png"/>
  	<tr>
  		<td>
  			exponential
  		<td>
  			<ul>
  				<li>lambda - rate parameter
  			</ul>
  		<td>
  			<img src="https://upload.wikimedia.org/math/a/a/4/aa4903b858058a7ceba1271512a86e08.png"/>
  	<tr>
  		<td>
  			gamma
  		<td>
  			<ul>
  				<li>k - order of the gamma distribution
   				<li>θ - scale parameter
   			</ul>
  		<td>
			<img src="https://upload.wikimedia.org/math/9/a/2/9a277651cacd3a06158a9d7800415972.png"/>
			, where
			<img src="https://upload.wikimedia.org/math/e/5/9/e59fe250c57082f60e35fa96379afd2f.png"/>
  	<tr>
  		<td>
  			poisson
  		<td>
  			<ul>
  				<li>lambda - distribution parameter, lambda
  			</ul>
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


#### 3.4 Neuromodulating connections

```python
# Volume transmission: init dopa_model
vt_ex = nest.Create('volume_transmitter')
vt_in = nest.Create('volume_transmitter')
DOPA_synparams_ex['vt'] = vt_ex[0]
DOPA_synparams_in['vt'] = vt_in[0]
nest.Connect(snc[snc_DA][k_IDs], vt_ex)
nest.Connect(snc[snc_DA][k_IDs], vt_in)
nest.Connect(vta[vta_DA0][k_IDs], vt_ex)
nest.Connect(vta[vta_DA1][k_IDs], vt_ex)
nest.CopyModel('stdp_dopamine_synapse', dopa_model_ex, DOPA_synparams_ex)
nest.CopyModel('stdp_dopamine_synapse', dopa_model_in, DOPA_synparams_in)
```


===============


## 4. Connection of devices

#### 4.1 Spike detector
The spike_detector device is a recording device. It is used to record spikes from a single neuron, or from multiple neurons at once. Data is recorded in memory or to file as for all RecordingDevices. By default, GID and time of each spike is recorded

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


#### 4.2 Multimeter
A multimeter records a user-defined set of state variables from connected nodes to memory, file or stdout. The multimeter must be configured with the list of variables to record from, otherwise it will not record anything.
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
			'to_file': False, 			# don't save to file
            'withtime': True, 			# add time
            'interval': 0.1,			# use interval 0.1ms
            'record_from': ['V_m'], 	# record voltage [mV]
            'withgid': True}			# add gid
```


#### 4.3 Generator

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
                 syn_spec=static_syn,                           	  # synapse parameters
                 conn_spec={'rule': 'fixed_outdegree',                # connection rules
                            'outdegree': int(len(part) * coef_part)}) # number of connections
    logger.debug("Generator => {0}. Element #{1}".format(name, spikegenerators[name][0]))
```
Where
```python
static_syn = {
    'model': 'static_synapse',
    'weight': w_Glu * 5,
    'delay': pg_delay
}
```
The following devices generate sequences of spikes which can be send to a neuron. These devices act like populations of neurons and connected to their targets like a neuron.


#### Table of type generators
<table>
	<tr align="center">
		<td width=33%>
			<b>poisson_generator</b>
		<td width=33%>
			<b>spike_generator</b>
		<td width=33%>
			<b>noise_generator</b>
	<tr valign="top">
		<td>
			The poisson_generator simulates a neuron that is firing with Poisson statistics, 
			i.e. exponentially distributed interspike intervals. It will generate a <i>unique</i>
			spike train for each of it's targets 
		<td>
			A spike generator can be used to generate spikes at specific times
  			which are given to the spike generator as an array.
  			Spike times are given in milliseconds, and must be sorted with the
  			earliest spike first. All spike times must be strictly in the future.
  			Trying to set a spike time in the past or at the current time step,
  			will cause a NEST error.
		<td>
			This device can be used to inject a Gaussian "white" noise current into a node.
			The current is not really white, but a piecewise constant current with Gaussian
			distributed amplitude. The current changes at intervals of dt. dt must be a
			multiple of the simulation step size.
	<tr>
		<td align="center" colspan="3">
			<b>Parameters</b>
	<tr valign="top">
		<td>
			<ul>
				<li><b>origin 	</b> -	Time origin for device timer in ms	
				<li><b>rate		</b> -	mean firing rate in Hz 
				<li><b>start 	</b> -	begin of device application with resp. to origin in ms 
				<li><b>stop 	</b> -	end of device application with resp. to origin in ms
			</ul>
		<td>
			<ul>
				<li><b>allow_offgrid_spikes </b> - see below
				<li><b>origin         		</b> - Time origin for device timer in ms
       			<li><b>precise_times        </b> - see below
       			<li><b>shift_now_spikes     </b> - see below
       			<li><b>spike_times    		</b> - array of spike-times in ms
       			<li><b>spike_weights  		</b> - array corrsponding spike-weights, the unit depends on the receiver
       			<li><b>start          		</b> - earliest possible time stamp of a spike to be emitted in ms
       			<li><b>stop           		</b> - earliest time stamp of a potential spike event that is not emitted in ms
			</ul>
		<td>
			<ul>
				<li><b>dt       </b> - interval between changes in current in ms, default 1.0ms
				<li><b>frequency</b> - Frequency of sine modulation in Hz
				<li><b>mean     </b> - mean value of the noise current in pA
				<li><b>origin   </b> - analogically
				<li><b>phase    </b> - Phase of sine modulation (0-360 deg)
				<li><b>start    </b> - analogically
				<li><b>std      </b> - standard deviation of noise current in pA
				<li><b>std_mod  </b> - modulated standard deviation of noise current in pA
       			<li><b>stop     </b> - analogically
			</ul>
	<tr>
		<td align="center" colspan="3">
			<b>Remarks</b>
	<tr valign="top">
		<td>
			A Poisson generator may, especially at high rates, emit more than one
   			spike during a single time step. If this happens, the generator does
   			not actually send out n spikes. Instead, it emits a single spike with
   			n-fold synaptic weight for the sake of efficiency.
   			<br/><a href="http://www.nest-simulator.org/cc/poisson_generator/">More</a>.
		<td>
			<ul>
				<li><b>precise_times</b> (default: false) 
     				If false, spike times will be rounded to simulation steps, i.e., multiples
     				of the resolution.
				<li><b>allow_offgrid_times</b> (default: false) 
     				If false, spike times will be rounded to the nearest step if they are
     				less than tic/2 from the step, otherwise NEST reports an error.
				<li><b>shift_now_spikes</b> (default: false) 
     				If false, spike times rounded down to the current point in time will
     				be considered in the past and ignored.
     				<br/><a href="http://www.nest-simulator.org/cc/spike_generator/">More</a>.
			</ul>	
		<td>
			<ul>
				<li>All targets receive different currents.
 				<li>The currents for all targets change at the same points in time.
 				<li>The interval between changes, dt, must be a multiple of the time step.
 				<li>The effect of this noise current on a neuron DEPENDS ON DT. Consider
   					the membrane potential fluctuations evoked when a noise current is
   					injected into a neuron.

			</ul>
			<br/><a href="http://www.nest-simulator.org/cc/noise_generator/">More</a>.

	<tr>
		<td align="center" colspan="3">
			<b>Example</b>
	<tr valign="top">
		<td>

			<ul>
				<li>rate: 100
				<li>start: 1
				<li>stop: 1000
			</ul>
			<img src="https://github.com/research-team/NEUCOGAR/blob/master/nest/dopamine/integrated/doc/poisson_generator.png" />
		<td>
			<ul>
				<li> spike_times: every 50 ms (from 1 to 1000ms)
				<li> spike_weights: 10 
			</ul>
			<img src="https://github.com/research-team/NEUCOGAR/blob/master/nest/dopamine/integrated/doc/spike_generator.png" />
		<td>
			<ul>
				<li>dt: 50
				<li>mean: 0.3
				<li>start: 1; stop: 1000
			</ul>
			<img src="https://github.com/research-team/NEUCOGAR/blob/master/nest/dopamine/integrated/doc/noise_generator.png" />
	<tr align="center">
		<td width=33%>
			<b>poisson_generator</b>
		<td width=33%>
			<b>spike_generator</b>
		<td width=33%>
			<b>noise_generator</b>
</table>
Also see infromation in NEST folder opt/nest/share/doc/nest/help/cc/



=========================


## 5. Simulation


=========================


## 6. Save results