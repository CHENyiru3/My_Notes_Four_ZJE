# eQTL分析及其与GWAS联合分析

eQTL(表达数量性状位点)分析是研究遗传变异如何影响基因表达的方法。将eQTL与GWAS联合分析可以帮助解释疾病相关变异的功能机制。

## eQTL分析基本步骤

1. **数据收集**
   - 基因型数据：SNP芯片或测序数据
   - 基因表达数据：RNA-seq或芯片数据
   - 样本信息：人口学特征、批次等协变量

2. **数据预处理**
   - 基因型数据：质控、缺失值填充、连锁不平衡计算
   - 表达数据：标准化、批次效应校正、离群值处理
   - 转录本定量：如使用Salmon、RSEM等工具

3. **eQTL映射**
   - 近端eQTL(cis-eQTL)：变异位点靠近目标基因(通常±1Mb)
   - 远端eQTL(trans-eQTL)：变异位点远离目标基因或在不同染色体上
   - 使用线性回归或混合模型检测SNP与基因表达的关联

4. **多重检验校正**
   - FDR控制
   - 置换测试
   - 考虑多组织、多条件分析的校正

5. **常用软件**
   - MatrixEQTL：快速eQTL分析工具
   - FastQTL：针对大数据集优化
   - QTLtools：综合工具包

## GWAS与eQTL联合分析

1. **共定位分析(Colocalization)**
   - 检测GWAS信号与eQTL信号是否共享相同的因果变异
   - 工具：coloc、HEIDI、eCAVIAR、FINEMAP

2. **转录组广泛关联研究(TWAS)**
   - 利用eQTL预测基因表达，然后与表型关联
   - 工具：PrediXcan、FUSION、S-PrediXcan

3. **Mendelian Randomization(MR)**
   - 使用eQTL作为工具变量评估基因表达与疾病的因果关系
   - 工具：MR-Base、TwoSampleMR

4. **功能注释和富集分析**
   - 整合ENCODE、Roadmap等功能组学数据
   - 使用FUMA、GARFIELD等工具进行富集分析

5. **多组织整合分析**
   - 使用GTEx等多组织eQTL数据
   - 识别组织特异性或共享的调控机制

## 实际应用案例

1. **肺功能GWAS与肺组织eQTL联合分析**
   - 识别GWAS信号共定位的基因
   - 发现潜在的致病基因和调控机制

2. **精神疾病GWAS与脑组织eQTL整合**
   - 识别特定脑区的调控变异
   - 揭示神经精神疾病的分子机制

## 分析注意事项

1. 考虑组织特异性和细胞类型特异性
2. 整合表观遗传学数据增强解释力
3. 考虑样本量和统计功效
4. 验证关键发现(如体外功能实验)

通过eQTL和GWAS的联合分析，可以将统计关联转化为生物学机制，为疾病的理解和干预提供更精确的分子靶点。


-----



Designing an eQTL Study to Identify Genetic Regulators of Brain Gene Expression in Neurodegenerative Disease

## 1. Experimental Purpose

**Scientific Question:** How do genetic variants influence gene expression in different brain regions affected by neurodegenerative disease, and do disease-associated variants act through region-specific gene regulation?

This experiment directly tests this question by correlating genome-wide genotypes with transcriptome-wide gene expression across multiple brain regions from the same individuals, comparing patterns between patients with neurodegenerative disease and neurologically normal controls.

**Purpose of Design:** While previous eQTL studies have examined brain tissue, most have focused on single brain regions or used bulk tissue. This design advances the field by analyzing multiple disease-relevant brain regions from the same individuals, enabling the detection of region-specific eQTLs and their potential role in selective vulnerability to neurodegeneration.

## 2. Model System

**Model System:** Post-mortem human brain tissue from individuals with neurodegenerative disease (Alzheimer's and Parkinson's) and neurologically normal controls, focusing on five key regions: prefrontal cortex, hippocampus, substantia nigra, cerebellum, and putamen.

**Appropriateness:** Human brain tissue is essential for this study as gene regulation is highly tissue-specific and species-specific. Brain region-specific eQTLs cannot be accurately modeled in other systems, and the disease context is critical for identifying dysregulated expression patterns.

**Alternative Models:**
- Induced pluripotent stem cell (iPSC)-derived neurons: Allow for experimental manipulation but lack brain region context and mature neural networks
- Organoids: Provide 3D tissue architecture but remain simplified models with variable reproducibility
- Animal models: Enable controlled genetic manipulation but have different regulatory landscapes than humans
- Blood eQTLs: More accessible but poorly reflect brain-specific regulation

