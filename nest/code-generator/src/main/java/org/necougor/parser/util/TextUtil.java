package org.necougor.parser.util;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.safety.Whitelist;

/**
 * Created by dalv6_000 on 29.03.2016.
 */
public class TextUtil {

    public static boolean isEmpty(String text) {
        if (text != null && !text.isEmpty()) {
            return false;
        } else {
            return true;
        }
    }

    public static String clearText(String text) {
        text = text.replaceAll(";", "");
        text = text.replaceAll("nbsp", "");
        text = text.replaceAll("&", "");
        return text.trim();
    }


    public static String br2nl(String html) {
        if (html == null)
            return html;
        return Jsoup.parse(html).text().replaceAll("\\<.*?>", "");
    }

    public static String clear(String text) {
        text = br2nl(text);
        return clearText(text);
    }

    public static void main(String[] args) {
        String clear = clear("&lt;div&gt;striatum&lt;br&gt;&lt;/div&gt;");
        System.out.println(clear);
    }

}
