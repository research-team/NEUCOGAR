import numpy as np
from numpy import dot

from pybrain.structure.connections.connection import Connection


NM_INTENCITY = 1.0

class NMConnection(Connection):
    """Simulates neuromodulation with randomized connection"""

    def __init__(self, *args, **kwargs):
        Connection.__init__(self, *args, **kwargs)
        n = self.outdim  # self.indim*self.outdim # connect only 1 input neuron to random output
        # self.params = np.random.random_integers(0, 1, n)
        self.params = np.ones(n)
    def _forwardImplementation(self, inbuf, outbuf):
        # outbuf += self.params * inbuf[0]
        if inbuf[0] > 0 and inbuf[1] > 0: #in other words if both activated
            outbuf[1] -= self.params[1] * NM_INTENCITY # then we decrease potential of second neuron
        elif inbuf[0] < 0 and inbuf[1] < 0: # if no one activated
            outbuf[0] += self.params[0] * NM_INTENCITY # then we increase potential of first neuron

    def _backwardImplementation(self, outerr, inerr, inbuf):
        inerr += dot(self.params, outerr)

    # no calculation for self.derivs - we don't want to "educate" this connection
    # this is why we don't inherit `ParameterContainer`
