## Neuron installation

[Neuron] (http://www.neuron.yale.edu/neuron/download) download and install

1. **Windows users**
  - compile the mod files using mknrndll and then put all .hoc .sys files in that folder.
  - start by double clicking the mosinit.hoc.
  
2. **Linux users** 
  - compile the mod files using nrnivmodl and then put all .hoc .sys files in *x86_x64*  folder
  - set PYTHONPATH in .bashrc 
  ```bash
export PYTHONPATH=$PYTHONPATH:$HOME/local/lib/python/site-packages
  ```
  - add config 
  ```bash
sudo ln -s /usr/lib/python2.7/plat-*/_sysconfigdata_nd.py /usr/lib/python2.7/
  ```
  or add *-nopython* to launch Neuron 
  - start nrngui
  - change working directory 
  - load hoc file (mosinit.hoc) in the working directory. 
  
3. **MacOS users** 
  - compile the mod files using mknrndll and then put all .hoc .sys files in *x86_x64*  folder
  - start nrngui
  - change working directory
  - load dll ("working directory"/.libs/libnrnmech.so)
  - load hoc file (mosinit.hoc) in the "working directory"
