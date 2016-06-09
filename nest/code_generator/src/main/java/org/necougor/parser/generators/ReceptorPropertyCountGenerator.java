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
    private Integer count;


    public ReceptorPropertyCountGenerator(List<String> expected, Integer count) {
        this.expected = expected;
        this.count = count;
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
        if (count != null) {
            LOG.debug("Recount the count of neuron with total number " + count);
            return configureWeight(prop);
        }
        return prop;
    }


    private Map<String, Integer> configureWeight(Map<String, Integer> prop) {
        Map<String, Integer> newProp = new HashMap<>();
        int total = 0;

        for (String key : prop.keySet()) {
            total += prop.get(key);
        }
        LOG.debug("Current total number of neuron is " + total);

        for (String key : prop.keySet()) {
            float coef = (float) prop.get(key) / (float) total;

            Float newVal = (coef * count);

            Integer value = newVal.intValue() < DEFAULT_COUNT ? DEFAULT_COUNT : newVal.intValue();
            newProp.put(key, value);
            LOG.debug("New neuron value to " + key + " is " + value);
        }

        return newProp;
    }


}
