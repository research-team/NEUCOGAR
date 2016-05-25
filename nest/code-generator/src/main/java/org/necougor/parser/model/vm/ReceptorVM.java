package org.necougor.parser.model.vm;

public class ReceptorVM extends BrainRegionVM {

    private boolean isSpikeGeneratorContains;

    public ReceptorVM(String id, String color, String value, String type, String parentId, Double x, Double y, Double width, Double height) {
        super(id, color, value, type, parentId, x, y, width, height);
    }

    public boolean isSpikeGeneratorContains() {
        return isSpikeGeneratorContains;
    }

    public void setSpikeGeneratorContains(boolean spikeGeneratorContains) {
        isSpikeGeneratorContains = spikeGeneratorContains;
    }
}
