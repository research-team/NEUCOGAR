from property import *
import nest.topology as tp
import nest.raster_plot
import nest
import math
import time
import matplotlib.pyplot as plt
from numpy import exp
import nest.voltage_trace
from func import *
nest.ResetKernel()



# neurons count
kol2= 24
kol3 =30
kol4 = 34
kol5 = 28
kol6 = 25
N = kol2+ kol3 + kol4 + kol5 + kol6
N_tal= 200
# glutamat neurons %
l2_Glu = 0.78
l3_Glu = 0.78
l4_GLu = 0.80
l5_Glu = 0.82
l6_Glu = 0.95
size = 7
bias_begin = 140. # minimal value for the bias current injection [pA]
bias_end = 200. # maximal value for the bias current injection [pA]
T = 600 # simulation time (ms)



'''
structure
'''
nest.CopyModel('iaf_psc_exp', 'pyr', iaf_neuronparams)
nest.CopyModel('iaf_psc_exp', 'in', iaf_neuronparams)
nest.CopyModel('stdp_synapse','exc',{'weight': 0.1})
nest.CopyModel('stdp_synapse','inh',{'weight': -18.0})


'''
Collumn num.1 ****************************************************************************
'''

# Layer2
row2_Glu = int(math.ceil(kol2*l2_Glu)/2)
row2_Gaba = (kol2 - row2_Glu*2)/2
sl2_Glu = tp.CreateLayer({'rows': row2_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [0., 0., 4.]})
sl2_Gaba = tp.CreateLayer({'rows': row2_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [0., 1., 4.]})
fig1 = tp.PlotLayer(sl2_Glu, nodesize=size, nodecolor='green')
fig2 = tp.PlotLayer(sl2_Gaba, nodesize=size, fig=fig1, nodecolor='red')


# Layer3
row3_Glu = int(math.ceil(kol3*l3_Glu)/2)
row3_Gaba = (kol3 - row3_Glu*2)/2
sl3_Glu = tp.CreateLayer({'rows': row3_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [0., 0., 5.]})
sl3_Gaba = tp.CreateLayer({'rows': row3_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [0., 1., 5.]})
fig2 = tp.PlotLayer(sl3_Glu, nodesize=size,fig=fig1, nodecolor='green')
fig2 = tp.PlotLayer(sl3_Gaba, nodesize=size, fig=fig1, nodecolor='red')


# Layer4
row4_Glu = int(math.ceil(kol4*l4_GLu)/2)
row4_Gaba = (kol4 - row4_Glu*2)/2
sl4_Glu = tp.CreateLayer({'rows': row4_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [0., 0., 3.]})
sl4_Gaba = tp.CreateLayer({'rows': row4_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [0., 1., 3.]})
fig2 = tp.PlotLayer(sl4_Glu, nodesize=size, nodecolor='green', fig=fig1)
fig2 = tp.PlotLayer(sl4_Gaba, nodesize=size, fig=fig1, nodecolor='red')

# Layer5
row5_Glu = int(math.ceil(kol5*l5_Glu)/2)
row5_Gaba = (kol5 - row5_Glu*2)/2
sl5_Glu = tp.CreateLayer({'rows': row5_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [0., 0., 2.]})
sl5_Gaba = tp.CreateLayer({'rows': row5_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [0., 1., 2.]})
fig2 = tp.PlotLayer(sl5_Glu, nodesize=size, nodecolor='green', fig=fig1)
fig2 = tp.PlotLayer(sl5_Gaba, nodesize=size, fig=fig1, nodecolor='red')

# Layer6
row6_Glu = int(math.ceil(kol6*l6_Glu)/2)
row6_Gaba = (kol6 - row6_Glu)/2
sl6_Glu = tp.CreateLayer({'rows': row6_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [0., 0., 1.]})
sl6_Gaba = tp.CreateLayer({'rows': row6_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [0., 1., 1.]})
fig2 = tp.PlotLayer(sl6_Glu, nodesize=size, nodecolor='green', fig=fig1)
fig2 = tp.PlotLayer(sl6_Gaba, nodesize=size, fig=fig1, nodecolor='red')


