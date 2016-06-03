package org.necougor.parser.util;

import org.necougor.parser.model.config.SynapseTypeConfig;
import org.necougor.parser.model.python.BrainRegion;
import org.necougor.parser.model.python.Receptor;
import org.necougor.parser.type.SynapseType;

import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Scanner;


public class CommonUtil {


    public static List<String> getAllDataFileNames(Map<String, BrainRegion> pythonBrainRegionMap) {
        List<String> propertyName = new ArrayList<>();
        for (String key : pythonBrainRegionMap.keySet()) {
            BrainRegion brainRegion = pythonBrainRegionMap.get(key);
            List<Receptor> innerReceptors = brainRegion.getInnerReceptors();
            for (Receptor innerReceptor : innerReceptors) {
                String varName = GeneratorUtil.createIndexVarName(brainRegion.getZoneName(), innerReceptor.getType());
                propertyName.add(varName);
            }
        }
        return propertyName;
    }


    public static List<String> getAllWeightLinks(Map<String, BrainRegion> pythonBrainRegionMap, Map<String, SynapseTypeConfig> stringSynapseTypeConfigMap) {
        List<String> propertyNames = new ArrayList<>();

        for (String key : pythonBrainRegionMap.keySet()) {
            final BrainRegion brainRegion = pythonBrainRegionMap.get(key);
            final List<Receptor> receptors = brainRegion.getInnerReceptors();
            for (Receptor receptor : receptors) {
                final String fromName = GeneratorUtil.createVarName(brainRegion.getZoneName(), receptor.getType());
                for (String type : stringSynapseTypeConfigMap.keySet()) {
                    final List<Receptor> connected = receptor.getConnectedReceptorBySynapseType(type);
                    if (!connected.isEmpty()) {
                        for (Receptor conn : connected) {
                            if (conn != null) {
                                final String toName = GeneratorUtil.createVarName(conn.getBrainRegion().getZoneName(), conn.getType());
                                String propertyName = fromName + "-" + toName;
                                propertyNames.add(propertyName);
                            }
                        }
                    }
                }
            }
        }
        return propertyNames;
    }


    public static List<String> readFileByLine(String path, Object classLoader) {
        List lines = new ArrayList<>();
        InputStream resourceAsStream = classLoader.getClass().getClassLoader().getResourceAsStream(path);
        Scanner scanner = new Scanner(resourceAsStream);
        while (scanner.hasNext()) {
            String line = scanner.nextLine().toLowerCase().trim();
            lines.add(line);
        }
        return lines;
    }


}
