# Experimental Design: Genome-Wide CRISPR Screen for Drug Resistance Mechanisms

## 1. Experimental Purpose
- **Scientific Question**: Which genes, when knocked out, confer resistance to drug X in cancer cell line Y?
- **Design Rationale**: Genome-wide CRISPR-Cas9 knockout screen allows unbiased identification of genes whose loss enables cell survival under drug selection pressure
- **Follow-up Studies**: Validate top hits with individual knockouts, investigate mechanism of resistance for key genes, test combinations of drug X with inhibitors targeting resistance pathways

## 2. Model System
- **Primary System**: Human cancer cell line relevant to drug X's therapeutic application (e.g., A375 melanoma cells for BRAF inhibitor screen)
- **Rationale**: Cancer cell lines provide stable Cas9 expression, consistent growth, and clinically relevant drug responses while enabling high-throughput screening
- **Alternatives**:
  - Patient-derived xenografts (pros: better clinical relevance; cons: more variable, complex, expensive)
  - Primary patient cells (pros: direct clinical relevance; cons: limited expansion, variable Cas9 efficiency)
  - Immortalized non-cancer cells (pros: define cancer-specific vs. general mechanisms; cons: may lack disease context)
- **Ethical Considerations**: Cell line authentication, appropriate biosafety practices, responsible use of patient-derived materials if applicable

## 3. Measurement Approach
- **Techniques**:
  - Lentiviral delivery of genome-wide gRNA library
  - Next-generation sequencing of gRNA abundance
  - Drug dose-response assays for validation
  - Western blotting and RT-qPCR for mechanism studies
- **Technical Replicates**: Duplicate NGS library preparations
- **Potential Biases**:
  - Variable Cas9 editing efficiency (use cells with validated high Cas9 activity)
  - Lentiviral MOI variations (maintain >500x library coverage throughout)
  - gRNA design efficiency differences (use validated libraries with multiple guides per gene)
  - PCR amplification bias (minimize PCR cycles, use UMIs if possible)

## 4. Group Setting
- **Experimental Groups**:
  - Treatment: Cells with gRNA library exposed to drug X at IC70-IC90 concentration
  - Control 1: Cells with gRNA library without drug treatment (T0 reference)
  - Control 2: Cells with gRNA library grown in parallel without drug (time-matched control)
  - Control 3: Cells with non-targeting gRNA library with drug treatment
- **Controlled Variables**: Cell passage number, Cas9 expression level, library coverage, drug concentration, treatment duration
- **Biological Replicates**: 3-4 independent infections and selections
- **Modified Design**: Include multiple drug concentrations to identify dose-dependent resistance mechanisms, or combine with CRISPRa screen to identify both loss- and gain-of-function resistance mechanisms

## 5. Data Analysis & Presentation
- **Data Processing**: 
  - gRNA counting from raw NGS reads
  - Normalization for sequencing depth
  - Guide-level fold-change calculation (treatment vs. control)
  - Gene-level enrichment scores using algorithms like MAGeCK or BAGEL
- **Statistical Analysis**:
  - False discovery rate correction for multiple hypothesis testing
  - Robust rank aggregation for combining multiple guides per gene
  - Gene set enrichment analysis for pathway-level insights
  - Principal component analysis to assess replicate consistency
- **Data Presentation**:
  - Volcano plots showing gene enrichment/depletion significance
  - Ranked bar charts of top hits with statistical significance
  - Pathway enrichment bubble plots
  - Validation data for selected hits showing individual knockout phenotypes
  - Network visualization of functionally related hits
- **Validation Methods**:
  - Individual CRISPR knockout of top hits
  - Rescue experiments with cDNA expression
  - Dose-response curves with and without gene knockout
  - Combinatorial drug testing targeting resistance pathways
  - Protein-protein interaction studies to elucidate mechanisms