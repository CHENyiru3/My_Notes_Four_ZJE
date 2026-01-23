- Traditional Drug:
	- High Investment --> Long time consumption --> High risk
### Antibody
- Structure:
	- Antibodies, also known as immunoglobulins (Igs), are Y-shaped proteins composed of two heavy chains and two light chains, connected by disulfide bonds
- Antigen binding
	- The variable regions (Fv) of the antibody, particularly the six loops called complementarity-determining regions (CDRs), are responsible for binding to specific antigens.
- Fab and Fc
	- Antibodies have two antigen-binding fragments (Fab) and one crystallizable domain (Fc
# 抗体设计流程：从计算设计到实验验证

## 一、计算设计阶段

1. **初始输入**
   - 抗原结构(晶体结构或计算预测)
   - 表位识别与选择
   - 现有抗体数据库分析

2. **设计方法**
   - 从头设计:构建主链→完成侧链→生成序列
   - 基于突变的优化:在约束搜索空间内系统探索突变
   - 结构预测工具:AlphaFold2, ESM-Fold, AF3, DMFold用于验证/预测

3. **可开发性评估**
   - MPGNN, RF Diffusion (DDPM), SCUBA-D计算亲和力
   - 额外指标:特异性、活性、稳定性
   - 迭代优化:基于计算预测的性质进行迭代改进

## 二、实验验证阶段

1. **抗体基因合成与表达**
   - **基因合成**
     * 优化密码子使用
     * 合成重链和轻链基因
     * 克隆至适当表达载体

   - **表达系统选择**
     * 哺乳动物细胞系(HEK293, CHO)
     * 杆状病毒-昆虫细胞系统
     * 酵母或大肠杆菌系统(适用于抗体片段)

   - **小规模表达筛选**
     * 瞬时转染优化
     * 表达条件筛选(温度、添加剂、培养时间)
     * ELISA或Western blot初步验证表达

2. **抗体蛋白纯化与质控**
   - **亲和层析纯化**
     * 蛋白A/G柱纯化(适用于Fc含抗体)
     * 抗原亲和柱(针对特定抗体)
     * 标签亲和纯化(His标签、FLAG标签等)

   - **进一步纯化**
     * 离子交换层析
     * 分子筛层析
     * 疏水相互作用层析

   - **质量控制分析**
     * SDS-PAGE和考马斯蓝染色
     * 质谱分析确认序列和修饰
     * 凝胶过滤分析评估聚集状态
     * 内毒素检测

3. **生物物理特性分析**
   - **结构完整性验证**
     * 圆二色谱(CD)分析二级结构
     * 差示扫描量热法(DSC)测定热稳定性
     * 动态光散射(DLS)评估均一性和聚集倾向

   - **稳定性测试**
     * 加速稳定性研究(高温、pH变化)
     * 冻融循环稳定性
     * 长期储存稳定性

   - **亲和力测定**
     * 表面等离子体共振(SPR)测量结合动力学参数
     * 等温滴定量热法(ITC)测量热力学参数
     * Bio-layer干涉法(BLI)快速筛选

4. **功能活性验证**
   - **抗原结合特性**
     * ELISA测定结合活性
     * 竞争结合实验评估表位特异性
     * 交叉反应性测试(与相关抗原或其他物种同源物)

   - **细胞水平功能验证**
     * 流式细胞术评估细胞表面抗原结合
     * 免疫荧光显微镜观察细胞定位
     * 细胞功能测定(如中和、抑制、激活等)

   - **效应功能测试**
     * 抗体依赖性细胞介导的细胞毒性(ADCC)测定
     * 补体依赖性细胞毒性(CDC)测定
     * 抗体依赖性细胞吞噬作用(ADCP)测定

5. **体外疗效评估**
   - **信号通路分析**
     * Western blot检测下游信号蛋白磷酸化
     * 荧光素酶报告基因测定
     * 磷酸化蛋白组学分析

   - **功能性测定**
     * 细胞增殖/凋亡测定
     * 细胞迁移/侵袭测定
     * 细胞分化测定
     * 病毒中和测定(用于抗病毒抗体)

   - **三维模型系统**
     * 类器官培养系统
     * 细胞球测试
     * 共培养系统

6. **体内初步评估**
   - **药代动力学研究**
     * 小鼠、大鼠或非人灵长类动物中的半衰期测定
     * 组织分布研究
     * 清除机制研究

   - **初步疗效研究**
     * 选择适当疾病模型(移植瘤、转基因或疾病诱导模型)
     * 剂量探索研究
     * 生物标志物响应评估

   - **初步安全性评估**
     * 急性毒性观察
     * 细胞因子释放测试
     * 组织交叉反应性研究

7. **抗体优化反馈**
   - **结构-功能关系分析**
     * 将实验数据与计算预测对比
     * 识别影响功能的关键残基
     * 归纳结构决定因素

   - **设计改进**
     * 基于实验数据修改计算模型
     * 设计新一代抗体改进特定性能
     * 亲和力成熟或人源化优化

   - **制剂开发初步研究**
     * 缓冲液筛选
     * 稳定剂评估
     * 冻干可行性研究

这一综合流程将计算设计与严格的实验验证相结合，确保开发的抗体不仅具有理想的理论特性，还具备实际的功能活性和药物开发潜力。通过实验数据反馈到计算模型，可以不断优化设计算法，提高预测准确性，加速抗体药物的开发过程。

----

# Antibody Design Pipeline: From Computational Design to Experimental Validation

## I. Computational Design Phase

1. **Initial Inputs**
   - Antigen structure (crystal structure or computational prediction)
   - Epitope identification and selection
   - Analysis of existing antibody databases

2. **Design Approaches**
   - De novo design: Build main chain → complete side chains → generate sequence
   - Mutation-based optimization: Systematic exploration of mutations within constrained search space
   - Structure prediction tools: AlphaFold2, ESM-Fold, AF3, DMFold for validation/prediction

3. **Developability Assessment**
   - MPGNN, RF Diffusion (DDPM), SCUBA-D for affinity computation
   - Additional metrics: specificity, activity, stability
   - Optimization loop: Iterative refinement based on computationally predicted properties

## II. Experimental Validation Phase

1. **Antibody Gene Synthesis and Expression**
   - **Gene Synthesis**
     * Codon optimization
     * Synthesis of heavy and light chain genes
     * Cloning into appropriate expression vectors

   - **Expression System Selection**
     * Mammalian cell lines (HEK293, CHO)
     * Baculovirus-insect cell system
     * Yeast or E. coli systems (for antibody fragments)

   - **Small-Scale Expression Screening**
     * Transient transfection optimization
     * Expression condition screening (temperature, additives, culture time)
     * Preliminary validation by ELISA or Western blot

2. **Antibody Protein Purification and Quality Control**
   - **Affinity Chromatography**
     * Protein A/G column purification (for Fc-containing antibodies)
     * Antigen affinity columns (for specific antibodies)
     * Tag-based purification (His-tag, FLAG-tag, etc.)

   - **Further Purification**
     * Ion exchange chromatography
     * Size exclusion chromatography
     * Hydrophobic interaction chromatography

   - **Quality Control Analysis**
     * SDS-PAGE and Coomassie blue staining
     * Mass spectrometry for sequence and modification confirmation
     * Gel filtration analysis for aggregation assessment
     * Endotoxin testing

3. **Biophysical Characterization**
   - **Structural Integrity Verification**
     * Circular dichroism (CD) for secondary structure analysis
     * Differential scanning calorimetry (DSC) for thermal stability
     * Dynamic light scattering (DLS) for homogeneity and aggregation propensity

   - **Stability Testing**
     * Accelerated stability studies (high temperature, pH variations)
     * Freeze-thaw cycle stability
     * Long-term storage stability

   - **Affinity Determination**
     * Surface plasmon resonance (SPR) for binding kinetics parameters
     * Isothermal titration calorimetry (ITC) for thermodynamic parameters
     * Bio-layer interferometry (BLI) for rapid screening

4. **Functional Activity Validation**
   - **Antigen Binding Characteristics**
     * ELISA for binding activity
     * Competition binding assays for epitope specificity
     * Cross-reactivity testing (with related antigens or homologs from other species)

   - **Cellular-Level Functional Validation**
     * Flow cytometry for cell surface antigen binding
     * Immunofluorescence microscopy for cellular localization
     * Cell-based functional assays (neutralization, inhibition, activation, etc.)

   - **Effector Function Testing**
     * Antibody-dependent cellular cytotoxicity (ADCC) assays
     * Complement-dependent cytotoxicity (CDC) assays
     * Antibody-dependent cellular phagocytosis (ADCP) assays

5. **In Vitro Efficacy Assessment**
   - **Signaling Pathway Analysis**
     * Western blot for downstream signaling protein phosphorylation
     * Luciferase reporter assays
     * Phospho-proteomics analysis

   - **Functional Assays**
     * Cell proliferation/apoptosis assays
     * Cell migration/invasion assays
     * Cell differentiation assays
     * Viral neutralization assays (for antiviral antibodies)

   - **Three-Dimensional Model Systems**
     * Organoid culture systems
     * Spheroid assays
     * Co-culture systems

6. **Preliminary In Vivo Evaluation**
   - **Pharmacokinetic Studies**
     * Half-life determination in mice, rats, or non-human primates
     * Tissue distribution studies
     * Clearance mechanism studies

   - **Preliminary Efficacy Studies**
     * Selection of appropriate disease models (xenografts, transgenic, or disease-induced models)
     * Dose exploration studies
     * Biomarker response assessment

   - **Preliminary Safety Assessment**
     * Acute toxicity observations
     * Cytokine release assays
     * Tissue cross-reactivity studies

7. **Antibody Optimization Feedback**
   - **Structure-Function Relationship Analysis**
     * Comparison of experimental data with computational predictions
     * Identification of key residues affecting function
     * Deduction of structural determinants

   - **Design Improvements**
     * Modification of computational models based on experimental data
     * Design of next-generation antibodies with improved specific properties
     * Affinity maturation or humanization optimization

   - **Preliminary Formulation Development**
     * Buffer screening
     * Stabilizer evaluation
     * Lyophilization feasibility studies

This comprehensive pipeline integrates computational design with rigorous experimental validation, ensuring that developed antibodies not only possess ideal theoretical characteristics but also demonstrate practical functional activity and drug development potential. By feeding experimental data back into computational models, design algorithms can be continuously optimized, improving prediction accuracy and accelerating the antibody drug development process.