'''
Collumn num.2 ***********************************************************************
'''
# Layer2
row2_Glu = int(math.ceil(kol2*l2_Glu)/2)
row2_Gaba = (kol2 - row2_Glu*2)/2
sl2_Glu = tp.CreateLayer({'rows': row2_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [2., 0., 4.]})
sl2_Gaba = tp.CreateLayer({'rows': row2_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [2., 1., 4.]})
fig1 = tp.PlotLayer(sl2_Glu, nodesize=size, fig=fig2, nodecolor='green')
fig2 = tp.PlotLayer(sl2_Gaba, nodesize=size, fig=fig2, nodecolor='red')


# Layer3
row3_Glu = int(math.ceil(kol3*l3_Glu)/2)
row3_Gaba = (kol3 - row3_Glu*2)/2
sl3_Glu = tp.CreateLayer({'rows': row3_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [2., 0., 5.]})
sl3_Gaba = tp.CreateLayer({'rows': row3_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [2., 1., 5.]})
fig2 = tp.PlotLayer(sl3_Glu, nodesize=size,fig=fig1, nodecolor='green')
fig2 = tp.PlotLayer(sl3_Gaba, nodesize=size, fig=fig1, nodecolor='red')


# Layer4
row4_Glu = int(math.ceil(kol4*l4_GLu)/2)
row4_Gaba = (kol4 - row4_Glu*2)/2
sl4_Glu = tp.CreateLayer({'rows': row4_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [2., 0., 3.]})
sl4_Gaba = tp.CreateLayer({'rows': row4_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [2., 1., 3.]})
fig2 = tp.PlotLayer(sl4_Glu, nodesize=size, nodecolor='green', fig=fig1)
fig2 = tp.PlotLayer(sl4_Gaba, nodesize=size, fig=fig1, nodecolor='red')

# Layer5
row5_Glu = int(math.ceil(kol5*l5_Glu)/2)
row5_Gaba = (kol5 - row5_Glu*2)/2
sl5_Glu = tp.CreateLayer({'rows': row5_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [2., 0., 2.]})
sl5_Gaba = tp.CreateLayer({'rows': row5_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [2., 1., 2.]})
fig2 = tp.PlotLayer(sl5_Glu, nodesize=size, nodecolor='green', fig=fig1)
fig2 = tp.PlotLayer(sl5_Gaba, nodesize=size, fig=fig1, nodecolor='red')

# Layer6
row6_Glu = int(math.ceil(kol6*l6_Glu)/2)
row6_Gaba = (kol6 - row6_Glu)/2
sl6_Glu = tp.CreateLayer({'rows': row6_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [2., 0., 1.]})
sl6_Gaba = tp.CreateLayer({'rows': row6_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [2., 1., 1.]})
fig2 = tp.PlotLayer(sl6_Glu, nodesize=size, nodecolor='green', fig=fig1)
fig2 = tp.PlotLayer(sl6_Gaba, nodesize=size, fig=fig1, nodecolor='red')


'''
Collumn num.3 ***********************************************************************
'''
# Layer2
row2_Glu = int(math.ceil(kol2*l2_Glu)/2)
row2_Gaba = (kol2 - row2_Glu*2)/2
sl2_Glu = tp.CreateLayer({'rows': row2_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [4., 0., 4.]})
sl2_Gaba = tp.CreateLayer({'rows': row2_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [4., 1., 4.]})
fig1 = tp.PlotLayer(sl2_Glu, nodesize=size, fig=fig2, nodecolor='green')
fig2 = tp.PlotLayer(sl2_Gaba, nodesize=size, fig=fig2, nodecolor='red')


# Layer3
row3_Glu = int(math.ceil(kol3*l3_Glu)/2)
row3_Gaba = (kol3 - row3_Glu*2)/2
sl3_Glu = tp.CreateLayer({'rows': row3_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [4., 0., 5.]})
sl3_Gaba = tp.CreateLayer({'rows': row3_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [4., 1., 5.]})
fig2 = tp.PlotLayer(sl3_Glu, nodesize=size,fig=fig1, nodecolor='green')
fig2 = tp.PlotLayer(sl3_Gaba, nodesize=size, fig=fig1, nodecolor='red')


