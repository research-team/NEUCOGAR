Izhikevich - *.m files by E. Izhikevich
1) net.m is from "2003 - Izhikevich - Simple Model of Spiking Neurons"
2) spnet.m is from "2006 - Izhikevich - Polychronization Computation with Spikes"
3) dasp.net is from "2007 - Izhikevich - Solving the distal reward problem through linkage of STDP and dopamine signaling"
All publications are there: http://www.izhikevich.org/publications/index.htm

test_network - my tests, based on Izhikevich's works. 
Description in commented part of each file. 
Each file is a single executable program w/o dependencies.
1) net_test.m - Simple network of 1000 leaky quadratic neurons. No STDP. No modulation.
2) ht5stdpspnet_test.m - Network of 1000 leaky neurons with STDP. Dopamine modulaion. Serotonin modulation (in two ways: by chaning of its fade rate, and by changing its value).