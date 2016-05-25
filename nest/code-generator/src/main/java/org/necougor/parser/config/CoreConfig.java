package org.necougor.parser.config;


import org.necougor.parser.services.BrainRegionServices;
import org.necougor.parser.services.ReceptorServices;
import org.necougor.parser.util.CommonUtil;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

import java.util.Formatter;
import java.util.HashMap;
import java.util.List;

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


}
