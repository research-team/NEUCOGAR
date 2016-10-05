# Interneuronal connectivity schemes

The real connectivity schemes are partially unknown, as very little experimental data is available.
It is known that connection probability is distance dependent in some experiments 
and is uniform within restricted neighbourhood in others.

In simulations three schemes are widely used, most of them based on random connections

We will consider all these three schemes with focus on the scaling behaviour

* **Full connectivity** - all connected to all
    ![Full connectivity with 9 neurons](http://neuronaldynamics.epfl.ch/online/x289.png) 
    ![Full connectivity with 18 neurons](http://neuronaldynamics.epfl.ch/online/x292.png)
    
    Number of links doubles when the size doubles.
    The appropriate scaling law for connections strength is: 	
    _wij = J0/N_
    
    Also weights can be chosen from gaussian distribution with mean _J0/N_ and stddev _sigma0/sqrt(N)_

* **Random connections with fixed probability** - the probability _p_ of connection is the same for all neurons 
	
	![Random with fixed probability, 9 neurons](http://neuronaldynamics.epfl.ch/online/x290.png)
	![Random with fixed probability, 18 neurons](http://neuronaldynamics.epfl.ch/online/x293.png)
	
	In simulations there are two ways to achieve this:
	
  - select randomly among all N^2 connections with probability _p_ 
	(mean number of connections for a neuron will be _\<C> = p*N_)

  - for each neuron, select _p_ neurons randomly and connect
  
  As number of connections grows linearly with size N, the appropriate scaling law would be
  
  _wij = J0 / C = J0 / pN_
  
  
* **Random connections with fixed number of partners** - fix number of presynaptic partners _C_ 
  and choose them randomly for each neuron. 
  
  In that case no scaling needed for _wij_
  
  ![Random with fixed number, 9 neurons](http://neuronaldynamics.epfl.ch/online/x291.png)
  ![Random with fixed number, 18 neurons](http://neuronaldynamics.epfl.ch/online/x294.png)
  

##Balanced excitation and inhibition

Let's consider a network of two populations, one excitatory and one inhibitory. 
In such a network we can adjust weights so that mean input current will be zero for any neuron.
But when we increase N, the amount of fluctuation decreases, so we need a way to control fluctuations.

The appropriate scaling formula for such tuning would be:

_wij = J0 / sqrt(C) = J0 / sqrt(pN)_


##Distance dependent connectivity

Within a brain area, connection probability is often modeled as distance dependent.

There are two ways to do it:

- Full connectivity with strength decreasing with distance

  ![Full connectivity with decreasing strength](http://neuronaldynamics.epfl.ch/online/x310.png)

- Random connections with probability decreasing with distance 

  ![Random connections with decreasing probability](http://neuronaldynamics.epfl.ch/online/x309.png)

