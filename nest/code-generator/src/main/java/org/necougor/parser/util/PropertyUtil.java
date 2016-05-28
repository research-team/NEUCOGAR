package org.necougor.parser.util;

import java.io.*;
import java.net.URL;
import java.util.Enumeration;
import java.util.HashMap;
import java.util.Map;
import java.util.Properties;


public class PropertyUtil {

    private String propFileName;

    //TODO: use classPath
    private static final String PREFIX = "properties/";

    public PropertyUtil(String propFileName) {
        this.propFileName = PREFIX + propFileName;
    }


    public static void main(String[] args) {
        PropertyUtil propertyUtil = new PropertyUtil("weight.property");
        propertyUtil.loadPropertyFile();
    }

    public Map<String, String> loadPropertyFile() {
        Properties prop = new Properties();
        InputStream input = null;
        Map<String, String> map = new HashMap<String, String>();
        try {
            URL resource = this.getClass().getClassLoader().getResource(propFileName);
            input = new FileInputStream(resource.getFile());
            prop.load(input);
            final Enumeration enumeration = prop.propertyNames();
            while (enumeration.hasMoreElements()) {
                final String key = (String) enumeration.nextElement();
                map.put(key, prop.getProperty(key));
            }

        } catch (IOException ex) {
            ex.printStackTrace();
        } finally {
            if (input != null) {
                try {
                    input.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
        return map;
    }


    public void writePropertyFile(Map<String, String> map) {
        Properties prop = new Properties();
        OutputStream output = null;
        try {
            URL resource = this.getClass().getClassLoader().getResource(propFileName);
            output = new FileOutputStream(resource.getFile());
            for (String key : map.keySet()) {
                prop.setProperty(key, map.get(key));
            }
            // save properties to project root folder
            prop.store(output, null);
        } catch (IOException io) {
            io.printStackTrace();
        } finally {
            if (output != null) {
                try {
                    output.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }

        }
    }
}