**Theme 1: Introduction and Synaptic Plasticity**

1. **Electrophysiological Recordings (General - often Patch Clamp: Voltage Clamp & Current Clamp)**
    
    - **Values Tested:**
        
        - **AMPA/NMDA Receptor Properties:** Rise time, decay time of currents (EPSCs), ion permeability (by changing ion concentrations and measuring reversal potentials), voltage-dependent Mg2+ block (for NMDARs by varying holding potential).
            
        - **Synaptic Strength/Amplitude (EPSCs/EPSPs):** The magnitude of the postsynaptic current or potential change. This is the fundamental readout for plasticity.
            
        - **Quantal Amplitude (a):** Amplitude of response to a single vesicle release (often measured via miniature EPSC analysis or statistical methods).
            
        - **Postsynaptic Potentials (PSPs):** Voltage changes (EPSPs, IPSPs) in response to synaptic input (measured in current clamp).
            
2. **Paired-Pulse Experiments (PPR)**
    
    - **Values Tested:**
        
        - **Initial Probability of Release (p):** Inferred from the Paired-Pulse Ratio (PPR = Amplitude of 2nd response / Amplitude of 1st response).
            
            - PPR < 1 (depression) suggests high initial 'p'.
                
            - PPR > 1 (facilitation) suggests low initial 'p'.
                
        - **Short-Term Plasticity Dynamics:** Nature and magnitude of facilitation or depression.
            
        - **Locus of LTP/LTD Expression (Indirect):** Changes (or lack thereof) in PPR after LTP/LTD induction can suggest pre- vs. postsynaptic mechanisms.
            
3. **Tetanic Stimulation / High-Frequency Stimulation (HFS)**
    
    - **Values Tested/Induced:**
        
        - **Induction of Post-Tetanic Potentiation (PTP):** A short-term increase in synaptic strength.
            
        - **Induction of NMDAR-Dependent Long-Term Potentiation (LTP):** A long-lasting increase in synaptic strength.
            
        - **Presynaptic Calcium Accumulation (Indirectly):** HFS leads to significant Ca2+ buildup, which is a value being manipulated/observed.
            
4. **Low-Frequency Stimulation (LFS) (e.g., 1-5 Hz)**
    
    - **Values Tested/Induced:**
        
        - **Induction of NMDAR-Dependent Long-Term Depression (LTD):** A long-lasting decrease in synaptic strength.
            
        - **Modest, Prolonged Intracellular Ca2+ Elevation (Indirectly):** LFS leads to a different Ca2+ dynamic than HFS.
            
5. **Coefficient of Variation (CV) Analysis (1/CV²)**
    
    - **Values Tested:**
        - **Locus of Synaptic Change (Pre- vs. Postsynaptic):** Changes in 1/CV² (inversely related to variance) can distinguish between presynaptic (changes in 'n' or 'p') and postsynaptic (changes in 'a') mechanisms of plasticity, as 1/CV² is proportional to n*p.
            

6. **Photon Glutamate Uncaging (especially Two-Photon Excitation)**
    
    - **Values Tested:**
        
        - **Postsynaptic Receptor Sensitivity/Number:** Directly probes the responsiveness of postsynaptic receptors by bypassing presynaptic release.
            
        - **Locus of LTP/LTD Expression (Direct):**
            
            - If natural (evoked) response increases but uncaging response doesn't change → presynaptic LTP.
                
            - If both natural and uncaging responses increase → postsynaptic LTP.
                
7. **Advanced Imaging (e.g., Calcium Imaging, Fluorescent Vesicle Reporters)**
    
    - **Values Tested:**
        
        - **Presynaptic Calcium Concentration/Dynamics:** Real-time changes in [Ca2+]i.
            
        - **Vesicle Trafficking Parameters:** Docking, fusion rates, size of vesicle pools (readily releasable pool, reserve pool).
            
        - **Structural Changes:** Synapse size, spine morphology.
            

**Theme 2: Inhibitory Synaptic Transmission**

