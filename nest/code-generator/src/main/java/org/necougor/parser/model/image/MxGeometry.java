package org.necougor.parser.model.image;

import javax.xml.bind.annotation.XmlAttribute;

public class MxGeometry {
    private String height;

    private String width;

    private String as;

    private String y;

    private String x;

    public String getHeight() {
        return height;
    }

    @XmlAttribute
    public void setHeight(String height) {
        this.height = height;
    }

    public String getWidth() {
        return width;
    }

    @XmlAttribute
    public void setWidth(String width) {
        this.width = width;
    }

    public String getAs() {
        return as;
    }

    @XmlAttribute
    public void setAs(String as) {
        this.as = as;
    }

    public String getY() {
        return y;
    }

    @XmlAttribute
    public void setY(String y) {
        this.y = y;
    }

    public String getX() {
        return x;
    }

    @XmlAttribute
    public void setX(String x) {
        this.x = x;
    }

    @Override
    public String toString() {
        return "ClassPojo [height = " + height + ", width = " + width + ", as = " + as + ", y = " + y + ", x = " + x + "]";
    }
}