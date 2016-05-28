package org.necougor.parser.services;

import org.necougor.parser.model.python.Receptor;

import java.util.*;


public class ReceptorServices {

    public Map<String, Receptor> pythonReceptorMap;
    public List<String> names;


    public Map<String, Receptor> getPythonReceptorMap() {
        return pythonReceptorMap;
    }

    public void setPythonReceptorMap(Map<String, Receptor> pythonReceptorMap) {
        this.pythonReceptorMap = pythonReceptorMap;
    }

    public List<String> getNames() {
        return names;
    }

    public void setNames(List<String> names) {
        this.names = names;
    }

    public ReceptorServices(){
    }

    public void addById(String id, Receptor Receptor){
        pythonReceptorMap.put(id, Receptor);
    }

    public Receptor getByIdOrNew(String id){
        Receptor Receptor = getById(id);
        if(Receptor==null){
            return new Receptor();
        }
        return Receptor;
    }

    public Receptor getById(String id){
        Receptor Receptor = pythonReceptorMap.get(id);
        return Receptor;
    }

    public boolean containsKey(String key){
        return pythonReceptorMap.containsKey(key);
    }

    public Map<String, Receptor> getpythonReceptorMap(){
        return pythonReceptorMap;
    }

    public Set<String> getKeys(){
        return pythonReceptorMap.keySet();
    }

}
