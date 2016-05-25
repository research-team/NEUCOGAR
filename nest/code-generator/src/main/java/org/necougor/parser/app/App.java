package org.necougor.parser.app;


import org.jsoup.Jsoup;
import org.jsoup.examples.HtmlToPlainText;
import org.necougor.parser.config.CoreConfig;
import org.necougor.parser.generators.DataFileGenerator;
import org.necougor.parser.generators.NeuromodulationFileGenerator;
import org.necougor.parser.model.image.MxCell;
import org.necougor.parser.model.image.MxGraphModel;
import org.necougor.parser.model.python.BrainRegion;
import org.necougor.parser.model.python.Receptor;
import org.necougor.parser.model.vm.BrainRegionVM;
import org.necougor.parser.model.vm.LinkVM;
import org.necougor.parser.model.vm.ReceptorVM;
import org.necougor.parser.services.BrainRegionServices;
import org.necougor.parser.services.ReceptorServices;
import org.necougor.parser.type.SynapseType;
import org.necougor.parser.util.ParseUtil;
import org.necougor.parser.util.TextUtil;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.stereotype.Component;

import javax.xml.bind.JAXBContext;
import javax.xml.bind.JAXBElement;
import javax.xml.bind.JAXBException;
import javax.xml.bind.Unmarshaller;
import javax.xml.transform.stream.StreamSource;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.net.URISyntaxException;
import java.net.URL;
import java.util.*;
import java.util.stream.Collectors;

@Component
public class App {

    private static final Logger LOG = LoggerFactory.getLogger(App.class);
    public static Map<String, BrainRegionVM> brainRegionMap;
    public static List<ReceptorVM> receptorVMs;
    public static List<ReceptorVM> spikeVMs;

    @Autowired
    private BrainRegionServices brainRegionServices;
    @Autowired
    private ReceptorServices receptorServices;
    @Autowired
    private DataFileGenerator dataFileGenerator;
    @Autowired
    private NeuromodulationFileGenerator neuromodulationFileGenerator;


    public boolean isBrainRegionVM(MxCell mxCell) {
        String value = mxCell.getValue();
        if (value != null && !value.isEmpty()) {
            String region = TextUtil.clear(value);
            if (brainRegionServices.getNames().contains(region.toLowerCase())) {
                LOG.debug("Find brain region: " + region);
                return true;
            }
        }
        return false;
    }


    private boolean isReceptorVm(MxCell mxCell) {
        String value = mxCell.getValue();
        if (value != null && !value.isEmpty()) {
            String region = TextUtil.clear(value);
            if (receptorServices.getNames().contains(region.toLowerCase())) {
                LOG.debug("Find receptor: " + region);
                return true;
            }
        }
        return false;
    }


    public List<BrainRegionVM> parseBrainRegion(List<MxCell> mxCells) {
        List<BrainRegionVM> brainRegionList = new LinkedList<BrainRegionVM>();

        for (MxCell mxCell : mxCells) {
            if (isBrainRegionVM(mxCell)) {
                String value = new HtmlToPlainText().getPlainText(Jsoup.parse(mxCell.getValue())).replaceAll("[^a-zA-Z]+", "");
                String color = getColor(mxCell);
                Double width = new Double(mxCell.getMxGeometry().getWidth());
                Double height = new Double(mxCell.getMxGeometry().getHeight());
                Double x = null;
                Double y = null;
                if (!TextUtil.isEmpty(mxCell.getMxGeometry().getX())) {
                    x = new Double(mxCell.getMxGeometry().getX());
                }

                if (!TextUtil.isEmpty(mxCell.getMxGeometry().getY())) {
                    y = new Double(mxCell.getMxGeometry().getY());
                }

                BrainRegionVM brainRegionVM = new BrainRegionVM(mxCell.getId(), color, value, null, mxCell.getParent(), x, y, width, height);
                brainRegionList.add(brainRegionVM);
            }
        }
        LOG.debug("Find brain " + brainRegionList.size() + " regions");
        return brainRegionList;
    }


