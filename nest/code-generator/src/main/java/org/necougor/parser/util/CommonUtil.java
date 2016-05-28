package org.necougor.parser.util;

import org.necougor.parser.model.python.BrainRegion;
import org.necougor.parser.model.python.Receptor;

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

    public static List<String> readFileByLine(String path,Object classLoader) {
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
