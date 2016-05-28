package org.necougor.parser.util;

import org.necougor.parser.model.python.Receptor;
import org.necougor.parser.model.vm.LinkVM;
import org.necougor.parser.model.vm.ReceptorVM;
import org.necougor.parser.type.NerounModel;
import org.necougor.parser.type.SynapseType;

public class ParseUtil {

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
    public static SynapseType getSynapseTypeByLink(LinkVM link) {
        final String color = link.getColor();
        if(color.equals("purple") || color.equals("orange")){
            return SynapseType.DA_ex;
        }
        if (color.equals("green")) {
            final String value = link.getValue();
            if (value.equals("In")) {
                return SynapseType.DA_in;
            } else if (value.equals("Ex")) {
                return SynapseType.DA_ex;
            }else{
                return SynapseType.DA_ex;
            }
           // return SynapseType.None;
        } else if (color.equals("FF0000")) {
            return SynapseType.Ach;
        } else if (color.equals("Blue")) {
            return SynapseType.GABA;
        } else if (color.equals("red")) {
            return SynapseType.Glu;
        }
        return SynapseType.None;
    }


    public static NerounModel getModelByReceptor(Receptor receptor) {
        return NerounModel.iaf_psc_alpha;
    }


}
