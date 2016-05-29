package org.necougor.parser.generators;


import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import org.necougor.parser.model.config.GeneratorConfig;
import org.necougor.parser.model.python.BrainRegion;
import org.necougor.parser.model.python.Receptor;
import org.necougor.parser.type.SynapseType;
import org.necougor.parser.util.CommonUtil;
import org.necougor.parser.util.GeneratorUtil;
import org.necougor.parser.util.PropertyUtil;
import org.necougor.parser.util.FileReaderWriterUtil;
import org.springframework.stereotype.Component;

import javax.annotation.PostConstruct;
import java.io.*;
import java.lang.reflect.Type;
import java.util.*;

@Component
public class NeuromodulationFileGenerator {

    public static final String FILE_NAME = "neuromodulaton.py";


    public static final String KEY_SYNAPSE_TYPE = "syn_type";
    public static final String KEY_WEIGHT_COEF = "weight_coef";

    public static final String KEY_GENERATOR_START_TIME = "startTime";
    public static final String KEY_GENERATOR_STOP_TIME = "stopTime";
    public static final String KEY_GENERATOR_RATE = "rate";
    public static final String KEY_GENERATOR_COEF = "coef_part";

    public static final String RECEPTOR_CONNECTION_PLACE_HOLDER = "connect(%1$2s, %2$2s, " + KEY_SYNAPSE_TYPE + "=%3$2s, " + KEY_WEIGHT_COEF + "=%4$.9f)";
    public static final String GENERATOR_CONNECTION_PLACE_HOLDER = "connect_generator(%1$2s, " + KEY_GENERATOR_START_TIME + "=%2$.9f, " + KEY_GENERATOR_STOP_TIME + "=%3$.9f, " + KEY_GENERATOR_RATE + "=%4$.9f, " + KEY_GENERATOR_COEF + "=%4$.9f)";
    public static final String DETECTOR_CONNECTION_PLACE_HOLDER = "connect_detector(%1$2s)";
    public static final String MULTIMETER_CONNECTION_PLACE_HOLDER = "connect_multimeter(%1$2s)";

    private static SynapseType[] types = {SynapseType.Ach, SynapseType.DA_ex, SynapseType.GABA, SynapseType.DA_in, SynapseType.Glu};


    public void generate(Map<String, BrainRegion> pythonBrainRegionMap) {

        String connections = generateConnections(pythonBrainRegionMap);
        String generators = generateSpikeGenerator(pythonBrainRegionMap);
        String decAndMult = generateDecetorAndMultimetr(pythonBrainRegionMap);
        String template = getTemplate();
        String result = String.format(template, connections, generators, decAndMult);
        FileReaderWriterUtil.writeGeneratedStringToFile(result, FILE_NAME);
    }

    public String getTemplate() {
        return FileReaderWriterUtil.readTemplateFileToString(FILE_NAME);
    }


    private String generateDecetorAndMultimetr(Map<String, BrainRegion> pythonBrainRegionMap) {
        String decAndMult = "";
        for (String key : pythonBrainRegionMap.keySet()) {
            final BrainRegion brainRegion = pythonBrainRegionMap.get(key);
            for (Receptor receptor : brainRegion.getInnerReceptors()) {
                String format = String.format(DETECTOR_CONNECTION_PLACE_HOLDER, GeneratorUtil.createVarName(brainRegion.getZoneName(), receptor.getType()));
                decAndMult = decAndMult + format + "\n";
                format = String.format(MULTIMETER_CONNECTION_PLACE_HOLDER, GeneratorUtil.createVarName(brainRegion.getZoneName(), receptor.getType()));
                decAndMult = decAndMult + format + "\n";
            }
        }
        return decAndMult;
    }


    private String generateSpikeGenerator(Map<String, BrainRegion> pythonBrainRegionMap) {
        String generatorsStrings = "";
        Map<String, GeneratorConfig> generatorConfigs = getStringGeneratorConfigMap();


        for (String key : pythonBrainRegionMap.keySet()) {
            final BrainRegion brainRegion = pythonBrainRegionMap.get(key);
            for (Receptor receptor : brainRegion.getInnerReceptors()) {
                if (receptor.isSpikeGeneratorConnected()) {
                    String propertyName = GeneratorUtil.createIndexVarName(receptor.getBrainRegion().getZoneName(), receptor.getType());
                    GeneratorConfig generatorConfig = generatorConfigs.get(propertyName);
                    final String format = String.format(Locale.US, GENERATOR_CONNECTION_PLACE_HOLDER, GeneratorUtil.createVarName(brainRegion.getZoneName(), receptor.getType()), generatorConfig.getStartTime(), generatorConfig.getStopTime(), generatorConfig.getRate(), generatorConfig.getCoef());
                    generatorsStrings = generatorsStrings + format + "\n";
                }
            }
        }

        return generatorsStrings;
    }

    private Map<String, GeneratorConfig> getStringGeneratorConfigMap() {
        InputStream resourceAsStream = Thread.currentThread().getContextClassLoader().getResourceAsStream("generatorConfig.json");
        BufferedReader br = new BufferedReader(
                new InputStreamReader(resourceAsStream));

        Type listType = new TypeToken<HashMap<String, GeneratorConfig>>() {
        }.getType();
        return new Gson().fromJson(br, listType);
    }

    private String generateConnections(Map<String, BrainRegion> pythonBrainRegionMap) {
        String connections = "";
        Map<String, Float> property;

        List<String> allDataFileNames = CommonUtil.getAllDataFileNames(pythonBrainRegionMap);
        property = new LinkWeightPropertyGenerator(allDataFileNames).load();


        for (String key : pythonBrainRegionMap.keySet()) {
            final BrainRegion brainRegion = pythonBrainRegionMap.get(key);
            final List<Receptor> receptors = brainRegion.getInnerReceptors();
            for (Receptor receptor : receptors) {
                final String fromName = GeneratorUtil.createVarName(brainRegion.getZoneName(), receptor.getType());
                for (SynapseType type : types) {
                    final List<Receptor> connected = receptor.getConnectedReceptorBySynapseType(type);
                    if (!connected.isEmpty()) {
                        for (Receptor conn : connected) {
                            if (conn != null) {
                                final String toName = GeneratorUtil.createVarName(conn.getBrainRegion().getZoneName(), conn.getType());
                                String propertyName = GeneratorUtil.createIndexVarName(conn.getBrainRegion().getZoneName(), conn.getType());
                                float weight = property.get(propertyName);
                                final String s = formatString(fromName, toName, type.toString(), weight);
                                connections = connections + s + "\n";
                            }
                        }
                    }
                }
            }
        }
        return connections;
    }


    public String formatString(String pre, String post, String synapseType, float weight) {
        return String.format(Locale.ENGLISH, RECEPTOR_CONNECTION_PLACE_HOLDER, pre, post, synapseType, weight);
    }

}
