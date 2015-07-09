#Instructions
Experiment description: [link](experiment_description.md)

##Dopamine pathway description
The last implementation of dopamine pathway is in step_3 folder is based on schema below. Список соединений частей представлен в файле [nest/step_3/BG_advanced.txt](https://github.com/research-team/NEUCOGAR/blob/master/nest/step_3/BG_advanced.txt)

![Interpretation of modern schema of dopamine pathway](./dopamine_pathway.png )

##Scripts
* dopa_neuromodulation_3.py:
    * отвечает за весь процесс сборки 
* parameters_3.py:
    * лишь устанавливает настройки параметров разных типов нейронов, синапсов, генераторов
    * дополнительные полезные методы
* property_3.py:
    * определение именованных ключей для читабельности в вышеприведенных скриптах
    * флаги включения-отключения дофаминовой нейромодуляции, случайного генератор шума, graphic display и тп.
    * именования папок для выходных результатов, 

##Графики
-графики по умолчанию не прорисовываются, но всегда сохраняются в result folder <br />
 
Python 2.7.6 (не выше не ниже)
Если заупускать через PyCharm то отметьте папку (project folder)/nest/step_3 и (extracted Nest Initiative framework)/nest/lib/python2.7/site-packages/ как source code через настройки
