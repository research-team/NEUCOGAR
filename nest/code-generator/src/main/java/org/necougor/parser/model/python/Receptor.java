package org.necougor.parser.model.python;


import org.necougor.parser.type.SynapseType;
import org.necougor.parser.util.ParseUtil;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.HashMap;

public class Receptor {

    private BrainRegion brainRegion;

    private int count;

    private String type;
    private String id;

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    private boolean isSpikeGeneratorConnected;

    private Map<SynapseType, List<Receptor>> connectedTo;

    public List<Receptor> getConnectedReceptorBySynapseType(SynapseType type) {
        if (!connectedTo.containsKey(type)) {
            connectedTo.put(type, new ArrayList<>());
        }
        return connectedTo.get(type);
    }

    public Map<SynapseType, List<Receptor>> getConnectedTo() {
        return connectedTo;
    }

    public void setConnectedTo(Map<SynapseType, List<Receptor>> connectedTo) {
        this.connectedTo = connectedTo;
    }

    public BrainRegion getBrainRegion() {
        return brainRegion;
    }

    public void setBrainRegion(BrainRegion brainRegion) {
        this.brainRegion = brainRegion;
    }

    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = count;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public boolean isSpikeGeneratorConnected() {
        return isSpikeGeneratorConnected;
    }

    public void setSpikeGeneratorConnected(boolean spikeGeneratorConnected) {
        isSpikeGeneratorConnected = spikeGeneratorConnected;
    }


    public Receptor() {
        this.connectedTo = new HashMap();
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Receptor receptor = (Receptor) o;

        if (type != null ? !type.equals(receptor.type) : receptor.type != null) return false;
        return id != null ? id.equals(receptor.id) : receptor.id == null;

    }

    @Override
    public int hashCode() {
        int result = type != null ? type.hashCode() : 0;
        result = 31 * result + (id != null ? id.hashCode() : 0);
        return result;
    }
}