    /**
     * Get from list of model only Receptors
     *
     * @param mxCells
     * @return
     */
    public List<ReceptorVM> parseReceptors(List<MxCell> mxCells) {
        List<ReceptorVM> receptorVMs = new LinkedList<>();

        for (MxCell mxCell : mxCells) {
            if (isReceptorVm(mxCell)) {
                String color = getColor(mxCell);
                Double x = null;
                Double y = null;
                Double height = null;
                Double width = null;
                String value = mxCell.getValue().replaceAll("\\<.*?>", "");
                if (mxCell.getMxGeometry().getX() != null) {
                    x = new Double(mxCell.getMxGeometry().getX());
                } else {
                    LOG.debug("Receptor " + value + " id-" + mxCell.getId() + " don't have x coordinate");
                }
                if (mxCell.getMxGeometry().getY() != null) {
                    y = new Double(mxCell.getMxGeometry().getY());
                } else {
                    LOG.debug("Receptor " + value + " id-" + mxCell.getId() + " don't have y coordinate");
                }
                if (mxCell.getMxGeometry().getHeight() != null) {
                    height = new Double(mxCell.getMxGeometry().getHeight());
                } else {
                    LOG.debug("Receptor " + value + " id-" + mxCell.getId() + " don't have height");
                }
                if (mxCell.getMxGeometry().getWidth() != null) {
                    width = new Double(mxCell.getMxGeometry().getWidth());
                } else {
                    LOG.debug("Receptor " + value + " id-" + mxCell.getId() + " don't have width");
                }
                ReceptorVM receptorVM = new ReceptorVM(mxCell.getId(), color, value, null, mxCell.getParent(), x, y, width, height);
                configSpikeGenerator(receptorVM);
                receptorVMs.add(receptorVM);
            }
        }
        LOG.debug("Find " + receptorVMs.size() + " receptors");
        return receptorVMs;
    }

    private void configSpikeGenerator(ReceptorVM receptorVM) {
        final String recepParentId = receptorVM.getParentId();
        for (ReceptorVM spikeVM : spikeVMs) {
            if (!TextUtil.isEmpty(spikeVM.getParentId()) && spikeVM.getParentId().equals(recepParentId)) {
                if (checkContains(receptorVM.getWidth(), receptorVM.getHeight(), receptorVM.getX(), receptorVM.getY(), spikeVM.getHeight(), spikeVM.getWidth(), spikeVM.getX(), spikeVM.getY())) {
                    receptorVM.setSpikeGeneratorContains(true);
                }
            }
        }
    }

    /**
     * Get color from model
     *
     * @param mxCell
     * @return
     */
    private String getColor(MxCell mxCell) {
        String style = mxCell.getStyle();
        if (!TextUtil.isEmpty(style)) {
            String template = "plain-";
            int index = style.indexOf(template);
            if (index != -1) {
                String substring = style.substring(index + template.length());
                int i = substring.indexOf(';');
                String color;
                if (i != -1) {
                    color = substring.substring(0, i);
                } else {
                    color = substring;
                }
                return color;
            } else {
                template = "strokeColor=#";
                index = style.indexOf(template);
                String substring = style.substring(index + template.length());
                int i = substring.indexOf(';');
                String color;
                if (i != -1) {
                    color = substring.substring(0, i);
                } else {
                    color = substring;
                }
                return color;
            }
        }
        return null;
    }

