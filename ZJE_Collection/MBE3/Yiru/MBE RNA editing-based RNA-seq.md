## 1. Experimental Purpose
- **Scientific Question**: What are the direct RNA targets and precise binding sites of RNA-binding protein X in living cells?
- **Design Rationale**: Fusion of RNA-binding protein (RBP) to an RNA editing enzyme (APOBEC) creates a chimeric protein that marks RNA binding sites with C-to-U conversions, detectable by RNA-seq without crosslinking artifacts
- **Follow-up Studies**: Motif analysis of binding sites, functional validation of key targets, structural studies of RBP-RNA interactions, comparison with other RBP mapping techniques (CLIP-seq)

## 2. Model System
- **Primary System**: Human cell line relevant to RBP function (e.g., neuronal cells for neuron-specific RBPs, cancer cells for cancer-relevant RBPs)
- **Rationale**: Cell lines provide controlled expression of the RBP-APOBEC fusion, high RNA yield, and consistent experimental conditions
- **Alternatives**:
  - Primary cells (pros: physiological relevance; cons: transfection challenges, variability)
  - Mouse models with inducible RBP-APOBEC (pros: in vivo context; cons: complex, expensive)
  - In vitro transcribed RNAs (pros: defined sequences; cons: lacks cellular context)
- **Ethical Considerations**: Cell line authentication, appropriate biosafety practices, responsible use of genetic modification tools

## 3. Measurement Approach
- **Techniques**:
  - Doxycycline-inducible expression of RBP-APOBEC fusion
  - RNA extraction with DNase treatment
  - Strand-specific RNA-seq with high depth
  - C-to-U editing site identification
- **Technical Replicates**: Duplicate RNA-seq libraries
- **Potential Biases**:
  - Expression level variations of RBP-APOBEC (use inducible system with titrated expression)
  - Off-target editing (include catalytically inactive APOBEC control)
  - RNA degradation artifacts (optimize RNA extraction protocol)
  - Sequence context preferences of APOBEC (account for in computational analysis)

## 4. Group Setting
- **Experimental Groups**:
  - Test: Cells expressing RBP-APOBEC fusion
  - Control 1: Cells expressing catalytically inactive APOBEC fusion (deaminase mutant)
  - Control 2: Cells expressing APOBEC only (no RBP)
  - Control 3: Cells expressing GFP-APOBEC (non-specific RNA binding)
  - Control 4: Uninduced cells (baseline editing)
- **Controlled Variables**: Induction time, expression level, RNA quality, sequencing depth
- **Biological Replicates**: 3-4 independent inductions and RNA preparations
- **Modified Design**: Include time-course of induction to capture kinetics of editing, or RBP mutants with altered RNA-binding specificity

## 5. Data Analysis & Presentation
- **Data Processing**: 
  - Read alignment to reference genome
  - C-to-U conversion identification
  - Background filtering using controls
  - Peak calling to identify significant binding sites
  - Motif discovery in binding regions
- **Statistical Analysis**:
  - Statistical significance of editing sites above background
  - Enrichment analysis for RNA types and cellular compartments
  - Correlation with RBP expression levels
  - Comparison with known binding motifs or CLIP-seq data
- **Data Presentation**:
  - Genome browser tracks showing editing sites
  - Metagene plots of binding distribution across transcript regions
  - Motif logos for identified binding sequences
  - Venn diagrams comparing targets with other datasets
  - Functional enrichment maps of target RNAs
- **Validation Methods**:
  - RT-qPCR validation of editing at selected sites
  - CLIP-seq or RIP-seq for orthogonal validation
  - Functional assays for key targets (e.g., minigene reporters)
  - Mutagenesis of binding sites to confirm direct interaction
  - RNA structure probing to assess structural context of binding