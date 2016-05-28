package org.necougor.parser.util;

public class GeneratorUtil {

    public static String createName(String regionType, String receptorType) {
        return regionType + "[" + receptorType + "]";
    }

    public static String createVarName(String regionType, String receptorType) {
        return regionType + "[" + regionType + "_" + receptorType + "]";
    }


    public static String createIndexVarName(String nRegion, String nReceptor) {
        return nRegion + "_" + nReceptor;
    }

}