# Layer4
row4_Glu = int(math.ceil(kol4*l4_GLu)/2)
row4_Gaba = (kol4 - row4_Glu*2)/2
sl4_Glu = tp.CreateLayer({'rows': row4_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [4., 0., 3.]})
sl4_Gaba = tp.CreateLayer({'rows': row4_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [4., 1., 3.]})
fig2 = tp.PlotLayer(sl4_Glu, nodesize=size, nodecolor='green', fig=fig1)
fig2 = tp.PlotLayer(sl4_Gaba, nodesize=size, fig=fig1, nodecolor='red')

# Layer5
row5_Glu = int(math.ceil(kol5*l5_Glu)/2)
row5_Gaba = (kol5 - row5_Glu*2)/2
sl5_Glu = tp.CreateLayer({'rows': row5_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [4., 0., 2.]})
sl5_Gaba = tp.CreateLayer({'rows': row5_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [4., 1., 2.]})
fig2 = tp.PlotLayer(sl5_Glu, nodesize=size, nodecolor='green', fig=fig1)
fig2 = tp.PlotLayer(sl5_Gaba, nodesize=size, fig=fig1, nodecolor='red')

# Layer6
row6_Glu = int(math.ceil(kol6*l6_Glu)/2)
row6_Gaba = (kol6 - row6_Glu)/2
sl6_Glu = tp.CreateLayer({'rows': row6_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [4., 0., 1.]})
sl6_Gaba = tp.CreateLayer({'rows': row6_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [4., 1., 1.]})
fig2 = tp.PlotLayer(sl6_Glu, nodesize=size, nodecolor='green', fig=fig1)
fig2 = tp.PlotLayer(sl6_Gaba, nodesize=size, fig=fig1, nodecolor='red')


'''
Collumn num.5 ***********************************************************************
'''
# Layer2
row2_Glu = int(math.ceil(kol2*l2_Glu)/2)
row2_Gaba = (kol2 - row2_Glu*2)/2
sl2_Glu = tp.CreateLayer({'rows': row2_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [2., 2.5, 4.]})
sl2_Gaba = tp.CreateLayer({'rows': row2_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [2., 3.5, 4.]})
fig1 = tp.PlotLayer(sl2_Glu, nodesize=size, fig=fig2, nodecolor='green')
fig2 = tp.PlotLayer(sl2_Gaba, nodesize=size, fig=fig2, nodecolor='red')


# Layer3
row3_Glu = int(math.ceil(kol3*l3_Glu)/2)
row3_Gaba = (kol3 - row3_Glu*2)/2
sl3_Glu = tp.CreateLayer({'rows': row3_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [2., 2.5, 5.]})
sl3_Gaba = tp.CreateLayer({'rows': row3_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [2., 3.5, 5.]})
fig2 = tp.PlotLayer(sl3_Glu, nodesize=size,fig=fig1, nodecolor='green')
fig2 = tp.PlotLayer(sl3_Gaba, nodesize=size, fig=fig1, nodecolor='red')


# Layer4
row4_Glu = int(math.ceil(kol4*l4_GLu)/2)
row4_Gaba = (kol4 - row4_Glu*2)/2
sl4_Glu = tp.CreateLayer({'rows': row4_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [2., 2.5, 3.]})
sl4_Gaba = tp.CreateLayer({'rows': row4_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [2., 3.5, 3.]})
fig2 = tp.PlotLayer(sl4_Glu, nodesize=size, nodecolor='green', fig=fig1)
fig2 = tp.PlotLayer(sl4_Gaba, nodesize=size, fig=fig1, nodecolor='red')

