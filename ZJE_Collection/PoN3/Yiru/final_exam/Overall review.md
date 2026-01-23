## Theme 1: Introduction and Synaptic plasticity

### Basic potential knowledge
#### Glutamate transmitter system
- ==Glutamate==
	- The primary excitatory neurotransmitter
- Glutamate transmission
	- Glutamate is packaged into vesicles in presynaptic terminals
	- After release, glutamate is primarily cleared (retake) by astrocytes through transporters
	- This astrocytic uptake is crucial for preventing over excitotoxicity
- Glutamate receptor![](https://i.imgur.com/pYRSdlW.png)
	- in Presynaptic terminals:
		- mGluRs and kainate receptors
			- as autoreceptors that modulate neurotransmitter
	- In Postsynaptic terminals:
	- NMDA receptors:
		- Slow rise and decay
		- high calcium permeability and voltage-dependent magnesium block
	- AMPA receptors:
		- fast rise and decay
		- AMPARs mediate most of the rapid excitatory synaptic signaling in the brain, responding to glutamate within milliseconds
	- At resting potential, NMDA receptors are blocked by Mg2+; initial slight stimulation activates AMPA receptors --> $Na+$ influx
	- Stronger depolarization removes Mg2+ block from NMDA receptors, and then NMDA allows both $Na+$ and $Ca^{2+}$ influx



#### Presynaptic release and synaptic plasticity
- Definition of Presynaptic release: is the process, a neuron releases neuotransmitters from synaptic vesicles into the synaptic cleft to communicate with another neuron.
- Presynaptic release is a primary target for ==synaptic plasticity ==mechanisms
	- Controlled by:
		- Calcium signaling: The primary trigger for vesicle fusion
		- Vesicle trafficking: Controls availability of release-ready vesicles
		- Modulatory systems: Fine-tune release probability
			- G protein coupleed receptors
			- autoreceptors: feedback control

>Synaptic strength of synaptic plasticity
- Amplitude = n x p x a
	- n = number of release sites
		- number of terminals or release sites
	- a = quantal amplitude
		- 是单个vesicle对于突触后神经元的影响
	- p = probability of release
		- determined by $Ca^{2+}$ and proportion of synapses with docked vesicles；均是正比关系
			- 什么是docked vesicle: near the membrane of presynaptic, ready to fuse and release
- This means the strength of a connection depends on how many release sites exist (n), how likely each is to release (p), and how strong each quantum's effect is (a)

> Paired Pulse ratios
- When you stimulate a neuron twice in quick succession, the second response is affected by the first
	- Paired pulse depression
		- If the first stimulus depletes available vesicles, the second response is smaller (depression)
	- Paired pulse facilitation
		- If the first stimulus leaves residual calcium, the second response is larger (facilitation)
- The p (inital state of release probability could be inferred from this ratio)

> Short-term plasticity (seconds to minutes)
- Facilitation occurs when calcium accumulates in the terminal, increasing release probability for subsequent stimuli
- Depression happens when readily-releasable vesicles are depleted, reducing probability temporarily
- ==Post-Tetanic potentiation==:
	- represents a longer-lasting enhancement of release after intense stimulation
	- during tetanus, calcium accumulation; after tetanus, residual calcium would increase probability of vesicle fusion

- How to detect these changes?
	- Paired-pulse experiments: Reveal initial state and short-term dynamics
	- Coefficient of variation analysis: Distinguishes pre vs. postsynaptic changes
	- Advanced imaging: Directly visualizes presynaptic function
	- Photon Glutamate Uncaging
		- Scientists use a special form of glutamate that's chemically "caged" (inactive) until exposed to light. 
		- Then **Two-photon excitation**: Using a special infrared laser that only activates the compound when two photons hit simultaneously
		- This creates a tiny activation spot (less than 1 micron - smaller than a single synapse)
		- If you induce LTP at a synapse and then:
			- Natural responses increase BUT uncaging responses don't change → presynaptic mechanism
			- Both natural AND uncaging responses increase → postsynaptic mechanism

> Long-term plasticity (hours to days)
- Presynaptic LTP/LTD can involve persistent changes in release machinery,calcium handling, or terminal size
- These changes alter the baseline probability of neurotransmitter release

- LTP: long term potentiation
	- NMDAR-dependent LTP
		- 1. **Initial activation**: High-frequency stimulation pre- and postsynaptic activity causes glutamate release from presynaptic terminals
		1. **AMPA receptor activation**: Glutamate binds to AMPARs, allowing Na⁺ influx and initial depolarization of the postsynaptic membrane
		2. **NMDA receptor unblocking**: The depolarization removes Mg²⁺ ions that normally block NMDA receptors at resting potential
		3. **Calcium influx**: With Mg²⁺ block removed, NMDA receptors allow Ca²⁺ entry into the postsynaptic cell
		4. **Calcium as second messenger**: The rapid rise in intracellular Ca²⁺ triggers several signaling cascades:
		    - Ca²⁺ binds to calmodulin, forming Ca²⁺/calmodulin complexes
		    - Ca²⁺/calmodulin activates CaMKII (calcium/calmodulin-dependent protein kinase II)
		    - CaMKII undergoes autophosphorylation at Thr286, becoming persistently active
		    - AMPA receptor move to membrane
	- LTP expression: maintain enhanced synaptic strength after LTP has been induced
		- related to postsynaptic modifications
			- increased AMPA receptor
		- unchanged paired-pulse ratio after LTP suggests that expression is primarily postsynaptic in classical NMDAR-dependent LTP.
	- ==Mossy Fibre LTP==
		- Different from NMDAR-dependent LTP
		- Presynaptic mechanism: depends on presynaptic $Ca^{2+}$ entry through voltage-gated calcium channels
		- cAMP-PKA pathway: Elevated Ca²⁺ activates adenylyl cyclase, increasing cAMP and activating PKA
		- Results in enhanced glutamate release rather than changes in postsynaptic sensiticity

- LTD: long term depression
	- synaptic weakening
	- crucial for information storage, memory refinement, and preventing network saturation.
	- NMDAR-dependent LTD
		- Induction with low-frequency stimulation, typically 1-5 Hz
		- Modest, prolonged elevation of intracellular $Ca^{2+}$ ; Lower $Ca^{2+}$ levels than LTP
		- This will cause: Activation of phosphatases, and cause dephosphorylation of AMPA receptors, and inhibition of CaMKII activity



## Theme 2: Inhibitory Synaptic transmission
- Why we need inhibition?
	- 1. precise control of action potential timing
		- like feedforward inhibition
	- 2. Preventing Pathological over-excitation
		- lack of inhibition would cause ==Seizures==
	- 3. modulating the impact of specific excitatory inputs
		- Inhibition can selectively dampen or gate certain excitatory pathways
	- 4. Enabling complex circuit operations like disinihibition
		- can inhibit other inhibition neurons

### GABA
- Glutamic Acid Decarboxylase(GAD) is a enzyme that can convert Glutamate into ==GABA==
	- GABA: primary inhibitory neurotransmitter in the central nervous system
	- reduce neuronal activity (calming effect)
- Two types of Synapses
	- Excitatory Synapses
		- presynaptic neuron: glutamatergic neurons
		- Postsynaptic neuron
	- Inhibitory synapses
		- Presynaptic neuron: ==GABAergic neurons==--> synthesize GABA
		- GABA then transported into synaptic nesicles, and this packaging is mediated by Vesicular GABA transporter (VGAT)
		- Then release into the synaptic cleft
- When a GABAergic neuron fires an action potential, the depolarization of the presynaptic terminal triggers the influx of $Ca^{2+}$ --> GABA release to cleft
### Reversal potential
- Represent a balance between the electrical gradient and the chemical concentration gradient
- The reversal potential for an ion is the membrane potential at which there is no net flow of that ion across the membrane, even if channels permeable to it are open.
**GABA-A Receptors: Fast, Direct Chloride-Mediated Inhibition**

- **Type:** GABA-A receptors are **fast-acting, ligand-gated ion channels**, also known as ionotropic receptors.
    
- **Mechanism:** When GABA binds directly to the GABA-A receptor, the integral ion channel opens. This channel is primarily permeable to **chloride ions (Cl⁻)**.
    
- **Role of KCC2 and Chloride Gradient:** In mature neurons, the **K⁺-Cl⁻-cotransporter (KCC2)** actively pumps Cl⁻ ions **out of the cell**. This action maintains a **low intracellular Cl⁻ concentration**, setting the reversal potential for chloride (E_Cl) at a value typically more negative than the action potential threshold (and often near or slightly more negative than the resting membrane potential).
- **Effect of Activation:**
    - Because intracellular Cl⁻ is kept low by KCC2, when GABA-A receptors open, Cl⁻ ions flow **into the cell** down their electrochemical gradient.
    - This influx of negatively charged Cl⁻ ions generates an **Inhibitory Postsynaptic Current (IPSC)**.
    - The IPSC leads to an **Inhibitory Postsynaptic Potential (IPSP)**, where the inside of the neuron becomes more negative (hyperpolarization) or is "clamped" near E_Cl, making it harder for the neuron to reach the threshold for firing an action potential. IPSPs (voltage changes) are measured using current clamp electrophysiology.
    - This results in rapid inhibition.
- ### Shunting inhibition
![](https://i.imgur.com/u6jKPWi.png)
- If AMPA and GABA-A open together: the EPSP caused by AMPA would be shunting inhibited by GABA-A
	- lower potential, because the potential would be used to resist GABA-A IPSP
	- GABA-A offer a existing path for positive channel moved from AMPA to leave

---
**GABA-B Receptors: Slow, G-Protein Mediated Potassium-Dependent Inhibition**
- **Type:** GABA-B receptors are **metabotropic receptors**, specifically **G_i/o protein-coupled receptors (GPCRs)**. They mediate slower and more prolonged inhibitory effects.
- **Mechanism:**
    1. Unlike GABA-A receptors, GABA-B receptors do not form an ion channel themselves.
    2. When GABA binds, the receptor activates an associated **G protein** located on the inner surface of the cell membrane.
    3. The activated G protein splits into its subunits (Gα_i/o and Gβγ).
    4. These subunits then interact with downstream effector proteins.
- **Effect of Activation (Postsynaptic):**
    - A primary postsynaptic effect involves the **Gβγ subunit directly activating G-protein-gated inwardly rectifying K⁺ (GIRK) channels** (as depicted in the image).
    - Since K⁺ concentration is much higher inside the cell than outside, opening these channels allows **K⁺ ions to flow outwards**.
    - This efflux of positive charge causes the membrane potential to move towards the very negative K⁺ reversal potential (E_K), resulting in **hyperpolarization** and a slow IPSP.

- **Slower Time Course:** The multi-step cascade (GABA binding → G protein activation → subunit dissociation → subunit interaction with effector/channel) means that the onset of GABA-B receptor effects is significantly slower (tens to hundreds of milliseconds) and longer-lasting (seconds) compared to the immediate response of GABA-A receptors.
- **Other Effects (Presynaptic & Biochemical):** GABA-B receptors can also be located presynaptically where Gβγ can inhibit Ca²⁺ channels, reducing neurotransmitter release. The Gα_i subunit can inhibit adenylyl cyclase, reducing cAMP levels and modulating cellular functions over longer timescales (as suggested by the adenylyl cyclase part of your image).
![](https://i.imgur.com/mF91Cmp.png)
![](https://i.imgur.com/3Rk4iZm.png)

### MODEL of GABAergic Neurons
- Principal Cells:
	- The main output neurons of a specific brain region.
	- They collect and process information within their area and then send signals out to other brain regions
- Interneurons
	- These neurons make connections within the same brain area. 
	- Can inhibiting bearby principal cells or other interneurons
	- GABAergic Nature: Many, if not most, interneurons are GABAergic. They are crucial for shaping the activity patterns within a brain region, preventing over-excitation, and refining signals.
- **Forms of inhibition**![](https://i.imgur.com/x4nQRcA.png)
	- 1. **Feedforward Inhibition (Top-Left in image):**
	    - **Mechanism:**
	        1. An incoming excitatory signal (e.g., from another brain area) arrives.
	        2. This signal splits: one branch excites the main target neuron (e.g., a principal cell).
	        3. The other branch excites an inhibitory interneuron.
	        4. This interneuron then quickly fires and inhibits the same main target neuron that just received the direct excitation.
	    - **Effect:** This creates a narrow window of opportunity for the target neuron to fire. The initial excitation might make it fire, but the subsequent inhibition quickly shuts it down or prevents prolonged firing. It helps to make the timing of neuronal responses more precise
	    - **Image:** The input (blue arrow) activates both the Excitatory cell (E, in black) and the Inhibitory cell (I, in red). The I cell then inhibits the E cell.
	- 1. **Feedback Inhibition (Top-Right in image):**
	    - **Mechanism:**
	        1. A target neuron (e.g., a principal cell) becomes active and fires.
	        2. This firing excites a nearby inhibitory interneuron.
	        3. The activated interneuron then fires and sends an inhibitory signal back to the original target neuron (or a population of similar neurons).
	    - **Effect:** This acts like a negative feedback loop. "Such inhibitory neurons are beneficial for preventing over-excitation and maintaining network stability." It helps to prevent runaway excitation, dampens activity after a neuron has fired, and can contribute to generating rhythmic activity.
	    - **Image:** The E cell activates the I cell, which then inhibits the E cell.
	- 3. Tonic inhibition
		- provides a constant background level of inhibition, setting the overall excitability
		- **Extracellular GABA:** There's a low, ambient concentration of GABA present in the space outside of synapses.
		- **Extrasynaptic Receptors:** Neurons have GABA-A receptors located outside the synaptic cleft (extrasynaptic) that are highly sensitive to GABA. These receptors bind to the ambient GABA.
		- **Image:** Shows ambient GABA molecules (small dots) influencing the neuron, representing this constant background inhibition.
	- 4. Lateral Inhibition
		- When one neuron (or a small group of neurons) becomes highly active, it activates inhibitory interneurons that then suppress the activity of adjacent, less active neurons.
		- This mechanism sharpens the representation of sensory information by making the "winner" (most active neuron) stand out more clearly against its "quieter" neighbors. 

### Interneuron: cell types and diversity
- Different brain region have different interneuron subtypes
- Where should the inhibitory synapses be?
	- Synapses on dendrites: modulate the integration of excitatory inputs
	- Synapses on distal dendritic 
	- Synapses on soma and proximal dendrites: basket cells

##### Fast-spiking cell
- are major class of inhibitory interneurons, and their electrophysiological property is:
	- their ability to fire action potentials at very high frequencies with little or no slowing down (adaptation).
		- 1. Have a relative low threshold for firing an action potential --> ready to be fired
		- 2. Faster repolarization: FS cells have specific types of potassium channels, notably **KV 3.1 channels**. 
			- When the cell depolarizes, these channels open quickly allowing K+ ions to rush out, rapidly repolarizing the membrane
- Fast-spiking interneuron-Mediated IPSCs (inhibitory postsynaptic currents) have fast kinetics
	- When an FS cell releases GABA onto a target neuron, the resulting inhibitory current is rapid in its onset and decay
-  ![](https://i.imgur.com/Ap8Ld9z.png)

##### Preventing runaway excitation
- Short-term plasticity
	- Paired-Pulse depression 
		- If an interneuron has a high initial probability of releasing GABA, repeated activation might lead to less GABA release per action potential
	- Paired-pulse facilitation
		- If an interneuron has a low initial probability of release, repeated activation can lead to more GABA release (e.g., due to residual calcium buildup). Interneurons with facilitating inputs become stronger as network activity increases.
- Two type of cell types
	- Parvalbumin (PV) basket cells
		- Inhibitory interneuron
		- Provide a **fast, strong, immediate brake** on network activity. Their high initial release probability ensures a rapid and potent inhibitory effect.
		- Often have P/Q-type Ca2+ channels and nanodomain signaling, leading to fast, reliable, and often depressing or robust (non-facilitating) synapses. They are good for strong, fast feedback inhibition.
	- Cholecystokinin(CCK) basket cells
		- Provide a **more graded and building form of inhibition** that strengthens as network activity persists or increases.
		- Prevent hyper-excitation
##### Disinhibition:
- Example : Long-range inputs (e.g., from motor cortex M1 to somatosensory cortex S1) can preferentially activate **VIP (Vasoactive Intestinal Polypeptide)-containing interneurons.**
	- VIP interneurons often target other interneurons, particularly SST-containing interneurons (which, as we saw, target dendrites).
	- So, M1 activates VIP cells in S1 → VIP cells inhibit SST cells in S1 → SST cells are less able to inhibit the dendrites of S1 principal cells → dendrites of S1 principal cells are disinhibited and more responsive to other excitatory inputs
## Theme 3: Leaning and memory
### Categorize memories
**A. By Content & Conscious Awareness (Qualitative Classification)**
    1.  **Declarative Memory (Explicit Memory):**
        *   **Definition:** Memories that can be consciously recalled and "declared" (facts, events).
        * Like episodic memory:情景式的
        * Which could be expressed easily
    2.  **Non-Declarative Memory (Implicit/Procedural Memory):**
        *   **Definition:** Memories expressed through performance without conscious awareness or recollection.
        - Which is more likely to be performed instead of expressed
**B. By Duration (Temporal Classification)**
    3.  **Immediate Memory:**
        *   **Duration:** Fractions of a second to seconds.
        *   **Characteristics:** Large capacity, rapid decay without attention.
    4.  **Short-Term Memory (STM):**
        *   **Duration:** Seconds to minutes.
        *   **Characteristics:** Limited capacity, requires rehearsal for maintenance.
        *   **==Working Memor==y (a key component/type of STM):**
            *   **Definition:** Actively holding and manipulating information to plan and carry out behavior (e.g., mental arithmetic, following complex instructions).
            *   **Putative Location:** Medial Prefrontal Cortex (mPFC) involvement
    5.  **Long-Term Memory (LTM):**
        *   **Duration:** Days to years, potentially a lifetime.
        *   **Characteristics:** Vast capacity, relatively stable but can be modified.
        *   **mPFC Role:** Also involved in the recall of remote (older) long-term memories (Lee et al., 2022).
### Structural brain, causing declarative memory
**A. Key Anatomical Structures:**
    1.  **Medial Temporal Lobe (MTL):** A collection of structures crucial for declarative memory formation.
    2.  **Hippocampus (within the MTL):**
        *   **Overall Role:** Essential for forming new declarative memories (especially episodic) and spatial navigation.
        *   **Internal Circuitry:** e.g., The "Trisynaptic Loop" (EC → DG → CA3 → CA1).
        *   **Subregions (Cornu Ammonis - CA):** Involved in binding elements of an experience, conscious recollection.
        *   **Debate on LTM storage:**
            *   *Standard Model of Systems Consolidation:* Hippocampus is temporary for LTM; memories eventually become independent and stored in the cortex.
            *   *Multiple Trace Theory:* Hippocampus is always needed for recalling detailed episodic LTMs.
    3.  **Entorhinal Cortex (EC) (gateway to the Hippocampus):**
        *   **Medial Entorhinal Cortex (MEC):** Contains **Grid Cells** (fire in hexagonal patterns creating a "cognitive map" for spatial navigation).
        *   **Lateral Entorhinal Cortex (LEC):** Processes multisensory information (olfactory, visual etc.), coding contextual elements for episodic memory.
    4.  **Dentate Gyrus (DG) (within the Hippocampus):**
        *   **Primary Role:** Critical for **Pattern Separation** (distinguishing similar memories).
        *   **Unique Feature:** Site of **Adult Neurogenesis** (birth of new neurons in adulthood).
### Cellular and network mechanisms
**A. Neural Plasticity: The Brain's Ability to Change**
    1.  **Concept (Santiago Ramon y Cajal, 1890s):** Learning involves changes in the connections between neurons.

**B. Engrams: The Physical Trace of Memory**
    2.  **Definition:** The hypothetical physical/biochemical change in the brain that represents a memory.
    3. Preferential allocation: Neurons with higher excitability at the time of learning are more likely to become part of engram for that memory
    4.  **Mechanism:** Involves specific populations of neurons ("engram neurons") activated during learning and reactivated during recall. Linked to dendritic spine changes.
    5. Silencing them prevents recall, and activating them can trigger recall 

**C. Specialized Cells for Spatial Memory & Navigation:**
    1.  **Place Cells (in the Hippocampus):**
        *   **Discovery:** O'Keefe & Dostrovsky, 1971.
        *   **Function:** Fire when an animal is in a specific location ("place field"), contributing to a "cognitive map."
        *   **Stability:** GABAergic CA1 place cells can be more stable than glutamatergic ones across context changes.
    2.  **Grid Cells (in the Medial Entorhinal Cortex):**
        *   **Function:** Fire in a hexagonal pattern as an animal navigates, providing a metric for space.
        *   **Interaction:** Input from grid cells likely contributes to the formation of place fields in the hippocampus.

**D. Pattern Separation (in the Dentate Gyrus):**
    1.  **Function:** The ability to distinguish between similar inputs or experiences, encoding them as distinct memories. Prevents interference.

**E. Adult Neurogenesis (in the Dentate Gyrus):**
    1.  **Function:** The birth of new neurons in adulthood, potentially contributing to learning, pattern separation, and memory flexibility.
### The influence of sleep on memory
A.  **Consolidation Enhancement:** Sleep plays a critical role in strengthening and reorganizing memories.
B.  **Key Processes During Sleep:**
    1.  **Memory Reactivation/Replay:** Neural patterns of recent experiences are replayed in the hippocampus and prefrontal cortex.
    2.  **Context Generalization:** Sleep can help generalize learned responses (e.g., fear) to similar contexts.
    3.  **Synaptic Plasticity Modulation:** Sleep oscillations (e.g., slow waves, spindles) coordinate changes at synapses, refining memory traces.
    4.  **Experience-Driven Maturation:** The efficiency of sleep-dependent consolidation can improve with experience.

### Attention and emotion
- Where cause attention
	- The medial prefrontal cortex in rodents
	- The dorsolateral prefrontal cortex in human 
	- Related to ==working memory ==(holding and manipulating information relevant to the current task); and preparatory attention (preparing to focus on an upcoming stimulus or task) 
- 
- Neuronal correlates of attention
	- 1. Changes in firing rates
		- **Increased Firing:** Neurons representing attended locations, features, or objects generally show increased firing rates.
		- **Decreased Firing (Suppression):** Neurons representing unattended locations or features can show decreased activity.
	- 2. Attractor networks
		- Attention might involve neural networks shifting from labile sates to stable attractor states
		- In these stable states, the "winning" neuronal population (representing the focus of attention) shows increased firing, while "losing" populations (representing unattended stimuli) show decreased firing.
- Attention related neurotransmitter
	- 1. Acetilcholine, Ach
		- Role: Arousal, attention, learning, memory.
		- Increased Ach can improve attention
		- Essential for spatial working memory
	- 2. Dopamine (DA)
		- Role: Reward signaling, decision-making, spatial working memory, spatial attention, target selection.
		- Clinical relevance: ADHD, schizophrenia, Parkinson's 
	- 3. Noradrenaline, NA
		- More complex; In PFC region, involved in top-down control, attention, working memory via α2 receptors in PFC
		- In sensory cortex, involved in bottom-up state control
	- 4. Serotonin (5-HT)
		- Role: Learning, memory, executive functioning.
		- Reduced 5-HT could impair LTM and decision-making but may enhance focused attention and not affect working memory
- Attention deficit
	- Caused by inherited effects and environment
- Bottom-Up attention: External stimulus
	- Fast, from senses
	- Automatic
- Top-down attention: internal goals and intentions
	- Goal-directed
	- From mind downwards

### Brain waves
![](https://i.imgur.com/8036pK7.png)
- From fastest wave to slowest wave:
	- ==Gamma==: binding and peak performance wave; fastest frequency, associated with high-level information processing, intense focus, and the binding of sensory information into a coherent perception
	- ==Beta==: the active& alert wave; Associated with **active wakefulness, alertness, focused attention, and active thinking/problem-solving.**
	- ==Alpha==: The relaxed and reflective wave; Characterizes a state of relaxed wakefulness, often with eye closed, reduce sensory processing
		- bridge between active thought and deeper relaxation/drowsiness
	- ==Theta==: memory wave; Associated with **drowsiness, light sleep (including REM sleep), deep relaxation, and processes like memory consolidation and creative insight.**
	- ==Delta==: deep sleep and restoration wave; Slowest frequency, dominant during **deep, dreamless (non-REM) sleep, essential for physical restoration and healing.**

### Limbic system
Contains:
- Amygdala: fear and emotion center
- Hypothalamic nuclei: Homeostasis
- Olfactory bulb: smell
- Septal nuclei: emotional related
- Nucleus accumbens: reward, motivation
- hippocamapl formation: memory
- Cingulate cortex: emotional processing, motivation, decision-making
- Areas of basal Ganglia
- Ventral tegmental area (VTA): reward, motivation
- Limbic midbrain areas: pain modulation, defensive behaviours

- Focusing on Amygdala
	- Kluver-Bucy syndrome, loss of amygdala will cause loss of emotional reactivity hypersexuality, oral fixation
	- Key subnuclei:
		- Lateral nucleus (LA)
			- Receives sensory input from thalamus and cortex
			- Process realtionship of events
		- Basolateral Nucleus (BLA)
			- Regulates behavioral and physiological responses to stress
			- Composed mainly of glutamatergic projection neurons and GABAergic interneurons
		- Central Nucleus (CE)
			- Crucial for physiological responses to stressors (fearful stimuli, stress, drug-related stimuli)
			- Outputs from LA project here to drive fear responses.

## Theme 5: Development and neurodevelopmental disorders
### Critical periods in brain development
- A discrete period of time during development when normal sensory experience is required for the brain to develop properly
	- Sensitive period for experience-dependent brain development
	- Example: brain visual development is about from 6 months to about 5 years of age. Normal visual input during this time is crucial for the development of visual pathways
##### ocular dominance plasticity
- A key model for studying critical periods, particularly in the visual cortex. 
- It refers to the change in neuronal responses in the visual cortex to input from one eye relative to the other due to ==altered visual experience==
- Key: shift in ocular dominance; if one eye is deprived of normal input during the critical period, the synapses carrying signals from that eye waken, while synapses from the open eye may strengthen
- ![](https://i.imgur.com/Nhz8g6H.png)
- Role of ODP:
	- Related to LTD of the synapses connected to the deprived eye
	- ODP results in LTD, blocking LTD blocks ODP
	- ==Recording techniques==
		- Single unit extracellular recordings: allow for many individual recordings to assess neuronal firing
		- Calcium fluorescence imaging: enables continuous recording from the same cells over time 
		- Visually-evoked potentials (VEPs): measure electrical responses in the brain to visual stimuli

#### Role of GABAergic inhibition in timing critical periods
- Development shift in GABA action: in young age of animal, GABA neurotransmitter can be somehow excitatory
- The maturation of GABAergic inhibition is a key factor defining the timing (opening and closing) of critical periods.
	- **Chloride Reversal Potential:** Changes from depolarized (excitatory) in young neurons to more hyperpolarized (inhibitory) in mature neurons
- The time of inhibition development should be 'just right'

#### **Metaplasticity:** 
The "plasticity of plasticity." Changes in the brain that alter its capacity for subsequent synaptic plasticity.
- **Example:** Dark rearing can shift the balance of plasticity towards potentiation (LTP). This might be related to changes in NMDA receptor subunit composition (e.g., a reduction in GluN2A-containing NMDARs).
    - **NMDA Receptors:** Composed of different subunits (e.g., GluN1, GluN2A, GluN2B). The subunit composition affects receptor properties and can change during development and with experience.

### Neurodevelopment disorders: schizophrenia and epilepsy
- Network oscillations
	- **Synchronized activity:** Neural oscillations are rhythmic, synchronized patterns of electrical activity across populations of neurons.
	- IPSPs can synchronize firing: 
		- Before IPSP: individual neurons in a population will tend to fire more asynchronously 
		- After small IPSP:
			- Can reset and delay with inhibition effects
	- How inhibition synchronizes
		- ING, interneuron Gamma
			- In a group of interneuron, they would auto- and intra- regulation to be sybchronized
		- PING, Pyramidal-interneuron Gamma
			- Excitatory pyramidal cells (+) fire, exciting inhibitory interneurons (-).
			- These interneurons then fire and broadly inhibit the pyramidal cells.
			- As the inhibition wears off, the pyramidal cells recover and become more likely to fire again, restarting the cycle.

##### 1. Schizophrenia
- One of the most common serious mental health conditions, 
- Hallucinations, delusions; speaking little, lack of pleasure in life
- Cognitive symptoms
	- Poor executive function
	- Trouble focusing
	- Working memory deficit
- Remove PV induces Schizophrenia
- Parvalbumin-containing (PV) interneurons  seems to be impaired in Schizophrenia case
	- PV responsible for feedforward inhibition
	- reduction in PV +ve neurons: physically fewer PV interneurons
	- reduction in PV +ve boutons: Boutons are the presynaptic terminals where neurotransmitters (in this case, GABA from PV neurons) are released. A reduction in PV-positive boutons means that even if the PV neuron cell bodies are present, their ability to form synaptic connections and release GABA onto target neurons is compromised.
	- reduction in GABA-A receptor
		- targeted by PV interneurons
	- NMDAR hypofunction may act via PV interneurons
		- NMDA receptors are glutamate receptors for excitatory neurotransmission and synaptic plasticity. PV interneuron contains NMDA receptors
		- When NMDA hypofunction
			- PV interneurons receive less excitatory drive from principal neurons or other excitatory inputs.
			- This reduced excitation leads to decreased firing of PV interneurons.
			- Consequently, PV interneurons release less GABA
- PV containing basket cells, fire on every cycle of gamma oscillation 
	- drive high-frequency oscillations like gamma
- ==**Synchronizing gamma oscillations are impaired in schizophrenia:**==
	- **Clinical Relevance:** This is a critical link. The evidence you listed previously (reduced PV neurons, boutons, GABAA α1 receptors, NMDAR hypofunction affecting PV cells) all point to a deficit in PV interneuron function.
##### 2. Epilepsy seizure
- Definition: abnormal excessive or synchronous activity in the brain
- Main cause: lack of inhibition while too much excitation
	- can be induced by glutamate agonists
	- May be caused by:
		- Mutations in GABA-related genes --> GABA dysfunction
		- Changes in GABA in non-genetic epilepsy
		- GABA-A receptor mutations
- Initial epilepsy seizure would lead to more seizure
	- Initial seizure reduce KCC2 expression 
	- KCC2 is responsible for the exclude Cl from cell-->keep Cl- level in a lower level 
	- So if lack of KCC2, intracellular Cl- level would increase, so GABA will somehow become a less inhibitory or even excitatory neurotransmitter--> more likely to over excitation
## Theme 6: Neurodegeneration
- Definition: Progressive loss of nerve structure and function
- Misfolded proteins is a big problem
	- Alzheimer's disease
		- Neurofibrillary tangles (tau)
		- Amyloid plaques
	- Parkinson's disease
		- Lewy body 
	- Amyotrophic lateral sclerosis
		- TDP-43 inclusion body (TDP-43 protein)
	- Prion disease
		- Prion plaque
	- Huntington's disease
		- huntington inclusion body (Huntingtin)
#### 1. Alzheimer's disease
Defined by brain deposition of ==numerous amyloid plaques== and ==neurofibrillary tangles== 
- Neurofibrillary tangles: aggregation of tau protein
	- Tau was hyperphosphorylated
- Based on different variant of AD, can have multiple syndromes

- Amyloid-beta: cleaved from Amyloid precursor protien (APP)
- Microtubule-Associated protein Tau
	- have 6 isoforms, but contribute to AD tau aggregates equally
##### AD's biomarkers
###### 1. PET: Positron emission 
- PET is a non-invasive imaging tech
![](https://i.imgur.com/cmfhDly.png)

- using radioactive compounds that bind fibrillary Aβ or tau.
###### 2. Cerebrospinal Fluid (CSF) biomarkers
CSF is collected via lumbar puncture and provides direct insight into brain biochemistry:

- **Amyloid-β42**: Decreases in CSF as it accumulates in brain plaques
- **Total tau and phosphorylated tau**: Increase with neuronal damage and tangle formation
- **Aβ42/Aβ40 ratio**: Improves diagnostic accuracy over Aβ42 alone
- **Neurofilament light chain (NfL)**: Indicates neuronal damage (though not specific to AD)
###### 3. Blood biomarkers
Recent advances have enabled less invasive blood tests:

- **Plasma p-tau181 and p-tau217**: Highly specific for AD pathology
- **Plasma Aβ42/Aβ40 ratio**: Correlates with brain amyloid burden
- **Plasma NfL**: Reflects neurodegeneration but isn't AD-specific
- **GFAP (Glial Fibrillary Acidic Protein)**: Indicates astrocytic activation
##### Neuropathological phases of amyloid-β deposition in AD
- Thal phase
	- Thal phase 1: basal temporal and orbitofrontal neocortex
	- Thal phase 2/3: throughout the neocortex, amygdala ... most section of brain
	- Thal phase 4/5: mesencephalon, lower brainstem, and cerebellar cortex
- Braak stages
	- Braak stage I/II: near locus coeruleus
	- Braak stage III/IV: hippocampal formation and ome parts of neocortex
	- Braak stage V/VI: large parts of the 
![](https://i.imgur.com/xae00p9.png)

##### Cause of AD
- Key factor: ==the accumulation of A$\beta$ ==is a critical, early, and causal event in the cascade of pathological changes that lead to Alzheimer's disease
- Mutations in Familial AD
	- 1. APP (Amyloid precursor protein) mutaiton
		- APP gene is located on Chromosome 21, and the mutations happen near the secretase cleavage sites
		- This will increase the production of A$\beta$
	- 2. PSEN1 and PSEN2 genes
		- Similar to APP mutations, these mutations directly lead to an increased production of the Aβ42 peptide
- Down Syndrome with early onset AD
	- they have three copies of APP gene so have more A$\beta$
- For those late-onset AD (not Familial AD)
	- ApoE ε4 allel as a major risk factor 
	- ApoE is involved in cholesterol transport but also plays a role in Aβ aggregation and clearance. ApoE  ε4 is a kind of less effective form of ApoE so may cause aggregation

#### 2. Parkinson's disease
- Primary cause: the death of dopamine neurons in a midbrain
- PD affects movement control, and the symptoms include shaking, rigidly, slowness, and difficulty with walking

- Key protein disorder: ==Lewy bodies==
	- The main protein componenet of Lewy bidy is alpha-synuclein; misfolded alpha-synuclein will aggregates to form these insoluble Lewy 
- Body first and brain-first PD:
	- Braak stage of PD
		-  ![](https://i.imgur.com/5nY2ezN.png)
	- Developing from down to up brain: 
		- From enteric nervous system (nervous system of the gut); synuclein detection of skin is positive
	- Developing from brain to body:
		- From olfactory buld; synuclein detection of skin is negative
- Mitochondial dysfunction is a core mechanism in PD
	- **Mutations:** Loss-of-function mutations in PINK1 or Parkin impair this quality control system. Damaged, dysfunctional mitochondria accumulate, leading to oxidative stress, energy deficits, and neuronal death, particularly in vulnerable dopamine neurons. This is a major cause of early-onset, recessive PD.

##### Treatment of Parkinson's disease
- 1. L-DOPA, the precurosor of dopamine: repleace the dopamine. 
- 2. Deep brain stimulation (DBS): Continuous high-frequency electrical stimulation is delivered to basal ganglia targets --> improve motor performances
- 3. Cell-replacement therapy: To replace the lost dopamine neurons with new healthy ones; 
	- Transplanting fetal dopaminergic precursor cells, or more recently, dopamine neurons derived from embryonic stem cells (ESCs) or induced pluripotent stem cells (iPSCs), into the striatum


#### 3. Prion disease
- The disease is caused by Prion protein
	- The Prion protein undergoes a misfolding event, and become insoluble --> will aggregation (PrP_sC)
- ==Protein-induced propagation==: once a abnormal prion protein form, it can convert more and more normal prion protein into abnormal form.
- **Pathological Consequences:** The accumulation of these misfolded, aggregated PrP<sup>Sc</sup> proteins leads to:
    - Neuronal dysfunction and death.
    - Formation of amyloid plaques (in some prion diseases).
    - Spongiform encephalopathy (the brain develops a characteristic sponge-like appearance due to the formation of numerous tiny holes, or vacuoles, in the tissue).
    - Progressive and invariably fatal neurodegeneration.
##### Disease model with prion-like disease
- Shared mechanics: Protein conformational change, which could cause misfolding; and further, this could lead to aggregation
- Like AD, PD, Prion disease: Can build animal model with lab-made aggregated protein seeds to lead disease development

- Detection of disease-specific misfolded proteins
	- Real-time quaking-induced coversion (RT-QulC)
		- **disease-specific misfolded protein "seeds" (like prion protein, alpha-synuclein, or tau) in patient samples** (e.g., cerebrospinal fluid) by amplifying them through seeded aggregation.

#### 4. Huntington's disease
- Cause: an expansion of CAG trinucleotide repeat in exon 1 of the Huntingtin gene (HTT)
	- lead to an abnormally long polyglutamine (polyQ) tract in the huntingtin protein
- Mutated huntingtin protein would misfold, and aggregate
- **Mechanism of Toxicity (PolyQ):**
    - **Gain-of-Function:** The expanded polyQ tract confers new, toxic properties on the huntingtin protein.
    - **Loss-of-Function:** The normal functions of the huntingtin protein (which are important for neuronal health, e.g., in intracellular transport, transcription) might also be impaired.
    - **Disruption of Interacting Proteins:** The expanded polyQ tract can abnormally interact with a multitude of other cellular proteins, disrupting their normal functions. This explains why different polyQ diseases (caused by polyQ expansions in different genes) have different symptoms – the specific "host protein" context matters.

#### 5. Amyotrophic lateral sclerosis
- Cause is not clear
- Pathology: selective motor neuron degeneration
- Key related genes
	- TDP-43: In ALS conditions, both mutant and wild-type TDP-43 accumulate in cytoplasmic inclusion bodies. (aggregation)


## Theme 7: Motor and sensory neuroscience
- All sensory system shared common tasks
	- sensory stimuli --> electrical signals
	- Optimization of detection
### Visual system
##### Eye and retina
- Retina has a layerd structure with specific cell types in each layer
- The eye projects the visual scene onto the retina’s photoreceptors
	- Light activates rhodopsin-->G-protein signaling --> decraese of cyclic-GMP level
	- --> hyperpolarize the photoreceptors, reducing glutamate release
![](https://i.imgur.com/F2NWPFK.png)

- How do Rods and cones detect light signals
	- Light activates rhodopsin (a kind of G-protein-coupled receptor)
	- This will cause greater amplification of the phototransduction cascade, and are used mostly for ==night vision==
	- Cones recover more rapidly and have a larger adaptation range, and serve daylight vision and motion vision
	- The presence of different kinds of cones with opsins that confer different spectral sensitivities-- short-, medium- and long- wavelength for trichromatic primates including humans, enables color vision

- Two types of cells in receptive fields: OFF and ON bipolar cells
	- Light --> Hyperpolarization cones --> less glutamate release
		- --> ==ionotropic glutamate recepto==r is less active --> fewer cations enter bipolar cell --> OFF biplolar cell is hyperpolarized
		- --> Metabotropic glutamate receptor is less active --> inhibitory G proteins are less active --> cation channels are less inhibited--> ON bipolar cell is depolarized
	- Bipolar cells acquire their center–surround receptive field through lateral inhibition of horizontal cells

Light → Photoreceptor Hyperpolarization (↓Glutamate) →  
1. **Direct Pathway (Center):**  
* → **OFF Bipolar:** (Ionotropic GluR) → Hyperpolarization (if light) → Modulates Glutamate release to OFF-Center RGC  
* → **ON Bipolar:** (Metabotropic GluR6) → Depolarization (if light) → Modulates Glutamate release to ON-Center RGC  
2. **Lateral Pathway (Surround via Horizontal Cells):**  
* Photoreceptors also modulate Horizontal Cells → Horizontal Cells provide inhibitory feedback to (surround) photoreceptors (and sometimes directly to bipolars) → This feedback antagonizes the center response.

### Movement Control
##### Management system: Hierarchy of control
- The highest level: think and plan
	- Neocortex
	- Basla ganglia
- The middle level: tactics and execution
	- Motor cortex and cerebellum
- Lowest level: execution and local operation
	- Brainstem
	- Spinal cord
##### Movement with mucle and neuron
- Key components for arm movement
	- the joints
	- skeletal muscles
	- nerves: transmit signals from the brain and spinal cord to muscle
- **Motor Neurons: The Messengers**
    - **Lower Motor Neurons (LMNs): The "Front-Line Workers"**
        - **Location:** Cell bodies in the anterior horn of the spinal cord or brainstem cranial nerve nuclei.
        - **Job:** Their axons project directly to skeletal muscles, forming **neuromuscular junctions**. When an LMN fires, the muscle fibers it connects to contract. They are the final common pathway for all motor commands.
    - **Upper Motor Neurons (UMNs): The "Supervisors"**
        - **Location:** Cell bodies in the motor regions of the cerebral cortex or brainstem.
        - **Job:** They control the LMNs. They send signals down to the LMNs (or interneurons that connect to LMNs) to initiate, modify, or stop movement.

##### Motor units and motor pools
- Alpha motor neurons
	- LLMs
	- ==Motor Units==: ONE alpha motor neuron + ALL the muscle fibers it innervates. This is the elementary component of motor control. Small motor units (few fibers per neuron) allow for fine control
	- **Motor Neuron Pool:** The collection of ALL alpha motor neurons that innervate a single muscle.

- Gamma motor neurons
	-  They adjust the tension of intrafusal fibers. This doesn't cause major muscle contraction for movement but is crucial for **regulating the sensitivity of muscle spindles**.

- Alpha-Gamma Coactivation
	- During voluntary movements, both alpha and gamma motor neurons are activated simultaneously. Alpha neurons cause the main muscle (extrafusal fibers) to contract, and gamma neurons cause the intrafusal fibers within the spindle to contract.
	- Spindle can detect the changes in muscle length
### Automatic response of reflexes
- Myotatic reflex (Stretch reflex): like knee-jerk
	- 1. Sudden stretch of a muscle (e.g., tapping the patellar tendon stretches the quadriceps).
	1. Muscle spindles in the stretched muscle are activated.
	2. Sensory neurons from the spindle send a signal directly to the spinal cord.
	3. In the spinal cord, these sensory neurons make a **monosynaptic** (single synapse) connection with alpha motor neurons that innervate the same muscle.
	4. The alpha motor neurons are activated, causing the stretched muscle to contract.
	- ==To resist sudden stretching (lengthening) of a muscle and help maintain muscle tone and posture.==
- Reciprocal inhibition
	- only one of Flexor and extensor would contract, and another one must relax
	- Inhibitory interneurons would prevent the contraction of antagonist muscle
- Withdrawal reflex 
	- Immediate response to pain: step on pin and then motor fibers in several segments are activated, so lift foot off to pin
- Crossed-extensor reflex
	- Maintain balance, after withdrawal reflex
	- While one foot withdraws from pain, the other one must support the body, so the signal would cross to the opposite side of spinal cord

##### Controling motor systems
- Cortical neurons send axonal projections via multiple tracts to various brain regions
- ==Pyramidal system==
	- Contain Corticospinal tracts
	- Responsible for voluntary, skilled movements
- Extrapyramidal system
	- Rubrospinal and tectospinal tracts, among others
	- Controls posture, muscle tone and automatic movements
### Movement disorders
- Basal ganglia
	- Help to facilitate movement that are required, and inhibit unwanted movement
- Two pathways of modulation of  basal ganglia
	- Direct Pathway: MSIT, more motor activity in movement
		- M: Motor cortex
		- S: Striatum
		- I: Internus
		- T: Thalamus
	- Indirect pathway: MS==EN==IT, more motor activity of unwanted movement
		- E: Externus
		- N: Nucleus
	- 首尾激活
	- 中间抑制卖出了N
- Parkinson's disease
	-  related to the loss of dopaminergic neurons in the substantia nigra pars compacta (SNs)
	- Problem:
		- defects in the both direct and indirect pathway, leading to less wanted and unwanted movement
		- Direct pathway: Dopamine is crucial for inhibiting the internus (I). Lack of Dopamine will lead to increased inhibition of the thalmus (T), resulting in reduced motor activity and inhibition
- Huntinton's disease
