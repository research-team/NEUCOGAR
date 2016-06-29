from func import *


logger = logging.getLogger('neuromodulation')
startbuild = datetime.datetime.now()

nest.ResetKernel()
nest.SetKernelStatus({'overwrite_files': True,
                      'local_num_threads': 4,
                      'resolution': 0.1})

generate_neurons(3000)

# parameters of synapse models

nest.CopyModel('stdp_synapse', glu_synapse, STDP_synparams_Glu)
nest.CopyModel('stdp_synapse', gaba_synapse, STDP_synparams_GABA)


logger.debug("* * * Start connection initialisation")



'''
spike out of thalamus *******************************************************
'''
#to 1 collumn
connect(thalamus[thalamus_Glu], l6[l6_Glu], syn_type=Glu)
connect(thalamus[thalamus_Glu], l5[l5_Glu], syn_type=Glu)
connect(thalamus[thalamus_Glu], l4[l4_Glu1], syn_type=Glu)
connect(thalamus[thalamus_Glu], l4[l4_Glu0], syn_type=Glu)
connect(thalamus[thalamus_Glu], l4[l4_Gaba0], syn_type=Glu)
connect(thalamus[thalamus_Glu], l3[l3_Glu1], syn_type=Glu)
connect(thalamus[thalamus_Glu], l3[l3_Gaba1], syn_type=Glu)
#to 2 collumn
connect(thalamus[thalamus_Glu], l6c2[l6c2_Glu], syn_type=Glu)
connect(thalamus[thalamus_Glu], l5c2[l5c2_Glu], syn_type=Glu)
connect(thalamus[thalamus_Glu], l4c2[l4c2_Glu1], syn_type=Glu)
connect(thalamus[thalamus_Glu], l4c2[l4c2_Glu0], syn_type=Glu)
connect(thalamus[thalamus_Glu], l4c2[l4c2_Gaba0], syn_type=Glu)
connect(thalamus[thalamus_Glu], l3c2[l3c2_Glu1], syn_type=Glu)
connect(thalamus[thalamus_Glu], l3c2[l3c2_Gaba1], syn_type=Glu)
#to 3 collumn
connect(thalamus[thalamus_Glu], l6c3[l6c3_Glu], syn_type=Glu)
connect(thalamus[thalamus_Glu], l5c3[l5c3_Glu], syn_type=Glu)
connect(thalamus[thalamus_Glu], l4c3[l4c3_Glu1], syn_type=Glu)
connect(thalamus[thalamus_Glu], l4c3[l4c3_Glu0], syn_type=Glu)
connect(thalamus[thalamus_Glu], l4c3[l4c3_Gaba0], syn_type=Glu)
connect(thalamus[thalamus_Glu], l3c3[l3c3_Glu1], syn_type=Glu)
connect(thalamus[thalamus_Glu], l3c3[l3c3_Gaba1], syn_type=Glu)
#to 4 collumn
connect(thalamus[thalamus_Glu], l6c4[l6c4_Glu], syn_type=Glu)
connect(thalamus[thalamus_Glu], l5c4[l5c4_Glu], syn_type=Glu)
connect(thalamus[thalamus_Glu], l4c4[l4c4_Glu1], syn_type=Glu)
connect(thalamus[thalamus_Glu], l4c4[l4c4_Glu0], syn_type=Glu)
connect(thalamus[thalamus_Glu], l4c4[l4c4_Gaba0], syn_type=Glu)
connect(thalamus[thalamus_Glu], l3c4[l3c4_Glu1], syn_type=Glu)
connect(thalamus[thalamus_Glu], l3c4[l3c4_Gaba1], syn_type=Glu)
#to 5 collumn
connect(thalamus[thalamus_Glu], l6c5[l6c5_Glu], syn_type=Glu)
connect(thalamus[thalamus_Glu], l5c5[l5c5_Glu], syn_type=Glu)
connect(thalamus[thalamus_Glu], l4c5[l4c5_Glu1], syn_type=Glu)
connect(thalamus[thalamus_Glu], l4c5[l4c5_Glu0], syn_type=Glu)
connect(thalamus[thalamus_Glu], l4c5[l4c5_Gaba0], syn_type=Glu)
connect(thalamus[thalamus_Glu], l3c5[l3c5_Glu1], syn_type=Glu)
connect(thalamus[thalamus_Glu], l3c5[l3c5_Gaba1], syn_type=Glu)
#to 6 collumn
connect(thalamus[thalamus_Glu], l6c6[l6c6_Glu], syn_type=Glu)
connect(thalamus[thalamus_Glu], l5c6[l5c6_Glu], syn_type=Glu)
connect(thalamus[thalamus_Glu], l4c6[l4c6_Glu1], syn_type=Glu)
connect(thalamus[thalamus_Glu], l4c6[l4c6_Glu0], syn_type=Glu)
connect(thalamus[thalamus_Glu], l4c6[l4c6_Gaba0], syn_type=Glu)
connect(thalamus[thalamus_Glu], l3c6[l3c6_Glu1], syn_type=Glu)
connect(thalamus[thalamus_Glu], l3c6[l3c6_Gaba1], syn_type=Glu)
#to 7 collumn
connect(thalamus[thalamus_Glu], l6c7[l6c7_Glu], syn_type=Glu)
connect(thalamus[thalamus_Glu], l5c7[l5c7_Glu], syn_type=Glu)
connect(thalamus[thalamus_Glu], l4c7[l4c7_Glu1], syn_type=Glu)
connect(thalamus[thalamus_Glu], l4c7[l4c7_Glu0], syn_type=Glu)
connect(thalamus[thalamus_Glu], l4c7[l4c7_Gaba0], syn_type=Glu)
connect(thalamus[thalamus_Glu], l3c7[l3c7_Glu1], syn_type=Glu)
connect(thalamus[thalamus_Glu], l3c7[l3c7_Gaba1], syn_type=Glu)
#to 8 collumn
connect(thalamus[thalamus_Glu], l6c8[l6c8_Glu], syn_type=Glu)
connect(thalamus[thalamus_Glu], l5c8[l5c8_Glu], syn_type=Glu)
connect(thalamus[thalamus_Glu], l4c8[l4c8_Glu1], syn_type=Glu)
connect(thalamus[thalamus_Glu], l4c8[l4c8_Glu0], syn_type=Glu)
connect(thalamus[thalamus_Glu], l4c8[l4c8_Gaba0], syn_type=Glu)
connect(thalamus[thalamus_Glu], l3c8[l3c8_Glu1], syn_type=Glu)
connect(thalamus[thalamus_Glu], l3c8[l3c8_Gaba1], syn_type=Glu)
#to 9 collumn
connect(thalamus[thalamus_Glu], l6c9[l6c9_Glu], syn_type=Glu)
connect(thalamus[thalamus_Glu], l5c9[l5c9_Glu], syn_type=Glu)
connect(thalamus[thalamus_Glu], l4c9[l4c9_Glu1], syn_type=Glu)
connect(thalamus[thalamus_Glu], l4c9[l4c9_Glu0], syn_type=Glu)
connect(thalamus[thalamus_Glu], l4c9[l4c9_Gaba0], syn_type=Glu)
connect(thalamus[thalamus_Glu], l3c9[l3c9_Glu1], syn_type=Glu)
connect(thalamus[thalamus_Glu], l3c9[l3c9_Gaba1], syn_type=Glu)