# Layer5
row5_Glu = int(math.ceil(kol5*l5_Glu)/2)
row5_Gaba = (kol5 - row5_Glu*2)/2
sl5_Glu = tp.CreateLayer({'rows': row5_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [2., 2.5, 2.]})
sl5_Gaba = tp.CreateLayer({'rows': row5_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [2., 3.5, 2.]})
fig2 = tp.PlotLayer(sl5_Glu, nodesize=size, nodecolor='green', fig=fig1)
fig2 = tp.PlotLayer(sl5_Gaba, nodesize=size, fig=fig1, nodecolor='red')

# Layer6
row6_Glu = int(math.ceil(kol6*l6_Glu)/2)
row6_Gaba = (kol6 - row6_Glu)/2
sl6_Glu = tp.CreateLayer({'rows': row6_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [2., 2.5, 1.]})
sl6_Gaba = tp.CreateLayer({'rows': row6_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [2., 3.5, 1.]})
fig2 = tp.PlotLayer(sl6_Glu, nodesize=size, nodecolor='green', fig=fig1)
fig2 = tp.PlotLayer(sl6_Gaba, nodesize=size, fig=fig1, nodecolor='red')

'''
Collumn num.4 ***********************************************************************
'''
# Layer2
row2_Glu = int(math.ceil(kol2*l2_Glu)/2)
row2_Gaba = (kol2 - row2_Glu*2)/2
sl2_Glu = tp.CreateLayer({'rows': row2_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [0., 2.5, 4.]})
sl2_Gaba = tp.CreateLayer({'rows': row2_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [0., 3.5, 4.]})
fig1 = tp.PlotLayer(sl2_Glu, nodesize=size, fig=fig2, nodecolor='green')
fig2 = tp.PlotLayer(sl2_Gaba, nodesize=size, fig=fig2, nodecolor='red')


# Layer3
row3_Glu = int(math.ceil(kol3*l3_Glu)/2)
row3_Gaba = (kol3 - row3_Glu*2)/2
sl3_Glu = tp.CreateLayer({'rows': row3_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [0., 2.5, 5.]})
sl3_Gaba = tp.CreateLayer({'rows': row3_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [0., 3.5, 5.]})
fig2 = tp.PlotLayer(sl3_Glu, nodesize=size,fig=fig1, nodecolor='green')
fig2 = tp.PlotLayer(sl3_Gaba, nodesize=size, fig=fig1, nodecolor='red')


# Layer4
row4_Glu = int(math.ceil(kol4*l4_GLu)/2)
row4_Gaba = (kol4 - row4_Glu*2)/2
sl4_Glu = tp.CreateLayer({'rows': row4_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [0., 2.5, 3.]})
sl4_Gaba = tp.CreateLayer({'rows': row4_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [0., 3.5, 3.]})
fig2 = tp.PlotLayer(sl4_Glu, nodesize=size, nodecolor='green', fig=fig1)
fig2 = tp.PlotLayer(sl4_Gaba, nodesize=size, fig=fig1, nodecolor='red')

# Layer5
row5_Glu = int(math.ceil(kol5*l5_Glu)/2)
row5_Gaba = (kol5 - row5_Glu*2)/2
sl5_Glu = tp.CreateLayer({'rows': row5_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [0., 2.5, 2.]})
sl5_Gaba = tp.CreateLayer({'rows': row5_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [0., 3.5, 2.]})
fig2 = tp.PlotLayer(sl5_Glu, nodesize=size, nodecolor='green', fig=fig1)
fig2 = tp.PlotLayer(sl5_Gaba, nodesize=size, fig=fig1, nodecolor='red')

# Layer6
row6_Glu = int(math.ceil(kol6*l6_Glu)/2)
row6_Gaba = (kol6 - row6_Glu)/2
sl6_Glu = tp.CreateLayer({'rows': row6_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [0., 2.5, 1.]})
sl6_Gaba = tp.CreateLayer({'rows': row6_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [0., 3.5, 1.]})
fig2 = tp.PlotLayer(sl6_Glu, nodesize=size, nodecolor='green', fig=fig1)
fig2 = tp.PlotLayer(sl6_Gaba, nodesize=size, fig=fig1, nodecolor='red')


