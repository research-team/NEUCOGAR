'''
Primal/initial dictionary of parts
It contains:
    EC: Enterial cortex
    CA1: Cornu ammonis 1
    CA3: Cornu ammonis 3
    DG: Dentate gyrus
    Sub: Subiculum
Prefix description:
    GABA - GABA
    Glu - glutamate
    ACh - acetylcholine
    NA  - noradreanaline
    DA  - dopamine
    SE  - serotonin
'''
from property import *
import numpy as np

enterial = ({k_name: 'Enterial cortex [GABA0]'},
 			{k_name: 'Enterial cortex [GABA1]'},
            {k_name: 'Enterial cortex [Glu]'},
            {k_name: 'Enterial cortex [ACh0]'},
            {k_name: 'Enterial cortex [ACh1]'},
            {k_name: 'Enterial cortex [NA]'},
            {k_name: 'Enterial cortex [DA0]'},
            {k_name: 'Enterial cortex [DA1]'},
            {k_name: 'Enterial cortex [DA2]'} )
enterial_GABA0, enterial_GABA1, enterial_Glu, enterial_ACh0, enterial_ACh1, enterial_NA, enterial_DA0, enterial_DA1, enterial_DA2 = np.arange(9)

dentate = ({k_name: 'Dentate gyrus [GABA]'},
		   {k_name: 'Dentate gyrus [Glu]'},
		   {k_name: 'Dentate gyrus [ACh]'},
		   {k_name: 'Dentate gyrus [NA]'},
		   {k_name: 'Dentate gyrus [DA]'},
		   {k_name: 'Dentate gyrus [SE]'} )
dentate_GABA, dentate_Glu, dentate_ACh, dentate_NA, dentate_DA, dentate_SE = np.arange(6)

#CA3 GABA1 Recheck
CA3 = ({k_name: 'CA3 [GABA0]'},
	   {k_name: 'CA3 [GABA1]'},
 	   {k_name: 'CA3 [Glu]'},
 	   {k_name: 'CA3 [ACh0]'},
 	   {k_name: 'CA3 [ACh1]'},
 	   {k_name: 'CA3 [NA]'},
 	   {k_name: 'CA3 [DA]'},
 	   {k_name: 'CA3 [SE]'} )
CA3_GABA0, CA3_GABA1, CA3_Glu, CA3_ACh0, CA3_ACh1, CA3_NA, CA3_DA, CA3_SE  = np.arange(8)

CA1 = ({k_name: 'CA1 [GABA]'},
	   {k_name: 'CA1 [Glu]'},
	   {k_name: 'CA1 [ACh]'},
	   {k_name: 'CA1 [DA]'} )
CA1_GABA, CA1_Glu, CA1_ACh, CA1_DA = np.arange(4)

Sub = ({k_name: 'Sub [GABA]'},
	   {k_name: 'Sub [Glu]'} )
sub_GABA, sub_Glu = np.arange(2)