1. **Electrophysiology (Current Clamp / Voltage Clamp)**
    
    - **Values Tested:**
        
        - **Reversal Potential (E_ion, specifically E_Cl for GABA-A, E_K for GABA-B):** The membrane potential at which there's no net flow of the specific ion. Crucial for determining if GABA is hyperpolarizing, shunting, or depolarizing.
            
        - **Inhibitory Postsynaptic Currents (IPSCs):** Amplitude, kinetics (rise/decay) of GABA-A and GABA-B mediated currents.
            
        - **Inhibitory Postsynaptic Potentials (IPSPs):** Amplitude, duration, and effect on membrane potential (hyperpolarization, shunting).
            
        - **Neuronal Excitability:** How IPSPs affect the likelihood of action potential firing.
            
        - **Shunting Inhibition:** Measured by observing the reduction in an EPSP's amplitude or depolarizing effect when co-activated with an IPSP near the resting potential.
            
2. **Pharmacological Manipulation (using specific receptor agonists/antagonists)**
    
    - **Values Tested:**
        
        - **Contribution of specific receptor subtypes (GABA-A vs. GABA-B) to inhibition:** By blocking one type and observing the remaining current/potential.
            
        - **Modulation of KCC2 function:** Drugs affecting KCC2 can alter E_Cl and thus GABA's effect, which can be measured electrophysiologically.
            
3. **Paired-Pulse Experiments (at inhibitory synapses)**
    
    - **Values Tested:**
        
        - **Initial GABA Release Probability (p_GABA):** Similar to excitatory synapses, PPR at inhibitory synapses can indicate high or low initial p_GABA.
            
        - **Short-Term Plasticity of Inhibitory Transmission:** Facilitation or depression of IPSCs/IPSPs.
            
4. **Optogenetic/Chemogenetic Manipulation of Interneuron Subtypes (e.g., PV, CCK, VIP, SST cells)**
    
    - **Values Tested:**
        
        - **Specific Role of Interneuron Subtypes in Circuit Function:** By selectively activating/silencing them and recording from target neurons (e.g., principal cells or other interneurons).
            
        - **Connectivity Patterns:** Mapping inputs and outputs of specific interneuron types.
            
        - **Impact on Network Oscillations:** How specific interneurons contribute to rhythms like gamma.
            

**Theme 3: Learning and Memory (Many experiments overlap with Theme 1, as synaptic plasticity is a core mechanism)**

1. **Behavioral Paradigms (e.g., Morris water maze, fear conditioning, novel object recognition)**
    
    - **Values Tested:**
        
        - **Memory Formation/Acquisition:** Learning curves, time to criterion.
            
        - **Memory Recall/Retrieval:** Performance on a test phase (e.g., time in target quadrant, freezing behavior).
            
        - **Memory Extinction/Consolidation:** Changes in memory strength over time or with new learning.
            
        - **Working Memory Capacity/Duration:** Performance on tasks requiring active maintenance and manipulation of information (e.g., delayed non-match to sample).
            
2. **Engram Tagging & Manipulation (e.g., c-fos based, activity-dependent reporters + opto/chemogenetics)**
    
    - **Values Tested:**
        
        - **Necessity of Engram Cells for Recall:** Silencing tagged cells and observing impaired memory.
            
        - **Sufficiency of Engram Cells for Recall:** Activating tagged cells and observing memory recall/expression (e.g., artificial fear memory).
            
        - **Excitability of Neurons for Engram Allocation:** Correlating pre-learning excitability with likelihood of being part of an engram.
            
3. **In Vivo Electrophysiology (Single-unit, Multi-unit, LFP recordings in behaving animals)**
    
    - **Values Tested:**
        
        - **Place Cell Firing Fields:** Location-specific firing of hippocampal neurons.
            
        - **Grid Cell Firing Patterns:** Hexagonal firing patterns in MEC.
            
        - **Neuronal Firing Rate Changes with Learning/Attention:** Correlation between task performance/attention and neuronal activity.
            
        - **Memory Reactivation/Replay (during sleep/rest):** Coordinated firing sequences mirroring waking experience.
            
        - **Neural Correlates of Attention:** Increased firing for attended stimuli, decreased for unattended; changes in synchrony/oscillations.
            
