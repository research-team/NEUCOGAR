package org.necougor.parser.model.image;

import javax.xml.bind.annotation.XmlAttribute;

public class Array {
    private MxPoint[] mxPoint;

    private String as;

    public MxPoint[] getMxPoint() {
        return mxPoint;
    }

    public void setMxPoint(MxPoint[] mxPoint) {
        this.mxPoint = mxPoint;
    }

    public String getAs() {
        return as;
    }

    @XmlAttribute
    public void setAs(String as) {
        this.as = as;
    }

    @Override
    public String toString() {
        return "ClassPojo [mxPoint = " + mxPoint + ", as = " + as + "]";
    }
}