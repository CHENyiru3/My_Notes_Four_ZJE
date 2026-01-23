# Experimental Workflow: IL-33 Regulation of Cold-Induced Thermogenesis

## I. Animal Model Preparation and Cold Exposure Protocol

1. **Mouse Strain Selection and Housing**
   - Select C57BL/6J mice (8-12 weeks old, both sexes or sex-matched)
   - House in standard conditions (22°C, 12h light/dark cycle)
   - For germ-free experiments, maintain mice in sterile isolators
   - Acclimate mice to housing conditions for at least 1 week

2. **Cold Exposure Protocol**
   - Divide mice into experimental groups:
     * Room temperature controls (22°C)
     * Acute cold exposure (6°C for 24-48h)
     * Chronic cold exposure (6°C for 7-14 days)
   - Transfer mice to pre-cooled cages with adequate bedding
   - Monitor body temperature using rectal probe thermometer
   - Record food intake and body weight daily

3. **Genetic Model Generation**
   - Generate cell-specific knockout models:
     * PDGFRβ-specific Cre mice crossed with IL-33flox/flox
     * CREB conditional knockout mice
   - Validate knockout efficiency by qPCR and Western blot
   - Generate reporter mice (e.g., IL-33-GFP) for cell tracking. This means that cells actively transcribing the IL-33 gene will also produce GFP, making them fluorescent and detectable by flow cytometry or fluorescence microscopy.

## II. Adipose Tissue Analysis and Cell Isolation

1. **Tissue Collection and Processing**
   - Euthanize mice according to ethical guidelines
   - Collect inguinal white adipose tissue (iWAT), epididymal WAT, and brown adipose tissue (BAT)
   - Weigh tissues and divide for:
     * Snap freezing in liquid nitrogen (gene/protein analysis)
     * Fixation in 4% paraformaldehyde (histology)
     * Fresh processing (cell isolation)

2. **Histological Analysis**
   - Process fixed tissues for paraffin embedding or OCT-compound frozen sections
   - Section tissues at 5-8μm thickness
   - Perform H&E staining for morphological analysis
   - Conduct UCP1 immunohistochemistry to identify beige adipocytes
   - Image using light microscopy and quantify beige adipocyte areas

3. **Adipose Tissue Fractionation**
   - Mince fresh adipose tissue and digest with collagenase
   - Centrifuge to separate floating adipocytes from stromal vascular fraction (SVF)
   - Filter SVF through 70μm strainer
   - Lyse red blood cells if necessary
   - Count cells using hemocytometer or automated cell counter

4. **PDGFRβ+DPP4+ Cell Isolation**
   - Stain SVF with fluorescent antibodies:
     * Anti-PDGFRβ (CD140b)
     * Anti-DPP4 (CD26)
     * Lineage markers (CD31, CD45) for exclusion
   - Perform fluorescence-activated cell sorting (FACS)
   - Collect PDGFRβ+DPP4+ and PDGFRβ+DPP4- populations
   - Verify purity by flow cytometry analysis of a sample aliquot

## III. Molecular and Cellular Analysis

1. **RNA Sequencing and Transcriptome Analysis**
   - Extract total RNA from:
     * Whole adipose tissue samples
     * Sorted PDGFRβ+DPP4+ cells
     * Other relevant cell populations
   - Assess RNA quality (Bioanalyzer, RNA integrity number >8)
   - Prepare RNA-seq libraries (poly-A selection or ribo-depletion)
   - Perform paired-end sequencing (Illumina platform)
   - Analyze data using standard bioinformatics pipeline:
     * Quality control and read alignment
     * Differential expression analysis
     * Pathway enrichment analysis
     * Visualization (heatmaps, volcano plots)

2. **Gene Expression Analysis**
   - Design primers for key genes (IL-33, UCP1, PGC1α, CREB, etc.)
   - Perform RT-qPCR on tissue and cell samples
   - Normalize to housekeeping genes (β-actin, GAPDH)
   - Calculate relative expression using 2^-ΔΔCt method
   - Validate RNA-seq findings for selected genes