    /**
     * Get all spike generators
     *
     * @param mxCells
     */
    static void findSpikeGenerator(List<MxCell> mxCells) {
        spikeVMs = new ArrayList<>();
        final ArrayList<MxCell> spikes = new ArrayList<>();
        String spike = "mxgraph.basic.8_point_star";
        for (MxCell mxCell : mxCells) {
            String style = mxCell.getStyle();
            if (!TextUtil.isEmpty(style)) {
                if (style.contains(spike)) {
                    Double x = null;
                    Double y = null;
                    Double height = null;
                    Double width = null;
                    if (mxCell.getMxGeometry().getX() != null) {
                        x = new Double(mxCell.getMxGeometry().getX());
                    } else {
                        LOG.debug("Spike " + mxCell.getId() + " don't have x coordinate");
                    }
                    if (mxCell.getMxGeometry().getY() != null) {
                        y = new Double(mxCell.getMxGeometry().getY());
                    } else {
                        LOG.debug("Spike " + mxCell.getId() + " don't have y coordinate");
                    }
                    if (mxCell.getMxGeometry().getHeight() != null) {
                        height = new Double(mxCell.getMxGeometry().getHeight());
                    } else {
                        LOG.debug("Spike " + mxCell.getId() + " don't have height");
                    }
                    if (mxCell.getMxGeometry().getWidth() != null) {
                        width = new Double(mxCell.getMxGeometry().getWidth());
                    } else {
                        LOG.debug("Spike " + " with id-" + mxCell.getId() + " don't have width");
                    }
                    ReceptorVM spikeVM = new ReceptorVM(mxCell.getId(), null, null, null, mxCell.getParent(), x, y, width, height);
                    spikeVM.setSpikeGeneratorContains(true);
                    spikeVMs.add(spikeVM);
                }
            }
        }
    }


    public void run() throws JAXBException, URISyntaxException, FileNotFoundException {
        URL resource = this.getClass().getClassLoader().getResource("serotonin_pathway.xml");

        FileInputStream fileInputStream = new FileInputStream(resource.getFile());

        JAXBContext jc = JAXBContext.newInstance(MxGraphModel.class);
        StreamSource xml = new StreamSource(fileInputStream);
        Unmarshaller unmarshaller = jc.createUnmarshaller();
        JAXBElement<MxGraphModel> je1 = unmarshaller.unmarshal(xml, MxGraphModel.class);
        MxGraphModel mxGraphModel = je1.getValue();


        //Get mxCells
        MxCell[] mxCells = mxGraphModel.getRoot().getMxCell();
        List<MxCell> mxCells1 = removeLegenda(mxCells);


        List<BrainRegionVM> brainRegionVMs = parseBrainRegion(mxCells1);
        brainRegionMap = new HashMap<>();
        for (BrainRegionVM brainRegionVM : brainRegionVMs) {
            brainRegionMap.put(brainRegionVM.getId(), brainRegionVM);
        }

        LOG.debug("####################################################");
        findSpikeGenerator(mxCells1);
        receptorVMs = parseReceptors(mxCells1);

        final List<LinkVM> links = findLinks(mxCells1);


        resolveInnerBrainRegion(brainRegionVMs);

        brainRegionMap.keySet().stream().filter(id -> !brainRegionServices.containsKey(id)).forEach(id -> {
            final BrainRegionVM brainRegionVM = brainRegionMap.get(id);
            BrainRegion brainRegion = new BrainRegion();
            brainRegion.setZoneName(brainRegionVM.getValue());
            final List<Receptor> receptorsByBrain = findReceptorsByBrain(brainRegionVM.getParentId());
            brainRegion.getAllReceptors().addAll(receptorsByBrain);
            brainRegion.getInnerReceptors().addAll(receptorsByBrain);
            brainRegionServices.addById(id, brainRegion);
        });

        configureLinks(links);

        addToAllReceptorsBrainRegion();
        System.out.println("############################################################");
        dataFileGenerator.generate(brainRegionServices.getPythonBrainRegionMap());
        System.out.println();
        neuromodulationFileGenerator.generate(brainRegionServices.getPythonBrainRegionMap());
    }

