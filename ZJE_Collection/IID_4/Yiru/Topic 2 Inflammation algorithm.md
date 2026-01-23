- Learn 3.2, 10.2
- Review key point in Topic 1:
	- Innate immune system have two ports to detect different types of pathogens
	- TLRs (Toll-like receptors) --> detect things outside membrane --> release pro-inflammatory cytokines like TNF, IL-6
	- RLRs (RIG-I-like receptors) --> detect internal virus --> release Type I interferons, in antiviral state
- inflammasome Logic
	- in a word: the NLRP3 inflammasome requires a **Two-factor authentication** to fire, two-signals are reuqired
		- Signal 1: priming (**permission**)
			- Trigger: PAMPs hit TLRs
			- Process: NF-kB activation
			- Result: Transcription of the raw materials ==NLRP3== and ==Pro-IL-1$\beta$== produced
		- Signal 2: activation (**Execution**)
			- Trigger: cellular homeostasis breach
				- Main reason: Potassium efflux
				- others: ATP binding P2X7 channels, pore-forming toxins
			- Process: 
				- 1. K+ drops
				- 2. NLRP3 oligomerizes
				- 3. Recruits ASC (adaptor)
				- 4. Recruits Pro-Caspase-1
			- Result: form active ==Caspase-1== enzyme
	- Event: **pyroptosis**
		- Cytokine processing: ==Caspase-1== cleaves ==Pro-IL-1$\beta$ and Pro-IL-18== into active forms
		- Cell lysis: Caspase-1 cleaves GSDMD
			- The N-terminal of GSDMD punches pores in the cell membrane
			- Outcome: release of cytokines + cell death

- Non-Canonical inflammasome
	- Sensor changes: Caspase-11 in mice; Caspase-4/5 in human
	- Trigger changes: They detect intracellular LPS, bypassing TLR4
	- Outcome: still, cleave GSDMD and cause pyroptosis, and then activate NLRP3

- Regulation system
	- Inhibitor: Bile Acids
	- Pathway: TGR5 receptor --> cAMP --> PKA --> inhibit NLRP3
	- Process: PKA **phosphorylates NLRP3**, preventing it from assembling. This creates a "ubiquitination brake" .

### **Take home logic for exam:**

1. **Dependencies:** You can see `if self.primed == False: return`. This is the **Two-Signal Model**.
    
2. **Regulation:** You can see `if self.pka_active: return`. This is the **Bile Acid Checkpoint**.
    
3. **Pathology:** You can see `ORF3a` forcing the `assemble` function directly. This is **COVID-19** or other kind of virus that can trigger signal 2