4. **Lesion Studies / Pharmacological Inactivation of Brain Regions (e.g., Hippocampus, mPFC, Amygdala)**
    
    - **Values Tested:**
        
        - **Necessity of a Brain Region for Specific Memory Types/Processes:** Observing deficits in learning/memory after inactivation.
            
5. **EEG/LFP Recordings**
    
    - **Values Tested:**
        
        - **Brain Wave Frequencies and Power (Delta, Theta, Alpha, Beta, Gamma):** Correlation with behavioral states (sleep, wakefulness, attention, task performance), memory consolidation processes.
            

**Theme 5: Development and Neurodevelopmental Disorders**

1. **Ocular Dominance Plasticity Paradigms (e.g., Monocular Deprivation - MD)**
    
    - **Values Tested (using techniques below):**
        
        - **Shift in Ocular Dominance:** The relative strength of input from the open vs. deprived eye to visual cortex neurons.
            
        - **Extent of LTD at Deprived Eye Synapses / LTP at Open Eye Synapses.**
            
2. **Recording Techniques for ODP:**
    
    - **Single-Unit Extracellular Recordings (in visual cortex):**
        
        - **Value Tested:** Firing rate responses of individual neurons to visual stimuli presented to each eye separately; calculation of Ocular Dominance Index (ODI).
            
    - **Calcium Fluorescence Imaging (in visual cortex):**
        
        - **Value Tested:** Population activity (Ca2+ transients) in response to monocular/binocular visual stimuli over time.
            
    - **Visually-Evoked Potentials (VEPs):**
        
        - **Value Tested:** Gross electrical response of visual cortex to stimulation of each eye.
            
3. **Pharmacological/Genetic Manipulation during Critical Periods**
    
    - **Values Tested:**
        
        - **Role of Specific Molecules (e.g., GABA, NMDA receptor subunits, LTD machinery) in opening/closing critical periods or mediating ODP:** By blocking/enhancing their function and observing effects on ODP.
            
        - **Chloride Reversal Potential (E_Cl) changes:** Measured electrophysiologically to track GABAergic maturation.
            
4. **Dark Rearing Experiments (Metaplasticity)**
    
    - **Values Tested:**
        
        - **Baseline Plasticity State:** How experience (or lack thereof) alters the subsequent capacity for LTP/LTD induction.
            
        - **NMDA Receptor Subunit Composition:** Biochemical analysis.
            
5. **Animal Models of Neurodevelopmental Disorders (e.g., genetic KOs/KIs, pharmacological models like NMDAR hypofunction for Schizophrenia, PTZ for epilepsy)**
    
    - **Values Tested (using electrophysiology, EEG, behavioral tests):**
        
        - **Gamma Oscillation Power/Coherence:** Often impaired in schizophrenia models.
            
        - **PV Interneuron Function/Number/Connectivity:** Histology, electrophysiology.
            
        - **Excitatory/Inhibitory Balance:** Measured via synaptic currents or network activity.
            
        - **Seizure Threshold/Severity:** In epilepsy models.
            
        - **KCC2 Expression/Function:** Biochemical or electrophysiological assessment (E_Cl).
            
        - **Cognitive/Behavioral Deficits:** Relevant to human symptoms.
            

**Theme 6: Neurodegeneration**

1. **Biomarker Assays:**
    
    - **PET Imaging (with specific radiotracers):**
        
        - **Value Tested:** Brain load/distribution of fibrillary Aβ plaques or tau tangles.
            
    - **Cerebrospinal Fluid (CSF) Analysis:**
        
        - **Value Tested:** Levels of Aβ42, Aβ42/Aβ40 ratio, total tau (t-tau), phosphorylated tau (p-tau), Neurofilament light chain (NfL).
            
    - **Blood Biomarker Tests:**
        
        - **Value Tested:** Plasma levels of p-tau181, p-tau217, Aβ42/Aβ40 ratio, NfL, GFAP.
            
