# Curation

A carefully selected subset of the projects in the [survey](README.md#survey) is presented here in the style of an [awesome list](https://github.com/sindresorhus/awesome).


## Table of Contents

- [Biomedical knowledge graphs](#biomedical-knowledge-graphs)
- [Tools](#tools)
- [Databases](#databases)
- [Ontologies and controlled vocabularies](#ontologies-and-controlled-vocabularies)
- [File formats](#file-formats)


## Biomedical knowledge graphs

- **Biomedical Data Translator** –
  [Publication (2022)](https://doi.org/10.1111/cts.13301),
  [Website](https://ncatstranslator.github.io/TranslatorTechnicalDocumentation/),
  [Code](https://github.com/NCATSTranslator/ReasonerAPI),
  [API](https://smart-api.info/portal/translator),
  [Demo](https://ui.transltr.io/demo)
  - Content:
    - A collection of harmonized APIs
  - Scope:
    - "integrated data from over 250 knowledge sources, each exposed via open application programming interfaces (APIs)"
    - "a diverse community of nearly 200 basic and clinical scientists, informaticians, ontologists, software developers, and practicing clinicians distributed over 11 teams and 28 institutions to form the Biomedical Data Translator Consortium"
  - Goals:
    - "integrate as many datasets as possible, using a ‘knowledge graph’–based architecture, and allow them to be cross-queried and reasoned over by translational researchers"
    - "integrating existing biomedical data sets and “translating” those data into insights intended to augment human reasoning and accelerate translational science"
    - "promote serendipitous discovery and augment human reasoning in a variety of disease spaces"
    - "federate autonomous reasoning agents and knowledge providers within a distributed system for answering translational questions"
  - Sub-projects that construct knowledge graphs:
    - **ROBOKOP** –
      [Publication (2019)](https://doi.org/10.1021/acs.jcim.9b00683),
      [Code](https://github.com/NCATS-Gamma/robokop),
      [Data](https://stars.renci.org/var/plater/bl-3.5.4/RobokopKG/929354295ba7d43c/)
    - **RTX-KG2** –
      [Publication (2022)](https://doi.org/10.1186/s12859-022-04932-3),
      [Code](https://github.com/RTXteam/RTX-KG2),
      [Data](http://rtx-kg2-public.s3-website-us-west-2.amazonaws.com/)


- **Bioteque** –
  [Publication (2022)](https://doi.org/10.1038/s41467-022-33026-0),
  [Website](https://bioteque.irbbarcelona.org),
  [Code](https://gitlabsbnb.irbbarcelona.org/bioteque/bioteque),
  [Data](https://bioteque.irbbarcelona.org/downloads)
  - Content:
    - 450,000 nodes of 12 types
    - 30 million edges of 67 types
    - Extracted from 150 data sources
    - Provided as triples in multiple TSV files
  - Scope:
    - "a resource of unprecedented size and scope that contains pre-calculated embeddings derived from a gigantic heterogeneous network"
    - "Bioteque embeddings retain the information contained in the large biological network"
  - Goals:
    - "make biomedical knowledge embeddings available to the broad scientific community"
    - "evaluate, characterize and predict a wide set of experimental observations"
    - "assessment of high-throughput protein-protein interactome data"
    - "prediction of drug response and new repurposing opportunities"


- **CKG** –
  [Publication (2023)](https://doi.org/10.1038/s41587-021-01145-6),
  [Website](https://ckg.readthedocs.io),
  [Code](https://github.com/MannLabs/CKG),
  [Data](https://doi.org/10.17632/mrcf7f4tc2)
  - Full name: Clinical Knowledge Graph
  - Content:
    - 20 million nodes
    - 220 million edges
    - Extracted from 26 databases, 10 ontologies, 7 million publications
    - Provided as Neo4j graph database
  - Scope:
    - "prior knowledge, experimental data and de-identified clinical patient information"
    - "harmonization of proteomics with other omics data while integrating the relevant biomedical databases and text extracted from scientific publications"
  - Goals:
    - "inform clinical decision-making"
    - "reveal candidate markers of prognosis and/or treatment"
    - "generate new hypotheses that ultimately translate into clinically actionable results"
    - "clinically meaningful queries and advanced statistical analyses"
    - "liver disease biomarker discovery"
    - "multi-proteomics data integration for cancer biomarker discovery and validation"
    - "prioritize treatment options for chemorefractory cases"


- **HALD** –
  [Publication (2023)](https://doi.org/10.1038/s41597-023-02781-0),
  [Website](https://bis.zju.edu.cn/hald),
  [Code](https://github.com/zexuwu/hald),
  [Data](https://doi.org/10.6084/m9.figshare.22828196.v4)
  - Full name: Human Aging and Longevity Dataset
  - Content:
    - 12,227 nodes of 10 types
    - 115,522 edges of various types
    - Extracted from 339,918 biomedical articles in PubMed
    - Provided as triples with additional information in multiple JSON and CSV files
  - Scope:
    - "a text mining-based human aging and longevity dataset of the biomedical knowledge graph from all published literature related to human aging and longevity in PubMed"
  - Goals:
    - "precision gerontology and geroscience analyses"
    - "provide predictions regarding the individuals’ lifespan under various treatment scenarios"
    - "devise novel, biologically-driven therapeutic and preventive strategies that address fundamental aging mechanisms"


- **Monarch KG** –
  [Publication (2024)](https://doi.org/10.1093/nar/gkad1082),
  [Website](https://monarchinitiative.org),
  [Code](https://github.com/monarch-initiative/monarch-ingest),
  [Data](https://data.monarchinitiative.org/monarch-kg/index.html)
  - Naming explanation: "The name ’Monarch Initiative’ was chosen because it is a community effort to create paths for diverse data to be put to use for disease discovery, not unlike the navigation routes that a monarch butterfly would take."
  - Content:
    - 862,115 nodes of 88 types
    - 11,412,471 edges of 23 types
    - Extracted from 33 biomedical resources and biomedical ontologies and "updated with the latest data from each source once a month"
    - Provided in various formats such as SQLite, Neo4J, RDF, KGX
  - Scope:
    - "Monarch App includes an ETL platform for ingesting, harmonizing, and serving diverse life science data relating genes, phenotypes, and diseases into a semantic KG for use in various downstream applications"
    - "Monarch KG integrates gene, disease, and phenotype data"
    - "Monarch Assistant, which will combine the ability of LLMs to answer questions in plain language with Monarch’s extensive KG and analysis algorithms"
  - Goals:
    - "learn different things about the relationship between genotype and phenotype from different organisms"
    - "collect, integrate, and make a broad compendium of species and sources computable"


- **OREGANO** –
  [Publication (2023)](https://doi.org/10.1038/s41597-023-02757-0),
  [Code](https://gitub.u-bordeaux.fr/erias/oregano),
  [Data](https://gitub.u-bordeaux.fr/erias/oregano/-/tree/master/Data_OREGANO/Graphs)
  - Content:
    - 88,937 nodes of 11 types
    - 824,231 edges of 19 types
    - Extracted from various drug, protein and phenotype databases
    - Provided as triples in a TSV file
  - Scope:
    - "a holistically constructed knowledge graph using the broadest possible features and drug characteristics"
    - "integration of natural compounds (i.e. herbal and plant remedies)"
    - "incorporating together disease and drug information and natural compounds"
  - Goals:
    - "computational drug repositioning"
    - "generate hypotheses (molecule/drug - target links) through link prediction"
    - "from the available data, determine whether a drug is potentially capable of binding to a new target"
    - "identify possible repositionable molecules using machine learning (or more specifically deep learning) algorithms"


- **PharMeBINet** –
  [Publication (2022)](https://doi.org/10.1038/s41597-022-01510-3),
  [Website](https://pharmebi.net/#/),
  [Code](https://github.com/ckoenigs/PharMeBINet),
  [Data](https://doi.org/10.5281/zenodo.5816976)
  - Full name: Pharmacological Medical Biochemical Network
  - Content:
    - 2,869,407 nodes of 66 types
    - 15,883,653 edges of 208 types
    - Extracted from 48 data sources
    - Provided as Neo4j graph database and GraphML file
  - Scope:
    - "heterogeneous information on drugs, ADRs, genes, proteins, gene variants, and diseases"
  - Goals:
    - "analysis of ADRs [Adverse Drug Reactions]"
    - "analysis of possible existing connections between gene variants and drugs"


- **PrimeKG** –
  [Publication (2023)](https://doi.org/10.1038/s41597-023-01960-3),
  [Website](https://zitniklab.hms.harvard.edu/projects/PrimeKG),
  [Code](https://github.com/mims-harvard/PrimeKG),
  [Data](https://doi.org/10.7910/DVN/IXA7BM)
  - Full name: Precision Medicine Knowledge Graph
  - Content:
    - 129,375 nodes of 10 types
    - 4,050,249 edges of 30 types
    - Extracted from 20 data sources
    - Provided as triples in a CSV file 
  - Scope:
    - "ten major biological scales, including disease-associated protein perturbations, biological processes and pathways, anatomical and phenotypic scales, and the entire range of approved drugs with their therapeutic action"
    - "improves on coverage of diseases, both rare and common, by one-to-two orders of magnitude compared to existing knowledge graphs"
  - Goals:
    - "support research in precision medicine"
    - "linking biomedical knowledge to patient-level health information"
    - "personalized diagnostic strategies and targeted treatments"
    - "providing a holistic and multimodal view of diseases"


- **SPOKE** –
  [Publication (2023)](https://doi.org/10.1093/bioinformatics/btad080),
  [Website](https://spoke.ucsf.edu),
  [Code](https://github.com/cns-iu/spoke-vis),
  [API](https://spoke.rbvi.ucsf.edu/swagger/)
  - Full name: Scalable Precision Medicine Open Knowledge Engine
  - Content:
    - 27,056,367 nodes of 21 types
    - 53,264,489 edges of 55 types
    - Extracted from 41 databases
    - Provided as a REST API that accepts graph queries, but "not available as a bulk download"
  - Scope:
    - "ranging from molecular and cellular biology to pharmacology and clinical practice"
    - "focuses on experimentally determined information"
    - "computational predictions and text mining from the literature are not currently prioritized"
  - Goals:
    - "applications relevant to precision medicine"
    - "provide insights into the understanding of diseases, discovering of drugs and proactively improving personal health"
    - "drug repurposing"
    - "disease prediction and interpretation of transcriptomic data"
    - "predict diagnosis"
    - "predict biomedical outcomes in a biologically meaningful manner"


- **SynLethKG** –
  [Publication (2021)](https://doi.org/10.1093/bioinformatics/btab271),
  [Website](https://synlethdb.sist.shanghaitech.edu.cn),
  [Code](https://github.com/JieZheng-ShanghaiTech/KG4SL),
  [Data](https://github.com/JieZheng-ShanghaiTech/KG4SL/tree/main/data)
  - Full name: Synthetic Lethality Knowledge Graph
  - Content:
    - 54,012 nodes of 11 types
    - 2,231,921 edges of 24 types
    - Extracted from SynLethDB and various gene, drug and compound databases
    - Provided as triples in a CSV file
  - Scope:
    - "genes, compounds, diseases, biological processes and 24 kinds of relationships that could be pertinent to SL"
  - Goals:
    - "identify SL gene pairs"
    - "discovery of anti-cancer drug targets"


## Tools

- **BioCypher** –
  [Publication (2023)](https://doi.org/10.1038/s41587-023-01848-y),
  [Website](https://biocypher.org),
  [GitHub](https://github.com/biocypher/biocypher),
  [PyPI](https://pypi.org/project/biocypher/)
  - Scope:
    - "a Python library that provides a low-code access point to data processing and ontology manipulation"
    - "a modular architecture that maximizes reuse of data and code in three ways: input, ontology and output"
    - "adhere to FAIR (Findable, Accessible, Interoperable and Reusable) and TRUST (Transparency, Responsibility, User focus, Sustainability and Technology) principles"
  - Goals:
    - "make the process of creating a biomedical knowledge graph easier than ever, but still flexible and transparent"
    - "abstracting the KG build process as a combination of modular input adapters"
    - "provides easy access to state-of-the-art KGs to the average biomedical researcher"
    - "creating a more interoperable biomedical research community"


- **KGX** –
  [Website](https://kgx.readthedocs.io),
  [GitHub](https://github.com/biolink/kgx),
  [PyPI](https://pypi.org/project/kgx)
  - Scope:
    - "a Python library and set of command line utilities"
    - "The core datamodel is a Property Graph (PG), represented internally in Python using a networkx MultiDiGraph model."
  - Goals:
    - "exchanging Knowledge Graphs (KGs) that conform to or are aligned to the Biolink Model"
    - "provide validation, to ensure the KGs are conformant to the Biolink Model"


## Databases

- **Collections**
  - [Database Commons](https://ngdc.cncb.ac.cn/databasecommons)
  - [NAR db status](https://nardbstatus.kalis-amts.de)
  - [Online Bioinformatics Resources Collection (OBRC)](https://www.hsls.pitt.edu/obrc)


## Ontologies and controlled vocabularies

- **Collections**
  - [BioPortal](https://www.bioontology.org)
  - [Ontology Lookup Service](https://www.ebi.ac.uk/ols4/)


- **Biolink Model** –
  [Publication (2022)](https://doi.org/10.1111/cts.13302)
  [Website](https://biolink.github.io/biolink-model)
  [Code](https://biolink.github.io/biolink-model/)
  - Scope:
    - "a unified data model that bridges across multiple ontologies, schemas, and data models"
    - "a map for bringing together data from different sources under one unified model, and as a bridge between ontological domains"
  - Goals:
    - "supported easier integration and interoperability of biomedical KGs"
    - "supports translation, integration, and harmonization across knowledge sources"


## File formats

- **KGX (.json, .jsonl, .tsv, .ttl)** –
  [Website](https://kgx.readthedocs.io/en/latest/kgx_format.html)


- **Neo4j (.dump)** –
  [Website](https://neo4j.com/docs/desktop-manual/current/operations/create-dump/),
  [Wikipedia](https://en.wikipedia.org/w/index.php?title=Neo4j)


- **Resource Description Framework (RDF)** –
  [Website](https://www.w3.org/TR/2014/NOTE-rdf11-primer-20140624/),
  [Wikipedia](https://en.wikipedia.org/wiki/Resource_Description_Framework)

  - **Turtle (.ttl)** –
    [Website](https://www.w3.org/TR/turtle),
    [Wikipedia](https://en.wikipedia.org/wiki/Turtle_(syntax))

  - **N-Triples (.nt)** –
    [Website](https://www.w3.org/TR/n-triples),
    [Wikipedia](https://en.wikipedia.org/w/index.php?title=N-Triples)

  - **Notation3 (.n3)** –
    [Website](https://www.w3.org/TeamSubmission/n3),
    [Wikipedia](https://en.wikipedia.org/w/index.php?title=Notation3)
