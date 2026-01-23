- ![](https://i.imgur.com/g6NGb9L.jpeg)

- B cell here main contribute to humoral immunity
- B cells are produced in lymph node
	- Naive B-lymphocyte go through recombination (like T cell), by receiving circulating free lgD antigen (by random chance) --> BCRs
	- --> activated B cell --> receptor-mediated endocytosis --> pull antigen in
	- --> In B cell, antigen produce an endosome, and B cell produce specific MHC2 that can bind to the antigen --> **MHC2** expose to membrane, the B lymphocyte is activated
- In T cell side:
	- macrophage will have MHC-2 (antigen specific) and MHC-1
	- How it interact with **Naive T helper cell**
		- Signal 1: T cell receptor (TCR) --> bind to antigen gotten by MHC2 & CD4 protein --> bind to MHC2
		- Signal 2: macrophage have long protein B7 that can bind the CD28 in T helper cell
		- Signal 3: Macrophage secrete IL-1,  IL-1 bind to T helper
			- Signal 1 +  Signal 2 + Signal 3 --> costimulation
				- T cell activated --> T helper secrete IL-2 --> can bind and activate T cell too -->==IL-4==, ==IL-5== secretion --> make the T cell to Th2 cell
- Why T cell side matters to B cell? --> cause clonal expansion
	- IL-4 released by T helper cell --> activate B lymphocyte --> proliferation of B cell (with special BCRs)
	- IL-5 function after the clonal expansion --> B cell start to differentiation 
		- --> memory B cells with BCR
		- --> plasma cells /effector B cells
	- IL-5 and IL-6 activate plasma cells--> secrete ==antibodies== (specific to antigen)
- Then antibodies can beat antigens
	- **Neutralization**: anitbody bind to the antigens on the surface of bacteria or virus
	- **Precipitation**: bind to circulating free antigens, and cause them to have precipitation
	- **Lysis**: produce protein that can cause the bacteria to lysis
	- **Attract macrophages**: antibody could produce proteins that attract the macrophage to kill the antibody

## B cell Tolerance

![Uploading file...9lo8v]()

- B cell will have VDJ recombination process to produce BCR, which is random --> will produce B cells that recognize self-antigens
	- ==Solution==: quality control system called tolerance

- **Central Tolerance**: Bone marrow; before B cells enter the blood, it must prove it is not dangerous
	- Stage: Immature B cells, expressing lgM on surface
	- Self-antigen Test:
		- protein, DNA, cell surface markers
		- Possible outcomes:
			- if B cell doesn't bind to any self-antigen
				- --> to the spleen to complete maturation
			- else if B cell binds tightly to a self-antigen
				- --> stop B cell moving from marrow; this triggers **Receptor editing**, RAG reactivation
					- the cell keeps the RAG1 and RAG2 genes activated
					- it deletes the existing light chain and rearranges a new one
					- In other word, it creates a new BCR with a new specificity
					- if pass: Survival and  export to periphery
					- else (still have auto-reactive): cell tries again or dies
				- Die: Clonal deletion (apoptosis)
					- the cell activates the intrinsic apoptotic pathway
			- else if weak reaction
				- The B cell binds weakly or to a soluble self-antigen
				- Cell becomes permanent non-responsiveness and die due to competition in the periphery
- **Peripheral tolerance** (as backup system)
	- Location in spleen, lymph nodes, and circulation
	- Stage: Transitional and mature B cells
	- **Mechanisms of removal**:
		- 1. Follicular exclusion: auto-reactive B cells are chemically excluded form the Follicles, which will let them die
		- 2. Resource Competition 
			- B cells compete for a critical survival cytokine called ==BAFF== (B cell activating factor)
			- Normal B cells are better at capturing BAFF
		- 3. Lack of T cell help
			- For a B cell to fully activate and cause damage, it usually needs confirmation signal from a helper T cell
			- If a B cell presents a **self-antigen** to a T cell, but the T cell (which has its own tolerance checks) does not recognize it, the B cell receives no help (no CD40L signal).
				- **Key Mechanism of B cell**: Linked Recognition
					- B cells do not just show exactly what they bound to on the outside
					- But they will cut the peptide and then present the parts, to T cells TCR 

|**Feature**|**Central Tolerance**|**Peripheral Tolerance**|
|---|---|---|
|**Location**|Bone Marrow 26|Spleen / Lymph Nodes 27|
|**B Cell Stage**|Immature B Cell (IgM+) 28|Transitional / Mature B Cell 29|
|**Primary Trigger**|Binding to self-antigen in marrow 30|Binding to self-antigen in periphery|
|**Key Mechanism 1**|**Receptor Editing:** RAG reactivation to change receptor 31313131|**Anergy:** Functional unresponsiveness 32|
|**Key Mechanism 2**|**Clonal Deletion:** Apoptosis via Bim 33|**Follicular Exclusion:** Denied entry to survival niches 34|
|**Key Mechanism 3**|**Anergy:** If antigen is soluble/weak|**Starvation:** Competition for **BAFF** 35|
