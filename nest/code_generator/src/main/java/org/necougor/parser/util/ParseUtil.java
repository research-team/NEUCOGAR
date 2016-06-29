package org.necougor.parser.util;

import org.necougor.parser.model.config.SynapseTypeConfig;
import org.necougor.parser.model.python.Receptor;
import org.necougor.parser.model.vm.LinkVM;
import org.necougor.parser.model.vm.ReceptorVM;
import org.necougor.parser.type.NerounModel;
import org.necougor.parser.type.SynapseType;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.util.Map;

@Component
public class ParseUtil {

    private static final Logger LOG = LoggerFactory.getLogger(ParseUtil.class);


    public static String clearText(String text) {
        text = TextUtil.br2nl(text);
        return TextUtil.clearText(text);
    }

    public static Receptor receptorVMToReceptor(ReceptorVM vm) {
        final Receptor receptor = new Receptor();
        String type = ParseUtil.clearText(vm.getValue());
        receptor.setType(type);
        receptor.setId(vm.getId());
        receptor.setSpikeGeneratorConnected(vm.isSpikeGeneratorContains());
        return receptor;
    }


    //TODO: make it by legend
    public static String getSynapseTypeByLink(LinkVM link, Map<String, SynapseTypeConfig> stringSynapseTypeConfigMap) {

        for (String key : stringSynapseTypeConfigMap.keySet()) {
            SynapseTypeConfig synapseTypeConfig = stringSynapseTypeConfigMap.get(key);
            if (link.getColor().equals(synapseTypeConfig.getColor())) {
                if (!TextUtil.isEmpty(link.getValue())) {
                    //have value text
                    if (!TextUtil.isEmpty(synapseTypeConfig.getValue())) {
                        //config have value param
                        if (synapseTypeConfig.getValue().equals(link.getValue())) {
                            LOG.debug("Link " + link.toString() + " define as " + key);
                            return key;
                        }
                    } else {
                        //config don't have value
                        continue;
                    }
                }else{
                    if(TextUtil.isEmpty(synapseTypeConfig.getValue())){
                        //value of rec and config are empty
                        LOG.debug("Link " + link.toString() + " define as " + key);
                        return key;
                    }else {
                        continue;
                    }
                }
            }


        }

        LOG.debug("Link " + link.toString() + " undefined, setting DA_ex");
        return "DA_ex";
    }


    public static NerounModel getModelByReceptor(Receptor receptor) {
        return NerounModel.iaf_psc_alpha;
    }


}
