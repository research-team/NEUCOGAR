Mesocorticolimbic pathway
===

This diagram was based on:
> **Differential nicotinic regulation of the nigrostriatal and mesolimbic
dopaminergic pathways: Implications for drug development**
*Sanna Janhunen Ã , Liisa Ahtee*
Division of Pharmacology and Toxicology, Faculty of Pharmacy, University of Helsinki, P.O. Box 56 (Viikinkaari 5), Helsinki, FIN-00014, Finland   
[Link](https://www.researchgate.net/c/nzt0d9/javascript/lib/pdfjs/web/viewer.html?file=https%3A%2F%2Fwww.researchgate.net%2Fprofile%2FSanna_Janhunen%2Fpublication%2F6656868_Janhunen_S_Ahtee_L_Differential_nicotinic_regulation_of_the_nigrostriatal_and_mesolimbic_dopaminergic_pathways_implications_for_drug_development_Neurosci_Biobehav_Rev_31_287-314%2Flinks%2F54acf9100cf21c47713a7d1b.pdf%3FinViewer%3D1%26pdfJsDownload%3D1%26origin%3Dpublication_detail)

Origin
---
![mesocorticolimbic](https://github.com/research-team/NEUCOGAR/blob/master/nest/mesolimbic/description/mesolimbic.png)  
![legend](https://github.com/research-team/NEUCOGAR/blob/master/nest/mesolimbic/description/legend.png)

Description
---

#### PFC *(Prefrontal cortex)*
![pfc](https://github.com/research-team/NEUCOGAR/blob/master/nest/mesolimbic/description/pfc.png)

* **Ouputs**

| Source    | Destination | Connection        |
|----------:|:------------|-------------------|
|PFC[Glu0]  | VTA[DA0]    | Glutamatergic     |
|PFC[Glu1]  | NAc[GABA1]  | Glutamatergic     |
|PFC[Glu1]  | VTA[GABA2]  | Glutamatergic     |


* **Inputs**  

| Source    | Destination | Connection        |
|----------:|:------------|-------------------|
|VTA[GABA0] | PFC         | GABAergic         |
|VTA[DA0]   | PFC         | Dopaminergic      |

#### NAc *(Nucleus Accumbens)* core/shell?
![nac](https://github.com/research-team/NEUCOGAR/blob/master/nest/mesolimbic/description/nac.png)

* **Outputs**

| Source    | Destination | Connection        |
|----------:|:------------|-------------------|
|NAc[GABA1] | VTA[GABA2]  | GABAergic         |

* **Inputs**

| Source    | Destination | Connection        |
|----------:|:------------|-------------------|
|PFC[Glu1]  | NAc[GABA1]  | Glutamatergic     |
|VTA[DA1]   | NAc[GABA1]  | Dopaminergic      |
|VTA[GABA2] | NAc[GABA1]  | GABAergic         |

* **Interneurons**

| Source    | Destination | Connection        |
|----------:|:------------|-------------------|
|NAc[GABA0] | NAc[GABA1]  | GABAergic         |
|NAc[Ach]   | NAc[GABA1]  | Acetylcholinergic |

#### VTA *(Ventral Tegmental area)*
![vta](https://github.com/research-team/NEUCOGAR/blob/master/nest/mesolimbic/description/vta.png)

* **Outputs**

| Source    | Destination | Connection        |
|----------:|:------------|-------------------|
|VTA[GABA0] | Cortex      | GABAergic         |
|VTA[GABA0] | TPP[GABA0]  | GABAergic         |
|VTA[DA0]   | PFC         | dopaminergic      |
|VTA[DA1]   | NAc[GABA1]  | dopaminergic      |
|VTA[GABA2] | NAc[GABA1]  | GABAergic         |
	  
* **Inputs**  

| Source    | Destination | Connection        |
|----------:|:------------|-------------------|
|PFC[Glu1]  | VTA[GABA2]  | Glutamatergic     |
|PFC[Glu0]  | VTA[DA0]    | Glutamatergic     |
|NAc[GABA1] | VTA[GABA2]  | GABAergic         |
|TPP[Ach]   | VTA[GABA0]  | Acetylcholinergic |
|TPP[Ach]   | VTA[DA1]    | Acetylcholinergic |
|TPP[GLu]   | VTA[GABA0]  | Glutamatergic     |
|TPP[Glu]   | VTA[DA1]    | Glutamatergic     |

* **Interneurons**

| Source    | Destination | Connection        |
|----------:|:------------|-------------------|
|VTA[GABA1] | VTA[DA0]    | GABAergic         |
|VTA[GABA1] | VTA[DA1]    | GABAergic         |

#### TPP *(Pedunculopontine Tegmental nucleus / PPTg??)*
![tpp](https://github.com/research-team/NEUCOGAR/blob/master/nest/mesolimbic/description/tpp.png)

* **Outputs**

| Source    | Destination | Connection        |
|----------:|:------------|-------------------|
|TPP[GABA]  | VTA[GABA0]  | GABAergic         |
|TPP[Ach]   | VTA[GABA0]  | Acetylcholinergic |
|TPP[Ach]   | VTA[DA1]    | Acetylcholinergic |
|TPP[GLu]   | VTA[GABA0]  | Glutamatergic     |
|TPP[Glu]   | VTA[DA1]    | Glutamatergic     |

* **Inputs**  

| Source    | Destination | Connection        |
|----------:|:------------|-------------------|
|VTA[GABA0] | TPP[GABA0]  | GABAergic         |

Results
---

#### Diagram
![result](https://github.com/research-team/NEUCOGAR/blob/master/Mesocorticolimbic.png)

#### Main connection's table  

| Source    | Destination | Connection        |
|----------:|:------------|-------------------|
|PFC[Glu1]  | NAc[GABA1]  | Glutamatergic     |
|PFC[Glu1]  | VTA[GABA2]  | Glutamatergic     |
|PFC[Glu0]  | VTA[DA0]    | Glutamatergic     |
|NAc[Ach]   | NAc[GABA1]  | Acetylcholinergic |
|NAc[GABA0] | NAc[GABA1]  | GABAergic         |
|NAc[GABA1] | VTA[GABA2]  | GABAergic         |
|VTA[GABA0] | PFC         | GABAergic         |
|VTA[GABA0] | TPP[GABA0]  | GABAergic         |
|VTA[DA0]   | PFC         | Dopaminergic      |
|VTA[GABA1] | VTA[DA0]    | GABAergic         |
|VTA[GABA1] | VTA[DA1]    | GABAergic         |
|VTA[DA1]   | NAc[GABA1]  | Dopaminergic      |
|VTA[GABA2] | NAc[GABA1]  | GABAergic         |
|TPP[GABA]  | VTA[GABA0]  | GABAergic         |
|TPP[Ach]   | VTA[GABA0]  | Acetylcholinergic |
|TPP[Ach]   | VTA[DA1]    | Acetylcholinergic |
|TPP[GLu]   | VTA[GABA0]  | Glutamatergic     |
|TPP[Glu]   | VTA[DA1]    | Glutamatergic     |
