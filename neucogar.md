# NeuCogAr (Neuromodulating Cognitive Architecture)

## Overview

The project to validate the 3D model of emotions based on Lövheim model of monoamine neuromodulators described on [wiki page](http://en.wikipedia.org/wiki/L%C3%B6vheim_cube_of_emotion).

Overview of the model could be found in this [seminar](https://github.com/max-talanov/1/blob/master/cognitive_technologies_seminars/2014-12-17%20Computational%20affective%20thinking%20model%20%20Techtalk.md#monoamines-model).

For validation purposes we use Neurosimulator [NEST](http://www.nest-simulator.org/)


## Researcher guide

### Read experiment description

Please use following experiment description: [experiment description](experiment_description.md)

### Download NEST

Please use latest version available here: http://www.nest-simulator.org/download/

### Install NEST

Please find installation guide here: http://www.nest-simulator.org/installation/

### Alternative installation with Vagrant

1. Install [Vagrant](https://www.vagrantup.com)
1. Copy files Vagrantfile and provision.sh from current folder
to some fresh one
1. Open terminal and cd to that folder
1. run `vagrant up`

After completion of `vagrant up` you should have running
virtual machine with Ubuntu and NEST 2.6.0 installed.


### Further documentation on NEST

Please find further documentation here: http://www.nest-simulator.org/documentation/

### Clone github repository

Clone repository via command line:

```shellscript
git clone https://github.com/development-team/4.git
```

or please use windows gui github client from: https://windows.github.com/

or please use tortoise git for windows from: https://code.google.com/p/tortoisegit/

Please use following repository address for cloning: https://github.com/research-team/NEUCOGAR.git

### Task traking system

Please use trello in SCRUM way to track and implement tasks: https://trello.com/b/lnHnRkWr/neucogar

### Additional reading to develop understanding

1. http://en.wikipedia.org/wiki/Neuromodulation
1. http://en.wikipedia.org/wiki/Dopamine
