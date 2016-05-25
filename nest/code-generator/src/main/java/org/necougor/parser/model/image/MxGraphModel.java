package org.necougor.parser.model.image;

import javax.xml.bind.annotation.XmlAttribute;

public class MxGraphModel {
    private String gridSize;
    private String dx;
    private String connect;

    private Root root;
    private String dy;
    private String guides;
    private String fold;
    private String pageHeight;
    private String math;
    private String arrows;
    private String page;
    private String pageWidth;
    private String tooltips;
    private String background;
    private String grid;

    private String pageScale;

    public String getGridSize() {
        return gridSize;
    }

    @XmlAttribute
    public void setGridSize(String gridSize) {
        this.gridSize = gridSize;
    }


    public String getDx() {
        return dx;
    }

    @XmlAttribute
    public void setDx(String dx) {
        this.dx = dx;
    }
    @XmlAttribute
    public String getConnect() {
        return connect;
    }


    public void setConnect(String connect) {
        this.connect = connect;
    }

    public Root getRoot() {
        return root;
    }

    public void setRoot(Root root) {
        this.root = root;
    }

    public String getDy() {
        return dy;
    }
    @XmlAttribute
    public void setDy(String dy) {
        this.dy = dy;
    }

    public String getGuides() {
        return guides;
    }
    @XmlAttribute
    public void setGuides(String guides) {
        this.guides = guides;
    }

    public String getFold() {
        return fold;
    }
    @XmlAttribute
    public void setFold(String fold) {
        this.fold = fold;
    }

    public String getPageHeight() {
        return pageHeight;
    }
    @XmlAttribute
    public void setPageHeight(String pageHeight) {
        this.pageHeight = pageHeight;
    }

    public String getMath() {
        return math;
    }
    @XmlAttribute
    public void setMath(String math) {
        this.math = math;
    }

    public String getArrows() {
        return arrows;
    }
    @XmlAttribute
    public void setArrows(String arrows) {
        this.arrows = arrows;
    }

    public String getPage() {
        return page;
    }
    @XmlAttribute
    public void setPage(String page) {
        this.page = page;
    }

    public String getPageWidth() {
        return pageWidth;
    }
    @XmlAttribute
    public void setPageWidth(String pageWidth) {
        this.pageWidth = pageWidth;
    }

    public String getTooltips() {
        return tooltips;
    }
    @XmlAttribute
    public void setTooltips(String tooltips) {
        this.tooltips = tooltips;
    }

    public String getBackground() {
        return background;
    }
    @XmlAttribute
    public void setBackground(String background) {
        this.background = background;
    }

    public String getGrid() {
        return grid;
    }
    @XmlAttribute
    public void setGrid(String grid) {
        this.grid = grid;
    }

    public String getPageScale() {
        return pageScale;
    }
    @XmlAttribute
    public void setPageScale(String pageScale) {
        this.pageScale = pageScale;
    }

    @Override
    public String toString() {
        return "ClassPojo [gridSize = " + gridSize + ", dx = " + dx + ", connect = " + connect + ", root = " + root + ", dy = " + dy + ", guides = " + guides + ", fold = " + fold + ", pageHeight = " + pageHeight + ", math = " + math + ", arrows = " + arrows + ", page = " + page + ", pageWidth = " + pageWidth + ", tooltips = " + tooltips + ", background = " + background + ", grid = " + grid + ", pageScale = " + pageScale + "]";
    }
}