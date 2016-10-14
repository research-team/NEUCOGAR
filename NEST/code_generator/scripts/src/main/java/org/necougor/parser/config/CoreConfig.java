package org.necougor.parser.config;


import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import org.necougor.parser.model.config.SynapseTypeConfig;
import org.necougor.parser.services.BrainRegionServices;
import org.necougor.parser.services.ReceptorServices;
import org.necougor.parser.util.CommonUtil;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.lang.reflect.Type;
import java.util.Formatter;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Configuration
@ComponentScan("org.necougor.parser")
public class CoreConfig {

    @Bean
    public BrainRegionServices brainRegionServices() {
        BrainRegionServices brainRegionServices = new BrainRegionServices();
        brainRegionServices.setPythonBrainRegionMap(new HashMap<>());

        List<String> names = CommonUtil.readFileByLine("names/brainRegionsNames.list",this);

        brainRegionServices.setNames(names);

        return brainRegionServices;
    }



    @Bean
    public ReceptorServices receptorServices() {
        ReceptorServices receptorServices = new ReceptorServices();
        receptorServices.setPythonReceptorMap(new HashMap<>());

        List<String> names = CommonUtil.readFileByLine("names/receptorsNames.list",this);
        receptorServices.setNames(names);

        return receptorServices;
    }

    @Bean
    public Formatter formatter() {
        StringBuilder sb = new StringBuilder();
        return new Formatter(sb);
    }

    @Bean(name="synapseConfig")
    public HashMap<String, SynapseTypeConfig> stringSynapseTypeConfigMap() {
        InputStream resourceAsStream = this.getClass().getClassLoader().getResourceAsStream("synapseType.json");
        BufferedReader br = new BufferedReader(
                new InputStreamReader(resourceAsStream));

        Type listType = new TypeToken<HashMap<String, SynapseTypeConfig>>() {
        }.getType();
        return new Gson().fromJson(br, listType);
    }

}