'''
Collumn num.6 ***********************************************************************
'''
# Layer2
row2_Glu = int(math.ceil(kol2*l2_Glu)/2)
row2_Gaba = (kol2 - row2_Glu*2)/2
sl2_Glu = tp.CreateLayer({'rows': row2_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [4., 2.5, 4.]})
sl2_Gaba = tp.CreateLayer({'rows': row2_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [4., 3.5, 4.]})
fig1 = tp.PlotLayer(sl2_Glu, nodesize=size, fig=fig2, nodecolor='green')
fig2 = tp.PlotLayer(sl2_Gaba, nodesize=size, fig=fig2, nodecolor='red')


# Layer3
row3_Glu = int(math.ceil(kol3*l3_Glu)/2)
row3_Gaba = (kol3 - row3_Glu*2)/2
sl3_Glu = tp.CreateLayer({'rows': row3_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [4., 2.5, 5.]})
sl3_Gaba = tp.CreateLayer({'rows': row3_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [4., 3.5, 5.]})
fig2 = tp.PlotLayer(sl3_Glu, nodesize=size,fig=fig1, nodecolor='green')
fig2 = tp.PlotLayer(sl3_Gaba, nodesize=size, fig=fig1, nodecolor='red')


# Layer4
row4_Glu = int(math.ceil(kol4*l4_GLu)/2)
row4_Gaba = (kol4 - row4_Glu*2)/2
sl4_Glu = tp.CreateLayer({'rows': row4_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [4., 2.5, 3.]})
sl4_Gaba = tp.CreateLayer({'rows': row4_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [4., 3.5, 3.]})
fig2 = tp.PlotLayer(sl4_Glu, nodesize=size, nodecolor='green', fig=fig1)
fig2 = tp.PlotLayer(sl4_Gaba, nodesize=size, fig=fig1, nodecolor='red')

# Layer5
row5_Glu = int(math.ceil(kol5*l5_Glu)/2)
row5_Gaba = (kol5 - row5_Glu*2)/2
sl5_Glu = tp.CreateLayer({'rows': row5_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [4., 2.5, 2.]})
sl5_Gaba = tp.CreateLayer({'rows': row5_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [4., 3.5, 2.]})
fig2 = tp.PlotLayer(sl5_Glu, nodesize=size, nodecolor='green', fig=fig1)
fig2 = tp.PlotLayer(sl5_Gaba, nodesize=size, fig=fig1, nodecolor='red')

# Layer6
row6_Glu = int(math.ceil(kol6*l6_Glu)/2)
row6_Gaba = (kol6 - row6_Glu)/2
sl6_Glu = tp.CreateLayer({'rows': row6_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [4., 2.5, 1.]})
sl6_Gaba = tp.CreateLayer({'rows': row6_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [4., 3.5, 1.]})
fig2 = tp.PlotLayer(sl6_Glu, nodesize=size, nodecolor='green', fig=fig1)
fig2 = tp.PlotLayer(sl6_Gaba, nodesize=size, fig=fig1, nodecolor='red')

'''
Collumn num.7 ***********************************************************************
'''
# Layer2
row2_Glu = int(math.ceil(kol2*l2_Glu)/2)
row2_Gaba = (kol2 - row2_Glu*2)/2
sl2_Glu = tp.CreateLayer({'rows': row2_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [0., 5., 4.]})
sl2_Gaba = tp.CreateLayer({'rows': row2_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [0., 6., 4.]})
fig1 = tp.PlotLayer(sl2_Glu, nodesize=size, fig=fig2, nodecolor='green')
fig2 = tp.PlotLayer(sl2_Gaba, nodesize=size, fig=fig2, nodecolor='red')


# Layer3
row3_Glu = int(math.ceil(kol3*l3_Glu)/2)
row3_Gaba = (kol3 - row3_Glu*2)/2
sl3_Glu = tp.CreateLayer({'rows': row3_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [0., 5., 5.]})
sl3_Gaba = tp.CreateLayer({'rows': row3_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [0., 6., 5.]})
fig2 = tp.PlotLayer(sl3_Glu, nodesize=size,fig=fig1, nodecolor='green')
fig2 = tp.PlotLayer(sl3_Gaba, nodesize=size, fig=fig1, nodecolor='red')


