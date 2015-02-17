#Cube of emotions experiment description

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

