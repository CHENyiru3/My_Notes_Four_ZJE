## S1.W1.1. Introduction to experimental design
## S1.W1.2. Experimental design I: Elements of experimental design
- Replicates
	- **techinical replicate**: 同一测试方法多测几次
	- **biological replicate**: 多个个体/样本
	- **method replicate**: 不同实验方法重新验证同个实验目的
- Randomisation and Stratification
	- If you can (and want to), fix a variable
	- If you do not fix a variable, stratify it
	- If you can neither fix nor stratify a variable, randomise it.
## S1.W1.3. Bioethics I: Scientific integrity
- 5 principles:
	- 1.Truthfulness (Trustworthiness/Honesty)
	- 2.Diligence (You did what you claim to have done + did it properly!)
	- 3.Objectivity (No conflict of interest - Political/Economic/ Commercial/Bias)
	- 4.Circumspection (Avoid over-optimism and exaggeration, “We think” vs “we hope” the data shows x.)
	- 5.Collegiality (Equal treatment of data regardless of status of authors + all who contributed are credited).
- Hawthorne Effect: 指人们在被观察或研究时，其行为会发生改变
## S1.W2.1. Bioethics II: Animal Experimentation
- Mouse model limitations
	- Rats lack gall bladders
	- Vitamin C is vital for only a few vertebrate species (notably humans and guinea pigs).
	- Of the 19 non-inhalation carcinogens that cause cancer in humans – only 7 do so in mice or rats.
- Developmental Areas, 可以回课件看
- **The 3 R’s Principle**
- Types of animal protectionist，可以回课件看
## S1.W2.2. Experimental design II
- **Accuracy**: 测得真实、正确数据的能力, 对应Systematic error
- **Precision**: 良好的可重复性 (Reproducibility), 对应Random error
- **Sensitivity**: TP / (TP + FN)
- **Specificity**: TN / (TN + FP)
- **Power** of a hypothesis test: the probability that the test correctly rejects the null hypothesis (H0)
- **Type I error**: "false positive", 指当原假设（H0​）实际上是正确的，但我们却错误地拒绝了; 犯第一类错误的概率即为α (自己设的significance level)
- **Type II error**: "false negative", 指原假设（H0​）实际上是错误的，但我们却没有拒绝, 犯第二类错误的概率即为β, 1-β就是Power
- **Effect size**: a number measuring the strength of the relationship between two variables in a population, or a sample-based estimate of that quantity. Its significance depends of the sample size
- **Internal Standard**（内标）是一种分析化学技术，常用于定量分析。它是指在样品中加入一个已知浓度的化合物（内标物），这个化合物与目标分析物在化学性质上相似，但在样品中并不存在，也可以与目标分析物分离开来。通过比较目标分析物和内标物的峰面积或高度，并结合内标物质的已知浓度，就可以计算出被分析物的含量，这可以提高分析结果的精确性和准确性，特别是在样品的处理和测量过程中可能导致的损失和变化。
- **Significant Figures**（有效数字）是指一个数值中能表示其精确性的数字位数。有效数字包括所有已知的数字及最后一个不确定的数字。它关系到测量结果的精确性和不确定性。例如，在数值 0.00456中，有效数字为3（4、5和6），而在数值 100.0中，有效数字为4（1、0、0和小数点后的一位0）。
## S1.W3.1. Experimental design III: Experimental bias
- Bias: 所有造成Systematic error的因素
	- Survivorship Bias (e.g.)
	- Sampling/Ascertainment/Selection bias：选取样本的方式不恰当
	- Experimenter bias：实验者受自身期望、偏好等主观因素影响
	- Reporting Bias：选择性报告或不客观描述解释
	- Biased Model Systems：模型自身局限、不合理假设或数据输入偏差等
	- Publication Bias：学术期刊倾向于发表显著结果研究，导致已发表研究不能全面反映领域真实情况而产生的偏差。