2. **Neuropathological Staging (Post-mortem or in animal models using histology/immunohistochemistry)**
    
    - **Values Tested:**
        
        - **Density and Distribution of Pathological Proteins:** Amyloid plaques (Thal phases), neurofibrillary tangles (Braak stages), Lewy bodies, TDP-43 inclusions, prion plaques.
            
        - **Neuronal Loss/Dysfunction in Specific Regions.**
            
3. **Genetic Testing (for familial forms or risk alleles)**
    
    - **Values Tested:**
        
        - **Presence of Mutations:** In APP, PSEN1, PSEN2 (familial AD), HTT (Huntington's CAG repeats), PINK1/Parkin (PD).
            
        - **ApoE Genotype (ε2, ε3, ε4):** Risk factor for late-onset AD.
            
4. **Animal Models of Neurodegenerative Diseases (transgenic, knock-in, toxin-induced, protein seed injection)**
    
    - **Values Tested:**
        
        - **Rate of Pathological Protein Aggregation & Spread.**
            
        - **Degree of Neuronal Dysfunction/Loss.**
            
        - **Severity of Behavioral/Motor Deficits** (e.g., cognitive tests for AD models, motor tests for PD models).
            
        - **Mitochondrial Function:** Assays for respiratory chain activity, ROS production, mitophagy.
            
5. **Real-Time Quaking-Induced Conversion (RT-QuIC)**
    
    - **Values Tested:**
        
        - **Presence and Seeding Activity of Misfolded Proteins (PrPSc, α-synuclein, tau) in biological samples (CSF, skin):** Provides diagnostic value by amplifying these specific aggregates.
            
6. **Deep Brain Stimulation (DBS) (as a treatment that underwent experimental testing)**
    
    - **Values Tested (during clinical trials/optimization):**
        
        - **Improvement in Motor Scores (e.g., UPDRS for PD).**
            
        - **Optimal Stimulation Parameters (frequency, amplitude, location).**
            
7. **Cell-Replacement Therapy Studies (preclinical and clinical trials)**
    
    - **Values Tested:**
        
        - **Graft Survival and Integration.**
            
        - **Restoration of Neurotransmitter Levels (e.g., dopamine in PD).**
            
        - **Functional Motor/Cognitive Improvement.**
            

**Theme 7: Motor and Sensory Neuroscience**

1. **Electrophysiology of Sensory Receptors (e.g., Photoreceptors in retina)**
    
    - **Values Tested:**
        
        - **Receptor Potential:** Graded potential change in response to stimulus (e.g., light hyperpolarizing photoreceptors).
            
        - **Signal Transduction Cascade Activity:** e.g., levels of cGMP in photoreceptors.
            
        - **Neurotransmitter Release Modulation:** e.g., reduced glutamate release from hyperpolarized photoreceptors.
            
2. **Electromyography (EMG)**
    
    - **Values Tested:**
        
        - **Muscle Activity/Contraction Strength & Timing.**
            
        - **Motor Unit Action Potentials (MUAPs):** To define motor units.
            
3. **Nerve Conduction Studies / Motor Evoked Potentials (MEPs)**
    
    - **Values Tested:**
        
        - **Integrity and Conduction Velocity of Motor/Sensory Nerves.**
            
        - **Excitability of Corticospinal Tract (using Transcranial Magnetic Stimulation - TMS to elicit MEPs).**
            
4. **Reflex Testing (e.g., tapping patellar tendon for myotatic reflex)**
    
    - **Values Tested:**
        
        - **Reflex Latency and Amplitude.**
            
        - **Integrity of Monosynaptic/Polysynaptic Reflex Arcs.**
            
        - **Muscle Spindle Sensitivity.**
            
5. **Animal Models of Movement Disorders (e.g., MPTP model for Parkinson's)**
    
    - **Values Tested:**
        
        - **Degree of Dopamine Neuron Loss (for PD models).**
            
        - **Severity of Motor Deficits (bradykinesia, rigidity, tremor).**
            
        - **Activity Changes in Basal Ganglia Nuclei (via electrophysiology or c-fos mapping).**
            

This list covers a wide range of experimental approaches. The specific "value" being tested often depends on the precise experimental design and the question being asked, but this gives a good overview based on your notes.