# Layer4
row4_Glu = int(math.ceil(kol4*l4_GLu)/2)
row4_Gaba = (kol4 - row4_Glu*2)/2
sl4_Glu = tp.CreateLayer({'rows': row4_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [0., 5., 3.]})
sl4_Gaba = tp.CreateLayer({'rows': row4_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [0., 6., 3.]})
fig2 = tp.PlotLayer(sl4_Glu, nodesize=size, nodecolor='green', fig=fig1)
fig2 = tp.PlotLayer(sl4_Gaba, nodesize=size, fig=fig1, nodecolor='red')

# Layer5
row5_Glu = int(math.ceil(kol5*l5_Glu)/2)
row5_Gaba = (kol5 - row5_Glu*2)/2
sl5_Glu = tp.CreateLayer({'rows': row5_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [0., 5., 2.]})
sl5_Gaba = tp.CreateLayer({'rows': row5_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [0., 6., 2.]})
fig2 = tp.PlotLayer(sl5_Glu, nodesize=size, nodecolor='green', fig=fig1)
fig2 = tp.PlotLayer(sl5_Gaba, nodesize=size, fig=fig1, nodecolor='red')

# Layer6
row6_Glu = int(math.ceil(kol6*l6_Glu)/2)
row6_Gaba = (kol6 - row6_Glu)/2
sl6_Glu = tp.CreateLayer({'rows': row6_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [0., 5., 1.]})
sl6_Gaba = tp.CreateLayer({'rows': row6_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [0., 6., 1.]})
fig2 = tp.PlotLayer(sl6_Glu, nodesize=size, nodecolor='green', fig=fig1)
fig2 = tp.PlotLayer(sl6_Gaba, nodesize=size, fig=fig1, nodecolor='red')

'''
Collumn num.8 ***********************************************************************
'''
# Layer2
row2_Glu = int(math.ceil(kol2*l2_Glu)/2)
row2_Gaba = (kol2 - row2_Glu*2)/2
sl2_Glu = tp.CreateLayer({'rows': row2_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [2., 5., 4.]})
sl2_Gaba = tp.CreateLayer({'rows': row2_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [2., 6., 4.]})
fig1 = tp.PlotLayer(sl2_Glu, nodesize=size, fig=fig2, nodecolor='green')
fig2 = tp.PlotLayer(sl2_Gaba, nodesize=size, fig=fig2, nodecolor='red')


# Layer3
row3_Glu = int(math.ceil(kol3*l3_Glu)/2)
row3_Gaba = (kol3 - row3_Glu*2)/2
sl3_Glu = tp.CreateLayer({'rows': row3_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [2., 5., 5.]})
sl3_Gaba = tp.CreateLayer({'rows': row3_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [2., 6., 5.]})
fig2 = tp.PlotLayer(sl3_Glu, nodesize=size,fig=fig1, nodecolor='green')
fig2 = tp.PlotLayer(sl3_Gaba, nodesize=size, fig=fig1, nodecolor='red')


# Layer4
row4_Glu = int(math.ceil(kol4*l4_GLu)/2)
row4_Gaba = (kol4 - row4_Glu*2)/2
sl4_Glu = tp.CreateLayer({'rows': row4_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [2., 5., 3.]})
sl4_Gaba = tp.CreateLayer({'rows': row4_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [2., 6., 3.]})
fig2 = tp.PlotLayer(sl4_Glu, nodesize=size, nodecolor='green', fig=fig1)
fig2 = tp.PlotLayer(sl4_Gaba, nodesize=size, fig=fig1, nodecolor='red')

