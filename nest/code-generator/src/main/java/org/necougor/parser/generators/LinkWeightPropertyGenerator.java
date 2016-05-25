package org.necougor.parser.generators;

import org.necougor.parser.util.PropertyUtil;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class LinkWeightPropertyGenerator {

    private final String propFileName = "connectionWeight.properties";
    private final List<String> expected;
    private static final Float DEFAULT_COUNT = 1f;
    private static final Logger LOG = LoggerFactory.getLogger(LinkWeightPropertyGenerator.class);

    public LinkWeightPropertyGenerator(List<String> expected) {
        this.expected = expected;
    }

    public Map<String, Float> load() {
        PropertyUtil propertyUtil = new PropertyUtil(propFileName);
        Map<String, String> property = propertyUtil.loadPropertyFile();
        Map<String, Float> prop = new HashMap<>();
        for (String key : property.keySet()) {
            prop.put(key, Float.valueOf(property.get(key)));
        }

        expected.stream().filter(exKey -> !prop.keySet().contains(exKey)).forEach(exKey -> {
            prop.put(exKey, DEFAULT_COUNT);
            property.put(exKey, DEFAULT_COUNT.toString());
            LOG.debug("Add default(" + DEFAULT_COUNT + ") weight receptors for " + exKey);
        });

        propertyUtil.writePropertyFile(property);
        return prop;
    }
}
