package org.necougor.parser.services;


import org.necougor.parser.model.python.BrainRegion;
import org.necougor.parser.util.PropertyUtil;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class BrainRegionServices {

    private Map<String, BrainRegion> pythonBrainRegionMap;

    public void setPythonBrainRegionMap(Map<String, BrainRegion> pythonBrainRegionMap) {
        this.pythonBrainRegionMap = pythonBrainRegionMap;
    }

    public void addById(String id, BrainRegion brainRegion){
        pythonBrainRegionMap.put(id, brainRegion);
    }

    public BrainRegion getByIdOrNew(String id){
        BrainRegion brainRegion = getById(id);
        if(brainRegion==null){
            return new BrainRegion();
        }
        return brainRegion;
    }

    public BrainRegion getById(String id){
        BrainRegion brainRegion = pythonBrainRegionMap.get(id);
        return brainRegion;
    }

    public boolean containsKey(String key){
        return pythonBrainRegionMap.containsKey(key);
    }

    public Map<String, BrainRegion> getPythonBrainRegionMap(){
        return pythonBrainRegionMap;
    }

    public Set<String> getKeys(){
        return pythonBrainRegionMap.keySet();
    }


    public List<String> names;

    public List<String> getNames() {
        return names;
    }

    public void setNames(List<String> names) {
        this.names = names;
    }
}
