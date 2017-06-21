# Cube of emotions experiment description

## General neuromodulation

### Description

Idea is based on basal ganglia dopamine neuromodulation described:

1. https://en.wikipedia.org/wiki/Basal_ganglia#Circuit_connections
1. https://github.com/max-talanov/1/blob/master/affective_computing_course/neurotransmission.md#emotional-loop

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

### Input

1. Spikes generators of the Cortex generate series of spikes that stimulates the Striatum.
1. Dopamine neurons produce dopamine that modulates Striatum.

## Output

1. In case of dopamine relative cortex activity (number of spikes) is increased.
1. In case of no dopamine modulation relative cortex activity (number of spikes) is decreased. 

## Computing power and memory distribution (attention)

### Description

1. Run some series of impulses that simulate **loud** sound in auditory cortex.
1. Run **noradrenaline neuromodulation** that simulate attention switch.
1. Run two steps above for training.
1. Run step number one.
1. This should initiate **noradrenaline neuromodulation** based on training, if we observe rise of noradrenaline concentration this should effectively indicate the association of **noradrenaline neuromodulation** with **loud** sound.
1. **Noradrenaline neuromodulation** also should switch an **attention** in terms of computational processes concentrate the **computing power and memory resources** on the current processes associated with **loud** sound.

### Input

Series of impulses simulating **loud** sound.

### Output

1. **Noradrenaline neuromodulation**
1. **Attention switch**
1. Concentration of **computational power and memory resources** on thinking process associated with **loud** sound.

### Precondition

None

### Postcondition

Computational and memory resources are concentrated on current process associated with **loud** sound.


## Stimulation and reward processing 

1. Run some series of impulses that simulate **quiet** sound in auditory cortex.
1. Run **dopamine + serotonin** neuromodulation that simulate reward.
1. Run two steps above for training.
1. Run step number one.
1. This should initiate **dopamine + serotonin neuromodulation** based on training, if we observe rise of **dopamine and serotonin** concentration this should effectively indicate the association of dopamine neuromodulation with **quiet** sound as **reward**.

### Input

Series of impulses simulating **quiet** sound.

### Output

1. **Dopamine + serotonin neuromodulation**
1. **Reward assignment**

### Precondition

None

### Postcondition

Reward assigned to the process associated with **quiet** sound.


