## NEST Installation (Python 2.7.6)
**Instruction for Ubuntu (+PyCharm)**

#### 1. Get standard configuration
```bash
sudo apt-get install build-essential autoconf automake libtool libltdl7-dev libreadline6-dev libncurses5-dev libgsl0-dev python-all-dev python-numpy python-scipy python-matplotlib ipython
```

#### 2. SciPy and NumPy | [Link](http://www.scipy.org/install.html)
```bash
sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose
```

#### 3. matplotlib | [Link](http://matplotlib.sourceforge.net)
```bash
sudo apt-get install python-matplotlib
```

#### 4. IPython | [Link](https://pypi.python.org/pypi/ipython#downloads)
```bash
tar -xzf ipython-4.0.0.tar.gz
cd ipython-4.0.0
sudo python setup.py install
```
#### 5. GNU Scientific Library | [Link](http://www.gnu.org/software/gsl/)
```bash
tar -xzf gsl-latest.tar.gz
cd gsl-1.16 
./configure
make
sudo make install
```

#### 6. NEST | [Link](http://www.nest-simulator.org/download/)
```bash
tar -xzvf nest-x.y.z.tar.gz                         #Unpack the tarball
mkdir nest-x.y.z-build                              #Create a build directory
cd nest-x.y.z-build                                 #Change to the build directory
../nest-x.y.z/configure --prefix=$HOME/opt/nest     #Configure NEST
```
You must see NEST Configuration Summary, where
> C++ compiler : g++

> C++ compiler flags : -W -Wall -pedantic -Wno-long-long -O2 -fopenmp

> Python bindings : Yes (Python 2.7: /usr/bin/python)

> Use threading : Yes (OpenMP)

> Use GSL : Yes

It's mean that previous packages were installed correctly. Continue installation:
```bash
make                                                #Compile by running
sudo make install                                   #Install by running
make installcheck                                   #Check installation
```
If the test completed without any errors, go to the next steps, else try to fix them.

#### 7. PYTHONPATH
It is important to prescribe an environment variable PYTHONPATH for
python interpreter. It is necessary that the interpreter could find
installed module PyNEST among its other modules.
```bash
cd ~/
nano .bashrc
```
add these two lines and save
> PYTHONPATH="$PYTHONPATH:$HOME/opt/nest/lib/python2.7/site-packages"

> export PYTHONPATH

After this, open terminal and run python. Input "import nest". If you see this message, so all great.

> ------------- N E S T --------------

> Copyright (C) 2004 The NEST Initiative

>  Version 2.4.2 Nov 15 2014 00:38:07

>  ... ... ... ...

**Installation completed! But ...**

#### 7. If you use PyCharm
> Settings -> Project:"title" -> ProjectStructure -> Add Content root -> choose "site-packages" from NEST folder. Mark as "Sources".

> **Thanks to member ILDAR9 for PyCharm instruсtion :)**

---
#### Change Python version (if you need)
```bash
sudo unlink /usr/bin/python
sudo ln -s /usr/bin/pythonX.Y /usr/bin/python
```
