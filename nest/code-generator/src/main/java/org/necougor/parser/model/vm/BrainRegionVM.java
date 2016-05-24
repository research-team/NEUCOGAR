package org.necougor.parser.model.vm;

public class BrainRegionVM extends CommonVM {

    private String value;

    private String type;

    private String parentId;

    private Double x;
    private Double y;

    private Double width;
    private Double height;



    public Double getWidth() {
        return width;
    }

    public void setWidth(Double width) {
        this.width = width;
    }

    public Double getHeight() {
        return height;
    }

    public void setHeight(Double height) {
        this.height = height;
    }

    public Double getX() {
        return x;
    }

    public void setX(Double x) {
        this.x = x;
    }

    public Double getY() {
        return y;
    }

    public void setY(Double y) {
        this.y = y;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getParentId() {
        return parentId;
    }

    public void setParentId(String parentId) {
        this.parentId = parentId;
    }

    public BrainRegionVM() {
        super();
    }

    public BrainRegionVM(String id, String color, String value, String type, String parentId, Double x, Double y, Double width, Double height) {
        super(id, color);
        this.value = value;
        this.type = type;
        this.parentId = parentId;
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
    }

    @Override
    public String toString() {
        return "BrainRegionVM{" +
                "value='" + value + '\'' +
                ", type='" + type + '\'' +
                ", parentId='" + parentId + '\'' +
                '}';
    }
}
