[structure]: ../integrated/doc/description.md

# Integrated dopamine with 3D layers

## File structure
All the scripts are located in `./scripts/`

Results are saved to `./results/` by default

Scripts descriptions:
- **neuromodulation.py** - main script for simulation
- **func.py** - helper functions
- **keys.py** - keys for dicts and lists
- **output.py** - helper functions for data output
- **globals.py** - global variables for internal use
- **parts.py** - brain parts definitions
- **simulation_params.py** - simulation parameters than can be adjusted
- **synapses.py** - synapses definition


## Brain parts
Every brain part is represented by two 3d `nest.topology` layers,
for outer and inner neurons, due to limitations of `nest.topology`.

Every layer is a set of neurons with positions uniformly generated in range (-0.5; 0;5) for every axis.

## Connections
Inner connections are made using spherical mask and Gaussian kernel, fixed number of connections is not implemented here.

Outer connections are made randomly, with fixed number of connections (no more than `MaxSynapses`).

Weights are fixed for every pair of layers and every synapse type.

Delays inside layers are increasing linearly with distance.



