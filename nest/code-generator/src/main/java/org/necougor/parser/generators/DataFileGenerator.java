package org.necougor.parser.generators;


import org.necougor.parser.model.python.BrainRegion;
import org.necougor.parser.model.python.Receptor;
import org.necougor.parser.util.CommonUtil;
import org.necougor.parser.util.FileReaderWriterUtil;
import org.necougor.parser.util.GeneratorUtil;
import org.necougor.parser.util.ParseUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.util.*;

@Component
public class DataFileGenerator {

    public static final String FILE_NAME = "data.py";

    public static final String KEY_NAME = "Name";
    public static final String KEY_NUMBER_NEURON = "NN";
    public static final String KEY_MODEL = "Model";
    public static final String KEY_IDS = "IDs";
    public static final String MODEL_TEMPLATE = "{'" + KEY_NAME + "': '%1$2s', '" + KEY_NUMBER_NEURON + "': %2$2d, '" + KEY_MODEL + "': '%3$2s', '" + KEY_IDS + "': nest.Create('%3$2s', %2$2d)}";

    @Autowired
    private Formatter formatter;

    public static Map<String, Integer> property;

    public void generate(Map<String, BrainRegion> pythonBrainRegionMap) {
        String data = generateData(pythonBrainRegionMap);
        String template = FileReaderWriterUtil.readTemplateFileToString(FILE_NAME);
        data = String.format(template, data);
        FileReaderWriterUtil.writeGeneratedStringToFile(data, FILE_NAME);
    }


    private String generateData(Map<String, BrainRegion> pythonBrainRegionMap) {
        List<String> allDataFileNames = CommonUtil.getAllDataFileNames(pythonBrainRegionMap);
        property = new ReceptorPropertyCountGenerator(allDataFileNames).load();
        String data = "";

        for (String key : pythonBrainRegionMap.keySet()) {
            final BrainRegion brainRegion = pythonBrainRegionMap.get(key);
            data = data + brainRegion.getZoneName() + " = (\n";
            final List<Receptor> brainReceptor = brainRegion.getInnerReceptors();
            for (int i = 0; i < brainReceptor.size(); i++) {
                Receptor receptor = brainReceptor.get(i);
                String stringModel = createStringModel(receptor, brainRegion);
                data = data + stringModel;
                if (i < brainReceptor.size() - 1 || brainReceptor.size() == 1) {
                    data += ",";
                }
                data += "\n";
            }
            data = data + ")\n";
            for (int i = 0; i < brainReceptor.size(); i++) {
                final String name1 = GeneratorUtil.createIndexVarName(brainRegion.getZoneName(), brainReceptor.get(i).getType());
                data = data + name1 + " = " + i + "\n";
            }
            data = data + "\n";
        }
        return data;
    }

    private String createStringModel(Receptor receptor, BrainRegion brainRegion) {
        String propertyName = GeneratorUtil.createIndexVarName(brainRegion.getZoneName(), receptor.getType());
        long count = property.get(propertyName);
        String name = GeneratorUtil.createVarName(brainRegion.getZoneName(), receptor.getType());
        String model = ParseUtil.getModelByReceptor(receptor).toString();

        String stringModel = formatter.format(MODEL_TEMPLATE, name, count, model).toString();
        return stringModel;
    }




}