- 如何设计unbiased的实验？可以参考课件例子
## S1.W5.1. Experimental design IV: Types
- Completely randomised design: 将实验对象完全随机地分配到不同处理组
- Randomised complete block design: 将实验对象按性质相同或相近分为若干区组，再将每个区组内的对象随机分配到不同处理组
- Split-plot design: 将实验单元分为主区和副区，分别安排不同处理因素
- Randomised Control Trial: 将研究对象随机分配到干预组和对照组，以评估干预措施效果
	- Placebo: 一种中立的控制干预，但可以与积极效果（安慰剂效应）相关联。
	- Nocebo: 一种负面的控制干预，受试者会经历负面影响
	- Hawthorne effect: 实验对象的行为会随着被观察而改变
	- Demand characteristics: 由受试者猜测研究目的并采取相应行动而产生的效应
	- ‘Screw-you’ effect: 实验对象的行为可能会破坏实验者的目的
- Cohort Studies
	- Retrospective (回顾性): 通过回顾过去的暴露和疾病发生情况，分析暴露因素与疾病关系
	- Prospective (前瞻性): 从现在开始追踪观察不同暴露组的研究对象，以确定疾病发生情况及与暴露因素关系
- Cross-Over design: 让研究对象在不同时期先后接受不同处理，以比较不同处理效果
- Cross-sectional: 在某一特定时间点对研究对象的特征和疾病状况进行调查
- Longitudinal: 对同一组研究对象在较长时间内进行跟踪，观察其变化
- Meta-analyses: 综合多个同类研究结果，进行定量分析以得出更具普遍性结论
- Multi-batch analyses: 对多个批次的数据进行分析，以考虑批次效应并获得更可靠结果
## S1.W7.1. Experimental design V: interpolation/extrapolation and mixed effects models
- Interpolation: Constructing new data points within the range of known data
- Extrapolation: Applying your model to calculate values outside of the range of observed data sample
- Mixed effects models: 统计模型，同时包含固定效应和随机效应，用于分析具有层次结构或聚类结构的数据，能在考虑个体差异等随机因素的同时，研究固定因素对响应变量的影响
- Random effects model: 将个体或群体的效应视为随机变量，强调从总体中抽取的样本所具有的随机性，更适合于研究个体或群体间的差异及变化，以及总体特征。
- Nested design: 一种实验设计方法，指的是一个因子（如细胞）被包含或嵌套在另一个因子（如胰腺）中，且不同组的嵌套对象彼此独立，不能跨组比较。主要作用：用来区分不同来源的变异，比如区分基因型的差异、胰腺之间的差异、以及细胞之间的差异。
## S1.W8.1. Models of genetically modified mice / animals

## S1.W8.2. Sex differences in disease susceptibility and drug response 

## S1.W8.3. Recap of statistical models and dealing with interactions

## S1.W9.1. Ensuring reproducible research, reporting and sharing code, protocols and data

## S1.W10.1. Introduction to experimental design framework

## S1.W10.2. <font color="#de7802">Seminar.</font> 

## S1.W11.1. Working with discrete data - contingency tables, χ2-test - Fisher's exact test

## S1.W11.2. <font color="#de7802">Seminar.</font> 

## S1.W12.1. <font color="#de7802">Seminar.</font> 

## S1.W13.1. Working with discrete and bounded data - logistic and binomial regression

## S1.W13.2. <font color="#de7802">Seminar.</font> 

## S1.W14.1. Introduction to machine learning 1(classification, clustering, dimensionality reduction)

## S1.W14.2. Introduction to machine learning 2(supervised learning, cross validation, evaluating classification performance)

## S1.W14.3. <font color="#de7802">Seminar.</font> 