**Ethical Considerations:** 
- Respectful handling of post-mortem tissue and informed consent from donors or next-of-kin
- Appropriate brain bank protocols and ethical approvals
- Consideration of donor wishes regarding data sharing and future research
- Responsible return of research results to scientific community and donor families

## 3. Measurement Approach

**Techniques:**
- Whole genome sequencing (30x coverage) for comprehensive genotyping
- RNA-sequencing (paired-end, 100M reads/sample) for gene expression quantification
- Single-nucleus RNA-sequencing on subset of samples for cell-type specific eQTLs
- ATAC-seq to assess chromatin accessibility in the same regions
- DNA methylation profiling using EPIC arrays

**Choice Rationale:** This multi-omic approach allows correlation between genetic variation, gene expression, and epigenetic regulation. WGS captures all potential regulatory variants, while deep RNA-seq enables detection of alternative splicing QTLs in addition to expression QTLs.

**Technical Replicates:** 
- 10% of samples processed in duplicate for RNA-seq quality control
- Technical standards included in each sequencing batch
- Randomization of disease and control samples across processing batches

**Potential Biases and Mitigation:**
- Post-mortem interval effects: Record PMI and include as covariate; exclude samples with PMI >24 hours
- RNA degradation: Measure RIN scores and exclude samples with RIN <6
- Batch effects: Implement batch correction algorithms; use technical controls
- Cell-type composition: Estimate cell-type proportions using deconvolution methods and include as covariates
- Medication effects: Record treatment history and analyze as potential confounder

## 4. Group Setting

**Experimental Groups:**
- 150 Alzheimer's disease cases
- 150 Parkinson's disease cases
- 200 neurologically normal controls
- All groups with 5 brain regions per individual (total ~2,500 samples)

**Controlled Variables:**
- Age at death (matched within 5-year ranges)
- Sex (balanced distribution)
- Post-mortem interval (<24 hours)
- Ancestry (principal components included in analysis)
- Brain pH (measured and included as covariate)
- Agonal state (recorded and included as covariate)

**Negative Controls:**
- Cerebellum as minimally affected region in Alzheimer's disease
- Prefrontal cortex as less affected region in Parkinson's disease
- Permutation-based null distributions for statistical testing

**Biological Replicates:** 
With 150-200 individuals per group across 5 brain regions, the study is powered to detect eQTLs explaining >5% of expression variance at FDR<0.05. This sample size enables identification of both common and moderately rare variant effects on gene expression.

**Modified Design Suggestion:**
Include longitudinal samples from brain banks with multiple tissue collections at different disease stages to capture dynamic changes in eQTL effects during disease progression.

## 5. Data Analysis & Presentation

**Data Processing:**
- RNA-seq alignment using STAR, quantification with Salmon
- Quality control: removal of low-quality samples (low mapping rate, high duplication)
- Normalization for library size and composition using TMM method
- Adjustment for technical covariates (RIN, batch, PMI)
- Variant calling from WGS using GATK pipeline

**Statistical Tests:**
- Linear regression models testing associations between genotypes and normalized expression values
- Adjustment for age, sex, ancestry PCs, and estimated cell-type proportions
- Multiple testing correction using Benjamini-Hochberg FDR
- Significance threshold: FDR < 0.05
- Bayesian colocalization analysis to identify shared causal variants between eQTLs and GWAS signals
- Differential eQTL analysis comparing disease vs. control

**Data Presentation:**
- Circular plots showing genome-wide distribution of significant eQTLs
- Heat maps displaying region-specificity of eQTL effects
- Box plots showing genotype-expression relationships for top eQTLs
- Network visualizations of eQTL-gene interactions in disease-relevant pathways
- Venn diagrams comparing eQTLs across brain regions

**Result Confirmation:**
- Replication in independent brain tissue datasets
- Cross-validation within dataset using leave-one-out approaches
- Validation of top eQTLs using qPCR in subset of samples
- Functional validation of selected eQTLs using CRISPR editing in neural cell models
- Integration with existing eQTL databases (GTEx, CommonMind, AMP-AD)

This design enables comprehensive mapping of the genetic architecture of gene expression in the human brain, with special emphasis on regions affected by neurodegenerative disease, potentially revealing mechanisms by which disease-associated variants exert their effects through altered gene regulation.