# Layer5
row5_Glu = int(math.ceil(kol5*l5_Glu)/2)
row5_Gaba = (kol5 - row5_Glu*2)/2
sl5_Glu = tp.CreateLayer({'rows': row5_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [2., 5., 2.]})
sl5_Gaba = tp.CreateLayer({'rows': row5_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [2., 6., 2.]})
fig2 = tp.PlotLayer(sl5_Glu, nodesize=size, nodecolor='green', fig=fig1)
fig2 = tp.PlotLayer(sl5_Gaba, nodesize=size, fig=fig1, nodecolor='red')

# Layer6
row6_Glu = int(math.ceil(kol6*l6_Glu)/2)
row6_Gaba = (kol6 - row6_Glu)/2
sl6_Glu = tp.CreateLayer({'rows': row6_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [2., 5., 1.]})
sl6_Gaba = tp.CreateLayer({'rows': row6_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [2., 6., 1.]})
fig2 = tp.PlotLayer(sl6_Glu, nodesize=size, nodecolor='green', fig=fig1)
fig2 = tp.PlotLayer(sl6_Gaba, nodesize=size, fig=fig1, nodecolor='red')

'''
Collumn num.9 ***********************************************************************
'''
# Layer2
row2_Glu = int(math.ceil(kol2*l2_Glu)/2)
row2_Gaba = (kol2 - row2_Glu*2)/2
sl2_Glu = tp.CreateLayer({'rows': row2_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [4., 5., 4.]})
sl2_Gaba = tp.CreateLayer({'rows': row2_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [4., 6., 4.]})
fig1 = tp.PlotLayer(sl2_Glu, nodesize=size, fig=fig2, nodecolor='green')
fig2 = tp.PlotLayer(sl2_Gaba, nodesize=size, fig=fig2, nodecolor='red')


# Layer3
row3_Glu = int(math.ceil(kol3*l3_Glu)/2)
row3_Gaba = (kol3 - row3_Glu*2)/2
sl3_Glu = tp.CreateLayer({'rows': row3_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [4., 5., 5.]})
sl3_Gaba = tp.CreateLayer({'rows': row3_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [4., 6., 5.]})
fig2 = tp.PlotLayer(sl3_Glu, nodesize=size,fig=fig1, nodecolor='green')
fig2 = tp.PlotLayer(sl3_Gaba, nodesize=size, fig=fig1, nodecolor='red')


# Layer4
row4_Glu = int(math.ceil(kol4*l4_GLu)/2)
row4_Gaba = (kol4 - row4_Glu*2)/2
sl4_Glu = tp.CreateLayer({'rows': row4_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [4., 5., 3.]})
sl4_Gaba = tp.CreateLayer({'rows': row4_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [4., 6., 3.]})
fig2 = tp.PlotLayer(sl4_Glu, nodesize=size, nodecolor='green', fig=fig1)
fig2 = tp.PlotLayer(sl4_Gaba, nodesize=size, fig=fig1, nodecolor='red')

# Layer5
row5_Glu = int(math.ceil(kol5*l5_Glu)/2)
row5_Gaba = (kol5 - row5_Glu*2)/2
sl5_Glu = tp.CreateLayer({'rows': row5_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [4., 5., 2.]})
sl5_Gaba = tp.CreateLayer({'rows': row5_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [4., 6., 2.]})
fig2 = tp.PlotLayer(sl5_Glu, nodesize=size, nodecolor='green', fig=fig1)
fig2 = tp.PlotLayer(sl5_Gaba, nodesize=size, fig=fig1, nodecolor='red')

# Layer6
row6_Glu = int(math.ceil(kol6*l6_Glu)/2)
row6_Gaba = (kol6 - row6_Glu)/2
sl6_Glu = tp.CreateLayer({'rows': row6_Glu, 'columns': 5, 'layers': 1,
'elements': 'pyr',
'center': [4., 5., 1.]})
sl6_Gaba = tp.CreateLayer({'rows': row6_Gaba, 'columns': 5, 'layers': 1,
'elements': 'in',
'center': [4., 6., 1.]})
fig2 = tp.PlotLayer(sl6_Glu, nodesize=size, nodecolor='green', fig=fig1)
fig2 = tp.PlotLayer(sl6_Gaba, nodesize=size, fig=fig1, nodecolor='red')


plt.show()