## S2.W1.1. <font color="#de7802">Seminar.</font> Deep learning for genomics modeling and interpretation
### 1. **Translatorner: A Transformer-based Model for mRNA Translation**
#### Experimental Purpose:
- **Scientific Question**: The study aims to understand the regulation of mRNA translation and its impact on protein abundance, which is crucial for understanding disease mechanisms. The central dogma of biology (DNA → RNA → Protein) is well-known, but the correlation between mRNA and protein levels is not perfect (0.39 to 0.79). The study seeks to model how mRNA translation is regulated and how this regulation affects protein levels.
- **Experimental Design**: The study uses a Transformer-based deep learning model (Translatorner) to predict ribosome profiling (translatome) from RNA-seq data and gene sequences. The model is trained on human data and tested on both human and mouse datasets to evaluate its ability to generalize across species.
#### Model System:
- **Model System**: The study uses human and mouse genomic data. These systems are appropriate because they are well-studied, and the conservation of regulatory mechanisms between humans and mice allows for cross-species validation.
- **Alternative Model Systems**: Other model systems like yeast or zebrafish could be used, but they may lack the complexity and relevance to human diseases. However, they are cheaper and easier to manipulate.
- **Ethical Considerations**: Using human genomic data requires ethical approval, especially when dealing with patient data. The study likely adheres to ethical guidelines for genomic research.
#### Measurement Approach:
- **Techniques**: The study uses ribosome profiling (Ribo-seq) and RNA-seq data. These are quantitative techniques that measure translation efficiency and mRNA abundance, respectively.
- **Method Choice**: Deep learning models (Transformers) were chosen because they can capture long-range dependencies in sequences, which is crucial for understanding translation regulation.
- **Technical Replicates**: The study likely uses multiple replicates to ensure robustness, though the exact number is not specified.
- **Potential Biases**: Biases could arise from data normalization or sequencing depth. These are minimized by using standardized protocols and cross-validation.
#### Group Setting:
- **Experimental Groups**: The model is trained on human data and tested on both human and mouse data. The groups are defined by cell types (e.g., epithelial cells, brain cells).
- **Negative Controls**: The study compares Translatorner with state-of-the-art models (e.g., Riboformer) to ensure that the improvements are not due to overfitting.
- **Biological Replicates**: The study uses multiple datasets (e.g., K562, epithelial cells) to ensure generalizability.
- **Modified Group Design**: A dose-response experiment could be added to study how varying levels of mRNA affect translation efficiency.
#### Data Analysis & Presentation:
- **Data Processing**: Raw data from Ribo-seq and RNA-seq are processed using deep learning models. The data are quantitative, and the model outputs are compared with experimental data.
- **Statistical Tests**: The study uses Pearson correlation coefficients (PCC) to compare predicted and observed ribosome profiling data.
- **Data Presentation**: Results are presented using scatter plots and enrichment plots, which are clear and free of misleading scaling.
- **Confirmation**: The model's predictions are validated using cross-species data and in silico mutagenesis, which confirms the robustness of the results.
### 2. **TransRBP: Modeling RBP Binding and Its Interaction with m6A**
#### Experimental Purpose:
- **Scientific Question**: The study aims to understand how RNA-binding proteins (RBPs) interact with m6A modifications and how these interactions affect RNA metabolism and disease.
- **Experimental Design**: The study develops a deep learning model (TransRBP) to predict RBP binding sites and their interaction with m6A. The model is trained on RNA sequences and tested for its ability to identify disease-related variants that alter RBP binding.
#### Model System:
- **Model System**: The study uses human genomic data, focusing on RBPs and m6A modifications. This system is appropriate because m6A is the most prevalent mRNA modification and plays a critical role in RNA metabolism.
- **Alternative Model Systems**: Other systems like yeast or bacteria could be used, but they lack the complexity of m6A regulation seen in higher eukaryotes.
- **Ethical Considerations**: Similar to Translatorner, the use of human genomic data requires ethical approval.
#### Measurement Approach:
- **Techniques**: The study uses RNA-seq data and m6A sequencing data. These are quantitative techniques that measure RNA abundance and m6A modifications.
- **Method Choice**: Deep learning models (Transformers) were chosen because they can capture complex interactions between RNA sequences and RBPs.
- **Technical Replicates**: The study likely uses multiple replicates, though the exact number is not specified.
- **Potential Biases**: Biases could arise from sequencing errors or incomplete annotation of m6A sites. These are minimized by using high-quality datasets and cross-validation.
#### Group Setting:
- **Experimental Groups**: The model is trained on RNA sequences and tested for its ability to predict RBP binding sites. The groups are defined by disease types (e.g., Parkinson’s disease, autism).
- **Negative Controls**: The study compares TransRBP with existing models to ensure that the improvements are not due to overfitting.
- **Biological Replicates**: The study uses multiple datasets to ensure generalizability.
- **Modified Group Design**: A dose-response experiment could be added to study how varying levels of m6A affect RBP binding.
#### Data Analysis & Presentation:
- **Data Processing**: Raw data from RNA-seq and m6A sequencing are processed using deep learning models. The data are quantitative, and the model outputs are compared with experimental data.
- **Statistical Tests**: The study uses Pearson correlation coefficients (PCC) to compare predicted and observed RBP binding data.
- **Data Presentation**: Results are presented using scatter plots and enrichment plots, which are clear and free of misleading scaling.
- **Confirmation**: The model's predictions are validated using in silico mutagenesis and experimental data, which confirms the robustness of the results.
### General Observations:
- Both studies leverage deep learning models (Transformers) to address complex questions in genomics. The models are trained on large datasets and validated using cross-species data and in silico experiments.
- The studies highlight the importance of model interpretability, using techniques like in silico mutagenesis and gradient-based interpretation to understand the contribution of different input modalities.
- The results have significant implications for understanding disease mechanisms, particularly in the context of translation regulation and RBP interactions with m6A modifications  
---
## S2.W2.1. Molecular interactions from structure perspective 
---
## S2.W2.2. <font color="#de7802">Seminar.</font> Empowering precision medicine with computational biology
### 1. **SpTransformer: Tissue-Specific Splicing Prediction**
#### Experimental Purpose:
- **Scientific Question**: The study aims to predict tissue-specific splicing alterations caused by single nucleotide variants (SNVs) and understand their role in human diseases.
- **Experimental Design**: SpTransformer, a Transformer-based deep learning model, is developed to predict splicing alterations in 15 different tissues. The model is trained on RNA-seq data and validated using clinical samples.
#### Model System:
- **Model System**: Human genomic data are used, as they are directly relevant to human diseases and precision medicine.
- **Alternative Model Systems**: Model organisms like mice could be used, but they may not fully capture the complexity of human splicing regulation.
- **Ethical Considerations**: Using human genomic data requires ethical approval, especially when dealing with patient data.
#### Measurement Approach:
- **Techniques**: RNA-seq data are used to measure splicing alterations. The data are quantitative, allowing for precise predictions.
- **Method Choice**: Transformers were chosen because they can capture long-range dependencies in sequences, which is crucial for understanding splicing regulation.
- **Technical Replicates**: The study likely uses multiple replicates to ensure robustness, though the exact number is not specified.
- **Potential Biases**: Biases could arise from sequencing errors or incomplete annotation of splicing events. These are minimized by using high-quality datasets and cross-validation.
#### Group Setting:
- **Experimental Groups**: The study compares splicing alterations in different tissues to understand tissue-specific effects.
- **Negative Controls**: Non-splicing variants are used as negative controls to ensure that the model can distinguish between splicing and non-splicing events.
- **Biological Replicates**: Multiple datasets are used to ensure generalizability.
- **Modified Group Design**: A dose-response experiment could be added to study how varying levels of splicing alterations affect tissue function.
#### Data Analysis & Presentation:
- **Data Processing**: Raw RNA-seq data are processed using SpTransformer to predict splicing alterations. The data are quantitative, and the model outputs are compared with experimental data.
- **Statistical Tests**: The study uses z-scores to define tissue-specific splicing alterations and enrichment analysis to identify disease-related genes.
- **Data Presentation**: Results are presented using scatter plots and enrichment plots, which are clear and free of misleading scaling.
- **Confirmation**: The model's predictions are validated using clinical samples and RNA-seq data, confirming the robustness of the results.
### General Observations:
- The studies leverage computational biology and deep learning to address complex questions in genomics, particularly in the context of cancer, genetic variants, and splicing regulation.
- The models are trained on large datasets and validated using cross-species data and experimental data, highlighting their robustness and generalizability.
- The results have significant implications for precision medicine, particularly in the context of cancer diagnosis, genetic variant interpretation, and understanding tissue-specific splicing alterations.
---
## S2.W2.3. Big data analysis - dimensionality reduction
---
## S2.W3.1. Large molecule de-novo design, using antibody as an example
---
## S2.W3.2. <font color="#de7802">Seminar.</font> Structural study of epigenetic regulation in transcription
### 1. **Experimental Purpose:**
- **Scientific Question**: The study aims to understand how **histone modifications** (e.g., acetylation, methylation) and **chromatin structure** regulate transcription. Specifically, it investigates the structural mechanisms by which histone modifications influence the binding of transcription machinery and the regulation of gene expression.
- **Experimental Design**: The study uses **structural biology techniques** (e.g., cryo-EM, X-ray crystallography) to determine the molecular structures of key epigenetic regulators, such as **histone acetyltransferases (HATs)** and **histone deacetylases (HDACs)**, and their interactions with nucleosomes and transcription factors.
### 2. **Model System:**
- **Model System**: The study primarily uses **yeast** and **human cells**, as these systems are well-characterized and provide a direct link to eukaryotic transcription regulation. The study focuses on the **SAGA complex**, a well-known HAT complex involved in transcription regulation.
- **Why This System?**: Yeast and human cells are appropriate for this study because they allow for the manipulation of specific histone modifications and chromatin structures. The SAGA complex is relevant because it plays a key role in regulating transcription through histone acetylation.
- **Alternative Model Systems**: Other model systems like **bacteria** or **plants** could be used, but they lack the complexity of eukaryotic chromatin and histone modifications.
- **Ethical Considerations**: Using human cell lines requires ethical approval, especially when dealing with patient-derived samples. The study likely adheres to ethical guidelines for genomic research.
### 3. **Measurement Approach:**
- **Techniques**: The study employs several techniques:
    - **Cryo-electron microscopy (cryo-EM)**: To determine the structures of epigenetic regulators (e.g., SAGA complex) and their interactions with nucleosomes.
    - **X-ray crystallography**: To obtain high-resolution structures of specific histone modifications and their interactions with transcription factors.
    - **Biochemical assays**: To study the functional roles of histone modifications in transcription regulation.
    - **Chromatin immunoprecipitation (ChIP)**: To study the binding of transcription factors to histone-modified chromatin.
