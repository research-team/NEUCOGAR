package org.necougor.parser.model.python;

import java.util.ArrayList;
import java.util.List;

public class BrainRegion {

    public BrainRegion() {
        allReceptors = new ArrayList<>();
        innerReceptors = new ArrayList<>();
        childBrainRegions = new ArrayList<>();
    }

    private String zoneName;

    private BrainRegion parent;

    private List<Receptor> allReceptors;

    private List<Receptor> innerReceptors;

    private List<BrainRegion> childBrainRegions;


    private boolean isLeaf;

    public boolean isLeaf() {
        return isLeaf;
    }

    public void setLeaf(boolean leaf) {
        isLeaf = leaf;
    }

    public List<Receptor> getInnerReceptors() {
        return innerReceptors;
    }

    public void setInnerReceptors(List<Receptor> innerReceptors) {
        this.innerReceptors = innerReceptors;
    }



    public BrainRegion getParent() {
        return parent;
    }

    public void setParent(BrainRegion parent) {
        this.parent = parent;
    }

    public List<Receptor> getAllReceptors() {
        return allReceptors;
    }

    public void setAllReceptors(List<Receptor> allReceptors) {
        this.allReceptors = allReceptors;
    }

    public String getZoneName() {
        return zoneName;
    }

    public void setZoneName(String zoneName) {
        this.zoneName = zoneName;
    }

    public List<BrainRegion> getChildBrainRegions() {
        return childBrainRegions;
    }

    public void setChildBrainRegions(List<BrainRegion> childBrainRegions) {
        this.childBrainRegions = childBrainRegions;
    }

}
