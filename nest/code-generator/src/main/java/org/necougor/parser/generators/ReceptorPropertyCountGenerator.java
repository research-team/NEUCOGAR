package org.necougor.parser.generators;

import org.necougor.parser.util.PropertyUtil;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ReceptorPropertyCountGenerator {

    private final String propFileName = "receptorsCount.properties";
    private final List<String> expected;
    private static final Integer DEFAULT_COUNT = 10;
    private static final Logger LOG = LoggerFactory.getLogger(ReceptorPropertyCountGenerator.class);

    public ReceptorPropertyCountGenerator(List<String> expected) {
        this.expected = expected;
    }

    public Map<String, Integer> load() {
        PropertyUtil propertyUtil = new PropertyUtil(propFileName);
        Map<String, String> property = propertyUtil.loadPropertyFile();
        Map<String, Integer> prop = new HashMap<>();
        for (String key : property.keySet()) {
            prop.put(key, Integer.valueOf(property.get(key)));
        }

        expected.stream().filter(exKey -> !prop.keySet().contains(exKey)).forEach(exKey -> {
            prop.put(exKey, DEFAULT_COUNT);
            property.put(exKey, DEFAULT_COUNT.toString());
            LOG.debug("Add default(" + DEFAULT_COUNT + ") count receptors for " + exKey);
        });

        propertyUtil.writePropertyFile(property);
        return prop;
    }
}