- **Why These Methods?**: Cryo-EM and X-ray crystallography were chosen because they allow for the visualization of molecular structures at atomic resolution, which is crucial for understanding the mechanisms of epigenetic regulation. Biochemical assays and ChIP were used to study the functional roles of histone modifications in transcription.
- **Technical Replicates**: The study likely uses multiple replicates (e.g., n=3 or more) to ensure the robustness of the structural data.
- **Potential Biases**: Biases could arise from sample preparation or data interpretation. These are minimized by using standardized protocols and cross-validation with biochemical assays.
### 4. **Group Setting:**
- **Experimental Groups**: The study compares several groups:
    - **Wild-type cells** vs. **cells with specific histone modifications**: To study the effects of histone modifications on transcription.
    - **Cells with intact SAGA complex** vs. **cells with SAGA complex mutations**: To study the role of the SAGA complex in transcription regulation.
    - **Cells treated with HDAC inhibitors** vs. **untreated cells**: To study the effects of histone deacetylation on transcription.
- **Negative Controls**: Cells without specific histone modifications or with intact SAGA complex serve as negative controls to study the effects of histone modifications and SAGA complex mutations.
- **Biological Replicates**: Multiple samples are used in each group (e.g., n=3 or more) to ensure reproducibility.
- **Modified Group Design**: A dose-response experiment could be added to study how varying levels of histone modifications or HDAC inhibitors affect transcription.
### 5. **Data Analysis & Presentation:**
- **Data Processing**: Raw structural data from cryo-EM and X-ray crystallography are processed to generate 3D models of the molecular structures. Biochemical and ChIP data are analyzed to study the functional roles of histone modifications in transcription.
- **Statistical Tests**: The study uses statistical validation methods (e.g., cross-validation, resolution assessment) to ensure the accuracy of the structural models. Differential binding analysis is performed to identify key transcription factors regulated by histone modifications.
- **Data Presentation**: Results are presented using **3D structural models**, **graphs**, and **tables**, which are clear and free of misleading scaling. For example, the study uses **electron density maps** to show the structures of histone modifications and **bar graphs** to compare transcription factor binding.
- **Confirmation**: The structural findings are confirmed using **biochemical assays** and **functional studies**, which validate the proposed mechanisms of epigenetic regulation.
### General Observations:
- The study provides a detailed understanding of how **histone modifications** and **chromatin structure** regulate transcription through the **SAGA complex** and other epigenetic regulators.
- The findings highlight the importance of **histone acetylation** and **deacetylation** in regulating gene expression and suggest potential therapeutic targets for diseases linked to epigenetic dysregulation.
- The results have significant implications for understanding the molecular basis of **epigenetic regulation** and developing therapies for **cancer** and other diseases.
---
## S2.W4.1. Single-cell spatial-temporal multi-omics
---
## S2.W4.2. Survival analysis
---
## S2.W4.3. <font color="#de7802">Seminar.</font> Host-microbial Interactions and Lipid Metabolism
### 1. **Experimental Purpose:**
- **Scientific Question**: The study aims to understand how the gut microbiota regulates host lipid metabolism and how dysbiosis (imbalance in the microbiota) contributes to metabolic disorders such as obesity and diabetes. Specifically, the study investigates the role of **Nfil3**, **Hdac3**, and **Snhg9** in mediating the effects of the microbiota on lipid metabolism.
- **Experimental Design**: The study uses **germ-free (GF) mice** and **conventional (CV) mice** to identify key genes regulated by the microbiota. The researchers then use **gene knockout models** and **bacterial gavage** to study the functional roles of these genes and specific bacterial strains in lipid metabolism.
### 2. **Model System:**
- **Model System**: The study primarily uses **germ-free (GF) mice** and **conventional (CV) mice**. These models are ideal for studying the effects of the microbiota on host metabolism because GF mice lack a gut microbiota, allowing researchers to isolate the effects of specific bacterial strains.
- **Why This System?**: Mice are appropriate for this study because their gut microbiota and lipid metabolism are well-characterized, and they allow for precise genetic manipulation. The use of GF mice is particularly relevant because it enables researchers to study the effects of specific bacterial strains on host metabolism.
- **Alternative Model Systems**: Other model systems like **zebrafish** or **Drosophila** could be used, but they lack the complexity of mammalian lipid metabolism and gut microbiota interactions.
- **Ethical Considerations**: Using mice requires ethical approval, especially when dealing with germ-free conditions and dietary interventions. The study likely adheres to ethical guidelines for animal research.
### 3. **Measurement Approach:**
- **Techniques**: The study employs several techniques:
    - **RNA sequencing (RNA-seq)**: To identify genes regulated by the microbiota.
    - **Biochemical assays**: To measure lipid levels and metabolic activity.
    - **Gene knockout models**: To study the functional roles of **Nfil3**, **Hdac3**, and **Snhg9** in lipid metabolism.
    - **Bacterial gavage**: To introduce specific bacterial strains (e.g., **Lactobacillus plantarum Pm001**) into GF mice and study their effects on lipid metabolism.
