import BlackboardQuiz
from flask import send_file
# from question_bank import questions
# create a function where it takes video ids, search through the question base indexed by ID and turns it into a BB package
# question bank format
questions={'10506': [['What types of bacteria are enriched by adding salt to the mud/water mix in a Winogradsky column?', ['halophiles', 'sulfur oxidizers', 'thermophiles', 'iron oxidizers'], 0], ['What types of bacteria are enriched by adding a nail to the mud/water mix in a Winogradsky column?', ['halophiles', 'sulfur oxidizers', 'thermophiles', 'iron oxidizers'], 3], ['What type of bacteria can form and a green or a purple layer in the Winogradsky column?', ['halophiles', 'sulfur oxidizers', 'thermophiles', 'iron oxidizers'], 1]], '10507': [['What is the purpose of constructing a Winogradsky column?', ['To provide a system for enriching microbial communities', 'To grow bacteria that is easily grown in a petri dish', 'To allow microbes to change color so they will be more easily seen', 'To make sure all the bacteria has an abundant oxygen supply.'], 0], ['In a Winogradsky column why do aerobic bacterial communities form at the top of the column while anerobic form at bottom?', ['A methane gradient', 'A light gradient', 'A sulfur gradient', 'An oxygen gradient'], 3], ['What is serial dilution?', ['A group of bacteria grown at different dilutions through use of varied nutrient medium', 'A concentration being reduced through successive resuspension in the same volumes of diluent', 'A series of bacterial being growth at different temperature to achieve different plating densities', 'A method of preparing a liquid form of bacterial medium'], 1]], '10508': [['Which of the following represents a proper way to perform a serial dilution?', ['Take 2 mL of a 5 mL sample, pipet this into 9 mL of diluent, and mix well. Take 1 mL of this sample, pipet this into 6 mL of diluent, and repeat the process until you have achieved the final dilution.', 'Take 1 mL of a 10 mL sample, pipet this into 9 mL of diluent, and mix will. Take 1 mL of this sample, pipet this into 9 mL of diluent, and repeat the process until you have achieved the final dilution.', 'Take 9 mL of a 10 mL sample, pipet this into 9 mL of diluent, and mix will. Take 1 mL of this sample, pipet this into 9 mL of diluent, and repeat the process until you have achieved the final dilution.', 'Take 10 mL of a 9 mL sample, pipet this into 1 mL of diluent, and mix will. Take 10 mL of this sample, pipet this into 9 mL of diluent and repeat the process until you have achieved the final dilution.'], 1], ['When would you use spread plating instead of streak plating?', ['Isolating a single colony from a mixed population', 'Producing many countable bacterial colonies', 'Growing bacterial samples from a Winogradsky column', 'Creating an anaerobic environment'], 1], ['When would it be preferable to use streak plating instead of spread plating?', ['Isolating a single colony from a mixed population', 'Producing many countable bacterial colonies', 'Growing bacterial samples from a Winogradsky column', 'Creating an anaerobic environment'], 0]], '10509': [['If 0.2 mL of a 1:10,000 dilution of bacteria yields 289 colonies, what is the CFU/mL for this sample?', ['10,900,000', '14,450,000', '144,500,00', '1,090,000,000'], 1], ['What percent of organisms are capable of be successfully cultured in the laboratory?', ['0%', '&lt;1%', '50%', '&gt;99%'], 1], ['What is meant when a microbial species is described as generalist?', ['Able to be grown in a laboratory', 'Capable of tolerating a wide variety of environments', 'In charge of commanding a bacterial army', 'Only able to thrive at 50&deg;C under high salt conditions'], 1]], '10510': [['What do experimental results indicate if a bacterial colony grows on Mannitol Salt Agar (MSA) and appears surrounded bright yellow media?', ['The bacteria are Gram negative and can ferment mannitol', 'The bacteria are Gram positive and cannot ferment mannitol', 'The bacteria are Gram positive and can ferment mannitol', 'The bacteria are Gram negative and cannot ferment mannitol'], 2], ['What do experimental results indicate if a bacterial colony grows on Eosin Methyl Blue media and appears as a dark, metallic colony?', ['The bacteria are Gram negative and can ferment lactose', 'The bacteria are Gram negative and cannot ferment lactose', 'The bacteria are Gram positive and cannot ferment lactose', 'The bacteria are Gram positive and can ferment lactose'], 0], ['A fastidious organism is an organism that is...', ['...fast growing under all conditions', '... is not culturable in the lab', '...culturable without any special nutrients', '... culturable, but only when specific conditions are met'], 3]], '10511': [['What is a clonal colony of bacteria?', ['A colony of bacteria that has been cloned by radioactivity', 'A genetically modified colony of bacteria', 'A colony of bacteria from multiple sources', 'A colony of bacteria originating from a single bacterium'], 3], ['Which NOT a part of the streak plating protocol?', ['Progressive bacterial dilution', 'Performed on solid media', 'One single zig-zig pattern', 'Uses a single petri dish'], 2], ['What is the purpose of using a flame sterilized inoculation loop when moving to the next section of the petri dish in streak plating?', ['To remove any remaining bacterial cells', 'To make sure only the resistant bacteria survive', 'The serial dilution only works when the loop is hot', 'The inoculation loop collects more bacteria when fresh'], 0]], '10512': [['How can streak plating be used to isolate single bacterial colonies?', ['The bacteria are selected using different antibiotics in each zone of the plate', 'The bacteria are prepared as serial dilutions in conical tubes and then streaked onto multiple plates', 'The bacterial are diluted by using multiple zones on a single plate, each streaked from the previous zone', 'The single bacterium is isolated by using a cell sorting apparatus before plate streaking'], 2], ['What is NOT a reason to use bacterial streak plating?', ['To determine colony morphology', 'To grow bacteria in suspension', 'To select media specific strains', 'To isolate single colonies'], 1], ['What is 16s rRNA?', ['The larger of the ribosomal subunits', 'The ribonucleotide component of the 30S ribosomal subunit', 'The smaller of the ribosomal subunits', 'The ribonucleotide component of the 50S ribosomal subunit'], 1]], '10513': [['Why is the 16s rRNA a good target for sequencing?', ['16s rRNA is composed completely of protein', '16s rRNA is completely composed of variable regions in most strains of bacteria', '16s rRNA contains both conserved regions and variable regions in different strains of bacterial', '16s rRNA is completely composed of conserved regions in most strains of bacteria'], 2], ['Which if the following reagents is not required for DNA amplification by PCR?', ['DNA template', 'RNA polymerase', 'Forward and reverse primers', 'DNA polymerase'], 1], ['What is a BLAST search?', ['A search tool that can be used to analyze agarose gel electrophoresis results', 'A bacterial lifecycle search that can classify different types of bacterial strains', 'A tool that searches a nucleotide sequence database and identifies nucleotides sequences based on percent similarity', 'A search engine that can find local bursts of DNA variation'], 2]], '10514': [['Which of the following features is present in a high quality chromatogram?', ['Distinct, evenly spaced peaks', 'All peaks are of the same color', 'Multiple peaks in the same locations', "Broad peaks at the 5' and 3' end"], 0], ['Which of the following would NOT be proper axes on a growth curve?', ['Growth vs time', 'OD vs. minutes', 'CFU/mL vs. OD', 'CFU/mL vs hours'], 2], ['Place the bacterial growth phases in the correct order.', ['Exponential, Death, Lag, Stationary', 'Lag, Stationary, Exponential, Death', 'Stationary, Exponential, Lag, Death', 'Lag, Exponential, Stationary, Death'], 3]], '10515': [['Which of the following doubling times represent the most optimal bacterial growth conditions for this set of values?', ['5 minutes and 5 seconds', '12 minutes and 3 seconds', '16 minutes and 25 seconds', '1 hour and 12 minutes'], 0], ['Bacterial doubling time should be determined in which growth phase?', ['Lag', 'Death', 'Exponential', 'Stationary'], 2], ['What is the purpose creating a standard curve of CFU/mL versus OD600 for a given growth curve?', ['To determine the bacterial doubling time', 'To estimate CFU/mL from OD600 measurements', 'To calculate the OD600 from the bacterial doubling time', 'To determine if the bacteria are in the stationary phase'], 1]], '10516': [['What is the minimum inhibitory concentration (MIC)?', ['The concentration of broth needed to grow bacteria', 'The smallest concentration of bacteria that can grow on a plate and still be visible', 'The lowest antibody concentration at which bacteria can no longer grow', 'gene complex coding immune response'], 2], ['What is the purpose of the plastic strip used in the Epsilometer- or E-test?', ['The strip kills all the surrounding bacteria', 'The strip contains the antibiotic gradient', 'The strip seeds the bacteria on the plate', 'The strip is preincubated in the MH-F broth'], 1], ['What is the standard for determining synergy using the Fractional Inhibitory Concentration (FIC) index?', ['&lt;0.5', '&gt;0.5', '=1', '&lt;1'], 0]], '10517': [['Which of the following NOT true of BOTH the cross and non-cross E-tests?', ['The test can be used to determine the FIC index', 'Multiple antibiotic strips are placed on the plate simultaneously.', 'The test uses plastic antibiotic strips', 'MHA plates are used to grow the bacteria'], 1], ['How does one determine the minimum inhibitory concentration in the broth test?', ['Looking at the growth inhibition zone', 'Reading the concentration on the plastic strip', 'Testing the FIC index', 'Examining the broth for lack of turbidity'], 3], ['<p>What cellular characteristic distinguishes Gram positive from Gram negative bacteria?</p>', ['<p>Gram negative bacteria do not have a cell wall</p>', '<p>Gram positive bacteria have a thick peptidoglycan cell wall</p>', '<p>Gram positive bacteria form spores</p>', '<p>Gram negative bacteria are always rod-shaped bacilli</p>'], 1]], '5081': [['Which of the following is NOT one of the reasons <i>S. cerevisiae</i> makes a great model system?', ['Yeast cells grow quickly and are easy to maintain in the lab.', 'Its genome is largely unknown, posing fascinating research topics.', 'It encodes proteins similar in sequence to other eukaryotes.', 'Its genetics are easily manipulated.'], 1], ['Shuttle vectors...', ['can only bring material to <i>E. coli</i>.', 'are lethal to their hosts.', 'can replicate in multiple species.', 'can only replicate in yeast.'], 2], ['Yeast produces alcohol as a byproduct due to...', ['fermentation in low oxygen conditions.', 'homologous recombination upon fermentation.', 'excess oxygen and fermentation.', 'homologous recombination and low oxygen conditions.'], 0]], '5082': [['A _______ can be used to introduce foreign DNA into the yeast genome via ______________.', ['Cyclin kinase, telomeres.', 'Budding event, DNA damage.', 'Shuttle vector, homologous recombination.', 'Hermaphrodite, budding.'], 2], ['Autophagy refers to...', ['the purification of key proteins.', 'the breakdown of the cell membrane, resulting in cell death.', 'the breakdown of expendable organelles into amino acids for cell resources.', 'the breakdown of DNA repair mechanisms.'], 2], ['The three main body segments of <i>Drosophila</i> are illustrated in <b>Figure 1</b>. Which of the following corresponds to the body segments labeled by A, B and C?<br /><br /><img src="ppg/d6/brg00016e02e89d2a6a4/q6-1.jpg" width="438" height="271" /><br /><br />Figure 1- The Three Main Body Segments of <i>Drosophila</i><br />', ['head, torso, bottom', 'head, thorax, abdomen', 'posterior, middle, anterior', 'head, abdomen, thorax'], 1]], '5103': [['Based on the data presented in Figure 2, what is the approximate lifespan of a fruit fly?<br /><br /><img src="ppg/d6/brg00016e02e89d2a6a4/q7-1.png" width="406" height="334" /><br /><br />Figure 2: The <i>Drosophila </i>Lifespan', ['0-20 days', '20-40 days', '40-60 days', '60-80 days'], 3], ['Which of the following statements is <b>NOT</b> true about <i>Drosophila </i>as a model organism?', ['Flies are inexpensive to maintain and house in a laboratory.', 'Their short life cycle allows scientists to perform genetic crosses quickly and frequently.', '<i>Drosophila </i>females are extremely fertile, allowing for high sample numbers.', '<i>Drosophila</i> are more genetically similar to humans than all other model organisms.'], 3], ['Which of these best describes the lack of genetic redundancy in <i>Drosophila</i>?', ['They often have fewer versions of a gene than mice, making direct links between a gene and a phenotype easier to study via gene mutation.', 'Most mutation experiments linking a gene to a phenotype are equally direct and simple to perform across all species, so genetic redundancy is not relevant.', 'Drosophila have such varied genetic copies contributing to a phenotype that mutation experiments linking genes and phenotypes are best performed in mice.', 'Drosophila have more genetic redundancy than mice.'], 0]], '5095': [['Linking a distinctive chromosomal banding pattern to a certain distinctive phenotype demonstrates...', ['The instability of a constantly shifting genome.', 'The ease of anesthetizing <i>Drosophila</i>.', 'The lack of scientific knowledge in the 1910s.', 'The chromosomal theory of inheritance.'], 3], ['Which of the following is NOT true regarding selectable markers on plasmid DNA for yeast transformation?', ["Yeast that doesn't successfully incorporate the plasmid will not survive in media containing the selectable marker.", 'The selectable marker is usually found in the multiple cloning site of the plasmid.', 'The selectable markers can encode for genes that enable drug-resistance.', 'The selectable markers can encode genes for enzymes which synthesize amino acids the yeast strain otherwise cannot produce.'], 1], ['Which of the following best represents the sequence of events used to transform yeast by lithium acetate transformation?', ['Yeast cells are grown from a single colony &#8594; Cells are heat-shocked &#8594; Transformed cells are harvested by centrifugation &#8594; Cells are plated on agar plates that select for the desired transformants', 'Yeast cells are grown from a single colony &#8594; Yeast cells are harvested by centrifugation &#8594; Yeast cells are incubated with the transformation mixture &#8594; Cells are plated on agar plates that select for the desired transformants &#8594; Transformed cells are harvested by centrifugation', 'Yeast cells are grown from a single colony &#8594; Yeast cells are harvested by centrifugation &#8594; Yeast cells are incubated with the transformation mixture &#8594;Cells are heat-shocked &#8594; Heat-shocked cells are harvested by centrifugation &#8594; Cells are plated on agar plates that select for the desired transformants', 'Yeast cells are grown from a single colony &#8594; Yeast cells are incubated with the transformation mixture&#8594; Yeast cells are harvested by centrifugation &#8594; Cells are plated on agar plates that select for the desired transformants'], 2]], '5084': [['In sexual cycling, haploid cells that contain a reporter and deleted locus can be combined into one cell through...', ['mitotic recombination.', 'meiotic recombination.', 'recombination.', 'enzyme-specific recombination.'], 1], ['What is an example of a positive control in a yeast transformation reaction?', ['A yeast cell suspension with plasmid DNA on a YPD plate that does not contain any antibiotics.', 'A yeast cell suspension on an appropriate selection plate, such as one that contains antibiotics.', 'A yeast cell suspension expressing plasmid DNA on an X-gal plate.', 'A yeast cell suspension expressing plasmid DNA on a plate that can only grow if the yeast can synthesize amino acids that they cannot normally produce.'], 0], ['Plasmids that can replicate in more than one host species are called:', ['RNA vectors', 'Linear vectors', 'Shuttle vectors', 'Supercoiled vectors'], 2]], '5104': [['You discover that the food in your population vial is covered with mold. What could you have added to prevent this?', ['More yeast.', 'Propionic acid.', 'Fermented fruit.', 'Nothing; mold growth in fly population vials is unstoppable.'], 1], ['A population of 500 flies would most likely be kept in a _________ at ______ &#176;C.', ['Bottle, 25 &#176;C', 'Vial, 37 &#176;C', 'Hutch, 4 &#176;C', 'Tube, -20 &#176;C'], 0], ['Which of these is NOT true about the pupal stage?', ['It occurs between the larval and adult stage.', 'When half the pupae have left their casings, it is time to change that container.', 'It determines which flies will retain mutations.', 'Larvae incubate and develop into adults during this stage.'], 2]], '5097': [['<p>CO<sub>2 </sub>is preferred as an anesthetic for flies because...</p>', ['<p>It causes severe mutations in your populations.</p>', '<p>It contains odors flies are attracted to.</p>', '<p>Each fly must be anesthetized individually.</p>', '<p>It does not cause acute mortality in flies.</p>'], 3], ['The Power Tower experiments can measure exercise by taking advantage of which natural response in flies?', ['Geophilic motion', 'Geophobic motion', 'Gravitas Geotaxis', 'Negative Geotaxis'], 3], ['Which of the following statements is NOT true about the gastrulation of an embryo?', ['Gastrulation is a process in which cell shape changes drive invaginations of a monolayer of cells.', 'Gastrulation results in the creation of three germ layers: the endoderm, mesoderm, and ectoderm.', 'During gastrulation, cells migrate to the periphery of the embryo and become individualized.', 'The germ layers established during gastrulation ultimately give rise to specific tissues.'], 2]], '5093': [['The <i>Drosophila</i> life cycle progresses through four distinct stages of development. What is the correct order of the <i>Drosophila </i>life cycle?', ['larva&#8594;embryo&#8594;pupa&#8594;adult', 'embryo&#8594;pupa&#8594;larva&#8594;adult', 'embryo&#8594;larva&#8594;pupa&#8594;adult', 'adult&#8594;larva&#8594;pupa&#8594;embryo'], 2], ['Virgin <i>Drosophila</i> females can be identified by...', ['sex combs on the forelegs.', 'exceptionally dark lower abdomens.', 'the curly wings genetic marker.', 'a very light body color.'], 3], ['Which of these genes initially establishes the posterior of the <i>Drosophila</i> embryo?', ['Bicoid', 'Nanos', 'Engrailed', 'GAL4'], 1]], '5110': [['Why do <i>Drosophila</i> geneticists use balancer chromosomes in genetic crosses?', ['To ensure an even distribution of stripes encoded by the pair-rule genes.', 'Balancer chromosomes prevent genetic recombination and contain genetic markers that are useful in determining the genotypes of the progeny.', 'Balancer chromosomes help distinguish males from females.', 'Flies that contain a balancer chromosome have a competitive advantage.'], 1], ['How many embryos can a fertilized female <i>Drosophila</i> lay?', ['A fertilized female <i>Drosophila</i> can lay up to 100 embryos per day.', 'A fertilized female <i>Drosophila</i> will lay at least 50 embryos per day.', 'A female <i>Drosophila</i> can lay up to 100 embryos in her lifetime.', 'A female <i>Drosophila</i> can lay up to 1000 embryos in her lifetime.'], 0], ['Through how many instar stages do <i>Drosophila</i> develop?', ['<i>Drosophila </i>go through two instars.', '<i>Drosophila </i>go through three instars.', '<i>Drosophila </i>go through five instars.', '<i>Drosophila </i>go through seven instars.'], 1]], '5096': [['How does a sucrose solution help when harvesting larvae?<br /><br /><img src="ppg/d6/brg00016e02e89d2a6a4/q28-1.png" width="432" height="288" />', ['Larvae float up on the sucrose solution.', 'Larvae are attracted to the solution.', 'Larvae are paralyzed by the solution.', 'Larvae become sticky in the solution.'], 0], ['What is an attribute of the blue and purple imaginal discs in this larva?', ['These structures develop into specific body parts of the adult fly.', 'These structures only form when activated by a reporter gene.', 'These structures do not change from larval form to the adult form.', 'These structures typically stay dormant during the fly lifespan.'], 0], ['What must be done to embryos to prepare them for live cell imaging?', ['Embryos must be warmed to 70 &#176;C.', 'Embryos must be soaked in hydrochloric acid.', 'Embryos must be dechorionated.', 'Embryos must be washed in 70% ethanol.'], 2]], '5106': [['In <b>Figure 1</b>, which range of optical density (OD) values at 600nm represent an active division and cell doubling phase for yeast cells?<br /><br /><b>Figure 1 &#8211; A Yeast Growth Curve (time code @2:18)</b><br /><br /><img src="ppg/d6/brg00016e02e89d2a6a4/q31-1.jpg" width="520" height="344" />', ['0.1 to 1.2', '1.1 to 1.2', '0.2 to 1.0', '0.1 to 0.15'], 2], ['What is an ideal starting optical density at 600nm for a yeast culture when growing a large quantity of cells?', ['0.5 - 1.0', '0.01 - 0.02', '1.0 - 1.5', '0.1 - 0.2'], 3], ['What is the approximate shelf life of yeast that has been grown on plates when stored at 4 &#176;C?', ['Up to 3 months', 'Up to 3 years', '1-3 years', 'Up to 3 days'], 0]], '5105': [['Individual colonies that form around yeast streaks on a plate each contain...', ['A pure genetic population of cells.', 'A mixed genetic population of cells.', 'Cells that can only grow at 15 &#176;C.', 'They do not contain viable cells.'], 0], ['Wild type yeast...', ['Do not need peptone to grow.', 'Can be used in log phase to study eukaryotic organelles.', 'Have a doubling time of about 30 days.', 'Cannot grow below 50 &#176;C when streaked on plates.'], 1], ['At what point during growth should you harvest yeast cells to optimize yield?', ['Lag phase', 'Log phase', 'Stationary phase', 'Metaphase'], 1]], '5083': [['The addition of chloroform to lysed cells differentiates the cell components into two different phases, the aqueous and organic. Which of the following statements is true regarding these phases?', ['The organic phase contains nucleic acids while the aqueous phase contains proteins. The DNA can then be precipitated from the organic phase with the addition of ethanol.', 'The organic phase contains proteins while the aqueous phase contains nucleic acids. The DNA can then be precipitated from the aqueous phase with the addition of ethanol.', 'The aqueous phase contains all proteins. The DNA can then be precipitated from the aqueous phase with the addition of ethanol.', 'The organic phase contains all proteins and nucleic acids. The DNA can then be precipitated from the organic phase with the addition of ethanol.'], 1], ['Which of the following sequences best represents the major steps in DNA isolation from yeast cells using a column binding protocol?', ['Cells are grown up and harvested by centrifugation &#8594; the cell walls are disrupted&#8594; the cells are lysed &#8594; the sample is centrifuged &#8594;the supernatant is loaded onto a silica column&#8594; following washing steps; the DNA is eluted from the column.', 'Cells are grown up and harvested by centrifugation &#8594; the cells are lysed &#8594; the cell walls are disrupted &#8594;the supernatant is loaded onto a silica column&#8594; following washing steps; the DNA is eluted from the column.', 'The cell walls are disrupted &#8594; the sample is centrifuged &#8594;the resuspended cell pellet is loaded onto a silica column&#8594; following washing steps; the DNA is eluted from the column.', 'Cells are grown up and harvested by centrifugation &#8594; the cells are lysed &#8594; the cell walls are digested &#8594; the sample is centrifuged &#8594;the resuspended cell pellet is loaded onto a silica column.'], 0], ['The destruction of the tough cell walls of yeast cells results in the formation of:', ['Spheroplasts', 'Chloroplasts', 'Protoplasts', 'Ectoblasts'], 0]], '5094': [['When performing nucleic acid isolation using column binding, a critical property of the elution buffer is...', ['that it denatures spheroplasts.', 'that it is extremely concentrated.', 'that it is chloroform-based.', 'that it is RNAse and DNAse free.'], 3], ['According to research on the replicative lifespan of yeast cells, approximately how many daughter cells can a single yeast cell produce before dying?', ['3', '30', '300', '3,000'], 1], ['<b>Figure 1</b> below shows several steps in the yeast cell cycle. Which of the labeled steps represents the START point, the point in which cells commit to the cell cycle? <br /><br /><b>Figure 1</b> (Note: This figure is a composite of events from time event @2:30 to 2:40 in the video.)<br /><br /><img src="ppg/d6/brg00016e02e89d2a6a4/q42-1.png" width="323" height="385" />', ['A', 'B', 'C', 'E'], 0]], '5113': [['Which of the steps in <b>Figure 1</b> represents meiosis in yeast?<br /><br /><b>Figure 1</b> (Note: This figure is a composite of events from time event @2:30 to 2:40 in the video.)<br /><br /><img src="brg00016e02e89d2a6a4/q43-1.jpg" width="323" height="385" /><br /><br />', ['A', 'C', 'D', 'E'], 3], ['Which of the following is NOT true regarding yeast reproduction?', ['Haploids are produced through the process of meiosis.', 'Nuclear fusion of haploid cells results in the zygote.', 'Zygotes cannot enter the mitotic cell cycle.', 'Interphase is comprised of G1, S, and G2 sub-phases.'], 2], ['In haploid yeast interactions, why would a Mat-a cell begin to adopt a schmoo morphology?', ['Excess cytoplasm is present in the cell.', 'Mat-a pheromones are present.', 'Mat-Alpha pheromones are present.', 'Excess diploid yeast are present.'], 2]]}

def find_questions(video_ids):
    id_list=video_ids.split(',')

    with BlackboardQuiz.Package("MyQuestionPools") as package:        
        #You may have multiple question pools in a single package, just
        #repeat this block with different pool names.
        with package.createPool('Demo for CS', description="Questions which are not generated/calculated", instructions="") as pool:
            for ids in id_list:
                if questions[ids]:
                    all_question = questions[ids]
                    for question in all_question:
                            pool.addMCQ(ids, question[0].replace('ppg/d6/',''), question[1],correct=question[2])
                # return str(questions[ids])
    return send_file("MyQuestionPools.zip",as_attachment=True)
        