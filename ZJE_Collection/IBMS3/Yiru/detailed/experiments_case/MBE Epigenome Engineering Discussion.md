## 1. Experimental Purpose
- **Scientific Question**: Epigenome engineering explores how specific epigenetic modifications affect gene expression and cellular function without altering DNA sequence. The experimental design directly tests this by using CRISPR-dCas9 fused to epigenetic enzymes to target precise genomic locations.
- **Repeated Designs**: Researchers often repeat similar designs to test different epigenetic modifiers (DNMT3A vs TET for methylation/demethylation), target different genomic regions, or study effects across different cell types to understand context-dependent regulation.

## 2. Model System
- **Current Systems**: Commonly uses cell culture models (e.g., HEK293, iPSCs, cancer cell lines) which allow for efficient transfection of CRISPR components and controlled experimental conditions.
- **Alternatives**: Mouse models offer in vivo context but are more complex and expensive. Organoids provide 3D tissue-like environments but with increased variability. Drosophila or zebrafish can be used for developmental studies.
- **Ethical Considerations**: Cell line work has minimal ethical concerns, though patient-derived cells require proper consent. Animal models raise standard animal welfare considerations.

## 3. Measurement Approach
- **Techniques**: Combines sequencing approaches (BS-seq, ChIP-seq, RNA-seq, ATAC-seq) providing quantitative measurements of epigenetic marks, chromatin accessibility, and gene expression changes.
- **Method Selection**: These methods offer genome-wide coverage and quantitative precision compared to alternatives like immunofluorescence or PCR-based approaches.
- **Technical Replicates**: Multiple sequencing reads per genomic region serve as technical replicates, with quality filters applied to ensure reliable signal detection.
- **Potential Biases**: Off-target binding of dCas9, variable transfection efficiency, and cell-cycle effects can introduce biases, minimized through proper controls and normalization.

## 4. Group Setting
- **Experimental Groups**: Typically includes dCas9-enzyme treated samples versus controls (untreated, dCas9-only without enzyme, or catalytically dead enzyme).
- **Negative Controls**: dCas9 without effector domains, non-targeting gRNAs, and catalytically inactive enzyme fusions serve as negative controls.
- **Biological Replicates**: 3-4 biological replicates are standard, generally sufficient for statistical power in controlled cell culture experiments.
- **Modified Design**: Adding time-course measurements would reveal dynamics and persistence of epigenetic modifications; testing combinatorial modifications would explore synergistic effects.

## 5. Data Analysis & Presentation
- **Data Processing**: Raw sequencing data undergoes quality filtering, alignment to reference genome, and normalization before quantifying epigenetic changes at target sites.
- **Statistical Tests**: Differential modification analysis uses tools like DESeq2 or edgeR, with multiple testing correction (FDR) to identify significant changes.
- **Data Presentation**: Results typically appear as genome browser tracks, heatmaps of modification patterns across targets, and correlation plots between epigenetic changes and gene expression.
- **Validation Methods**: Findings are confirmed through orthogonal techniques like targeted bisulfite sequencing, ChIP-qPCR, and functional assays (luciferase reporters, phenotypic readouts) to establish causal relationships.