![](https://i.imgur.com/4Xbn4Sd.jpeg)

- Learn: 3.1 and 3.2
- Core idea: the immune system treats pathogens as specific input (**pathogen-associated molecular patterns, PAMPs**), and different inputs trigger different **signalling pathways**, which may cause cell death
- Pattern recognition receptors (**PRRs**), recognise PAMPs or molecules from damaged cells (DAMPs)
	- **TLRs, Toll-like receptors**: surface or endosomal sensor
		- Example: TLR4 detects LPS (which is a kind of bacteria)
		- Pathway: 
			- ![](https://i.imgur.com/mWmEC5L.png)
			- Dimerized TLRs --> MyD88 --> IRAKs --> TRAF6 --> NF-$\kappa$B (a kind of transcription factor) --> transcription of **pro-inflammatory cytokines**
				- Pro-inflammatory cytokines are signaling molecules secreted by immune cells that promote and regulate inflammation to fight infection. They are crucial for the immune response but can also cause tissue damage if their levels are too high or chronic. Key examples include TNF-α, IL-1, and IL-6.
	- **RLRs, RIG-I-like Receptors**: cytosolic sensors
		- ![](https://i.imgur.com/XPRYEHB.png)
		- Input is Viral RNA (released inside cell)
		- Pathway: viral RNA --> RIG-I --> MAVS (mitochondrial adaptor) --> IRF3 --> Type I interferons and inflammatory cytokines
- The **inflammasome**
	- cytosolic multiprotein complexes of the innate immune system responsible for the activation of inflammatory response and cell death
	- MLRP3 inflammasome 
		- A multi-protein complex, NLRP3 (sensor) + ASC (adaptor) + Caspase-1 (Effector)
		- priming and activation: singal 1 and 2
			- Signal 1, Priming: TLR activation activates NF-$\kappa$B
			- Signal 2, Activation: Disturbance in the cell, specifically K+ efflux, ROS, or crystals
			- Results
				- **Caspase-1 Activation:** It acts as molecular scissors.
				- **Cytokine Release:** Cleaves Pro-IL-1$\beta$ and Pro-IL-18 into active forms.
				- **Pyroptosis:** Cleaves **Gasdermin D (GSDMD)**, which punches pores in the cell membrane to release the cytokines and kill the cell
					- Pyroptosis rely on GSDMD, which will activate IL-1$\beta$ and IL-18 maturation and cell lysis
			- In the **Canonical NLRP3 Pathway**, the order is strict: **Signal 1 must happen before Signal 2** for a successful immune response.


- **Cell death**: silent death (Apoptosis) and lytic death (Necroptosis and pyroptosis)
	- Apoptosis: non-lytic, membrane stays intact
		- ![](https://i.imgur.com/eAscr1p.png)
		- Intrinsic pathway:
			- response to internal stimuli, like biochemical stress, DNA damage, and withgrawal of growth factors
			- mitochondrial stress --> ==BAX/ BAK== pore formation (MOMP) --> Cytochrome c release --> Apoptosome --> Caspase-9 --> Caspase-3
			- Bcl-2 family protein act as protecotrs blocking BAX/BAK
			- ![](https://teachmeanatomy.info/wp-content/uploads/AdobeStock_1467325541-1024x655.png)
		- Extrinsic pathway
			- initiated by external stimuli, primarily through the binding of ligands to death receptors on the cell surface![](https://teachmeanatomy.info/wp-content/uploads/AdobeStock_1479708809-1024x825.png)
			- Death receptor --> FADD --> Caspase-8 --> Caspase-3
	- Necroptosis
		- When it happens: only when Caspase-8 is inhibited (like by virus)
		- Machinery
			- RIPK1 recruits RIPK3 via the RHIM domain
			- They form a complex called the necrosome
			- RIPK3 phosphorylates MLKL
		- Phosphorylated MLKL oligomerizes and moves to the plasma membrane to form pores, causing the cell to burst.
- **Caspase-8** is the Key switch
	- Active Caspase-8 can cleave RIPK1 and RIPK3, destorying the necroptosis machinery. ==Result = Apoptosis==
	- Inactivate Caspase-8: RIPK1 and RIPK3 accumulate and phosphorylate MLKL. ==Result = Necroptosis==

| **Feature**                | **Apoptosis**                                                                                                                                                     | **Necroptosis**                                                                                                                                                      | **Pyroptosis**                                                                                                                                                                    |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Primary Trigger**        | **Intrinsic:** Cellular stress (DNA damage, oxidative stress) sensed by Bcl-2 family.<br><br>  <br><br>**Extrinsic:** Death Receptor ligation (e.g., FasL, TNF)2. | **Receptor Activation + Caspase Inhibition:**<br><br>  <br><br>TNFR1 or TLR activation _in the presence of_ Caspase-8 inhibition (e.g., by viral proteins or drugs). | **Inflammasome Activation:**<br><br>  <br><br>Sensing of PAMPs/DAMPs (e.g., LPS, ATP, Crystals) by sensors like NLRP3, AIM2, or NLRC.                                             |
| **Caspase Involvement**    | **Caspase-Dependent:**<br><br>  <br><br>• **Initiators:** Caspase-8 (extrinsic) or Caspase-9 (intrinsic) .<br><br>  <br><br>• **Executioners:** Caspase-3, -7.    | **Caspase-Independent:**<br><br>  <br><br>Occurs _only_ when Caspase-8 is inactivated. Relies on kinases **RIPK1** and **RIPK3**                                     | **Caspase-Dependent:**<br><br>  <br><br>Relies on "Inflammatory Caspases":<br><br>  <br><br>• **Caspase-1** (Canonical) 8.<br><br>  <br><br>• **Caspase-4/5/11** (Non-canonical). |
| **Key Effector Mechanism** | **MOMP:** Mitochondrial Outer Membrane Permeabilization via **BAX/BAK**                                                                                           | **MLKL Pores:** Phosphorylated MLKL oligomerizes and translocates to the plasma membrane to form pores                                                               | **GSDMD Pores:** Caspase-1 cleaves **Gasdermin D**, forming pores that release IL-1β/IL-18.                                                                                       |
| **Outcome**                | **Non-Inflammatory (Silent):**<br><br>  <br><br>Cell shrinks, membrane remains intact (initially), formation of apoptotic bodies, phagocytosis 13.                | **Pro-Inflammatory (Lytic):**<br><br>  <br><br>Cell swells and bursts, releasing DAMPs. Often used as a backup anti-viral defense.                                   | **Pro-Inflammatory (Lytic):**<br><br>  <br><br>Cell bursts, releasing mature cytokines (**IL-1β, IL-18**) and DAMPs.                                                              |
### **Key Logic Checks for Exam:**

1. **The Caspase-8 Switch:** If Caspase-8 is active $\rightarrow$ Apoptosis. If Caspase-8 is blocked $\rightarrow$ Necroptosis 16.
    
2. **The Pore Formers:** Necroptosis uses **MLKL**; Pyroptosis uses **GSDMD** (Gasdermin D). Both cause lysis, but GSDMD is specifically linked to IL-1$\beta$ release.
    
3. **Mitochondria:** Apoptosis is heavily defined by mitochondrial permeabilization (MOMP), whereas Necroptosis and Pyroptosis focus on plasma membrane permeabilization

- Also,  why Pyroptosis is inflammatory (GSDMD pores) while Apoptosis is silent?
	- inflammation means a system: detecting PAMP or DAMP; then effector cells secrete cytokines and chemokines
	- So the key point is that, pyroptosis would cause membrane to be broken via GSDMD pores --> ==DAMPs will go out (like ATP, DNA)== --> altert to system 
	- But instead, apoptosis will let the cell die as a whole --> content contained in Apoptotic bodies --> cleaning up old cells, no response


## More about: complement proteins
- innate immunology system. they have the ability to activate in a domino-like chain reaction called a cascade --> enhance the ability of antibodies and phagocytic cells to clear microbes and damaged cells from an organism
#### Classical pathway
- After a antibody bind to bacteria 
	- Complement protien C1 bind to antibody
	- C4 binds to C1
	- C2 binds to  C4
	- C3 binds to C2 --> C3 split up, C3a moves away, C3b remains
	- C5b binds to C3b, C5a moves away
	- ...until C9
	- ==C3a and C5a== are chemotactic factor --> enhance inflammatory response
- MAC formation: membrane attack complex, formed by C5b, C6-C9, break off from the chain
	- Na+ and H2O flow into cell --> cause cell lysis
- So now C3b expose; macrophage bind to C3b with C3b receptor --> cause phagosytosis

#### Alternative pathway
- C3b bind to bacteria membrane antigen directly; followed by C5b, C6-9
- C5b-C9 can also form MAC and break off; C3b bind macrophage directly

#### Lectin pathway
- start with C4 bind to a kind of sugar on antibody; other no difference

## More about Toll-like receptor and interferon
- when the cell is damaged:
	- transcript factor IRF will activate the expression IFN(interferon)
	- IFN has three types
		- $\alpha$
		- $\beta$
		- $\gamma$
	- IFN $\alpha$ and $\beta$ can be released, to warn other cells to produce protein kinase R --> damage the RNA of virus --> prevent the infection of nearby health cells
- When macrophage get the signal of virus:
	- release IFN alpha and beta