'''
connect layers gaba,glu into collumns *******************************************
'''
# connect into collumn num. 1 **********************
connect(l2[l2_Gaba0], l4[l4_Glu0], syn_type=GABA, weight_coef=0.000005)
connect(l3[l3_Gaba0], l3[l3_Glu1], syn_type=GABA, weight_coef=0.00005)
connect(l3[l3_Gaba1], l3[l3_Glu1], syn_type=GABA, weight_coef=0.0001)
connect(l3[l3_Glu1], thalamus[thalamus_Glu], syn_type=GABA, weight_coef=0.00005)
connect(l4[l4_Glu0], l3[l3_Glu1], syn_type=Glu)
connect(l4[l4_Glu0], l2[l2_Gaba1], syn_type=Glu)
connect(l4[l4_Glu1], l3[l3_Glu1], syn_type=Glu)
connect(l4[l4_Gaba0], l2[l2_Gaba0], syn_type=GABA, weight_coef=0.00005)
connect(l5[l5_Glu], l3[l3_Glu1], syn_type=Glu)
connect(l5[l5_Glu], l3[l3_Gaba1], syn_type=Glu)
connect(l5[l5_Glu], l3[l3_Gaba0], syn_type=Glu)
connect(l5[l5_Glu], l2[l2_Gaba0], syn_type=Glu)
connect(l6[l6_Glu], l4[l4_Glu1], syn_type=Glu)
# connect into collumn num. 2 **********************
connect(l2c2[l2c2_Gaba0], l4c2[l4c2_Glu0], syn_type=GABA, weight_coef=0.000005)
connect(l3c2[l3c2_Gaba0], l3c2[l3c2_Glu1], syn_type=GABA, weight_coef=0.00005)
connect(l3c2[l3c2_Gaba1], l3c2[l3c2_Glu1], syn_type=GABA, weight_coef=0.0001)
connect(l3c2[l3c2_Glu1], thalamus[thalamus_Glu], syn_type=GABA, weight_coef=0.00005)
connect(l4c2[l4c2_Glu0], l3c2[l3c2_Glu1], syn_type=Glu)
connect(l4c2[l4c2_Glu0], l2c2[l2c2_Gaba1], syn_type=Glu)
connect(l4c2[l4c2_Glu1], l3c2[l3c2_Glu1], syn_type=Glu)
connect(l4c2[l4c2_Gaba0], l2c2[l2c2_Gaba0], syn_type=GABA, weight_coef=0.00005)
connect(l5c2[l5c2_Glu], l3c2[l3c2_Glu1], syn_type=Glu)
connect(l5c2[l5c2_Glu], l3c2[l3c2_Gaba1], syn_type=Glu)
connect(l5c2[l5c2_Glu], l3c2[l3c2_Gaba0], syn_type=Glu)
connect(l5c2[l5c2_Glu], l2c2[l2c2_Gaba0], syn_type=Glu)
connect(l6c2[l6c2_Glu], l4c2[l4c2_Glu1], syn_type=Glu)
# connect into collumn num. 3 **********************
connect(l2c3[l2c3_Gaba0], l4c3[l4c3_Glu0], syn_type=GABA, weight_coef=0.000005)
connect(l3c3[l3c3_Gaba0], l3c3[l3c3_Glu1], syn_type=GABA, weight_coef=0.00005)
connect(l3c3[l3c3_Gaba1], l3c3[l3c3_Glu1], syn_type=GABA, weight_coef=0.0001)
connect(l3c3[l3c3_Glu1], thalamus[thalamus_Glu], syn_type=GABA, weight_coef=0.00005)
connect(l4c3[l4c3_Glu0], l3c3[l3c3_Glu1], syn_type=Glu)
connect(l4c3[l4c3_Glu0], l2c3[l2c3_Gaba1], syn_type=Glu)
connect(l4c3[l4c3_Glu1], l3c3[l3c3_Glu1], syn_type=Glu)
connect(l4c3[l4c3_Gaba0], l2c3[l2c3_Gaba0], syn_type=GABA, weight_coef=0.00005)
connect(l5c3[l5c3_Glu], l3c3[l3c3_Glu1], syn_type=Glu)
connect(l5c3[l5c3_Glu], l3c3[l3c3_Gaba1], syn_type=Glu)
connect(l5c3[l5c3_Glu], l3c3[l3c3_Gaba0], syn_type=Glu)
connect(l5c3[l5c3_Glu], l2c3[l2c3_Gaba0], syn_type=Glu)
connect(l6c3[l6c3_Glu], l4c3[l4c3_Glu1], syn_type=Glu)
# connect into collumn num. 4 **********************
connect(l2c4[l2c4_Gaba0], l4c4[l4c4_Glu0], syn_type=GABA, weight_coef=0.000005)
connect(l3c4[l3c4_Gaba0], l3c4[l3c4_Glu1], syn_type=GABA, weight_coef=0.00005)
connect(l3c4[l3c4_Gaba1], l3c4[l3c4_Glu1], syn_type=GABA, weight_coef=0.0001)
connect(l3c4[l3c4_Glu1], thalamus[thalamus_Glu], syn_type=GABA, weight_coef=0.00005)
connect(l4c4[l4c4_Glu0],  l3c4[l3c4_Glu1], syn_type=Glu)
connect(l4c4[l4c4_Glu0],  l2c4[l2c4_Gaba1], syn_type=Glu)
connect(l4c4[l4c4_Glu1],  l3c4[l3c4_Glu1], syn_type=Glu)
connect(l4c4[l4c4_Gaba0], l2c4[l2c4_Gaba0], syn_type=GABA, weight_coef=0.00005)
connect(l5c4[l5c4_Glu],   l3c4[l3c4_Glu1], syn_type=Glu)
connect(l5c4[l5c4_Glu],   l3c4[l3c4_Gaba1], syn_type=Glu)
connect(l5c4[l5c4_Glu],   l3c4[l3c4_Gaba0], syn_type=Glu)
connect(l5c4[l5c4_Glu],   l2c4[l2c4_Gaba0], syn_type=Glu)
connect(l6c4[l6c4_Glu],   l4c4[l4c4_Glu1], syn_type=Glu)
# connect into collumn num. 5 **********************
connect(l2c5[l2c5_Gaba0], l4c5[l4c5_Glu0], syn_type=GABA, weight_coef=0.000005)
connect(l3c5[l3c5_Gaba0], l3c5[l3c5_Glu1], syn_type=GABA, weight_coef=0.00005)
connect(l3c5[l3c5_Gaba1], l3c5[l3c5_Glu1], syn_type=GABA, weight_coef=0.0001)
connect(l3c5[l3c5_Glu1], thalamus[thalamus_Glu], syn_type=GABA, weight_coef=0.00005)
connect(l4c5[l4c5_Glu0],  l3c5[l3c5_Glu1], syn_type=Glu)
connect(l4c5[l4c5_Glu0],  l2c5[l2c5_Gaba1], syn_type=Glu)
connect(l4c5[l4c5_Glu1],  l3c5[l3c5_Glu1], syn_type=Glu)
connect(l4c5[l4c5_Gaba0], l2c5[l2c5_Gaba0], syn_type=GABA, weight_coef=0.00005)
connect(l5c5[l5c5_Glu],   l3c5[l3c5_Glu1], syn_type=Glu)
connect(l5c5[l5c5_Glu],   l3c5[l3c5_Gaba1], syn_type=Glu)
connect(l5c5[l5c5_Glu],   l3c5[l3c5_Gaba0], syn_type=Glu)
connect(l5c5[l5c5_Glu],   l2c5[l2c5_Gaba0], syn_type=Glu)
connect(l6c5[l6c5_Glu],   l4c5[l4c5_Glu1], syn_type=Glu)
# connect into collumn num. 6 **********************
connect(l2c6[l2c6_Gaba0], l4c6[l4c6_Glu0], syn_type=GABA, weight_coef=0.000005)
connect(l3c6[l3c6_Gaba0], l3c6[l3c6_Glu1], syn_type=GABA, weight_coef=0.00005)
connect(l3c6[l3c6_Gaba1], l3c6[l3c6_Glu1], syn_type=GABA, weight_coef=0.0001)
connect(l3c6[l3c6_Glu1], thalamus[thalamus_Glu], syn_type=GABA, weight_coef=0.00005)
connect(l4c6[l4c6_Glu0],  l3c6[l3c6_Glu1], syn_type=Glu)
connect(l4c6[l4c6_Glu0],  l2c6[l2c6_Gaba1], syn_type=Glu)
connect(l4c6[l4c6_Glu1],  l3c6[l3c6_Glu1], syn_type=Glu)
connect(l4c6[l4c6_Gaba0], l2c6[l2c6_Gaba0], syn_type=GABA, weight_coef=0.00005)
connect(l5c6[l5c6_Glu],   l3c6[l3c6_Glu1], syn_type=Glu)
connect(l5c6[l5c6_Glu],   l3c6[l3c6_Gaba1], syn_type=Glu)
connect(l5c6[l5c6_Glu],   l3c6[l3c6_Gaba0], syn_type=Glu)
connect(l5c6[l5c6_Glu],   l2c6[l2c6_Gaba0], syn_type=Glu)
connect(l6c6[l6c6_Glu],   l4c6[l4c6_Glu1], syn_type=Glu)
# connect into collumn num. 7 **********************
connect(l2c7[l2c7_Gaba0], l4c7[l4c7_Glu0], syn_type=GABA, weight_coef=0.000005)
connect(l3c7[l3c7_Gaba0], l3c7[l3c7_Glu1], syn_type=GABA, weight_coef=0.00005)
connect(l3c7[l3c7_Gaba1], l3c7[l3c7_Glu1], syn_type=GABA, weight_coef=0.0001)
connect(l3c7[l3c7_Glu1], thalamus[thalamus_Glu], syn_type=GABA, weight_coef=0.00005)
connect(l4c7[l4c7_Glu0],  l3c7[l3c7_Glu1], syn_type=Glu)
connect(l4c7[l4c7_Glu0],  l2c7[l2c7_Gaba1], syn_type=Glu)
connect(l4c7[l4c7_Glu1],  l3c7[l3c7_Glu1], syn_type=Glu)
connect(l4c7[l4c7_Gaba0], l2c7[l2c7_Gaba0], syn_type=GABA, weight_coef=0.00005)
connect(l5c7[l5c7_Glu],   l3c7[l3c7_Glu1], syn_type=Glu)
connect(l5c7[l5c7_Glu],   l3c7[l3c7_Gaba1], syn_type=Glu)
connect(l5c7[l5c7_Glu],   l3c7[l3c7_Gaba0], syn_type=Glu)
connect(l5c7[l5c7_Glu],   l2c7[l2c7_Gaba0], syn_type=Glu)
connect(l6c7[l6c7_Glu],   l4c7[l4c7_Glu1], syn_type=Glu)
# connect into collumn num. 8 **********************
connect(l2c8[l2c8_Gaba0], l4c8[l4c8_Glu0], syn_type=GABA, weight_coef=0.000005)
connect(l3c8[l3c8_Gaba0], l3c8[l3c8_Glu1], syn_type=GABA, weight_coef=0.00005)
connect(l3c8[l3c8_Gaba1], l3c8[l3c8_Glu1], syn_type=GABA, weight_coef=0.0001)
connect(l3c8[l3c8_Glu1], thalamus[thalamus_Glu], syn_type=GABA, weight_coef=0.00005)
connect(l4c8[l4c8_Glu0],  l3c8[l3c8_Glu1], syn_type=Glu)
connect(l4c8[l4c8_Glu0],  l2c8[l2c8_Gaba1], syn_type=Glu)
connect(l4c8[l4c8_Glu1],  l3c8[l3c8_Glu1], syn_type=Glu)
connect(l4c8[l4c8_Gaba0], l2c8[l2c8_Gaba0], syn_type=GABA, weight_coef=0.00005)
connect(l5c8[l5c8_Glu],   l3c8[l3c8_Glu1], syn_type=Glu)
connect(l5c8[l5c8_Glu],   l3c8[l3c8_Gaba1], syn_type=Glu)
connect(l5c8[l5c8_Glu],   l3c8[l3c8_Gaba0], syn_type=Glu)
connect(l5c8[l5c8_Glu],   l2c8[l2c8_Gaba0], syn_type=Glu)
connect(l6c8[l6c8_Glu],   l4c8[l4c8_Glu1], syn_type=Glu)
# connect into collumn num. 9 **********************
connect(l2c9[l2c9_Gaba0], l4c9[l4c9_Glu0], syn_type=GABA, weight_coef=0.000005)
connect(l3c9[l3c9_Gaba0], l3c9[l3c9_Glu1], syn_type=GABA, weight_coef=0.00005)
connect(l3c9[l3c9_Gaba1], l3c9[l3c9_Glu1], syn_type=GABA, weight_coef=0.0001)
connect(l3c9[l3c9_Glu1], thalamus[thalamus_Glu], syn_type=GABA, weight_coef=0.00005)
connect(l4c9[l4c9_Glu0],  l3c9[l3c9_Glu1], syn_type=Glu)
connect(l4c9[l4c9_Glu0],  l2c9[l2c9_Gaba1], syn_type=Glu)
connect(l4c9[l4c9_Glu1],  l3c9[l3c9_Glu1], syn_type=Glu)
connect(l4c9[l4c9_Gaba0], l2c9[l2c9_Gaba0], syn_type=GABA, weight_coef=0.00005)
connect(l5c9[l5c9_Glu],   l3c9[l3c9_Glu1], syn_type=Glu)
connect(l5c9[l5c9_Glu],   l3c9[l3c9_Gaba1], syn_type=Glu)
connect(l5c9[l5c9_Glu],   l3c9[l3c9_Gaba0], syn_type=Glu)
connect(l5c9[l5c9_Glu],   l2c9[l2c9_Gaba0], syn_type=Glu)
connect(l6c9[l6c9_Glu],   l4c9[l4c9_Glu1], syn_type=Glu)