- **Why These Methods?**: RNA-seq was chosen to identify genes regulated by the microbiota, while biochemical assays were used to measure lipid levels and metabolic activity. Gene knockout models and bacterial gavage were used to study the functional roles of specific genes and bacterial strains.
- **Technical Replicates**: The study likely uses multiple replicates (e.g., n=3 or more) to ensure the robustness of the data.
- **Potential Biases**: Biases could arise from differences in mouse strains or dietary conditions. These are minimized by using standardized protocols and controls.
### 4. **Group Setting:**
- **Experimental Groups**: The study compares several groups:
    - **Germ-free (GF) mice** vs. **conventional (CV) mice**: To study the effects of the microbiota on lipid metabolism.
    - **Gene knockout mice** (e.g., **Nfil3ΔIEC**, **Hdac3ΔIEC**) vs. **wild-type mice**: To study the functional roles of specific genes in lipid metabolism.
    - **Mice treated with specific bacterial strains** (e.g., **Lactobacillus plantarum Pm001**) vs. **control mice**: To study the effects of specific bacterial strains on lipid metabolism.
- **Negative Controls**: GF mice and wild-type mice serve as negative controls to study the effects of the microbiota and gene knockouts on lipid metabolism.
- **Biological Replicates**: Multiple mice are used in each group (e.g., n=8) to ensure reproducibility.
- **Modified Group Design**: A dose-response experiment could be added to study how varying levels of specific bacterial strains or gene expression affect lipid metabolism.
### 5. **Data Analysis & Presentation:**
- **Data Processing**: Raw RNA-seq data are processed to identify differentially expressed genes. Biochemical data are analyzed to measure lipid levels and metabolic activity.
- **Statistical Tests**: The study uses statistical methods (e.g., t-tests, ANOVA) to compare gene expression and lipid levels between groups. Differential expression analysis is performed to identify key genes regulated by the microbiota.
- **Data Presentation**: Results are presented using **graphs** and **tables**, which are clear and free of misleading scaling. For example, the study uses **bar graphs** to compare lipid levels and **scatter plots** to show gene expression changes.
- **Confirmation**: The findings are confirmed using **gene knockout models** and **bacterial gavage**, which validate the role of specific genes and bacterial strains in regulating lipid metabolism.
### General Observations:
- The study provides a detailed understanding of how the gut microbiota regulates host lipid metabolism through specific genes (**Nfil3**, **Hdac3**, and **Snhg9**).
- The findings highlight the importance of **Lactobacillus plantarum Pm001** in promoting **Snhg9** expression and protecting mice from diet-induced obesity.
- The results have significant implications for understanding the molecular basis of **microbiota-host interactions** and developing **microbiota-based therapies** for metabolic disorders.
---
## S2.W5.1. Binary trees and Random Forest
---
## S2.W5.2. <font color="#de7802">Seminar.</font> How to Do a Scientific Project Step-by-step
### 1. **Experimental Purpose:**
- **Scientific Question**: The study aims to understand how **IL-33**, a cytokine produced by **PDGFRβ+DPP4+ cells**, regulates cold-induced thermogenesis and the formation of beige adipocytes in white adipose tissue (WAT). Specifically, the study investigates whether IL-33 expression is induced by cold exposure and how it contributes to thermogenic remodeling.
- **Experimental Design**: The study uses a combination of **RNA sequencing (RNA-seq)**, **flow cytometry**, **histology**, and **CRISPR/Cas9 gene editing** to explore the role of IL-33 in cold-induced thermogenesis. The researchers first identify IL-33 as a key player in the process and then investigate the molecular mechanisms underlying its regulation.
### 2. **Model System:**
- **Model System**: The study primarily uses **mouse models**, particularly **PDGFRβ+DPP4+ cells** in inguinal white adipose tissue (iWAT). These cells are identified as the main source of IL-33 in iWAT. The study also uses **germ-free (GF)** and **conventional (CV)** mice to study the effects of cold exposure on adipose tissue.
- **Why This System?**: Mice are appropriate for this study because they allow for the manipulation of specific cell populations and genes, and their adipose tissue responds to cold exposure in a manner similar to humans. The use of PDGFRβ+DPP4+ cells is relevant because these cells are known to play a role in adipose tissue remodeling.
- **Alternative Model Systems**: Other model systems, such as **cell cultures** or **zebrafish**, could be used, but they lack the complexity of in vivo adipose tissue remodeling and the interaction between different cell types.
- **Ethical Considerations**: Using mice requires ethical approval, especially when dealing with cold exposure and gene editing. The study likely adheres to ethical guidelines for animal research.
### 3. **Measurement Approach:**
- **Techniques**: The study employs several techniques:
    - **RNA-seq**: To analyze gene expression changes in response to cold exposure.
    - **Flow cytometry**: To study immune cell populations (e.g., ILC2s) in adipose tissue.
    - **Histology**: To visualize beige adipocyte formation in adipose tissue.
    - **CRISPR/Cas9**: To knock out **CREB**, a transcription factor that regulates IL-33 expression.
    - **Chromatin Immunoprecipitation (ChIP)**: To study the binding of CREB to the IL-33 promoter.
