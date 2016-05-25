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

    public static String clearText(String text){
        text = text.replaceAll(";", "");
        text = text.replaceAll("nbsp", "");
        text = text.replaceAll("&", "");
        return text.trim();
    }


    public static String br2nl(String html) {
        if (html == null)
            return html;
        Document document = Jsoup.parse(html);
        document.outputSettings(new Document.OutputSettings().prettyPrint(false));//makes html() preserve linebreaks and spacing
        document.select("br").append("\\n");
        document.select("p").prepend("\\n\\n");
        String s = document.html().replaceAll("\\\\n", "\n");
        return Jsoup.clean(s, "", Whitelist.none(), new Document.OutputSettings().prettyPrint(false));
    }

    public static String clear(String text){
        text = br2nl(text);
        return clearText(text);
    }

}