'''
connect collumn with other collumn****************************************************
'''
'''
 1 | 2 | 3
 4 | 5 | 6
 7 | 8 | 9
'''
#collumn num.1
connect(l2[l2_Gaba1], l2c2[l2c2_Gaba1], syn_type=GABA)
connect(l2[l2_Gaba1], l2c4[l2c4_Gaba1], syn_type=GABA)
connect(l2[l2_Gaba1], l2c5[l2c5_Gaba1], syn_type=GABA)
#collumn num.2
connect(l2c2[l2c2_Gaba1], l2[l2_Gaba1], syn_type=GABA)
connect(l2c2[l2c2_Gaba1], l2c3[l2c3_Gaba1], syn_type=GABA)
connect(l2c2[l2c2_Gaba1], l2c4[l2c4_Gaba1], syn_type=GABA)
connect(l2c2[l2c2_Gaba1], l2c5[l2c5_Gaba1], syn_type=GABA)
connect(l2c2[l2c2_Gaba1], l2c6[l2c6_Gaba1], syn_type=GABA)
#collumn num.3
connect(l2c3[l2c3_Gaba1], l2c2[l2c2_Gaba1], syn_type=GABA)
connect(l2c3[l2c3_Gaba1], l2c5[l2c5_Gaba1], syn_type=GABA)
connect(l2c3[l2c3_Gaba1], l2c6[l2c6_Gaba1], syn_type=GABA)
#collumn num.4
connect(l2c4[l2c4_Gaba1], l2[l2_Gaba1], syn_type=GABA)
connect(l2c4[l2c4_Gaba1], l2c2[l2c2_Gaba1], syn_type=GABA)
connect(l2c4[l2c4_Gaba1], l2c7[l2c7_Gaba1], syn_type=GABA)
connect(l2c4[l2c4_Gaba1], l2c5[l2c5_Gaba1], syn_type=GABA)
connect(l2c4[l2c4_Gaba1], l2c8[l2c8_Gaba1], syn_type=GABA)
#collumn num.5
connect(l2c5[l2c5_Gaba1], l2[l2_Gaba1], syn_type=GABA)
connect(l2c5[l2c5_Gaba1], l2c2[l2c2_Gaba1], syn_type=GABA)
connect(l2c5[l2c5_Gaba1], l2c3[l2c3_Gaba1], syn_type=GABA)
connect(l2c5[l2c5_Gaba1], l2c4[l2c4_Gaba1], syn_type=GABA)
connect(l2c5[l2c5_Gaba1], l2c6[l2c6_Gaba1], syn_type=GABA)
connect(l2c5[l2c5_Gaba1], l2c7[l2c7_Gaba1], syn_type=GABA)
connect(l2c5[l2c5_Gaba1], l2c8[l2c8_Gaba1], syn_type=GABA)
connect(l2c5[l2c5_Gaba1], l2c9[l2c9_Gaba1], syn_type=GABA)
#collumn num.6
connect(l2c6[l2c6_Gaba1], l2c2[l2c2_Gaba1], syn_type=GABA)
connect(l2c6[l2c6_Gaba1], l2c3[l2c3_Gaba1], syn_type=GABA)
connect(l2c6[l2c6_Gaba1], l2c5[l2c5_Gaba1], syn_type=GABA)
connect(l2c6[l2c6_Gaba1], l2c8[l2c8_Gaba1], syn_type=GABA)
connect(l2c6[l2c6_Gaba1], l2c9[l2c9_Gaba1], syn_type=GABA)
#collumn num.7
connect(l2c7[l2c7_Gaba1], l2c4[l2c4_Gaba1], syn_type=GABA)
connect(l2c7[l2c7_Gaba1], l2c5[l2c5_Gaba1], syn_type=GABA)
connect(l2c7[l2c7_Gaba1], l2c8[l2c8_Gaba1], syn_type=GABA)
#collumn num.8
connect(l2c8[l2c8_Gaba1], l2c4[l2c4_Gaba1], syn_type=GABA)
connect(l2c8[l2c8_Gaba1], l2c5[l2c5_Gaba1], syn_type=GABA)
connect(l2c8[l2c8_Gaba1], l2c6[l2c6_Gaba1], syn_type=GABA)
connect(l2c8[l2c8_Gaba1], l2c8[l2c8_Gaba1], syn_type=GABA)
connect(l2c8[l2c8_Gaba1], l2c7[l2c7_Gaba1], syn_type=GABA)
#collumn num.9
connect(l2c9[l2c9_Gaba1], l2c5[l2c5_Gaba1], syn_type=GABA)
connect(l2c9[l2c9_Gaba1], l2c6[l2c6_Gaba1], syn_type=GABA)
connect(l2c9[l2c9_Gaba1], l2c8[l2c8_Gaba1], syn_type=GABA)




logger.debug("* * * Creating spike generators...")



if generator_flag:
    connect_generator(thalamus[thalamus_Glu], rate=100, coef_part=1)


logger.debug("* * * Attaching spikes detector")
for part in getAllParts():
    connect_detector(part)

del generate_neurons, connect, connect_generator, connect_detector

endbuild = datetime.datetime.now()

simulate()
get_log(startbuild, endbuild)
save(GUI=status_gui)