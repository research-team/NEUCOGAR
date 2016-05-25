package org.necougor.parser.model.image;

import javax.xml.bind.annotation.XmlAttribute;

public class MxCell {
    private String id;

    private String edge;

    private String style;

    private String source;

    private String target;

    private String parent;


    public String getValue() {
        return value;
    }

    @XmlAttribute
    public void setValue(String value) {
        this.value = value;
    }

    private String value;

    private MxGeometry mxGeometry;

    public String getId() {
        return id;
    }

    @XmlAttribute
    public void setId(String id) {
        this.id = id;
    }

    public String getEdge() {
        return edge;
    }

    @XmlAttribute
    public void setEdge(String edge) {
        this.edge = edge;
    }

    public String getStyle() {
        return style;
    }

    @XmlAttribute
    public void setStyle(String style) {
        this.style = style;
    }

    public String getSource() {
        return source;
    }

    @XmlAttribute
    public void setSource(String source) {
        this.source = source;
    }

    public String getTarget() {
        return target;
    }

    @XmlAttribute
    public void setTarget(String target) {
        this.target = target;
    }

    public String getParent() {
        return parent;
    }

    @XmlAttribute
    public void setParent(String parent) {
        this.parent = parent;
    }

    public MxGeometry getMxGeometry() {
        return mxGeometry;
    }

    public void setMxGeometry(MxGeometry mxGeometry) {
        this.mxGeometry = mxGeometry;
    }

    @Override
    public String toString() {
        return "ClassPojo [id = " + id + ", edge = " + edge + ", style = " + style + ", source = " + source + ", target = " + target + ", parent = " + parent + ", mxGeometry = " + mxGeometry + "]";
    }
}