- **Why These Methods?**: RNA-seq was chosen to identify genes regulated by cold exposure, while flow cytometry and histology were used to study the cellular and tissue-level effects of IL-33. CRISPR/Cas9 and ChIP assays were used to investigate the molecular mechanisms of IL-33 regulation.
- **Technical Replicates**: The study likely uses multiple replicates (e.g., n=4 or more) to ensure the robustness of the data.
- **Potential Biases**: Biases could arise from differences in mouse strains or environmental conditions. These are minimized by using standardized protocols and controls.
### 4. **Group Setting:**
- **Experimental Groups**: The study compares several groups:
    - **Cold-exposed mice (6°C)** vs. **room temperature mice (22°C)**: To study the effects of cold exposure on IL-33 expression and thermogenic remodeling.
    - **PDGFRβ+DPP4+ cells** vs. **PDGFRβ+DPP4- cells**: To identify the source of IL-33 in iWAT.
    - **CREB knockout mice** vs. **wild-type mice**: To study the role of CREB in regulating IL-33 expression.
- **Negative Controls**: Mice kept at room temperature and wild-type mice serve as negative controls to study the effects of cold exposure and CREB knockout.
- **Biological Replicates**: Multiple mice are used in each group (e.g., n=8) to ensure reproducibility.
- **Modified Group Design**: A dose-response experiment could be added to study how varying levels of cold exposure or IL-33 expression affect thermogenic remodeling.
### 5. **Data Analysis & Presentation:**
- **Data Processing**: Raw RNA-seq data are processed to identify differentially expressed genes. Flow cytometry and histology data are analyzed to study cell populations and tissue remodeling. ChIP assay data are analyzed to study the binding of CREB to the IL-33 promoter.
- **Statistical Tests**: The study uses statistical methods (e.g., t-tests, ANOVA) to compare gene expression, cell populations, and transcription factor binding between groups. Differential expression analysis is performed to identify key genes regulated by cold exposure and IL-33.
- **Data Presentation**: Results are presented using **graphs**, **tables**, and **histological images**, which are clear and free of misleading scaling. For example, the study uses **volcano plots** to show differentially expressed genes and **bar graphs** to compare IL-33 expression levels.
- **Confirmation**: The findings are confirmed using **gene knockout models** (e.g., CREB knockout) and **functional assays** (e.g., ChIP assays), which validate the role of IL-33 and CREB in cold-induced thermogenesis.
### General Observations:
- The study provides a detailed understanding of how **IL-33**, produced by **PDGFRβ+DPP4+ cells**, regulates cold-induced thermogenesis and beige adipocyte formation.
- The findings highlight the importance of **CREB** as a transcription factor that drives IL-33 expression in response to cold exposure.
- The results have significant implications for understanding the molecular basis of **cold-induced thermogenesis** and developing therapies for **obesity** and **metabolic disorders**.