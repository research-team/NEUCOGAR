import math
import numpy as np
import matplotlib.pyplot as plt

def trapsyn(dt, Tfin, gsyn):
	VCl = -68; #mV
	Cm = 1; #micro F/cm^2
	gCl = 0.3; #mS/cm^2
	z = 2./dt;
	Nt = int(math.ceil(1 + Tfin / dt)); #number of time steps
	V = np.zeros((Nt, 1)); t = np.zeros((Nt, 1)); #preallocate space
	g = np.zeros((Nt, np.size(gsyn['gmax']) ));
	j = 0;
	V[0] = VCl;
	a0 = gCl / Cm; b0 = gCl * VCl / Cm;
	for j in xrange(1, Nt):
		t[ j ] = (j - 1) * dt;
		g[j, :] = gsyn['gmax'] * ((t[j] -gsyn['t1']) / gsyn['taua'] ) * np.exp(1 - (t[j] - gsyn['t1'])/gsyn['taua']) * ( t[j] > gsyn['t1'] )
		a1 = (gCl + sum(g[j, :])) / Cm;
		tmp = np.dot(g[j, :], gsyn['Vsyn'].T);
		b1 = (gCl*VCl + np.dot(g[j, :], gsyn['Vsyn'].T) )/Cm;
		V[ j ] = ( (z - a0) * V[j-1] + b0 + b1) / (z + a1);
		a0 = a1;
		b0 = b1
	return t, V, g

def main():
	gsyn = {"gmax":np.array([[0.2]]), "taua":np.array([[2.0]]), "t1":np.array([[5.0]]), "Vsyn":np.array([[0.0]])};
	[t, V1, g1] = trapsyn(0.01, 35, gsyn);
	gsyn2 = {"gmax":0.2 * np.array([[1., 1.]]), "taua":2 * np.array([[1., 1.]]), "t1":np.array([[4., 5.]]), "Vsyn":np.array([[-68, 0]])}
	[t, V2, g2] = trapsyn(0.01, 35, gsyn2);
	
	plt.plot(t, g1, t, g2);
	plt.legend(("exitatory,solo", "inhibitory, paired", "excitatory, paired"))
	plt.xlabel('Time(ms)');
	plt.ylabel('g_syn(mS/cm^2)');
	plt.show()

	plt.plot(t, V1, t, V2);
	plt.legend(("excitatory only", "inhibitory and excitatory"))
	plt.xlabel('Time(ms)');
	plt.ylabel('V(mV)');
	plt.show()

if __name__ == "__main__":
	main()