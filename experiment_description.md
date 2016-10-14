#Cube of emotions experiment description

##General neuromodulation

###Description

Idea is based on basal ganglia dopamine neuromodulation described:

1. https://en.wikipedia.org/wiki/Basal_ganglia#Circuit_connections
1. https://github.com/max-talanov/1/blob/master/computational%20emotional%20thinking%20course/neurotransmission.md#emotional-loop

In short:

![Basal ganglia connectivity diagram](http://upload.wikimedia.org/wikipedia/commons/4/45/Basal-ganglia-classic.png)

Connectivity diagram showing excitatory glutamatergic pathways as red, inhibitory GABAergic pathways as blue, and modulatory dopaminergic pathways as magenta. (Abbreviations: GPe: globus pallidus external; GPi: globus pallidus internal; STN: subthalamic nucleus; SNc: substantia nigra compacta; SNr: substantia nigra reticulata)

The antagonistic functions of the direct and indirect pathways are modulated by the **substantia nigra pars compacta (SNc)**, which produces **dopamine**. In the presence of dopamine, D1-receptors in the basal ganglia stimulate the GABAergic neurons, favoring the direct pathway, and thus increasing movement. The GABAergic neurons of the indirect pathway are stimulated by excitatory neurotransmitters acetylcholine and glutamate. This sets off the indirect pathway that ultimately results in inhibition of upper motor neurons, and less movement. In the presence of dopamine, D2-receptors in the basal ganglia inhibit these GABAergic neurons, which reduces the indirect pathways inhibitory effect. **Dopamine therefore increases the excitatory effect of the direct pathway (causing movement) and reduces the inhibitory effect of the indirect pathway (preventing full inhibition of movement)**. 

This way we have to simulate:

1. Cortex
1. Striatum
1. GPe: globus pallidus external
1. GPi: globus pallidus internal 
1. STN: subthalamic nucleus
1. SNc: substantia nigra compacta
1. SNr: substantia nigra reticulata

With two main pathways/algorithms:

**Direct pathway**

**Cortex** (stimulates) → **Striatum** (inhibits) → **"SNr-GPi" complex** (less inhibition of thalamus) → **Thalamus** (stimulates) → **Cortex** (stimulates) → **Muscles, etc.**

**Indirect pathway**

**Cortex** (stimulates) → **Striatum** (inhibits) → **GPe** (less inhibition of STN) → **STN** (stimulates) → **"SNr-GPi" complex** (inhibits) → **Thalamus** (is stimulating less) → **Cortex** (is stimulating less) → Muscles, etc.

Neuromodulation is implemented by SNc via production of the **dopamine** that influences Striatum triggering direct or indirect pathway.

###Input

1. Spikes generators of the Cortex generate series of spikes that stimulates the Striatum.
1. Dopamine neurons produce dopamine that modulates Striatum.

##Output

1. In case of dopamine relative cortex activity (number of spikes) is increased.
1. In case of no dopamine modulation relative cortex activity (number of spikes) is decreased. 

##Assumptions

We propose to start from following structure:

1. Cortex = 100 neurons, iaf_psc_exp glutamatergic
1. Striatum = 10 neurons, iaf_psc_exp GABAergic 
1. GPe: globus pallidus external = 10 neurons, iaf_psc_exp GABAergic
1. GPi: globus pallidus internal = 10 neurons, iaf_psc_exp GABAergic
1. STN: subthalamic nucleus = 10 neurons, iaf_psc_exp glutamatergic
1. SNr: substantia nigra reticulata = 10 neurons, iaf_psc_exp GABAergic
1. SNc: substantia nigra compacta = 10 neurons, iaf_psc_exp dopaminergic
1. Thalamus = 10 neurons, iaf_psc_exp glutamatergic

This is really coarse model that do not take in account real scales and cytoarchitecture of neurons in the structures listed above. There are several evolutions available: create proper neurons of cortical and subcortical areas of brain, create proper neuron populations of proper scales, create proper topology of the neuronal networks for each area. Thus we could use 100 cortex neurons, 10 rest, then increase to 5000 cortex, 30 rest, then 4000000 cortex and rest based on actual number of neurons in brain areas of a mouse.

We can start experiments with iaf_psc_exp, if the experiments goes too long we could use iaf_cond_alpha instead, then we could use iaf_psc_alpha.

##Computing power and memory distribution (attention)

###Description

1. Run some series of impulses that simulate **loud** sound in auditory cortex.
1. Run **noradrenaline neuromodulation** that simulate attention switch.
1. Run two steps above for training.
1. Run step number one.
1. This should initiate **noradrenaline neuromodulation** based on training, if we observe rise of noradrenaline concentration this should effectively indicate the association of **noradrenaline neuromodulation** with **loud** sound.
1. **Noradrenaline neuromodulation** also should switch an **attention** in terms of computational processes concentrate the **computing power and memory resources** on the current processes associated with **loud** sound.

###Input

Series of impulses simulating **loud** sound.

###Output

1. **Noradrenaline neuromodulation**
1. **Attention switch**
1. Concentration of **computational power and memory resources** on thinking process associated with **loud** sound.

###Precondition

None

###Postcondition

Computational and memory resources are concentrated on current process associated with **loud** sound.


##Stimulation and reward processing 

1. Run some series of impulses that simulate **quiet** sound in auditory cortex.
1. Run **dopamine + serotonin** neuromodulation that simulate reward.
1. Run two steps above for training.
1. Run step number one.
1. This should initiate **dopamine + serotonin neuromodulation** based on training, if we observe rise of **dopamine and serotonin** concentration this should effectively indicate the association of dopamine neuromodulation with **quiet** sound as **reward**.

###Input

Series of impulses simulating **quiet** sound.

###Output

1. **Dopamine + serotonin neuromodulation**
1. **Reward assignment**

###Precondition

None

###Postcondition

Reward assigned to the process associated with **quiet** sound.



Simplistic neuromodulation model
================================

Model
-----

We assume that neuromodulator is either increase or decrease membrane potential
of neurones it attaches to. Each particular neuromodulator either increases
or decreases membrane potential.

We model neuromodulator release as activation of post-output neuron that links
back to "working" (hidden layer) neurons. For simplistic ANNs (perceptron-like)
we can model neuromodulator effect as additional coefficient in neuron's function.


Experiment 1
------------

### Preparation

Make ANN (perceptron) that classifies input signal as either "dangerous" or
"not dangerous", connect "dangerous" output to "noradrenaline-stimulating" neuron
and that neuron to half of "working" (hidden layer) neurons.

### Experiment

1. Train ANN to classify prepared signals
2. Give trained ANN mix of two "dangerous" signals
3. Check whether output increases superlinearly



Neuromodulators effect on recognition validation
================================================

Setup
-----

We have two neural networks and output of the first one is fead as input to the second.
The first neural network is trained to recognize (visual images of) food or danger
(e.g. recognize apples and cats). The second one is trained to classify output of the
first network into groups "go towards it", "go away from it" or "do nothing".

Assumptions
-----------

We assume that neurobiologically valid neuromediator effect on neural network is implemented.

Experiment
----------

1. Prepare a mixed image of food and danger images such that cascade of our two neural  networks
without neuromediator classifies it as "go towards it" (e.g. 0.6\*apple + 0.3\*cat + 0.1\*background)
2. Find level of neuromediator (dophamine or noradrenaline) when cascade starts to classify
the mixed image as "go away from it" (emotional state of fear)

