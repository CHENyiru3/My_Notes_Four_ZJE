## 1. Experimental Purpose
- **Scientific Question**: Which human genes are essential for virus X infection and replication?
- **Design Rationale**: Genome-wide CRISPR screen enables identification of host dependency factors required for viral entry, replication, assembly, or release
- **Follow-up Studies**: Investigate mechanism of top hits, develop small molecule inhibitors targeting key host factors, test for broad-spectrum activity against related viruses

## 2. Model System
- **Primary System**: Human cell line susceptible to virus X infection (e.g., Huh7 cells for hepatitis C virus)
- **Rationale**: Permissive cell lines that support complete viral lifecycle while maintaining high Cas9 editing efficiency provide ideal platform for identifying host factors
- **Alternatives**:
  - Primary human cells (pros: physiological relevance; cons: difficult to scale, variable editing)
  - Immortalized cells from target organs (pros: tissue-specific factors; cons: may have altered cellular pathways)
  - Reporter virus systems (pros: biosafety, high-throughput; cons: may miss late-stage factors)
- **Ethical Considerations**: Biosafety protocols for viral work, cell line authentication, appropriate containment levels

## 3. Measurement Approach
- **Techniques**:
  - Lentiviral delivery of genome-wide sgRNA library to Cas9-expressing cells
  - Viral challenge with optimized MOI
  - Cell survival/death assay or FACS-based sorting of infected vs. uninfected cells
  - Next-generation sequencing of sgRNA abundance pre/post-selection
- **Technical Replicates**: Duplicate NGS library preparations, multiple infection timepoints
- **Potential Biases**:
  - Viral stock variations (standardize preparation, titration)
  - Infection efficiency differences (optimize viral MOI)
  - Cell death from Cas9 toxicity (include essential gene controls)
  - Off-target effects (use libraries with minimal predicted off-targets)

## 4. Group Setting
- **Experimental Groups**:
  - Test: sgRNA library-transduced cells infected with virus X
  - Control 1: Uninfected sgRNA library cells (baseline sgRNA distribution)
  - Control 2: Non-targeting sgRNA library with viral infection
  - Control 3: Time-matched uninfected cells for growth-related effects
- **Controlled Variables**: Cell density, viral dose, infection duration, sgRNA library coverage
- **Biological Replicates**: 3-4 independent library transductions and viral challenges
- **Modified Design**: Include CRISPR screens with multiple viral strains to identify strain-specific vs. conserved host factors

## 5. Data Analysis & Presentation
- **Data Processing**: 
  - sgRNA read counting from sequencing data
  - Normalization to library depth
  - Enrichment/depletion calculation relative to uninfected controls
  - Gene-level significance using MAGeCK or similar algorithms
- **Statistical Analysis**:
  - False discovery rate control for multiple testing
  - Comparison with published essential gene datasets
  - Pathway and network analysis of hits
  - Comparison with known viral interactors from proteomics data
- **Data Presentation**:
  - Manhattan plots of gene significance across the genome
  - Cellular pathway maps highlighting hit clusters
  - Validation data for top hits showing infection rates with individual knockouts
  - Comparison with previous genetic screens or interactome studies
- **Validation Methods**:
  - Individual gene knockout confirmation
  - Viral replication assays with knockout cell lines
  - Rescue experiments with cDNA expression
  - Protein-protein interaction studies with viral components
  - Small molecule inhibition of identified pathways