     public static void main(String[] args) throws JAXBException {
        AnnotationConfigApplicationContext annotationConfigApplicationContext = new AnnotationConfigApplicationContext(CoreConfig.class);
        App bean = annotationConfigApplicationContext.getBean(App.class);
        try {
            bean.run();
        } catch (URISyntaxException e) {
            e.printStackTrace();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    private void addToAllReceptorsBrainRegion() {
        for (String s : brainRegionServices.getKeys()) {
            final BrainRegion brainRegion = brainRegionServices.getById(s);
            for (Receptor receptor : brainRegion.getAllReceptors()) {
                receptor.setBrainRegion(brainRegion);
            }
        }
    }


    private void configureLinks(List<LinkVM> links) {
        List<LinkVM> temp = new ArrayList<>();
        int id = 0;
        //resolve bedirect links
        for (LinkVM link : links) {
            if (link.isBeDirect()) {
                LinkVM reverse = link.reverse();
                reverse.setId("id" + id);
                id++;
                temp.add(reverse);
            }
        }
        links.addAll(temp);


        //On brain region link pointer
        for (LinkVM link : links) {
            final SynapseType synapseType = ParseUtil.getSynapseTypeByLink(link);
            if (brainRegionServices.containsKey(link.getSource())) {
                //From brain region
                final BrainRegion brainRegion = brainRegionServices.getById(link.getSource());
                ArrayList<Receptor> fromReceptors = new ArrayList<>();
                fromReceptors.addAll(brainRegion.getInnerReceptors());
                for (BrainRegion childRegion : brainRegion.getChildBrainRegions()) {
                    fromReceptors.addAll(childRegion.getInnerReceptors());
                }
                if (brainRegionServices.containsKey(link.getTarget())) {
                    //Region to Region link
                    BrainRegion targetBrainRegion = brainRegionServices.getById(link.getTarget());
                    ArrayList<Receptor> toReceptors = new ArrayList<>();
                    for (BrainRegion toChildBrainRegion : targetBrainRegion.getChildBrainRegions()) {
                        toReceptors.addAll(toChildBrainRegion.getInnerReceptors());
                    }
                    toReceptors.addAll(targetBrainRegion.getInnerReceptors());
                    for (Receptor fromReceptor : fromReceptors) {
                        fromReceptor.getConnectedReceptorBySynapseType(synapseType).addAll(toReceptors);
                    }
                } else {
                    for (Receptor from : fromReceptors) {
                        //From Region to Receptor
                        from.getConnectedReceptorBySynapseType(synapseType).add(receptorServices.getById(link.getTarget()));
                    }
                }
            } else {
                if (brainRegionServices.containsKey(link.getTarget())) {
                    //From Receptor to Brain Region
                    final BrainRegion targetRegion = brainRegionServices.getById(link.getTarget());
                    ArrayList<Receptor> toReceptors = new ArrayList<>();
                    for (BrainRegion toChildBrainRegion : targetRegion.getChildBrainRegions()) {
                        toReceptors.addAll(toChildBrainRegion.getInnerReceptors());
                    }
                    toReceptors.addAll(targetRegion.getInnerReceptors());
                    receptorServices.getById(link.getSource()).getConnectedReceptorBySynapseType(synapseType).addAll(toReceptors);
                } else {
                    //From Receptor to Receptor
                    receptorServices.getById(link.getSource()).getConnectedReceptorBySynapseType(synapseType).add(receptorServices.getById(link.getTarget()));
                }

            }
        }


    }


    private List<Receptor> findReceptorsByBrain(String id) {
        return receptorVMs.stream().filter(receptorVM -> receptorVM.getParentId().equals(id)).map(this::mVtoReceptorConverter).collect(Collectors.toCollection(ArrayList::new));
    }

    private Receptor mVtoReceptorConverter(ReceptorVM vm) {
        final Receptor receptor = ParseUtil.receptorVMToReceptor(vm);
        receptorServices.addById(vm.getId(), receptor);
        return receptor;
    }

    private Map<String, List<BrainRegionVM>> resolveInnerBrainRegion(List<BrainRegionVM> brainRegionVMs) {
        Map<String, List<BrainRegionVM>> map = new HashMap<>();

        for (BrainRegionVM brainRegionVM : brainRegionVMs) {
            String parentId = brainRegionVM.getParentId();
            if (map.get(parentId) == null) {
                ArrayList<BrainRegionVM> brList = new ArrayList<>();
                brList.add(brainRegionVM);
                map.put(parentId, brList);
            } else {
                map.get(parentId).add(brainRegionVM);
            }
        }


        for (String s : map.keySet()) {
            List<BrainRegionVM> brainRegionVMs1 = map.get(s);
            if (brainRegionVMs1.size() > 1) {
                findBrainDependency(brainRegionVMs1);
                resolverInnerReceptorsForBrainRegion(brainRegionVMs1, brainRegionVMs1.get(0).getParentId());
            }
        }

        return map;
    }

    private void resolverInnerReceptorsForBrainRegion(List<BrainRegionVM> brainRegionVMs1, String parentId) {
        HashMap<BrainRegionVM, List<ReceptorVM>> recepList = new HashMap<>();
        List<ReceptorVM> newList = new ArrayList<>();

        receptorVMs.stream().filter(vm -> vm.getParentId().equals(parentId)).forEach(newList::add);


        for (BrainRegionVM brainRegionVM : brainRegionVMs1) {
            newList.stream().filter(receptorVM -> elementIsContainsIn(brainRegionVM, receptorVM)).forEach(receptorVM -> {
                List<ReceptorVM> container = recepList.getOrDefault(brainRegionVM, new ArrayList<>());
                container.add(receptorVM);
                recepList.put(brainRegionVM, container);
            });
        }


        for (BrainRegionVM brainRegionVM : recepList.keySet()) {
            final BrainRegion brainRegion = brainRegionServices.getById(brainRegionVM.getId());
            final List<Receptor> receptors = new ArrayList<>();
            for (ReceptorVM vm : recepList.get(brainRegionVM)) {
                Receptor receptor = ParseUtil.receptorVMToReceptor(vm);
                receptors.add(receptor);
                receptorServices.addById(vm.getId(), receptor);
            }
            brainRegion.getAllReceptors().addAll(receptors);
            brainRegion.getInnerReceptors().addAll(receptors);
        }


        //resolve only inner receptors
        for (String key : brainRegionServices.getKeys()) {
            BrainRegion brainRegion = brainRegionServices.getPythonBrainRegionMap().get(key);
            if (brainRegion.isLeaf()) {
                while (brainRegion.getParent() != null) {
                    brainRegion.getParent().getInnerReceptors().removeAll(brainRegion.getAllReceptors());
                    brainRegion = brainRegion.getParent();
                }
            }
        }


        //resolve inner receptors, not leaf
        for (String key : brainRegionServices.getKeys()) {
            BrainRegion brainRegion = brainRegionServices.getPythonBrainRegionMap().get(key);
            while (brainRegion.getParent() != null) {
                brainRegion.getParent().getInnerReceptors().removeAll(brainRegion.getInnerReceptors());
                brainRegion = brainRegion.getParent();
            }
        }


    }


    //Add all brainRegion to map
    private void findBrainDependency(List<BrainRegionVM> brainRegionVMs1) {
        //Finding root
        BrainRegionVM root = brainRegionVMs1.get(0);
        double maxWidth = brainRegionVMs1.get(0).getWidth();
        double maxHeight = brainRegionVMs1.get(0).getHeight();

        for (BrainRegionVM brainRegionVM : brainRegionVMs1) {
            Double height = brainRegionVM.getHeight();
            Double width = brainRegionVM.getWidth();
            if (height > maxHeight && width > maxWidth) {
                root = brainRegionVM;
                maxHeight = height;
                maxWidth = width;
            }

        }

        System.out.println("Root is " + root);

        brainRegionVMs1.remove(root);
        root.setX(new Double(0));
        root.setY(new Double(0));
        brainRegionVMs1.add(root);


        HashMap<BrainRegionVM, List<BrainRegionVM>> brainRegionContainer = new HashMap<>();


        for (BrainRegionVM brainRegionVM : brainRegionVMs1) {
            for (BrainRegionVM regionVM : brainRegionVMs1) {
                if (elementIsContainsIn(brainRegionVM, regionVM)) {
                    List<BrainRegionVM> container = brainRegionContainer.getOrDefault(brainRegionVM, new ArrayList<>());
                    container.add(regionVM);
                    brainRegionContainer.put(brainRegionVM, container);
                }
            }
        }

        HashMap<BrainRegionVM, List<BrainRegionVM>> cont = new HashMap<>();


        if (brainRegionContainer.keySet().size() == 1) {
            cont = brainRegionContainer;
        } else {
            for (BrainRegionVM first : brainRegionContainer.keySet()) {
                for (BrainRegionVM second : brainRegionContainer.keySet()) {
                    if (first != second) {
                        final List<BrainRegionVM> firstList = brainRegionContainer.get(first);
                        final List<BrainRegionVM> secondList = brainRegionContainer.get(second);
                        if (secondList.size() < firstList.size()) {
                            firstList.removeAll(secondList);
                        }
                        cont.put(first, firstList);
                    }
                }
            }
        }


        //Create model python model
        for (BrainRegionVM parentRegion : cont.keySet()) {
            BrainRegion brainRegion = brainRegionServices.getByIdOrNew(parentRegion.getId());
            brainRegion.setZoneName(parentRegion.getValue());
            for (BrainRegionVM childRegion : cont.get(parentRegion)) {
                BrainRegion region = brainRegionServices.getByIdOrNew(childRegion.getId());
                region.setZoneName(childRegion.getValue());
                region.setParent(brainRegion);
                brainRegion.getChildBrainRegions().add(region);
                if (!cont.keySet().contains(childRegion)) {
                    region.setLeaf(true);
                    System.out.println(region.getZoneName() + " is leaf");
                }
                brainRegionServices.addById(childRegion.getId(), region);
            }
            brainRegionServices.addById(parentRegion.getId(), brainRegion);
        }
    }

    private boolean elementIsContainsIn(BrainRegionVM container, BrainRegionVM regionVM) {
        Double width = container.getWidth();
        Double height = container.getHeight();
        Double x = container.getX();
        Double y = container.getY();

        Double regionVMHeight = regionVM.getHeight();
        Double regionVMWidth = regionVM.getWidth();
        Double regionVMX = regionVM.getX();
        Double regionVMY = regionVM.getY();

        if (checkContains(width, height, x, y, regionVMHeight, regionVMWidth, regionVMX, regionVMY)) return true;

        return false;
    }

    private boolean checkContains(Double width, Double height, Double x, Double y, Double regionVMHeight, Double regionVMWidth, Double regionVMX, Double regionVMY) {
        if ((regionVMX > x && regionVMY > y) && (y + height > regionVMY + regionVMHeight && regionVMX > x) && (x + width > regionVMX + regionVMWidth && regionVMY > y) && (regionVMX + regionVMWidth < x + width && regionVMY + regionVMHeight < y + height)) {
            return true;
        }
        return false;
    }

    private List<LinkVM> findLinks(List<MxCell> mxCells1) {
        List<LinkVM> linkVMs = new ArrayList<>();
        for (MxCell mxCell : mxCells1) {
            if (!TextUtil.isEmpty(mxCell.getSource()) && !TextUtil.isEmpty(mxCell.getTarget()) && !mxCell.getSource().equals(mxCell.getTarget())) {
                boolean thisLinkIsBeDirect = isThisLinkIsBeDirect(mxCell);
                LinkVM linkVM = new LinkVM(mxCell.getId(), getColor(mxCell), mxCell.getSource(), mxCell.getTarget(), thisLinkIsBeDirect, mxCell.getValue());
                linkVMs.add(linkVM);
            }
        }
        return linkVMs;
    }


    private boolean isThisLinkIsBeDirect(MxCell mxCell) {
        String ling = "startArrow=classic";
        String style = mxCell.getStyle();
        if (!TextUtil.isEmpty(style)) {
            if (style.contains(ling)) {
                return true;
            } else {
                return false;
            }
        }
        return false;
    }


    private List<MxCell> removeLegenda(MxCell[] mxCells) {
        String legendaParent = null;
        List<MxCell> list = new ArrayList<>();
        for (MxCell mxCell : mxCells) {
            String value = mxCell.getValue();
            if (!TextUtil.isEmpty(value) && value.contains("Legenda")) {
                legendaParent = mxCell.getParent();
                break;
            }
        }

        if (TextUtil.isEmpty(legendaParent)) {
            return Arrays.asList(mxCells);
        }

        for (MxCell mxCell : mxCells) {
            String parent = mxCell.getParent();
            if (!TextUtil.isEmpty(parent) && !parent.equals(legendaParent)) {
                list.add(mxCell);
            }
        }
        return list;
    }
}