3. **Protein Expression Analysis**
   - Extract proteins from tissues and cells
   - Quantify protein concentration (BCA assay)
   - Perform Western blotting for:
     * IL-33 and its receptor ST2
     * UCP1 and other thermogenic markers
     * CREB and phospho-CREB
     * Signaling pathway components
   - Conduct ELISA to measure IL-33 levels in tissue and serum

4. **Flow Cytometry Analysis of Immune Cells**
   - Prepare single-cell suspensions from SVF
   - Stain with antibodies for:
     * ILC2s (Lineage-CD45+KLRG1+ST2+)
     * Eosinophils (CD11b+Siglec-F+)
     * Other immune cell populations
   - Analyze using multicolor flow cytometry
   - Quantify cell numbers and percentages
   - Assess activation status through marker expression

## IV. Functional Studies and Mechanistic Investigations

1. **CRISPR/Cas9 Gene Editing**
   - Design sgRNAs targeting CREB binding sites in IL-33 promoter
   - Validate sgRNA efficiency in cell culture
   - Transfect PDGFRβ+DPP4+ cells or use in vivo delivery methods
   - Confirm editing by sequencing and functional assays
   - Assess effects on IL-33 expression and cold response

2. **Chromatin Immunoprecipitation (ChIP)**
   - Crosslink proteins to DNA in adipose tissue or isolated cells
   - Sonicate chromatin to appropriate fragment size
   - Immunoprecipitate with anti-CREB antibody
   - Purify DNA and perform qPCR for IL-33 promoter regions
   - For genome-wide analysis, perform ChIP-seq
   - Analyze binding sites and motifs using bioinformatics tools

3. **In Vitro Cell Culture Studies**
   - Establish primary cultures of PDGFRβ+DPP4+ cells
   - Treat cells with:
     * β-adrenergic agonists (e.g., isoproterenol)
     * cAMP analogs to mimic cold stimulation
     * CREB inhibitors or activators
   - Measure IL-33 expression and secretion
   - Perform co-culture experiments with adipocyte precursors
   - Assess effects on adipogenic and thermogenic gene expression

4. **In Vivo Functional Assays**
   - Perform metabolic cage studies to measure:
     * Oxygen consumption and CO2 production
     * Energy expenditure
     * Physical activity
   - Conduct glucose and insulin tolerance tests
   - Measure core body temperature during cold challenge
   - Use infrared thermography to assess heat production

## V. Intervention Studies and Pathway Validation

1. **IL-33 Administration and Neutralization**
   - Administer recombinant IL-33 to mice at room temperature
   - Neutralize IL-33 using anti-IL-33 antibodies during cold exposure
   - Assess effects on:
     * Beige adipocyte formation
     * UCP1 expression
     * Thermogenic capacity
     * ILC2 recruitment and activation

2. **ILC2 Depletion and Reconstitution**
   - Deplete ILC2s using anti-CD90.2 or genetic approaches
   - Reconstitute with adoptive transfer of sorted ILC2s
   - Evaluate the necessity of ILC2s for IL-33-mediated thermogenesis
   - Analyze downstream mediators (e.g., IL-4, IL-13)

3. **Pharmacological Interventions**
   - Target CREB pathway using specific inhibitors
   - Modulate β-adrenergic signaling with agonists/antagonists
   - Assess effects on IL-33 expression and thermogenic remodeling
   - Identify potential therapeutic targets

4. **Microbiome Studies (for GF vs. CV comparison)**
   - Collect fecal samples for 16S rRNA sequencing
   - Compare microbiome composition between temperature conditions
   - Perform fecal microbiota transplantation experiments
   - Analyze correlations between specific bacterial taxa and IL-33 expression

## VI. Data Integration and Analysis

