package org.necougor.parser.util;


import java.io.*;
import java.net.URISyntaxException;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;

public class FileReaderWriterUtil {

    private static final String TEMPLATE_PATH_PREFIX = "template/";
    private static final String GENERATED_PATH_PREFIX = "generated/";

    private static String readFileToString(String path) {
        byte[] encoded = new byte[0];
        try {
            URL path1 = new FileReaderWriterUtil().getClass().getClassLoader().getResource(path);
            encoded = Files.readAllBytes(Paths.get(path1.toURI()));
        } catch (IOException e) {
            e.printStackTrace();
        } catch (URISyntaxException e) {
            e.printStackTrace();
        }
        return new String(encoded, StandardCharsets.UTF_8);
    }

    public static String readTemplateFileToString(String templateName) {
        return readFileToString(TEMPLATE_PATH_PREFIX + templateName);
    }

    public static void writeGeneratedStringToFile(String text, String fileName) {
        PrintWriter printWriter = null;
        try {
            URL resource = new FileReaderWriterUtil().getClass().getClassLoader().getResource(GENERATED_PATH_PREFIX+fileName);
            File file = new File(resource.toURI());
            printWriter = new PrintWriter(file);
            printWriter.write(text);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (URISyntaxException e) {
            e.printStackTrace();
        } finally {
            if (printWriter != null) {
                printWriter.close();
            }
        }
    }

}
