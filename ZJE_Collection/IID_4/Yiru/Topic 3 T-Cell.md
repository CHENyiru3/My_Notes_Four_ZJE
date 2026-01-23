
![](https://i.imgur.com/zYawHoZ.jpeg)

## **1. T Cell Development (The "Education" Phase)**

- **Origin:** Starts in the **Red Bone Marrow** as a T cell precursor.
    
- **Migration:** Travels to the **Thymus** (primary lymphoid organ).
    
    - **Mechanism:** Thymus releases **chemotactic agents** (e.g., thymosin) to attract T cell precursors.
        

### **Step 1: Receptor Formation (Gene Shuffling)**

- **Trigger:** Chemotactic agents bind to the naive T cell's receptor.
    
- **Action:** Activates **RAG1** and **RAG2** (Recombination-Activating Genes).
    
- **Result:** These recombinases shuffle DNA segments to create a unique **TCR (T Cell Receptor)**.
    
    - _Goal:_ Create a receptor specific for **one** unique antigen (Note: TCRs bind Antigen-MHC complexes, not antibodies directly).
        

### **Step 2: Lineage Commitment (The "Double Positive" Stage)**

- T cells initially express **both** CD4 and CD8 (Double Positive).
    
- **CD8:** Binds to **MHC Class I**.
    
- **CD4:** Binds to **MHC Class II**.
    

### **Step 3: The Exams (Selection Process)**

1. **Positive Selection (The "Competence" Test):**
    
    - _Question:_ Can this TCR recognize my own MHC molecules?
        
    - _Process:_ Thymic epithelial cells present MHC.
        
    - _Pass:_ TCR binds MHC with moderate affinity (Survival signal received).
        
    - _Fail:_ No binding $\rightarrow$ **Death by Neglect** (Apoptosis).
        
2. **Negative Selection (The "Loyalty" Test):**
    
    - _Question:_ Does this TCR attack "self" tissues?
        
    - _Process:_ Thymic cells present "self-peptides" on MHC.
        
    - _Fail:_ High-affinity binding to self $\rightarrow$ **Clonal Deletion** (Apoptosis triggered by **FAS ligand** released by thymic cells).
        
    - _Pass:_ Low/No binding to self $\rightarrow$ Survives.
        

### **Step 4: Final Maturation & Choice**

- **The Choice:**
    
    - Upregulate **CD4**, Downregulate CD8 $\rightarrow$ **T Helper Cell (Th)** $\rightarrow$ Secondary Lymphoid Organs.
        
    - Upregulate **CD8**, Downregulate CD4 $\rightarrow$ **T Cytotoxic Cell (Tc)** $\rightarrow$ Secondary Lymphoid Organs.
        
- **The Exception (Treg):**
    
    - Some self-reactive CD4+ cells are not killed but diverted to become **Natural Tregs**.
        
    - _Location:_ Occurs mainly in **Hassall’s Corpuscles** in the thymus.
        
    - _Mechanism:_ Upregulate **CD25** and **FoxP3** (dependent on IL-2).
        

---

## **2. Classification Cheat Sheet**

### **A. The "Rule of 8"**

- **CD4** x **MHC II** = 8 (Helpers talk to Generals/APCs).
    
- **CD8** x **MHC I** = 8 (Killers check Civilians/Nucleated cells).
    

### **B. CD4+ Helper T Lineages**

_Input Cytokines $\rightarrow$ Master Transcription Factor $\rightarrow$ Output Cytokines_

| **Lineage** | **Input (Induction)**                                                              | **Master Switch** | **Output (Effector)**  | **Main Function**                                                        |
| ----------- | ---------------------------------------------------------------------------------- | ----------------- | ---------------------- | ------------------------------------------------------------------------ |
| **Th1**     | IL-12, IFN-$\gamma$                                                                | **T-bet**         | **IFN-$\gamma$**, TNF  | **Intracellular Defense:** Viruses, bacteria inside macrophages.         |
| **Th2**     | IL-4                                                                               | **GATA3**         | **IL-4**, IL-5, IL-13  | **Extracellular Defense:** Parasites (Worms), Allergy.                   |
| **Th17**    | Mouse: TGF-$\beta$ + IL-6<br><br>  <br><br>Human: TGF-$\beta$ + IL-1$\beta$ + IL-6 | **ROR$\gamma$t**  | **IL-17**, IL-22       | **Mucosal Defense:** Fungi, Extracellular bacteria. Autoimmunity driver. |
| **Treg**    | TGF-$\beta$, IL-2                                                                  | **FoxP3**         | **TGF-$\beta$**, IL-10 | **Suppression:** Immune tolerance, preventing autoimmunity.              |
| **Tfh**     | IL-6, IL-21                                                                        | **Bcl6**          | **IL-21**              | **B Cell Help:** Antibody production.                                    |

### **C. Unconventional T Cells**

| **Cell Type**              | **Recognition Target**               | **Key Feature**                                 |
| -------------------------- | ------------------------------------ | ----------------------------------------------- |
| **NKT Cells**              | **Lipids** on **CD1d**               | Bridge Innate/Adaptive. Rapid cytokine release. |
| **$\gamma\delta$ T Cells** | **Stress Signals** & Phosphoantigens | No MHC required. Barrier defense (Skin/Gut).    |

---

## **3. Cell-Mediated Immunity (The Killers)**

_This is the detailed section you requested on how cells kill._

### **A. Cytotoxic T Lymphocytes (CTLs)**

- **Identity:** CD8+, Adaptive Immunity.
    
- **Target:** Virus-infected cells, Tumor cells, Intracellular bacteria.
    
- **Recognition:** TCR binds to specific **Antigen + MHC Class I**.
    
- **Mechanism of Killing:**
    
    1. **Perforin/Granzyme Pathway (Main):**
        
        - CTL releases granules.
            
        - **Perforin:** Punches holes (pores) in the target cell membrane.
            
        - **Granzymes:** Enter through holes and activate **Caspases** inside the target.
            
        - _Result:_ Apoptosis (clean cell suicide).
            
    2. **Fas Ligand (FasL) Pathway:**
        
        - CTL expresses FasL on its surface.
            
        - Binds to **Fas receptor (CD95)** on the target cell.
            
        - _Result:_ Triggers the "Death Domain" signal cascade $\rightarrow$ Apoptosis.
            

### **B. Natural Killer (NK) Cells**

- **Identity:** Innate Lymphoid Cell (No TCR), Innate Immunity.
    
- **Target:** Cells trying to "hide" from CTLs by removing MHC I, or stressed cells.
    
- **Recognition (The "Missing Self" Hypothesis):**
    
    - **Inhibitory Receptor:** Binds to **Normal MHC Class I**. If detected $\rightarrow$ "Don't Kill."
        
    - **Activating Receptor:** Binds to **Stress Ligands** (e.g., MICA/MICB) on infected cells.
        
    - _Trigger:_ **Low MHC I** + **High Stress Signal** = **KILL**.
        
- **Mechanism:** Uses Perforin and Granzymes (same as CTL).
    
- **ADCC (Antibody-Dependent Cell-mediated Cytotoxicity):**
    
    - NK cells have **CD16 (Fc Receptor)**.
        
    - If a target is coated in antibodies (IgG), CD16 binds the antibody tail.
        
    - _Result:_ NK cell degranulates and kills the target.


### Tregs
- Immune tolerance, preventing autoimmunity.
- access a unique transcription factor called **FOXP3**
- Further subtypes
	- natural Tregs (nTregs): in peripheral immune tolerance
	- induced Tregs (iTregs): naive T cells; control inflammation
- Produce **anti-inflammatory** cytokines: IL-10 and TGF-$\beta$ 
	- inhibit other immune cells; cause the cytolysis of activated T cells
- Metabolic regulation
	- reduce the level of glucose and amino acids that is necessary for other immune cells
- Moderate DC cells
	- prevent DC cells --> prevent other immune cells
- Regulating cancer and infections
	- suppressing the immune cells --> targeting cancer cells
	- prevent immune mediated damage to host tissue and promote immune tolerance