1. **Statistical Analysis**
   - Apply appropriate statistical tests:
     * Student's t-test for two-group comparisons
     * ANOVA with post-hoc tests for multiple groups
     * Non-parametric tests for non-normal distributions
   - Control for multiple comparisons (Benjamini-Hochberg)
   - Ensure adequate power through appropriate sample sizes
   - Present data as mean ± SEM with individual data points

2. **Multi-omics Integration**
   - Correlate transcriptomic data with protein expression
   - Integrate ChIP-seq with RNA-seq to identify direct CREB targets
   - Link cellular composition with functional outcomes
   - Develop pathway models of IL-33-mediated thermogenesis

3. **Visualization and Presentation**
   - Create clear figures showing key findings
   - Use consistent color schemes and labeling
   - Include appropriate controls in all data presentations
   - Develop schematic models summarizing the mechanism

This comprehensive experimental workflow enables detailed investigation of how IL-33 produced by PDGFRβ+DPP4+ cells regulates cold-induced thermogenesis, from the initial cold stimulus to CREB activation, IL-33 production, ILC2 recruitment, and ultimate beige adipocyte formation. The approach integrates multiple techniques spanning molecular biology, cell biology, and physiology to provide a complete understanding of this important metabolic pathway.


-----

# 实验工作流程：IL-33调控冷诱导产热

## 一、动物模型准备和冷暴露方案

1. **小鼠品系选择与饲养**
   - 选择C57BL/6J小鼠(8-12周龄，两性或性别匹配)
   - 在标准条件下饲养(22°C，12小时光照/黑暗周期)
   - 对于无菌实验，将小鼠维持在无菌隔离器中
   - 使小鼠适应饲养条件至少1周

2. **冷暴露方案**
   - 将小鼠分为实验组：
     * 室温对照组(22°C)
     * 急性冷暴露组(6°C持续24-48小时)
     * 慢性冷暴露组(6°C持续7-14天)
   - 将小鼠转移到预冷却的笼子中，提供足够垫料
   - 使用直肠温度计监测体温
   - 每日记录食物摄入量和体重

3. **基因模型构建**
   - 生成细胞特异性敲除模型：
     * PDGFRβ特异性Cre小鼠与IL-33flox/flox交配
     * CREB条件性敲除小鼠
   - 通过qPCR和Western blot验证敲除效率
   - 生成报告基因小鼠(如IL-33-GFP)用于细胞追踪

## 二、脂肪组织分析和细胞分离

1. **组织收集和处理**
   - 按照伦理指南安乐死小鼠
   - 收集腹股沟白色脂肪组织(iWAT)、附睾白色脂肪组织和棕色脂肪组织(BAT)
   - 称重组织并分为：
     * 液氮快速冷冻(基因/蛋白分析)
     * 4%多聚甲醛固定(组织学)
     * 新鲜处理(细胞分离)

2. **组织学分析**
   - 处理固定组织进行石蜡包埋或OCT冷冻切片
   - 将组织切片厚度为5-8μm
   - 进行H&E染色进行形态学分析
   - 进行UCP1免疫组织化学染色识别米色脂肪细胞
   - 使用光学显微镜成像并量化米色脂肪细胞面积

3. **脂肪组织分离**
   - 剪碎新鲜脂肪组织并用胶原酶消化
   - 离心分离浮游脂肪细胞和基质血管部分(SVF)
   - 通过70μm滤网过滤SVF
   - 必要时溶解红细胞
   - 使用血球计数器或自动细胞计数器计数

4. **PDGFRβ+DPP4+细胞分离**
   - 用荧光抗体染色SVF：
     * 抗PDGFRβ(CD140b)
     * 抗DPP4(CD26)
     * 谱系标记物(CD31, CD45)用于排除
   - 进行荧光激活细胞分选(FACS)
   - 收集PDGFRβ+DPP4+和PDGFRβ+DPP4-细胞群
   - 通过流式细胞术分析样品等分验证纯度

