import scipy as sp
import pylab as plt
from scipy.integrate import odeint


#=====================
# P A R A M E T E R S
#=====================

"""
    I   [mA]  milli-amp       Amperage
    V   [mV]  milli-volt      Voltage
    g   [mS]  milli-siemens   Conductance. For example 5 Om = 200 mS (5^(-1))
    C   [uF]  micro-farad     Capacitance
"""

C_m = 1.0       # Membrane capacitance, in uF/cm^2
g_Na = 120.0    # Sodium (Na) maximum conductances, in mS/cm^2
g_K = 36.0      # Postassium (K) maximum conductances, in mS/cm^2
g_L = 0.3       # Leak maximum conductances, in mS/cm^2
E_Na = 50.0     # Sodium (Na) Nernst reversal potentials, in mV
E_K = -77.0     # Postassium (K) Nernst reversal potentials, in mV
E_L = -54.387   # Leak Nernst reversal potentials, in mV

time = sp.arange(0.0, 40.0, 0.01) # The time to integrate over


#=====================
# CALCULATION OF CHANNELS
#=====================

""" NAF Fast NA """
# The formulas of HH and 'eaps' are same for Na
# ina = gbar * ( pow( m , exp_m ) ) * ( pow( h , exp_h ) ) * ( v - ena ) ;

# TODO: try to find and describe the full realization of channel
# Dm = Dm  / (1. - dt*( ( ( ( - 1.0 ) ) ) / mtau )) ;
# Dh = Dh  / (1. - dt*( ( ( ( - 1.0 ) ) ) / htau )) ;
#

""" NAX Fast NA Axonal"""
# the same functionality as NAF!!!

"""Channel Na+ gating kinetics. Functions of membrane voltage"""
def alpha_m(V):
    return 0.1 * (V + 40.0) / (1.0 - sp.exp( -(V + 40.0) / 10.0 ) )

def beta_m(V):
    return 4.0 * sp.exp(-(V + 65.0) / 18.0)


"""Channel Cl- gating kinetics. Functions of membrane voltage"""
def alpha_h(V):
    return 0.07 * sp.exp(-(V + 65.0) / 20.0)

def beta_h(V):
    return 1.0 / (1.0 + sp.exp(-(V + 35.0) / 10.0))


"""Channel K+ gating kinetics. Functions of membrane voltage"""
def alpha_n(V):
    return 0.01 * (V + 55.0) / (1.0 - sp.exp(-(V + 55.0) / 10.0))

def beta_n(V):
    return 0.125 * sp.exp(-(V + 65) / 80.0)


"""Membrane current (in uA/cm^2)"""
def I_Na(V, m, h):
    """
    :param V: voltage
    :param m: channel
    :param h: channel
    :return:
    """
    return g_Na * m ** 3 * h * (V - E_Na)

def I_K(V, n):
    """
    :param V: voltage
    :param n:
    :return:
    """
    return g_K * n ** 4 * (V - E_K)

def I_L(V):
    """
    :param V: voltage
    :return:
    """
    return g_L * (V - E_L)


"""External Current (in uA/cm^2)"""
def I_inj(t):
    return 30 * (t > 5) - 35 * (t > 30)


"""Calculate membrane potential & activation variables"""
def dALL_dt(X, t):
    """
    :param X: numpy.ndarray
    :param t: time (float)
    :return: dV_dt, dm_dt, dh_dt, dn_dt (all float64)
    """

    V, m, h, n = X

    dV_dt = I_inj(t) - I_Na(V, m, h) - I_K(V, n) - I_L(V) / C_m
    dm_dt = alpha_m(V) * (1.0 - m) - beta_m(V) * m
    dh_dt = alpha_h(V) * (1.0 - h) - beta_h(V) * h
    dn_dt = alpha_n(V) * (1.0 - n) - beta_n(V) * n
    return dV_dt, dm_dt, dh_dt, dn_dt


#=====================
# DRAWING AND COMPUTING
#=====================


def Main():
    # dy/dt    func | y0: V    m    h     n  | times
    X = odeint(dALL_dt, (-65, 0.05, 0.6, 0.32), time)
    V = X[:, 0]
    m = X[:, 1]
    h = X[:, 2]
    n = X[:, 3]
    ina = I_Na(V, m, h)
    ik = I_K(V, n)
    il = I_L(V)
    plt.figure()

    plt.subplot(4, 1, 1)
    plt.title('Hodgkin-Huxley Neuron')
    plt.plot(time, V, 'k')
    plt.ylabel('V (mV)')

    plt.subplot(4, 1, 2)
    plt.plot(time, ina, 'c', label='$I_{Na}$')
    plt.plot(time, ik, 'y', label='$I_{K}$')
    plt.plot(time, il, 'm', label='$I_{L}$')
    plt.ylabel('Current')
    plt.legend()

    plt.subplot(4, 1, 3)
    plt.plot(time, m, 'r', label='m (Na+)')
    plt.plot(time, h, 'g', label='h (Cl-)')
    plt.plot(time, n, 'b', label='n (K+)')
    plt.ylabel('Gating Value')
    plt.legend()

    plt.subplot(4, 1, 4)
    i_inj_values = [I_inj(ta) for ta in time]
    plt.plot(time, i_inj_values, 'k')
    plt.xlabel('t (ms)')
    plt.ylabel('$I_{inj}$ ($\\mu{A}/cm^2$)')
    plt.ylim(-1, 40)

    plt.show()


if __name__ == '__main__':
    Main()