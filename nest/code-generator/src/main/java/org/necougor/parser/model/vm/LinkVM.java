package org.necougor.parser.model.vm;

public class LinkVM extends CommonVM {

    private String source;
    private String target;
    private String value;

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public boolean isBeDirect() {
        return isBeDirect;
    }

    public void setBeDirect(boolean beDirect) {
        isBeDirect = beDirect;
    }

    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }

    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }

    private boolean isBeDirect;

    public LinkVM(String id, String color, String source, String target, boolean isBeDirect, String value) {
        super(id, color);
        this.source = source;
        this.target = target;
        this.isBeDirect = isBeDirect;
        this.value = value;
    }

    public LinkVM reverse() {
        final String source = getSource();
        final String target = getTarget();
        final LinkVM linkVM = new LinkVM(getId(), getColor(), target, source, false, getValue());
        this.target = source;
        this.source = linkVM.getSource();
        setBeDirect(false);
        return linkVM;
    }

    public LinkVM copy() {
        return new LinkVM(getId(), getColor(), getSource(), getTarget(), false, getValue());
    }

}