## 三、分子和细胞分析

1. **RNA测序和转录组分析**
   - 从以下样本提取总RNA：
     * 整个脂肪组织样本
     * 分选的PDGFRβ+DPP4+细胞
     * 其他相关细胞群
   - 评估RNA质量(Bioanalyzer，RNA完整性数值>8)
   - 制备RNA-seq文库(poly-A选择或ribo-depletion)
   - 进行双端测序(Illumina平台)
   - 使用标准生物信息学流程分析数据：
     * 质量控制和读段比对
     * 差异表达分析
     * 通路富集分析
     * 可视化(热图，火山图)

2. **基因表达分析**
   - 设计关键基因引物(IL-33, UCP1, PGC1α, CREB等)
   - 对组织和细胞样本进行RT-qPCR
   - 使用看家基因(β-actin, GAPDH)标准化
   - 使用2^-ΔΔCt方法计算相对表达
   - 验证选定基因的RNA-seq发现

3. **蛋白表达分析**
   - 从组织和细胞中提取蛋白质
   - 测定蛋白质浓度(BCA法)
   - 进行以下Western blot：
     * IL-33及其受体ST2
     * UCP1和其他产热标记物
     * CREB和磷酸化CREB
     * 信号通路组分
   - 进行ELISA测量组织和血清中IL-33水平

4. **免疫细胞流式细胞术分析**
   - 从SVF制备单细胞悬液
   - 用以下抗体染色：
     * ILC2s(Lineage-CD45+KLRG1+ST2+)
     * 嗜酸性粒细胞(CD11b+Siglec-F+)
     * 其他免疫细胞群
   - 使用多色流式细胞术分析
   - 量化细胞数量和百分比
   - 通过标记物表达评估激活状态

## 四、功能研究和机制调查

1. **CRISPR/Cas9基因编辑**
   - 设计靶向IL-33启动子中CREB结合位点的sgRNAs
   - 在细胞培养中验证sgRNA效率
   - 转染PDGFRβ+DPP4+细胞或使用体内递送方法
   - 通过测序和功能测定确认编辑
   - 评估对IL-33表达和冷响应的影响

2. **染色质免疫沉淀(ChIP)**
   - 在脂肪组织或分离的细胞中将蛋白质与DNA交联
   - 将染色质超声处理至适当片段大小
   - 用抗CREB抗体进行免疫沉淀
   - 纯化DNA并对IL-33启动子区域进行qPCR
   - 对于全基因组分析，进行ChIP-seq
   - 使用生物信息学工具分析结合位点和基序

3. **体外细胞培养研究**
   - 建立PDGFRβ+DPP4+细胞的原代培养
   - 用以下物质处理细胞：
     * β-肾上腺素能激动剂(如异丙肾上腺素)
     * cAMP类似物模拟冷刺激
     * CREB抑制剂或激活剂
   - 测量IL-33表达和分泌
   - 进行与脂肪细胞前体的共培养实验
   - 评估对脂肪生成和产热基因表达的影响

4. **体内功能测定**
   - 进行代谢笼研究测量：
     * 氧气消耗和CO2产生
     * 能量消耗
     * 体力活动
   - 进行葡萄糖和胰岛素耐受性测试
   - 在冷挑战期间测量核心体温
   - 使用红外热成像评估产热

## 五、干预研究和通路验证

1. **IL-33给药和中和**
   - 在室温下给小鼠施用重组IL-33
   - 在冷暴露期间使用抗IL-33抗体中和IL-33
   - 评估对以下方面的影响：
     * 米色脂肪细胞形成
     * UCP1表达
     * 产热能力
     * ILC2招募和激活

2. **ILC2清除和重建**
   - 使用抗CD90.2或基因方法清除ILC2s
   - 通过分选的ILC2s过继转移进行重建
   - 评估ILC2对IL-33介导产热的必要性
   - 分析下游介质(如IL-4, IL-13)

