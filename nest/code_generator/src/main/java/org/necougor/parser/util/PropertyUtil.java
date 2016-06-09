package org.necougor.parser.util;

import java.io.*;
import java.net.URL;
import java.util.Enumeration;
import java.util.HashMap;
import java.util.Map;
import java.util.Properties;


public class PropertyUtil {

    private String propFileName;

    private static final String PREFIX = "./properties/";

    public PropertyUtil(String propFileName) {
        this.propFileName = PREFIX + propFileName;
    }


    public Map<String, String> loadPropertyFile() {
        File file = new File(propFileName);
        try {
            file.createNewFile();
        } catch (IOException e) {
            e.printStackTrace();
        }
        Properties prop = new Properties();
        InputStream input = null;
        Map<String, String> map = new HashMap<String, String>();
        try {
            FileInputStream fis = new FileInputStream(propFileName);
            BufferedReader in = new BufferedReader(new InputStreamReader(fis));
            prop.load(in);
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
            FileOutputStream fis = new FileOutputStream(propFileName);
            for (String key : map.keySet()) {
                prop.setProperty(key, map.get(key));
            }
            // save properties to project root folder
            OutputStreamWriter writer = new OutputStreamWriter(fis);
            prop.store(writer, null);
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