3. **药理学干预**
   - 使用特定抑制剂靶向CREB通路
   - 用激动剂/拮抗剂调节β-肾上腺素能信号
   - 评估对IL-33表达和产热重塑的影响
   - 确定潜在的治疗靶点

4. **微生物组研究(用于GF vs CV比较)**
   - 收集粪便样本进行16S rRNA测序
   - 比较不同温度条件下的微生物组成
   - 进行粪便微生物群移植实验
   - 分析特定细菌类群与IL-33表达之间的相关性

## 六、数据整合和分析

1. **统计分析**
   - 应用适当的统计检验：
     * 两组比较使用Student's t检验
     * 多组使用ANOVA及事后检验
     * 非正态分布使用非参数检验
   - 控制多重比较(Benjamini-Hochberg)
   - 通过适当的样本量确保足够的统计功效
   - 将数据呈现为均值±标准误差，并显示个体数据点

2. **多组学整合**
   - 将转录组数据与蛋白表达相关联
   - 整合ChIP-seq与RNA-seq识别直接CREB靶点
   - 将细胞组成与功能结果联系起来
   - 开发IL-33介导产热的通路模型

3. **可视化和展示**
   - 创建显示关键发现的清晰图表
   - 使用一致的配色方案和标签
   - 在所有数据展示中包含适当的对照
   - 开发总结机制的示意模型

这一综合实验工作流程使研究人员能够详细研究PDGFRβ+DPP4+细胞产生的IL-33如何调控冷诱导产热，从最初的冷刺激到CREB激活、IL-33产生、ILC2招募，最终形成米色脂肪细胞。该方法整合了跨越分子生物学、细胞生物学和生理学的多种技术，提供了对这一重要代谢通路的完整理解。


------

### 1. **Experimental Purpose:**
- **Scientific Question**: The study aims to understand how **IL-33**, a cytokine produced by **PDGFRβ+DPP4+ cells**, regulates cold-induced thermogenesis and the formation of beige adipocytes in white adipose tissue (WAT). Specifically, the study investigates whether IL-33 expression is induced by cold exposure and how it contributes to thermogenic remodeling.
- **Experimental Design**: The study uses a combination of **RNA sequencing (RNA-seq)**, **flow cytometry**, **histology**, and **CRISPR/Cas9 gene editing** to explore the role of IL-33 in cold-induced thermogenesis. The researchers first identify IL-33 as a key player in the process and then investigate the molecular mechanisms underlying its regulation.
### 2. **Model System:**
- **Model System**: The study primarily uses **mouse models**, particularly **PDGFRβ+DPP4+ cells** in inguinal(腹股沟的) white adipose tissue (iWAT). These cells are identified as the main source of IL-33 in iWAT. The study also uses **germ-free (GF)** and **conventional (CV)** mice to study the effects of cold exposure on adipose tissue.
- **Why This System?**: Mice are appropriate for this study because they allow for the manipulation of specific cell populations and genes, and their adipose tissue responds to cold exposure in a manner similar to humans. The use of PDGFRβ+DPP4+ cells is relevant because these cells are known to play a role in adipose tissue remodeling.
- **Alternative Model Systems**: Other model systems, such as **cell cultures** or **zebrafish**, could be used, but they lack the complexity of in vivo adipose tissue remodeling and the interaction between different cell types.
- **Ethical Considerations**: Using mice requires ethical approval, especially when dealing with cold exposure and gene editing. The study likely adheres to ethical guidelines for animal research.
### 3. **Measurement Approach:**
- **Techniques**: The study employs several techniques:
    - **RNA-seq**: To analyze gene expression changes in response to cold exposure.
    - **Flow cytometry**: To study immune cell populations (e.g., ILC2s,一种调节脂肪的免疫细胞) in adipose tissue.
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


