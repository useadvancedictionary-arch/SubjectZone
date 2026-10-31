#!/usr/bin/env python3
"""Build Chemistry IX exercise solutions JSON directly."""
import json

items = []
_qid = 0

def q(ch, section, number, qtype, question, answer, explanation, pdf_page,
      options=None, correct=None):
    global _qid
    _qid += 1
    sec_labels = {'A': 'MCQs', 'B': 'Short Questions', 'C': 'Detailed Answers', 'D': 'Numerical'}
    items.append({
        'id': f'chem9-ch{ch:02d}-{section}{number:02d}',
        'chapter': ch,
        'section': sec_labels.get(section, section),
        'sectionCode': section,
        'type': qtype,
        'number': number,
        'question': question,
        'answer': answer,
        'explanation': explanation,
        'pdfPage': pdf_page,
        'bookPage': pdf_page - 3,
        'figure': None,
        'options': options,
        'optionsRaw': options,
        'correctAnswer': correct,
    })

# ============================================================
# CHAPTER 1: Fundamentals of Chemistry (PDF pages 33-35)
# ============================================================
# Section A: MCQs
q(1,'A',1,'mcq','Which branch of chemistry deals with hydrocarbons and their derivatives?',
  'Organic chemistry','Organic chemistry studies carbon-based compounds, primarily hydrocarbons and their derivatives.',
  33,options=['Inorganic chemistry','Physical chemistry','Organic chemistry','Biochemistry'],correct='Organic chemistry')

q(1,'A',2,'mcq','Atomic mass expressed in grams is called:',
  'Gram atomic mass','When atomic mass of an element is expressed in grams, it is called gram atomic mass (one mole of atoms).',
  33,options=['Atomic mass','Gram atomic mass','Molecular mass','Formula mass'],correct='Gram atomic mass')

q(1,'A',3,'mcq','A substance that can be separated by physical means is:',
  'Mixture','A mixture contains two or more substances that can be separated by physical methods like filtration, distillation.',
  33,options=['Mixture','Compound','Element','Molecule'],correct='Mixture')

q(1,'A',4,'mcq','The molar mass of H2SO4 is:',
  '98 gm','Molar mass of H2SO4 = 2(1) + 32 + 4(16) = 2 + 32 + 64 = 98 g/mol.',
  33,options=['49 gm','96 gm','98 gm','100 gm'],correct='98 gm')

q(1,'A',5,'mcq','A molecule consisting of two atoms is called:',
  'Diatomic molecule','A molecule made up of two atoms (same or different) is called a diatomic molecule, e.g., H2, O2, HCl.',
  33,options=['Monoatomic molecule','Triatomic molecule','Polyatomic molecule','Diatomic molecule'],correct='Diatomic molecule')

q(1,'A',6,'mcq','The formula that indicates the actual number and type of atoms in a molecule is:',
  'Molecular formula','Molecular formula shows the exact number of each type of atom present in one molecule of a substance.',
  33,options=['Empirical formula','Structural formula','Molecular formula','Simplest formula'],correct='Molecular formula')

q(1,'A',7,'mcq','Ethyl alcohol was first prepared by:',
  'Al-Razi','Al-Razi (Rhazes) was a Persian alchemist who first prepared ethyl alcohol through fermentation.',
  33,options=['Jabir-bin-Hayan','Al-Razi','Boyle','Dalton'],correct='Al-Razi')

q(1,'A',8,'mcq','Which of the following is a homoatomic molecule?',
  'H2','A homoatomic molecule consists of atoms of the same element. H2 contains two hydrogen atoms.',
  33,options=['H2','H2O','CO2','NH3'],correct='H2')

q(1,'A',9,'mcq','The empirical formula of H2O2 is:',
  'HO','The simplest whole number ratio of H:O in H2O2 is 1:1, so the empirical formula is HO.',
  33,options=['H2O','HO','H2O2','HO2'],correct='HO')

q(1,'A',10,'mcq','A pure form of matter is called:',
  'Substance','A substance (pure substance) has constant composition and distinct properties.',
  33,options=['Mixture','Solution','Colloid','Substance'],correct='Substance')

# Section B: Short Questions
q(1,'B',1,'short','Differentiate between physical chemistry and analytical chemistry.',
  'Physical chemistry deals with the relationship between composition and properties of matter, energy changes, and reaction rates. Analytical chemistry deals with techniques and methods to determine the composition of substances.',
  'Physical chemistry focuses on energy, rates, and physical properties. Analytical chemistry focuses on identifying and quantifying substances.',34)

q(1,'B',2,'short','How is a molecule classified? Give examples.',
  'Molecules are classified based on number of atoms: monoatomic (He, Ne), diatomic (H2, O2, HCl), triatomic (H2O, CO2), polyatomic (CH4, C6H12O6). Also classified as homoatomic (O2, N2) or heteroatomic (H2O, CO2).',
  'Classification is based on atom count and whether atoms are same or different elements.',34)

q(1,'B',3,'short','Differentiate between: (a) Atom and Ion (b) Molecule and Molecular ion (c) Compound and Mixture.',
  '(a) Atom is neutral; ion has a charge (gained or lost electrons). (b) Molecule is neutral; molecular ion has a charge. (c) Compound has fixed composition with chemical bonding; mixture has variable composition with no chemical bonding.',
  'Key differences: charge state for atom/ion and molecule/molecular ion; chemical bonding and fixed vs variable composition for compound/mixture.',34)

q(1,'B',4,'short','Define gram atomic mass, gram molecular mass, and gram formula mass.',
  'Gram atomic mass: atomic mass of an element expressed in grams (e.g., 1g mol of H = 1g). Gram molecular mass: molecular mass expressed in grams (e.g., 1g mol of H2O = 18g). Gram formula mass: formula mass of an ionic compound expressed in grams (e.g., 1g mol of NaCl = 58.5g).',
  'All three express mass in grams for one mole, but differ based on atoms, molecules, or formula units.',34)

q(1,'B',5,'short','Write the empirical and molecular formula of: H2SO4, CO2, Glucose, Benzene.',
  'H2SO4: Empirical = H2SO4, Molecular = H2SO4 (same). CO2: Empirical = CO2, Molecular = CO2 (same). Glucose: Empirical = CH2O, Molecular = C6H12O6. Benzene: Empirical = CH, Molecular = C6H6.',
  'When the molecular formula cannot be simplified further, empirical and molecular formulas are the same.',34)

q(1,'B',6,'short','What is a free radical? Give an example.',
  'A free radical is an atom or group of atoms with an unpaired electron, making it highly reactive. Example: Chlorine free radical (Cl.) formed when Cl2 is exposed to sunlight.',
  'Free radicals are formed by homolytic cleavage and are very reactive due to the unpaired electron.',34)

q(1,'B',7,'short','What is the relationship between empirical formula and molecular formula?',
  'Molecular formula = n x Empirical formula, where n is a whole number. n = Molecular mass / Empirical formula mass. The empirical formula gives the simplest ratio, while the molecular formula gives the actual number of atoms.',
  'The molecular formula is always a whole number multiple of the empirical formula.',34)

q(1,'B',8,'short','Why are H2 and O2 considered elements but water (H2O) is a compound?',
  'H2 and O2 consist of atoms of only one type of element, so they are elements. Water (H2O) consists of two different elements (H and O) chemically combined in a fixed ratio, so it is a compound.',
  'Elements contain only one type of atom; compounds contain two or more different types of atoms chemically bonded.',34)

# Section C: Detailed Questions
q(1,'C',1,'detailed','Define chemical species, ion, molecular ion, and free radical with examples.',
  'Chemical species: Any chemical entity (atom, ion, molecule, radical) with a specific composition. Ion: An atom or group of atoms with a net charge due to loss or gain of electrons (e.g., Na+, Cl-). Molecular ion: A molecule that has gained or lost electrons, acquiring a charge (e.g., CH4+, N2). Free radical: An atom or group with an unpaired electron, highly reactive (e.g., Cl., CH3.).',
  'These are all types of chemical species distinguished by their charge state and electron configuration.',34)

q(1,'C',2,'detailed','Describe the applications of chemistry in daily life.',
  'Chemistry is applied in: (1) Medicine - drug synthesis, diagnostics. (2) Agriculture - fertilizers, pesticides. (3) Food industry - preservatives, flavoring. (4) Construction - cement, steel, glass. (5) Textiles - synthetic fibers, dyes. (6) Cosmetics - soaps, creams. (7) Energy - fuels, batteries. (8) Environment - pollution control, water treatment.',
  'Chemistry touches virtually every aspect of modern life, from health to industry to environment.',34)

q(1,'C',3,'detailed','Explain empirical formula and molecular formula with examples.',
  'Empirical formula: The simplest whole number ratio of atoms in a compound. Example: Glucose C6H12O6 has empirical formula CH2O (ratio 1:2:1). Molecular formula: The actual number of atoms of each element in a molecule. Example: Glucose molecular formula is C6H12O6. Relationship: Molecular formula = n x Empirical formula, where n = molecular mass / empirical formula mass.',
  'The empirical formula gives the simplest ratio; the molecular formula gives the actual count.',34)

q(1,'C',4,'detailed','Describe the steps for balancing a chemical equation.',
  'Steps: (1) Write the unbalanced equation with correct formulas. (2) Count atoms of each element on both sides. (3) Start balancing with the element that appears in the fewest compounds. (4) Use coefficients (not subscripts) to balance. (5) Balance oxygen and hydrogen last. (6) Check that all atoms are balanced. (7) Ensure coefficients are in the simplest whole number ratio.',
  'Balancing ensures the law of conservation of mass is satisfied - same number of each atom on both sides.',34)

q(1,'C',5,'detailed','Describe the main branches of chemistry.',
  'Main branches: (1) Organic Chemistry - study of carbon compounds. (2) Inorganic Chemistry - study of non-carbon compounds and minerals. (3) Physical Chemistry - relationship between composition and properties, energy, rates. (4) Analytical Chemistry - techniques to determine composition. (5) Biochemistry - chemistry of living organisms. (6) Industrial Chemistry - large-scale production. (7) Nuclear Chemistry - study of nuclear reactions. (8) Environmental Chemistry - chemical processes in the environment.',
  'Each branch focuses on different aspects of matter and its transformations.',35)

# ============================================================
# CHAPTER 2: Atomic Structure (PDF pages 56-57)
# ============================================================
# Section A: MCQs
q(2,'A',1,'mcq','The sum of protons and neutrons in an atom is called:',
  'Number of nucleons','The sum of protons and neutrons equals the mass number, also called the number of nucleons.',
  56,options=['Atomic number','Number of nucleons','Number of electrons','Charge number'],correct='Number of nucleons')

q(2,'A',2,'mcq','If the proton number of an element is 19, its electronic configuration will be:',
  '2, 8, 8, 1','Potassium (Z=19): K shell=2, L shell=8, M shell=8, N shell=1. Total = 2+8+8+1 = 19.',
  56,options=['2, 8, 9','2, 8, 8, 1','2, 8, 7, 2','2, 8, 6, 3'],correct='2, 8, 8, 1')

q(2,'A',3,'mcq','The nucleon number of potassium is 39 and its atomic number is 19. The number of neutrons is:',
  '20','Neutrons = Mass number - Atomic number = 39 - 19 = 20.',
  56,options=['19','39','20','18'],correct='20')

q(2,'A',4,'mcq','The relative abundance of C-12 is:',
  '98.89%','Carbon-12 is the most abundant isotope of carbon, making up about 98.89% of natural carbon.',
  56,options=['1.10%','0.01%','98.89%','99.99%'],correct='98.89%')

q(2,'A',5,'mcq','Electronic configuration is the distribution of:',
  'Electrons','Electronic configuration describes how electrons are distributed among the various shells and subshells of an atom.',
  56,options=['Protons','Neutrons','Electrons','Nucleons'],correct='Electrons')

q(2,'A',6,'mcq','The most penetrating radiation is:',
  'Neutron','Neutrons have no charge and can penetrate deeply through matter without being deflected by electric or magnetic fields.',
  56,options=['Alpha rays','Beta rays','Gamma rays','Neutron'],correct='Neutron')

q(2,'A',7,'mcq','The number of subshells in the L shell is:',
  'Two','The L shell (n=2) has two subshells: 2s and 2p.',
  56,options=['One','Two','Three','Four'],correct='Two')

q(2,'A',8,'mcq','De Broglie proposed the wave-particle duality of electron in:',
  '1923','Louis de Broglie proposed in 1923 that electrons exhibit both wave and particle properties.',
  56,options=['1905','1913','1923','1932'],correct='1923')

q(2,'A',9,'mcq','The screen material used in Rutherford experiment was:',
  'Zinc sulphide','Rutherford used a zinc sulphide (ZnS) screen that produced flashes of light when struck by alpha particles.',
  56,options=['Barium sulphide','Zinc sulphide','Calcium carbonate','Sodium chloride'],correct='Zinc sulphide')

q(2,'A',10,'mcq','Which rays are used for sterilization of surgical instruments?',
  'Gamma-rays','Gamma rays have high penetrating power and are used to sterilize surgical instruments and medical equipment.',
  56,options=['Alpha-rays','Beta-rays','Gamma-rays','X-rays'],correct='Gamma-rays')

# Section B: Short Questions
q(2,'B',1,'short','Draw the structure of isotopes of chlorine to justify the definition of isotopes.',
  'Chlorine has two isotopes: Cl-35 (17 protons, 18 neutrons) and Cl-37 (17 protons, 20 neutrons). Both have the same atomic number (17) but different mass numbers (35 and 37). This justifies the definition: isotopes are atoms of the same element with the same number of protons but different number of neutrons.',
  'Isotopes have identical chemical properties but different physical properties due to different neutron counts.',57)

q(2,'B',2,'short','An atom has 5 electrons in M shell. (a) Find its atomic number. (b) Write electronic configuration. (c) Name the element.',
  '(a) Atomic number = 2 + 8 + 5 = 15. (b) Electronic configuration: K=2, L=8, M=5 or 1s2 2s2 2p6 3s2 3p3. (c) The element is Phosphorus (P).',
  'The M shell is the third shell (n=3). Filling K=2, L=8, then 5 in M gives Z=15 = Phosphorus.',57)

q(2,'B',3,'short','Justify that Rutherford atomic model has defects.',
  'Defects: (1) According to classical physics, an accelerating charged particle (electron in orbit) should emit radiation and lose energy, spiraling into the nucleus - but atoms are stable. (2) It could not explain the line spectra of atoms. (3) It did not explain the distribution of electrons around the nucleus.',
  'Rutherford model failed to explain atomic stability and spectral lines, which Bohr model later addressed.',57)

q(2,'B',4,'short','Describe the wave-particle duality of electron according to De Broglie hypothesis.',
  'De Broglie proposed that electrons (and all matter) exhibit both wave and particle properties. The wavelength of a particle is lambda = h/mv, where h is Planck constant, m is mass, and v is velocity. This means electrons can behave as waves (showing diffraction and interference) and as particles (having mass and momentum).',
  'This duality was confirmed by electron diffraction experiments and is fundamental to quantum mechanics.',57)

q(2,'B',5,'short','What are the limitations of Bohr atomic model?',
  'Limitations: (1) Could not explain spectra of multi-electron atoms. (2) Could not explain the splitting of spectral lines in magnetic field (Zeeman effect) and electric field (Stark effect). (3) Did not explain the wave nature of electrons. (4) Could not explain the shape of molecules. (5) Violated Heisenberg uncertainty principle by specifying exact orbits.',
  'Bohr model worked well for hydrogen but failed for more complex atoms.',57)

q(2,'B',6,'short','Differentiate between shell and subshell with examples.',
  'Shell: A main energy level designated by principal quantum number n (K, L, M, N...). Each shell can hold 2n squared electrons. Example: K shell (n=1) holds 2 electrons. Subshell: A subdivision of a shell designated by letters s, p, d, f. Each shell has n subshells. Example: L shell (n=2) has 2s and 2p subshells.',
  'Shells are major energy levels; subshells are subdivisions within shells with different shapes.',57)

q(2,'B',7,'short','How are the atoms of O-17 and O-16 similar or different from each other?',
  'Similar: Both have 8 protons and 8 electrons (same atomic number), so they have identical chemical properties and electronic configuration. Different: O-17 has 9 neutrons while O-16 has 8 neutrons, so they have different mass numbers and slightly different physical properties.',
  'These are isotopes of oxygen - same element, different neutron count.',57)

q(2,'B',9,'short','Write down the names of subatomic particles, their masses in a.m.u, and their unit charges.',
  'Proton: mass = 1.0073 a.m.u, charge = +1. Neutron: mass = 1.0087 a.m.u, charge = 0. Electron: mass = 0.00055 a.m.u (1/1836 of proton), charge = -1.',
  'Protons and neutrons have nearly equal mass (~1 a.m.u); electrons are ~1836 times lighter.',57)

# Section C: Detailed Questions
q(2,'C',1,'detailed','Discuss Rutherford gold foil experiment in the light of structure of atom.',
  'Rutherford bombarded a thin gold foil with alpha particles. Observations: (1) Most alpha particles passed straight through - atom is mostly empty space. (2) Some were deflected at small angles - positive charge is concentrated. (3) Very few (1 in 20,000) bounced back - a small, dense, positively charged nucleus exists at the center. Conclusion: Atom has a tiny, dense, positively charged nucleus containing most of the mass, with electrons orbiting around it at large distances.',
  'This experiment disproved the plum pudding model and established the nuclear model of the atom.',57)

q(2,'C',2,'detailed','Write down the applications of isotopes in daily life.',
  'Applications: (1) Medicine: I-131 for thyroid treatment, Co-60 for cancer therapy, P-32 for leukemia. (2) Agriculture: P-32 as fertilizer tracer. (3) Industry: Co-60 for detecting pipe leaks, thickness measurement. (4) Archaeology: C-14 for dating ancient artifacts. (5) Energy: U-235 as nuclear fuel. (6) Food preservation: Gamma radiation from Co-60 to kill bacteria.',
  'Isotopes have diverse applications in medicine, industry, agriculture, and research.',57)

q(2,'C',3,'detailed','Explain how Bohr atomic model is different from Rutherford atomic model.',
  'Rutherford: Electrons orbit the nucleus in any path; could not explain stability or spectra. Bohr: (1) Electrons revolve in fixed circular orbits (energy levels/shells) with fixed energy. (2) Electrons do not radiate energy while in a fixed orbit. (3) Energy is emitted/absorbed only when electrons jump between orbits. (4) Each orbit is designated K, L, M, N... with energy increasing with distance from nucleus.',
  'Bohr introduced quantized energy levels, solving the stability problem.',57)

q(2,'C',4,'detailed','Prove that the modern theory of De Broglie is related to Einstein and Planck equations.',
  'Planck equation: E = hv. Einstein equation: E = mc squared. De Broglie combined these: hv = mc squared. Since v = c/lambda, we get hc/lambda = mc squared, so lambda = h/mc. For a particle with velocity v: lambda = h/mv. This shows that matter has wave properties, with wavelength inversely proportional to momentum (mv).',
  'De Broglie unified wave and particle theories by combining quantum theory with relativity.',57)

q(2,'C',5,'detailed','How are cathode rays produced? What are their major characteristics?',
  'Production: In a discharge tube at low pressure (~0.01 torr) with high voltage (~10,000V), rays travel from cathode to anode. These are cathode rays - streams of electrons. Characteristics: (1) Travel in straight lines. (2) Cast shadows of objects. (3) Rotate a paddle wheel (have momentum). (4) Deflected toward positive plate (negatively charged). (5) Deflected by magnetic field. (6) Produce fluorescence. (7) Have e/m ratio same regardless of gas used.',
  'Cathode rays are electrons - their properties are independent of the gas in the tube.',57)

q(2,'C',6,'detailed','Describe the Schrodinger atomic model.',
  'Schrodinger (1926) developed the quantum mechanical model based on wave mechanics. Key points: (1) Electrons behave as waves (De Broglie). (2) Exact position and momentum cannot be known simultaneously (Heisenberg). (3) Electrons exist in orbitals - 3D regions of space where probability of finding an electron is maximum. (4) Described by wave function psi. (5) Four quantum numbers (n, l, m, s) describe each electron. (6) Orbitals have specific shapes: s=spherical, p=dumbbell, d=clover.',
  'The quantum mechanical model replaced fixed orbits with probability-based orbitals.',57)

q(2,'C',7,'detailed','Describe briefly the experiments which provide evidence of electron, proton, and neutron in an atom.',
  'Electron: J.J. Thomson cathode ray experiment (1897) - rays deflected by electric and magnetic fields, e/m ratio measured, proved existence of negatively charged particles. Proton: Goldstein canal ray experiment (1886) - positive rays from perforated cathode, e/m ratio depended on gas, lightest positive ray from H2 gave proton. Neutron: Chadwick (1932) bombarded Be with alpha particles, observed neutral radiation that could knock out protons from paraffin - proved existence of neutral particle with mass ~1 a.m.u.',
  'Each subatomic particle was discovered through distinct experiments over several decades.',57)

q(2,'C',8,'detailed','How many protons, neutrons, and electrons are present in: (i) Fe-56 (ii) O-17 (iii) Cl-37 (iv) U-235 (v) C-14?',
  '(i) Fe-56: p=26, n=56-26=30, e=26. (ii) O-17: p=8, n=17-8=9, e=8. (iii) Cl-37: p=17, n=37-17=20, e=17. (iv) U-235: p=92, n=235-92=143, e=92. (v) C-14: p=6, n=14-6=8, e=6.',
  'For neutral atoms: protons = atomic number, neutrons = mass number - atomic number, electrons = protons.',57)

# ============================================================
# CHAPTER 3: Periodic Table and Periodicity of Properties (PDF pages 72-74)
# ============================================================
# Section A: MCQs
q(3,'A',1,'mcq','Mendeleev periodic law was about:',
  'Atomic Mass','Mendeleev arranged elements by increasing atomic mass and observed periodic repetition of properties.',
  72,options=['Atomic Number','Electronic Configuration','Atomic Radius','Atomic Mass'],correct='Atomic Mass')

q(3,'A',2,'mcq','Periodic table is divided into s, p, d, f blocks based on:',
  'Electronic Configuration','The block classification is based on which subshell (s, p, d, f) the last electron enters.',
  72,options=['Atomic Mass','Electronic Configuration','Atomic Number','Chemical Properties'],correct='Electronic Configuration')

q(3,'A',3,'mcq','4th and 5th periods are called:',
  'Long period','The 4th and 5th periods contain 18 elements each, making them long periods.',
  72,options=['Short period','Long period','Very long period','Normal period'],correct='Long period')

q(3,'A',4,'mcq','Which property decreases along a period?',
  'Atomic Radius','Atomic radius decreases across a period due to increasing nuclear charge pulling electrons closer.',
  72,options=['Ionization Energy','Atomic Radius','Electronegativity','Electron Affinity'],correct='Atomic Radius')

q(3,'A',5,'mcq','Group VIIA elements are called:',
  'Halogens','Group VIIA (17) elements are called halogens (F, Cl, Br, I, At) meaning salt-formers.',
  72,options=['Noble gases','Alkali metals','Halogens','Alkaline earth metals'],correct='Halogens')

q(3,'A',6,'mcq','Moseley stated that properties of elements are periodic function of:',
  'Atomic Number','Moseley corrected Mendeleev law: properties are periodic function of atomic number, not atomic mass.',
  72,options=['Atomic Mass','Electronic Configuration','Atomic Radius','Atomic Number'],correct='Atomic Number')

q(3,'A',7,'mcq','Shielding effect across a period:',
  'Same','Shielding effect remains approximately same across a period because electrons are added to the same shell.',
  72,options=['Increases','Decreases','Remains constant','Same'],correct='Same')

q(3,'A',8,'mcq','The ability of an atom to attract shared pair of electrons is called:',
  'Electronegativity','Electronegativity is the ability of an atom in a molecule to attract shared electrons toward itself.',
  72,options=['Ionization Energy','Electronegativity','Electron Affinity','Atomic Radius'],correct='Electronegativity')

q(3,'A',9,'mcq','Electron affinity decreases from top to bottom because:',
  'Atomic size increases','As atomic size increases down a group, the nucleus is farther from incoming electron, reducing attraction.',
  72,options=['Nuclear charge increases','Atomic size increases','Shielding decreases','Ionization energy increases'],correct='Atomic size increases')

q(3,'A',10,'mcq','All Transition Elements are:',
  'Metals','All transition elements (d-block) are metals with characteristic metallic properties.',
  72,options=['Non-metals','Metals','Metalloids','Noble gases'],correct='Metals')

# Section B: Short Questions
q(3,'B',1,'short','Distinguish between periods and groups.',
  'Periods: Horizontal rows in periodic table (7 periods). Elements in a period have same number of electron shells. Groups: Vertical columns (18 groups). Elements in a group have same number of valence electrons and similar chemical properties.',
  'Periods = rows (same shells); Groups = columns (same valence electrons and similar properties).',74)

q(3,'B',2,'short','Describe the trend of electronegativity within group and period with examples.',
  'Across a period (left to right): Electronegativity increases due to increasing nuclear charge. Example: Na(0.9) < Mg(1.2) < Al(1.5) < Si(1.8) < P(2.1) < S(2.5) < Cl(3.0). Down a group: Electronegativity decreases due to increasing atomic size. Example: F(4.0) > Cl(3.0) > Br(2.8) > I(2.5).',
  'Electronegativity increases across periods and decreases down groups.',74)

q(3,'B',3,'short','Explain the similarity of chemical and physical properties of elements in the same family.',
  'Elements in the same family (group) have the same number of valence electrons, which determines chemical behavior. Example: All alkali metals (Group IA) have 1 valence electron, are highly reactive, form +1 ions, and react vigorously with water.',
  'Same valence electron configuration leads to similar chemical and physical properties.',74)

q(3,'B',4,'short','Justify that periodicity of properties is dependent upon number of protons in an atom.',
  'Moseley showed that atomic number (number of protons) determines the position of an element. As proton number increases, electrons are added in a regular pattern, causing periodic repetition of properties. Example: Li(3), Na(11), K(19) all have 1 valence electron and similar properties.',
  'Atomic number (proton count) determines electron configuration, which determines properties.',74)

q(3,'B',5,'short','Identify which halogens exist as gases, liquid and solid.',
  'Fluorine (F2) and Chlorine (Cl2) are gases at room temperature. Bromine (Br2) is a liquid. Iodine (I2) and Astatine (At) are solids. This trend is due to increasing molecular size and van der Waals forces down the group.',
  'Physical state changes from gas to liquid to solid down the group due to increasing intermolecular forces.',74)

q(3,'B',6,'short','Why do Alkaline earth metals show irregular melting and boiling points?',
  'Alkaline earth metals (Group IIA) show irregular melting/boiling points because their crystal structures vary. Be and Mg have hexagonal close packing, Ca and Sr have face-centered cubic, and Ba has body-centered cubic. Different crystal structures lead to different melting points.',
  'Different crystal structures among group members cause irregular trends in melting/boiling points.',74)

q(3,'B',7,'short','Why do ionization energy, electron affinity and electronegativity exhibit same trend in periods and groups?',
  'All three properties depend on effective nuclear charge and atomic size. Across a period: nuclear charge increases, size decreases, so all three increase. Down a group: size increases, shielding increases, so all three decrease. They all measure attraction between nucleus and electrons.',
  'All three properties depend on nuclear charge and atomic radius, so they follow similar trends.',74)

# Section C: Detailed Questions
q(3,'C',1,'detailed','Discuss in detail the long form of periodic table.',
  'The long form (modern periodic table) is based on atomic number. It has 7 periods and 18 groups. Periods: 1st (2 elements), 2nd-3rd (8 each), 4th-5th (18 each), 6th (32), 7th (incomplete). Groups: IA-VIIIA (main group), IB-VIIIB (transition). Blocks: s-block (Groups IA, IIA), p-block (Groups IIIA-VIIIA), d-block (transition metals), f-block (lanthanides and actinides). Elements are arranged by increasing atomic number.',
  'The long form resolves anomalies of Mendeleev table and is based on electronic configuration.',74)

q(3,'C',2,'detailed','Determine the demarcation of periodic table into s, p, d and f blocks.',
  's-block: Groups IA and IIA (last electron enters s subshell). p-block: Groups IIIA to VIIIA (last electron enters p subshell). d-block: Groups IB to VIIIB (transition metals, last electron enters d subshell). f-block: Lanthanides and Actinides (last electron enters f subshell). The block is determined by the subshell in which the differentiating (last) electron enters.',
  'Block classification is based on the subshell receiving the last electron.',74)

q(3,'C',3,'detailed','Identify the electronic configuration of Na, Ca, F, Si.',
  'Na (Z=11): 1s2 2s2 2p6 3s1 or [Ne] 3s1. Ca (Z=20): 1s2 2s2 2p6 3s2 3p6 4s2 or [Ar] 4s2. F (Z=9): 1s2 2s2 2p5 or [He] 2s2 2p5. Si (Z=14): 1s2 2s2 2p6 3s2 3p2 or [Ne] 3s2 3p2.',
  'Electronic configuration shows how electrons are distributed in shells and subshells.',74)

q(3,'C',4,'detailed','Determine the location of families on periodic table.',
  'Alkali metals: Group IA (Li, Na, K, Rb, Cs, Fr). Alkaline earth metals: Group IIA (Be, Mg, Ca, Sr, Ba, Ra). Halogens: Group VIIA (F, Cl, Br, I, At). Noble gases: Group VIIIA (He, Ne, Ar, Kr, Xe, Rn). Transition metals: Groups IB to VIIIB (d-block). Lanthanides and Actinides: f-block at bottom.',
  'Each family occupies a specific group based on valence electron configuration.',74)

q(3,'C',5,'detailed','Discuss that Mendeleev periodic law provides a base for modern periodic table.',
  'Mendeleev arranged elements by atomic mass and observed periodic repetition of properties. He left gaps for undiscovered elements and predicted their properties accurately. Although his law was based on atomic mass, it established the concept of periodicity. Moseley later corrected it to atomic number, but Mendeleev fundamental idea of periodic classification remained the foundation.',
  'Mendeleev established periodicity concept; Moseley refined it from atomic mass to atomic number.',74)

q(3,'C',6,'detailed','Explain how shielding effect influences the periodic trends.',
  'Shielding effect: Inner electrons shield outer electrons from full nuclear charge. Across a period: Shielding remains roughly constant (electrons added to same shell), so effective nuclear charge increases, causing atomic radius to decrease and ionization energy to increase. Down a group: Shielding increases (more inner shells), so effective nuclear charge felt by valence electrons decreases, causing atomic radius to increase and ionization energy to decrease.',
  'Shielding effect explains why properties change differently across periods vs down groups.',74)

# ============================================================
# CHAPTER 4: Chemical Bonding (PDF pages 93-96)
# ============================================================
# Section A: MCQs
q(4,'A',1,'mcq','Which of the following is an ionic compound?',
  'NaCl','NaCl is formed by transfer of electron from Na to Cl, creating Na+ and Cl- ions held by ionic bond.',
  93,options=['H2O','CO2','NH3','NaCl'],correct='NaCl')

q(4,'A',2,'mcq','The interaction between electron deficient hydrogen and electronegative atom is called:',
  'Hydrogen bond','Hydrogen bonding occurs when H is bonded to highly electronegative atom (F, O, N) and interacts with lone pair of another electronegative atom.',
  93,options=['Ionic bond','Covalent bond','Hydrogen bond','Metallic bond'],correct='Hydrogen bond')

q(4,'A',3,'mcq','Two F atoms share electrons to achieve configuration of:',
  'Ne','Each F atom (1s2 2s2 2p5) needs 1 electron to complete octet. By sharing, both achieve Ne configuration (1s2 2s2 2p6).',
  93,options=['He','Ne','Ar','Kr'],correct='Ne')

q(4,'A',4,'mcq','Number of electrons lost by Group IIIA elements:',
  '3','Group IIIA elements (B, Al, Ga, In, Tl) have 3 valence electrons and lose all 3 to form +3 ions.',
  93,options=['1','2','3','4'],correct='3')

q(4,'A',5,'mcq','An atom that loses two electrons becomes:',
  'Magnesium','Magnesium (Mg) has 2 valence electrons and loses both to form Mg2+ ion.',
  93,options=['Sodium','Calcium','Magnesium','Aluminum'],correct='Magnesium')

q(4,'A',6,'mcq','In NaCl lattice, each Na+ is surrounded by:',
  '6 Cl- ions','In NaCl crystal lattice, each Na+ ion is surrounded by 6 Cl- ions in octahedral arrangement.',
  93,options=['6 Cl- ions','8 Cl- ions','4 Cl- ions','12 Cl- ions'],correct='6 Cl- ions')

q(4,'A',7,'mcq','Ionic compounds at room temperature are:',
  'Crystalline solids','Ionic compounds form regular crystal lattices at room temperature due to strong ionic bonds.',
  93,options=['Liquids','Crystalline solids','Gases','Amorphous solids'],correct='Crystalline solids')

q(4,'A',8,'mcq','The rule that atoms tend to achieve 8 electrons in valence shell is:',
  'Octet rule','Octet rule states that atoms tend to gain, lose, or share electrons to achieve 8 electrons in valence shell (noble gas configuration).',
  93,options=['Octet rule','Duplet rule','Hund rule','Aufbau principle'],correct='Octet rule')

q(4,'A',9,'mcq','The bond formed between cation and anion is:',
  'Ionic bond','Ionic bond is the electrostatic attraction between positively charged cation and negatively charged anion.',
  93,options=['Covalent bond','Ionic bond','Metallic bond','Hydrogen bond'],correct='Ionic bond')

q(4,'A',10,'mcq','Noble gases are stable because they have:',
  '8 electrons in valence shell','Noble gases have complete octet (8 electrons in valence shell, except He with 2), making them chemically inert.',
  93,options=['High atomic mass','8 electrons in valence shell','Low density','High ionization energy'],correct='8 electrons in valence shell')

q(4,'A',11,'mcq','A bond with 3 shared pairs of electrons is:',
  'Triple covalent bond','Triple covalent bond involves sharing of 3 electron pairs (6 electrons) between two atoms, e.g., N2.',
  93,options=['Single covalent bond','Triple covalent bond','Double covalent bond','Ionic bond'],correct='Triple covalent bond')

q(4,'A',12,'mcq','A non-metal forms anion by:',
  'Gain of electrons','Non-metals have high electronegativity and gain electrons to achieve noble gas configuration, forming negatively charged anions.',
  93,options=['Loss of electrons','Gain of electrons','Sharing electrons','None'],correct='Gain of electrons')

q(4,'A',13,'mcq','When identical atoms share electrons equally, the bond is:',
  'Non-polar covalent bond','When two identical atoms share electrons equally (same electronegativity), the bond is non-polar covalent, e.g., H2, Cl2.',
  93,options=['Non-polar covalent bond','Polar covalent bond','Ionic bond','Coordinate bond'],correct='Non-polar covalent bond')

q(4,'A',14,'mcq','Synthetic resins are used where:',
  'Adhesion is required','Synthetic resins (epoxy, polyester) are used as adhesives where strong bonding between surfaces is required.',
  93,options=['Cooking','Adhesion is required','Cleaning','Fertilizer'],correct='Adhesion is required')

q(4,'A',15,'mcq','Oxygen belongs to Group VIA. Number of valence electrons:',
  '6','Group VIA (16) elements have 6 valence electrons (ns2 np4 configuration).',
  93,options=['4','5','6','7'],correct='6')

q(4,'A',16,'mcq','Unshared pairs of electrons are called:',
  'Lone pairs','Lone pairs (non-bonding pairs) are electron pairs that are not involved in bonding, e.g., 2 lone pairs on O in H2O.',
  93,options=['Bond pairs','Lone pairs','Shared pairs','Valence electrons'],correct='Lone pairs')

q(4,'A',17,'mcq','Intermolecular forces are:',
  'Weaker','Intermolecular forces (between molecules) are much weaker than intramolecular forces (within molecules/chemical bonds).',
  93,options=['Weaker','Stronger','Equal','Very strong'],correct='Weaker')

q(4,'A',18,'mcq','Ionic crystals have:',
  'High melting points','Ionic crystals have high melting points due to strong electrostatic forces between ions in the lattice.',
  93,options=['High melting points','Low melting points','Low boiling points','Soft texture'],correct='High melting points')

q(4,'A',19,'mcq','Mutual sharing of electrons between atoms forms:',
  'Covalent bond','Covalent bond is formed by mutual sharing of electron pairs between atoms.',
  93,options=['Ionic bond','Metallic bond','Covalent bond','Hydrogen bond'],correct='Covalent bond')

q(4,'A',20,'mcq','In a diagram showing same electronegativity, the bond is:',
  'A-B (equal sharing)','When two atoms have same electronegativity, electrons are shared equally, shown as A-B with equal sharing.',
  93,options=['A-B (equal sharing)','A+B-','A-B+','A=B'],correct='A-B (equal sharing)')

# Section B: Short Questions
q(4,'B',1,'short','Draw dot/cross diagrams for F with H and K.',
  'F with H (HF): F has 7 valence electrons, H has 1. They share 1 pair: H:F with 3 lone pairs on F. F with K (KF): K transfers 1 electron to F, forming K+ and F- ions. K+ has no dots, F- has 8 dots (complete octet).',
  'HF shows covalent bonding (sharing); KF shows ionic bonding (transfer).',95)

q(4,'B',2,'short','Explain octet and duplet rule.',
  'Octet rule: Atoms tend to achieve 8 electrons in valence shell (noble gas configuration) by gaining, losing, or sharing electrons. Applies to most elements. Duplet rule: Atoms tend to achieve 2 electrons in valence shell (He configuration). Applies to H, Li, Be which need only 2 electrons to complete their first shell.',
  'Octet = 8 electrons (most elements); Duplet = 2 electrons (H, Li, Be).',95)

q(4,'B',3,'short','An ion is formed by losing 3 electrons. What is its charge and which group does it belong to?',
  'Losing 3 electrons creates a +3 charge (cation). The element belongs to Group IIIA (13) which has 3 valence electrons. Example: Al loses 3 electrons to form Al3+.',
  'Group IIIA elements lose 3 electrons to form +3 ions.',95)

q(4,'B',4,'short','Why does oxygen form anion?',
  'Oxygen (Group VIA) has 6 valence electrons and needs 2 more to complete octet. It gains 2 electrons to form O2- anion, achieving Ne configuration (2, 8).',
  'Oxygen gains 2 electrons to achieve stable noble gas configuration.',95)

q(4,'B',5,'short','Differentiate between lone pair and bond pair.',
  'Lone pair: Pair of electrons not involved in bonding, belongs to one atom only. Example: 2 lone pairs on O in H2O. Bond pair: Pair of electrons shared between two atoms in a covalent bond. Example: O-H bond pairs in H2O.',
  'Lone pairs are non-bonding; bond pairs are shared in covalent bonds.',95)

q(4,'B',6,'short','Why does table salt (NaCl) have high melting point?',
  'NaCl has high melting point (801 C) because it forms a crystal lattice with strong electrostatic forces between Na+ and Cl- ions. Large amount of energy is required to break these ionic bonds.',
  'Strong ionic bonds in crystal lattice require high energy to break.',95)

q(4,'B',7,'short','How does electronegativity affect bond formation?',
  'Large electronegativity difference (>1.7): Ionic bond (electron transfer). Small difference (0.4-1.7): Polar covalent bond (unequal sharing). Zero difference: Non-polar covalent bond (equal sharing). Electronegativity determines bond type and polarity.',
  'Electronegativity difference determines whether bond is ionic, polar covalent, or non-polar covalent.',95)

q(4,'B',8,'short','Why does Mg lose 2 electrons easily?',
  'Mg (Group IIA) has 2 valence electrons (3s2). Losing both gives Mg2+ with stable Ne configuration (2, 8). The ionization energies for first 2 electrons are relatively low, and the resulting ion is stable.',
  'Losing 2 electrons gives Mg stable noble gas configuration with low energy cost.',95)

q(4,'B',9,'short','Why do metals form ionic bonds rather than covalent bonds?',
  'Metals have low ionization energies and low electronegativity. They easily lose electrons to form cations rather than sharing electrons. The resulting cations attract non-metal anions through strong electrostatic forces, forming ionic bonds.',
  'Low ionization energy makes electron loss easier than sharing.',95)

q(4,'B',10,'short','Differentiate between ion and atom.',
  'Atom: Neutral particle with equal protons and electrons. Chemically reactive (except noble gases). Ion: Charged particle formed by loss or gain of electrons. Cations (+) formed by losing electrons; anions (-) formed by gaining electrons. Ions have stable noble gas configuration.',
  'Atoms are neutral; ions are charged with stable electron configuration.',95)

q(4,'B',11,'short','What are dipole-dipole forces?',
  'Dipole-dipole forces are attractive forces between polar molecules. The positive end of one polar molecule attracts the negative end of another. Example: HCl molecules attract each other through dipole-dipole interactions. Stronger than London forces but weaker than hydrogen bonds.',
  'Dipole-dipole forces occur between polar molecules with permanent dipoles.',95)

q(4,'B',12,'short','What are the uses of adhesives?',
  'Adhesives (glues, epoxy resins) are used for: (1) Joining materials (wood, metal, plastic). (2) Construction (bonding tiles, panels). (3) Aerospace (aircraft assembly). (4) Medical (surgical adhesives). (5) Electronics (circuit bonding). (6) Automotive (body assembly).',
  'Adhesives provide strong bonding between surfaces in various industries.',95)

q(4,'B',13,'short','Differentiate between intermolecular and intramolecular forces.',
  'Intermolecular forces: Forces between molecules (weak). Include van der Waals, dipole-dipole, hydrogen bonding. Determine physical properties (mp, bp). Intramolecular forces: Forces within molecules (strong). Include ionic, covalent, metallic bonds. Determine chemical properties.',
  'Intermolecular = between molecules (weak); Intramolecular = within molecules (strong bonds).',95)

q(4,'B',14,'short','What are the characteristics of metallic bond?',
  'Metallic bond: (1) Formed by attraction between metal cations and delocalized electrons (electron sea). (2) Electrons are free to move (conductivity). (3) Malleable and ductile (layers can slide). (4) High melting points (strong bonding). (5) Lustrous (electrons reflect light).',
  'Metallic bonding involves delocalized electrons shared among all metal atoms.',95)

q(4,'B',15,'short','Why are ionic compounds hard but covalent compounds have low mp/bp?',
  'Ionic compounds: Strong electrostatic forces in crystal lattice make them hard with high mp/bp. Covalent compounds: Weak intermolecular forces between molecules require little energy to break, resulting in low mp/bp. (Note: Network covalent like diamond are exceptions with very high mp.)',
  'Ionic lattice forces are strong; covalent molecular forces are weak.',95)

q(4,'B',16,'short','What are the characteristics of ionic compounds?',
  'Characteristics: (1) Crystalline solids at room temperature. (2) High melting and boiling points. (3) Hard and brittle. (4) Conduct electricity when molten or dissolved (not as solids). (5) Soluble in polar solvents (water). (6) Form crystal lattices.',
  'Ionic compounds have characteristic physical properties due to strong ionic bonds.',95)

q(4,'B',17,'short','Why are ionic compounds solid at room temperature?',
  'Ionic compounds are solid because strong electrostatic forces between oppositely charged ions form a rigid crystal lattice. Large amount of energy is needed to overcome these forces and melt the solid.',
  'Strong ionic bonds in crystal lattice keep ions in fixed positions at room temperature.',95)

q(4,'B',18,'short','What are the effects of hydrogen bonding?',
  'Effects: (1) High boiling points (water bp 100 C vs H2S bp -60 C). (2) High surface tension of water. (3) Ice floats on water (lower density). (4) DNA double helix structure. (5) Protein secondary structure. (6) High viscosity of glycerol.',
  'Hydrogen bonding significantly affects physical properties of compounds.',95)

q(4,'B',19,'short','Complete the chart for elements with atomic numbers 11-16.',
  'Na(11): Group IA, Period 3, Metal, 1 valence e-. Mg(12): Group IIA, Period 3, Metal, 2 valence e-. Al(13): Group IIIA, Period 3, Metal, 3 valence e-. Si(14): Group IVA, Period 3, Metalloid, 4 valence e-. P(15): Group VA, Period 3, Non-metal, 5 valence e-. S(16): Group VIA, Period 3, Non-metal, 6 valence e-.',
  'Elements 11-16 span Period 3 from metal to non-metal.',95)

# Section C: Detailed Questions
q(4,'C',1,'detailed','Explain ionic bond and formation of NaCl.',
  'Ionic bond: Electrostatic attraction between cation and anion formed by electron transfer. NaCl formation: Na (2,8,1) loses 1 electron to become Na+ (2,8). Cl (2,8,7) gains 1 electron to become Cl- (2,8,8). Na+ and Cl- attract each other through electrostatic forces, forming ionic bond. The resulting NaCl crystal lattice has each Na+ surrounded by 6 Cl- and vice versa.',
  'Ionic bonding involves complete electron transfer and electrostatic attraction.',96)

q(4,'C',2,'detailed','Why are elements stable?',
  'Elements achieve stability by attaining noble gas electron configuration (complete octet/duplet). This can be done by: (1) Losing electrons (metals form cations). (2) Gaining electrons (non-metals form anions). (3) Sharing electrons (covalent bonding). Noble gases are already stable with complete valence shells.',
  'Stability comes from achieving noble gas electron configuration.',96)

q(4,'C',3,'detailed','Explain covalent bond formation and single, double, triple bonds.',
  'Covalent bond: Formed by mutual sharing of electron pairs between non-metal atoms. Single bond: 1 shared pair (2 electrons), e.g., H-H, H-Cl. Double bond: 2 shared pairs (4 electrons), e.g., O=O, C=O. Triple bond: 3 shared pairs (6 electrons), e.g., N triple bond N, C triple bond C. More shared pairs = stronger, shorter bond.',
  'Covalent bonds vary in strength based on number of shared electron pairs.',96)

q(4,'C',4,'detailed','Show electron arrangement in molecules: H2O, N2, CH4, C2H2, Cl2, H2.',
  'H2O: O shares 1 pair with each H, 2 lone pairs on O. N2: N triple bond N, 1 lone pair on each N. CH4: C shares 1 pair with each of 4 H atoms. C2H2: C triple bond C, each C shares 1 pair with H. Cl2: Cl-Cl single bond, 3 lone pairs on each Cl. H2: H-H single bond.',
  'Electron arrangement shows how atoms share electrons to achieve stable configuration.',96)

q(4,'C',5,'detailed','Explain metallic bond.',
  'Metallic bond: Attraction between metal cations and delocalized valence electrons (electron sea model). Metal atoms lose valence electrons which become free to move throughout the metal lattice. The positive metal ions are held together by the sea of delocalized electrons. Properties: conductivity (free electrons), malleability (layers slide), ductility, luster (electrons reflect light), high mp (strong bonding).',
  'Metallic bonding involves delocalized electrons shared among all metal cations.',96)

q(4,'C',6,'detailed','What is coordinate covalent bond?',
  'Coordinate covalent bond (dative bond): A covalent bond where both shared electrons come from one atom (donor). The donor atom has a lone pair; the acceptor has an empty orbital. Example: NH3 + H+ forms NH4+ (N donates lone pair to H+). Another example: H2O + H+ forms H3O+. Once formed, it is identical to a regular covalent bond.',
  'Coordinate bond differs only in formation; once formed it is like any covalent bond.',96)

q(4,'C',7,'detailed','Explain ionic character of covalent bond.',
  'No bond is 100% ionic or 100% covalent. When electronegativity difference is large (>1.7), bond is mostly ionic. When small (<0.4), bond is mostly covalent. Intermediate differences (0.4-1.7) give polar covalent bonds with partial ionic character. Example: HCl has polar covalent bond with partial charges H(delta+)Cl(delta-).',
  'Bond character exists on a spectrum from pure covalent to pure ionic.',96)

q(4,'C',8,'detailed','Differentiate between polar and non-polar covalent bonds.',
  'Non-polar covalent: Equal sharing of electrons between atoms with same/similar electronegativity. No charge separation. Example: H2, Cl2, CH4. Polar covalent: Unequal sharing due to electronegativity difference. Creates partial charges (dipole). Example: HCl (H+Cl-), H2O (bent shape with O negative, H positive).',
  'Polarity depends on electronegativity difference between bonded atoms.',96)

q(4,'C',9,'detailed','What is the importance of glues and epoxy resins?',
  'Glues and epoxy resins are important adhesives used for: (1) Strong bonding of materials (metal, wood, plastic, glass). (2) Construction and repair work. (3) Aerospace industry (aircraft assembly). (4) Medical applications (dental fillings, surgical adhesives). (5) Electronics (circuit board assembly). (6) Automotive industry. Epoxy resins form very strong, durable bonds resistant to heat and chemicals.',
  'Adhesives provide versatile bonding solutions across many industries.',96)

# ============================================================
# CHAPTER 5: Physical States of Matter (PDF pages 121-122)
# ============================================================
# Section A: MCQs
q(5,'A',1,'mcq','The fastest diffusing gas is:',
  'Hydrogen','Hydrogen (H2) has the lowest molecular mass (2 g/mol), so it diffuses fastest according to Graham law.',
  121,options=['Hydrogen','Oxygen','Nitrogen','Carbon dioxide'],correct='Hydrogen')

q(5,'A',2,'mcq','Vapour pressure increases with:',
  'Increase of temperature','Vapour pressure increases with temperature because more molecules have enough energy to escape from liquid surface.',
  121,options=['Decrease of temperature','Increase of temperature','Increase of volume','Decrease of volume'],correct='Increase of temperature')

q(5,'A',3,'mcq','Freezing point depends on:',
  'Nature of liquid','Freezing point is a characteristic property that depends on the nature of the liquid substance.',
  121,options=['Nature of liquid','Volume of liquid','Shape of container','Amount of liquid'],correct='Nature of liquid')

q(5,'A',4,'mcq','One atmospheric pressure equals:',
  '101325 Pascal','Standard atmospheric pressure = 1 atm = 760 mmHg = 101325 Pa = 101.325 kPa.',
  121,options=['760 Pascal','1000 Pascal','101325 Pascal','100000 Pascal'],correct='101325 Pascal')

q(5,'A',5,'mcq','Which does not affect boiling point?',
  'Initial temperature of liquid','Boiling point depends on atmospheric pressure, nature of liquid, and impurities, but not on initial temperature.',
  121,options=['Atmospheric pressure','Nature of liquid','Initial temperature of liquid','Impurities'],correct='Initial temperature of liquid')

q(5,'A',6,'mcq','Liquid mobility is lesser than:',
  'Gases','Liquids have less mobility than gases because liquid molecules are closer together with stronger intermolecular forces.',
  121,options=['Solids','Gases','Plasma','Crystals'],correct='Gases')

q(5,'A',7,'mcq','Solids with sharp melting point are:',
  'Diamond','Diamond is a crystalline solid with sharp melting point. Crystalline solids have definite melting points; amorphous solids do not.',
  121,options=['Glass','Rubber','Plastic','Diamond'],correct='Diamond')

q(5,'A',8,'mcq','The lightest form of matter is:',
  'Gases','Gases are the lightest state of matter with lowest density because molecules are far apart with weak intermolecular forces.',
  121,options=['Solids','Liquids','Gases','Plasma'],correct='Gases')

q(5,'A',9,'mcq','During evaporation, molecules leave the surface because:',
  'Energy is high','Molecules with high kinetic energy overcome intermolecular forces and escape from liquid surface during evaporation.',
  121,options=['Energy is low','Energy is high','Pressure is high','Temperature is low'],correct='Energy is high')

q(5,'A',10,'mcq','Gas density increases when:',
  'Pressure increased','Increasing pressure compresses gas molecules closer together, increasing density (mass per unit volume).',
  121,options=['Pressure increased','Temperature increased','Volume increased','Pressure decreased'],correct='Pressure increased')

# Section B: Short Questions
q(5,'B',1,'short','What is allotropy? Give examples.',
  'Allotropy is the existence of an element in two or more different forms (allotropes) in the same physical state. Examples: Carbon exists as diamond, graphite, and fullerene. Oxygen exists as O2 (oxygen) and O3 (ozone). Phosphorus exists as white, red, and black phosphorus.',
  'Allotropes have different structures and properties but same chemical composition.',122)

q(5,'B',2,'short','What is effusion?',
  'Effusion is the process by which gas molecules escape through a tiny hole into a vacuum or lower pressure region. Graham law: Rate of effusion is inversely proportional to square root of molar mass. Lighter gases effuse faster. Example: H2 effuses faster than O2.',
  'Effusion differs from diffusion: effusion is through a small hole; diffusion is mixing of gases.',122)

q(5,'B',3,'short','Define boiling point, melting point, and freezing point.',
  'Boiling point: Temperature at which liquid vapour pressure equals atmospheric pressure. Melting point: Temperature at which solid changes to liquid. Freezing point: Temperature at which liquid changes to solid. Melting point and freezing point of a substance are the same temperature.',
  'These are characteristic temperatures for phase changes.',122)

q(5,'B',4,'short','What is density of liquid?',
  'Density of liquid is mass per unit volume (d = m/V). It depends on temperature (decreases with increasing temperature) and nature of liquid. Water has maximum density at 4 C (1 g/cm3). Density determines whether objects float or sink.',
  'Liquid density is typically between solid and gas densities.',122)

q(5,'B',5,'short','Give examples of plasma.',
  'Plasma examples: (1) Sun and stars (ionized gases at high temperature). (2) Neon signs (ionized noble gases). (3) Lightning (ionized air). (4) Fluorescent tubes. (5) Plasma TV screens. (6) Solar wind. Plasma is the most abundant state of matter in the universe.',
  'Plasma is ionized gas with free electrons and ions, found at very high temperatures.',122)

q(5,'B',6,'short','What is Bose-Einstein condensate?',
  'Bose-Einstein condensate (BEC) is a state of matter formed at temperatures near absolute zero (0 K or -273 C). Atoms lose individual identity and behave as a single quantum entity. Predicted by Bose and Einstein, first created in 1995. Atoms occupy the same quantum state.',
  'BEC is the fifth state of matter, occurring at extremely low temperatures.',122)

q(5,'B',7,'short','State the postulates of kinetic molecular theory of gases.',
  'Postulates: (1) Gases consist of tiny particles (molecules/atoms) in constant random motion. (2) Volume of gas molecules is negligible compared to container volume. (3) No intermolecular forces (ideal gas). (4) Collisions are perfectly elastic (no energy loss). (5) Average kinetic energy is proportional to absolute temperature. (6) Pressure is due to molecular collisions with container walls.',
  'Kinetic molecular theory explains gas behavior based on molecular motion.',122)

# Section C: Detailed Questions
q(5,'C',1,'detailed','Describe evaporation and factors affecting it.',
  'Evaporation: Process where liquid molecules at surface gain enough energy to escape into vapour phase. It occurs at all temperatures (below boiling point). Factors: (1) Temperature - higher temp increases evaporation. (2) Surface area - larger area increases rate. (3) Humidity - lower humidity increases evaporation. (4) Wind speed - faster wind increases evaporation. (5) Nature of liquid - volatile liquids evaporate faster.',
  'Evaporation is a surface phenomenon that cools the remaining liquid.',122)

q(5,'C',2,'detailed','State and explain Boyle law.',
  'Boyle law: At constant temperature, volume of a given mass of gas is inversely proportional to its pressure. V is proportional to 1/P, or PV = constant. P1V1 = P2V2. Explanation: Increasing pressure pushes gas molecules closer, reducing volume. Graph: P vs V is hyperbola; P vs 1/V is straight line.',
  'Boyle law describes inverse relationship between pressure and volume at constant temperature.',122)

q(5,'C',3,'detailed','Differentiate between amorphous and crystalline solids.',
  'Crystalline solids: Regular, ordered arrangement of particles (crystal lattice). Sharp melting point. Anisotropic (properties vary with direction). Examples: NaCl, diamond, quartz. Amorphous solids: Irregular, random arrangement. No sharp melting point (soften over range). Isotropic (same properties in all directions). Examples: glass, rubber, plastic.',
  'Crystalline solids have ordered structure; amorphous solids have disordered structure.',122)

q(5,'C',4,'detailed','State and explain Charles law.',
  'Charles law: At constant pressure, volume of a given mass of gas is directly proportional to its absolute temperature. V is proportional to T, or V/T = constant. V1/T1 = V2/T2. Temperature must be in Kelvin. Explanation: Increasing temperature increases molecular kinetic energy, causing gas to expand.',
  'Charles law describes direct relationship between volume and temperature at constant pressure.',122)

q(5,'C',5,'detailed','Describe diffusion in liquids.',
  'Diffusion in liquids: Movement of liquid molecules from region of higher concentration to lower concentration. Slower than gas diffusion because liquid molecules are closer together with stronger intermolecular forces. Example: Ink spreading in water. Rate depends on: temperature (faster at higher temp), molecular size (smaller diffuses faster), viscosity (lower viscosity = faster).',
  'Liquid diffusion is slower than gas diffusion due to stronger intermolecular forces.',122)

q(5,'C',6,'detailed','What factors affect boiling point?',
  'Factors: (1) Atmospheric pressure - higher pressure increases boiling point (pressure cooker). (2) Nature of liquid - different liquids have different boiling points. (3) Impurities - dissolved substances increase boiling point (boiling point elevation). (4) Intermolecular forces - stronger forces = higher boiling point. Example: Water bp 100 C at 1 atm, but lower at high altitudes.',
  'Boiling point varies with pressure, purity, and intermolecular forces.',122)

q(5,'C',7,'detailed','What is vapour pressure?',
  'Vapour pressure: Pressure exerted by vapour molecules in equilibrium with liquid in a closed container. At equilibrium, rate of evaporation = rate of condensation. Vapour pressure increases with temperature (more molecules escape). Liquids with high vapour pressure are volatile (evaporate easily). Boiling occurs when vapour pressure = atmospheric pressure.',
  'Vapour pressure is a measure of liquid tendency to evaporate.',122)

# Section D: Numericals
q(5,'D',1,'numerical','Convert temperatures: (a) 100 C to K (b) 150 C to K (c) 780 K to C (d) 170 K to C.',
  '(a) 100 C = 100 + 273 = 373 K. (b) 150 C = 150 + 273 = 423 K. (c) 780 K = 780 - 273 = 507 C. (d) 170 K = 170 - 273 = -103 C.',
  'K = C + 273; C = K - 273.',122)

q(5,'D',2,'numerical','Using Charles law: V1=90.5, V2=120, T1=33 C. Find T2.',
  'T1 = 33 + 273 = 306 K. V1/T1 = V2/T2, so T2 = V2 x T1/V1 = 120 x 306/90.5 = 405.3 K = 132.3 C.',
  'Charles law: V1/T1 = V2/T2 (temperature in Kelvin).',122)

q(5,'D',3,'numerical','Using Charles law: V=78 ml at 35 C. Find V2 at 80 C.',
  'T1 = 35 + 273 = 308 K, T2 = 80 + 273 = 353 K. V1/T1 = V2/T2, so V2 = V1 x T2/T1 = 78 x 353/308 = 89.4 ml.',
  'Volume increases with temperature at constant pressure.',122)

q(5,'D',4,'numerical','Using Boyle law: V=40 dm3 at 1 atm. Find V2 at 3 atm.',
  'P1V1 = P2V2, so V2 = P1V1/P2 = 1 x 40/3 = 13.33 dm3.',
  'Volume decreases as pressure increases (inverse relationship).',122)

q(5,'D',5,'numerical','Using Boyle law: V=800 cm3 at P=750 mm. Find P2 when V=250 cm3.',
  'P1V1 = P2V2, so P2 = P1V1/V2 = 750 x 800/250 = 2400 mm Hg.',
  'Pressure increases as volume decreases.',122)

q(5,'D',6,'numerical','Using Boyle law: P=8 atm, V=15 L. Find V2 when P=6 atm.',
  'P1V1 = P2V2, so V2 = P1V1/P2 = 8 x 15/6 = 20 L.',
  'Volume increases as pressure decreases.',122)

# ============================================================
# CHAPTER 6: Solutions (PDF pages 143-146)
# ============================================================
# Section A: MCQs
q(6,'A',1,'mcq','Alloy is a homogeneous mixture of:',
  'Two solids','An alloy is a homogeneous mixture of two or more metals (or metal and non-metal) in solid state.',
  143,options=['Two solids','Two liquids','Two gases','Solid and liquid'],correct='Two solids')

q(6,'A',2,'mcq','Saturated KCl solution on heating becomes:',
  'Unsaturated','Heating a saturated solution increases solubility, making it unsaturated as more solute can now dissolve.',
  143,options=['Unsaturated','Supersaturated','Saturated','Dilute'],correct='Unsaturated')

q(6,'A',3,'mcq','Sand in water is an example of:',
  'Suspension','Sand in water forms a suspension - heterogeneous mixture with large particles that settle down.',
  143,options=['Solution','Suspension','Colloid','Emulsion'],correct='Suspension')

q(6,'A',4,'mcq','Solubility is defined per ___ grams of solvent:',
  '100','Solubility is the amount of solute (in grams) that dissolves in 100 grams of solvent at a given temperature.',
  143,options=['50','100','200','1000'],correct='100')

q(6,'A',5,'mcq','Which is a heterogeneous mixture?',
  'Sand and water','Sand and water form a heterogeneous mixture (suspension) where components are not uniformly distributed.',
  143,options=['Salt in water','Sand and water','Sugar in water','Alcohol in water'],correct='Sand and water')

q(6,'A',6,'mcq','2 moles of NaCl equals:',
  '117 grams','Molar mass of NaCl = 23 + 35.5 = 58.5 g/mol. 2 moles = 2 x 58.5 = 117 grams.',
  143,options=['58.5 grams','100 grams','116 grams','117 grams'],correct='117 grams')

q(6,'A',7,'mcq','Molarity of 40g NaCl in 500 cm3 solution:',
  '1.4 M','Moles of NaCl = 40/58.5 = 0.684 mol. Volume = 500 cm3 = 0.5 L. Molarity = 0.684/0.5 = 1.37 M approx 1.4 M.',
  143,options=['1.4 M','2.0 M','0.7 M','1.0 M'],correct='1.4 M')

q(6,'A',8,'mcq','In 10% w/w sugar solution, amount of water is:',
  '90 g of water','10% w/w means 10g sugar in 100g solution. Water = 100 - 10 = 90g.',
  143,options=['90 g of water','100 g of water','10 g of water','110 g of water'],correct='90 g of water')

q(6,'A',9,'mcq','Which is a true solution?',
  'Ink in water','Ink in water forms a true solution - homogeneous mixture with very small particles that do not scatter light.',
  143,options=['Starch in water','Soap in water','Ink in water','Toothpaste'],correct='Ink in water')

q(6,'A',10,'mcq','Which solution has the most water?',
  '0.25 M','Most dilute solution (0.25 M) has the most water per mole of solute.',
  143,options=['1.0 M','0.5 M','0.75 M','0.25 M'],correct='0.25 M')

q(6,'A',11,'mcq','When saturated solution is diluted, it becomes:',
  'Unsaturated solution','Adding solvent (diluting) to a saturated solution makes it unsaturated as concentration decreases below saturation point.',
  143,options=['Saturated solution','Unsaturated solution','Supersaturated','Precipitate forms'],correct='Unsaturated solution')

q(6,'A',12,'mcq','Butter is an example of:',
  'Liquid in solid','Butter is an emulsion of liquid fat droplets dispersed in solid matrix - liquid in solid colloid.',
  143,options=['Solid in liquid','Liquid in liquid','Liquid in solid','Gas in liquid'],correct='Liquid in solid')

q(6,'A',13,'mcq','Solid solute in liquid solvent is:',
  'Solids in liquid','When solid dissolves in liquid, it forms a solid-in-liquid solution. Example: salt in water.',
  143,options=['Liquids in liquid','Gases in liquid','Solids in solid','Solids in liquid'],correct='Solids in liquid')

q(6,'A',14,'mcq','Particle size in suspension is:',
  'Greater than 1000 nm','Suspension particles are larger than 1000 nm (10^3 nm), visible to naked eye, and settle down.',
  143,options=['Less than 1 nm','1-100 nm','100-1000 nm','Greater than 1000 nm'],correct='Greater than 1000 nm')

q(6,'A',15,'mcq','Give examples of each type of solution.',
  'Solid-Liquid: Salt in water. Gas-Gas: Air. Solid-Solid: Alloys (brass). Liquid-Solid: Amalgam (Hg in metal). Liquid-Gas: Humidity. Liquid-Liquid: Alcohol in water.',
  'Solutions can involve any combination of states.',143)

# Section B: Short Questions
q(6,'B',1,'short','Explain solute-solvent interaction in NaCl solution.',
  'When NaCl dissolves in water, water molecules (polar) surround Na+ and Cl- ions. Oxygen end (negative) of water attracts Na+; hydrogen end (positive) attracts Cl-. This ion-dipole interaction overcomes ionic bonds in NaCl crystal, dissolving it.',
  'Water polarity enables it to dissolve ionic compounds through ion-dipole interactions.',145)

q(6,'B',2,'short','Differentiate between saturated and unsaturated solution.',
  'Saturated solution: Contains maximum amount of solute that can dissolve at a given temperature. No more solute can dissolve. Unsaturated solution: Contains less solute than maximum capacity. More solute can still dissolve.',
  'Saturation depends on temperature and nature of solute/solvent.',145)

q(6,'B',3,'short','Define solution and its components.',
  'Solution: Homogeneous mixture of two or more substances. Components: Solute (substance being dissolved, present in smaller amount) and Solvent (substance doing the dissolving, present in larger amount). Example: Salt water - salt is solute, water is solvent.',
  'Solutions are homogeneous; solute dissolves in solvent.',145)

q(6,'B',4,'short','What is mass/volume percent?',
  'Mass/volume percent (m/v%): Mass of solute (g) per 100 mL of solution. Formula: (mass of solute/volume of solution) x 100. Example: 5% m/v NaCl means 5g NaCl in 100 mL solution.',
  'm/v% is commonly used in medicine and biology.',145)

q(6,'B',5,'short','What is one molar solution?',
  'One molar (1 M) solution contains 1 mole of solute dissolved in 1 liter (1000 cm3) of solution. Example: 1 M NaCl = 58.5g NaCl in 1 L solution.',
  'Molarity = moles of solute per liter of solution.',145)

q(6,'B',6,'short','What is Tyndall effect in colloidal solutions?',
  'Tyndall effect: Scattering of light by colloidal particles. When light beam passes through colloid, path becomes visible due to light scattering. Not seen in true solutions (particles too small). Example: Headlight beams visible in fog.',
  'Tyndall effect distinguishes colloids from true solutions.',145)

q(6,'B',7,'short','Define dilution, concentration, solubility, and molarity.',
  'Dilution: Adding solvent to decrease concentration. Concentration: Amount of solute per unit volume/mass of solution. Solubility: Maximum amount of solute that dissolves in 100g solvent at given temperature. Molarity: Moles of solute per liter of solution (mol/L).',
  'These terms describe different aspects of solution composition.',145)

q(6,'B',8,'short','Why do polar and ionic substances dissolve in polar solvents?',
  'Polar solvents (like water) have partial charges that attract ions and polar molecules. Ion-dipole and dipole-dipole interactions between solute and solvent overcome solute-solute and solvent-solvent forces, allowing dissolution.',
  'Like dissolves like: polar dissolves polar and ionic.',145)

q(6,'B',9,'short','Why do polar substances not dissolve in nonpolar solvents?',
  'Polar substances have strong dipole-dipole or ionic interactions. Nonpolar solvents only have weak London forces. The solvent cannot overcome the strong solute-solute interactions, so polar substances do not dissolve in nonpolar solvents.',
  'Polar and nonpolar substances are immiscible due to different intermolecular forces.',145)

q(6,'B',10,'short','How are solutions beneficial for the community?',
  'Solutions are beneficial in: (1) Medicine - IV fluids, syrups, disinfectants. (2) Agriculture - fertilizers, pesticides in solution. (3) Industry - chemical reactions in solution. (4) Food - beverages, cooking. (5) Cleaning - detergents, soaps in water. (6) Environment - natural water cycles.',
  'Solutions are essential in daily life, industry, and nature.',145)

q(6,'B',11,'short','Why does salt dissolve in water?',
  'Salt (NaCl) dissolves in water because water is polar. Water molecules surround Na+ and Cl- ions through ion-dipole interactions, overcoming the ionic bonds in NaCl crystal lattice. The hydration energy released is greater than lattice energy.',
  'Water polarity and ion-dipole interactions enable salt dissolution.',145)

q(6,'B',12,'short','Why is air considered a solution with gas as solvent?',
  'Air is a homogeneous mixture of gases (N2 78%, O2 21%, others 1%). Nitrogen is the solvent (present in largest amount), and other gases are solutes. All components are in gas phase, making it a gas-gas solution.',
  'Air is a gas-gas solution with nitrogen as the solvent.',145)

q(6,'B',13,'short','Why does gasoline not dissolve in water?',
  'Gasoline is nonpolar (hydrocarbon mixture). Water is polar. Nonpolar gasoline cannot form favorable interactions with polar water molecules. Water molecules prefer to hydrogen bond with each other rather than interact with gasoline. Like dissolves like.',
  'Nonpolar and polar substances are immiscible.',145)

# Section C: Detailed Questions
q(6,'C',1,'detailed','How to prepare dilute solution from concentrated solution?',
  'Use dilution formula: M1V1 = M2V2. Steps: (1) Calculate volume of concentrated solution needed (V1 = M2V2/M1). (2) Measure V1 of concentrated solution. (3) Add to volumetric flask. (4) Add distilled water to make total volume V2. (5) Mix well. Example: To make 500 mL of 0.1 M from 1 M: V1 = 0.1 x 500/1 = 50 mL.',
  'Dilution reduces concentration by adding solvent; moles of solute remain constant.',146)

q(6,'C',2,'detailed','Explain solubility and effect of nature of solute and solvent.',
  'Solubility: Maximum amount of solute that dissolves in 100g solvent at given temperature. Nature of solute and solvent: Like dissolves like. Polar solutes dissolve in polar solvents (salt in water). Nonpolar solutes dissolve in nonpolar solvents (oil in benzene). Ionic compounds dissolve in polar solvents. Temperature and pressure also affect solubility.',
  'Solubility depends on solute-solvent interactions and conditions.',146)

q(6,'C',3,'detailed','How does solubility increase with temperature?',
  'For most solids in liquids: Solubility increases with temperature because dissolution is endothermic (absorbs heat). Higher temperature provides more energy to break solute-solute bonds. Example: More sugar dissolves in hot water than cold. Exception: Some salts (Ce2(SO4)3) have decreasing solubility with temperature.',
  'Temperature effect depends on whether dissolution is endothermic or exothermic.',146)

q(6,'C',4,'detailed','Explain attraction of Na+ and Cl- to water molecules.',
  'Water is polar with partial negative charge on O and partial positive on H. Na+ (positive) is attracted to O end of water molecules. Cl- (negative) is attracted to H end of water molecules. This ion-dipole interaction forms hydration shells around ions, stabilizing them in solution and overcoming lattice energy.',
  'Ion-dipole interactions between water and ions enable dissolution.',146)

q(6,'C',5,'detailed','Explain like dissolves like principle.',
  'Like dissolves like: Substances with similar intermolecular forces dissolve in each other. Polar dissolves polar (salt in water). Nonpolar dissolves nonpolar (oil in benzene). Polar does not dissolve nonpolar (oil not in water). Reason: Similar intermolecular forces allow solute-solvent interactions to replace solute-solute and solvent-solvent interactions.',
  'Similar polarity and intermolecular forces enable dissolution.',146)

q(6,'C',6,'detailed','Differentiate between solution, colloids, and suspension.',
  'Solution: Homogeneous, particle size <1 nm, does not scatter light, particles do not settle, passes through filter paper. Example: Salt water. Colloid: Heterogeneous (appears homogeneous), particle size 1-1000 nm, shows Tyndall effect, particles do not settle, passes through filter paper. Example: Milk. Suspension: Heterogeneous, particle size >1000 nm, particles visible, settle down, does not pass through filter paper. Example: Muddy water.',
  'Classification based on particle size and properties.',146)

# ============================================================
# CHAPTER 7: Electrochemistry (PDF pages 162-163)
# ============================================================
# Section A: MCQs
q(7,'A',1,'mcq','Alloy of Cu and Sn is:',
  'Bronze','Bronze is an alloy of copper (Cu) and tin (Sn), known for hardness and corrosion resistance.',
  162,options=['Brass','Bronze','Steel','Solder'],correct='Bronze')

q(7,'A',2,'mcq','Which of the following is an alloy?',
  'Steel','Steel is an alloy of iron and carbon (with other elements). Brass and bronze are also alloys.',
  162,options=['Iron','Copper','Steel','Zinc'],correct='Steel')

q(7,'A',3,'mcq','1 Faraday equals:',
  '96500 C','1 Faraday = charge of 1 mole of electrons = 96500 Coulombs (approximately).',
  162,options=['9650 C','96500 C','965000 C','965 C'],correct='96500 C')

q(7,'A',4,'mcq','Which is a non-electrolyte?',
  'Urea','Urea (CO(NH2)2) does not ionize in water and does not conduct electricity, making it a non-electrolyte.',
  162,options=['NaCl','HCl','NaOH','Urea'],correct='Urea')

q(7,'A',5,'mcq','Which is an oxidizing agent?',
  'Cl2','Cl2 is an oxidizing agent because it accepts electrons (gets reduced) from other substances.',
  162,options=['Na','H2','Cl2','Mg'],correct='Cl2')

q(7,'A',6,'mcq','Which is a reducing agent?',
  'Al','Aluminum is a reducing agent because it donates electrons (gets oxidized) to other substances.',
  162,options=['Cl2','O2','Al','F2'],correct='Al')

q(7,'A',7,'mcq','Which is a weak electrolyte?',
  'CH3COOH','Acetic acid (CH3COOH) partially ionizes in water, making it a weak electrolyte.',
  162,options=['HCl','NaCl','NaOH','CH3COOH'],correct='CH3COOH')

q(7,'A',8,'mcq','Cathode of dry cell is:',
  'Graphite','In a dry cell (Leclanche cell), the cathode is a graphite (carbon) rod surrounded by MnO2.',
  162,options=['Zinc','Copper','Iron','Graphite'],correct='Graphite')

q(7,'A',9,'mcq','1 gram equivalent weight of Al is:',
  '9 g','Al has valency 3 and atomic mass 27. Equivalent weight = 27/3 = 9 g.',
  162,options=['9 g','18 g','27 g','3 g'],correct='9 g')

q(7,'A',10,'mcq','Which statement is correct?',
  'Reduction occurs at cathode','In electrochemical cells, reduction (gain of electrons) always occurs at cathode. Oxidation occurs at anode.',
  162,options=['Oxidation occurs at cathode','Reduction occurs at anode','Reduction occurs at cathode','Ions lose electrons at cathode'],correct='Reduction occurs at cathode')

# Section B: Short Questions
q(7,'B',1,'short','Define oxidation and reduction reactions with examples.',
  'Oxidation: Loss of electrons or increase in oxidation number. Example: Na loses electron to become Na+ (oxidation). Reduction: Gain of electrons or decrease in oxidation number. Example: Cl2 gains electrons to become 2Cl- (reduction). OIL RIG: Oxidation Is Loss, Reduction Is Gain (of electrons).',
  'Oxidation and reduction always occur together (redox reactions).',163)

q(7,'B',2,'short','Why do ionic compounds conduct electricity in molten or aqueous solutions only?',
  'In solid state, ions are fixed in crystal lattice and cannot move. In molten state or aqueous solution, ions are free to move and carry electric current. Mobile ions are required for electrical conductivity.',
  'Free mobile ions are needed for electrical conduction.',163)

q(7,'B',3,'short','What is electrolytic cell? Explain with diagram.',
  'Electrolytic cell: Device that uses electrical energy to drive non-spontaneous chemical reaction (electrolysis). Components: (1) Power source (battery). (2) Two electrodes (anode +, cathode -). (3) Electrolyte (ionic solution/molten salt). At anode: oxidation occurs. At cathode: reduction occurs. Example: Electrolysis of water produces H2 and O2.',
  'Electrolytic cells convert electrical energy to chemical energy.',163)

q(7,'B',4,'short','Define oxidizing and reducing agent with examples.',
  'Oxidizing agent: Substance that accepts electrons (gets reduced) and oxidizes another substance. Example: Cl2, O2, KMnO4. Reducing agent: Substance that donates electrons (gets oxidized) and reduces another substance. Example: Na, H2, Al.',
  'Oxidizing agent gets reduced; reducing agent gets oxidized.',163)

q(7,'B',5,'short','Examine chemical equations and identify oxidizing agent, reducing agent, substance oxidized, substance reduced.',
  '(1) Zn + Cl2 to ZnCl2: Zn oxidized (loses e-), Cl2 reduced (gains e-). Reducing agent: Zn. Oxidizing agent: Cl2. (2) Br2 + H2S to 2HBr + S: H2S oxidized (S loses e-), Br2 reduced. Reducing agent: H2S. Oxidizing agent: Br2. (3) 2Ca + O2 to 2CaO: Ca oxidized, O2 reduced. (4) 2Li + S to Li2S: Li oxidized, S reduced.',
  'Identify by tracking electron transfer and oxidation number changes.',163)

q(7,'B',6,'short','Identify the alloy: Cu-Zn, Cu-Al-Mg-Ni, Cu-Zn-Sn.',
  'Cu-Zn: Brass (used in musical instruments, decorations). Cu-Al-Mg-Ni: Aluminum bronze (used in aircraft parts, marine hardware). Cu-Zn-Sn: Gunmetal (used in guns, bearings, valves).',
  'Different alloy compositions give different properties and uses.',163)

# Section C: Detailed Questions
q(7,'C',1,'detailed','Describe the dry cell with diagram.',
  'Dry cell (Leclanche cell): Primary cell (non-rechargeable). Anode: Zinc container (negative terminal). Cathode: Graphite rod (positive terminal) surrounded by MnO2. Electrolyte: NH4Cl paste. Reactions: Anode: Zn to Zn2+ + 2e- (oxidation). Cathode: 2MnO2 + 2NH4+ + 2e- to Mn2O3 + 2NH3 + H2O (reduction). Voltage: 1.5V. Used in torches, radios, clocks.',
  'Dry cell is a portable primary battery.',163)

q(7,'C',2,'detailed','What is battery? How does lead storage battery work?',
  'Battery: Combination of two or more cells connected together. Lead storage battery (car battery): Rechargeable secondary cell. Anode: Pb. Cathode: PbO2. Electrolyte: H2SO4. Discharging: Pb + PbO2 + 2H2SO4 to 2PbSO4 + 2H2O. Charging: Reverse reaction. Each cell produces 2V; car battery has 6 cells = 12V.',
  'Lead storage battery is rechargeable and used in automobiles.',163)

q(7,'C',3,'detailed','Explain process of electrolysis in electrolytic cell.',
  'Electrolysis: Decomposition of electrolyte by passing electric current. Process: (1) Connect electrodes to power source. (2) Anode (+): Oxidation occurs, anions lose electrons. (3) Cathode (-): Reduction occurs, cations gain electrons. (4) Ions move toward opposite electrodes. Example: Electrolysis of molten NaCl produces Na metal at cathode and Cl2 gas at anode.',
  'Electrolysis converts electrical energy to chemical change.',163)

q(7,'C',4,'detailed','What is alloy? Explain its classification with examples.',
  'Alloy: Homogeneous mixture of two or more metals (or metal and non-metal). Classification: (1) Substitutional alloy: Atoms of similar size replace each other. Example: Brass (Cu-Zn). (2) Interstitial alloy: Small atoms fit between larger atoms. Example: Steel (Fe-C). Properties: Alloys are harder, stronger, more corrosion resistant than pure metals.',
  'Alloys have improved properties compared to pure metals.',163)

q(7,'C',5,'detailed','What is rusting? How can it be prevented?',
  'Rusting: Corrosion of iron in presence of oxygen and moisture. Reaction: 4Fe + 3O2 + 6H2O to 4Fe(OH)3 (rust). Prevention: (1) Painting/coating. (2) Galvanizing (coating with Zn). (3) Alloying (stainless steel). (4) Cathodic protection. (5) Keeping dry. (6) Using rust inhibitors.',
  'Rusting requires both oxygen and moisture; preventing either stops rusting.',163)

q(7,'C',6,'detailed','What is electroplating? How can steel be electroplated with Tin, Zinc, and Silver?',
  'Electroplating: Coating metal object with thin layer of another metal using electrolysis. Object is cathode; coating metal is anode; electrolyte contains coating metal ions. Tin plating: Steel cathode, Sn anode, SnSO4 electrolyte. Zinc plating (galvanizing): Steel cathode, Zn anode, ZnSO4 electrolyte. Silver plating: Steel cathode, Ag anode, AgNO3 electrolyte.',
  'Electroplating provides corrosion resistance and decorative finish.',163)

q(7,'C',7,'detailed','State and explain Faraday first and second law of electrolysis.',
  'First law: Mass of substance deposited/liberated at electrode is directly proportional to quantity of electricity passed. m = ZIt (Z = electrochemical equivalent). Second law: When same quantity of electricity passes through different electrolytes, masses deposited are proportional to their chemical equivalent weights. m1/m2 = E1/E2. 1 Faraday (96500 C) deposits 1 gram equivalent.',
  'Faraday laws quantify the relationship between electricity and chemical change.',163)

# ============================================================
# CHAPTER 8: Chemical Reactivity (PDF pages 185-186)
# ============================================================
# Section A: MCQs
q(8,'A',1,'mcq','Which is an alkaline earth metal?',
  'Ba','Barium (Ba) is in Group IIA (alkaline earth metals). Others: Be, Mg, Ca, Sr, Ra.',
  185,options=['Na','K','Li','Ba'],correct='Ba')

q(8,'A',2,'mcq','Symbol of Barium is:',
  'Ba','Barium chemical symbol is Ba (from Latin Barys meaning heavy).',
  185,options=['B','Ba','Br','Bm'],correct='Ba')

q(8,'A',3,'mcq','Chlorine can be displaced by:',
  'F','Fluorine is more reactive than chlorine (higher in Group VIIA), so it can displace Cl from its compounds.',
  185,options=['F','Br','I','At'],correct='F')

q(8,'A',4,'mcq','Which is a strong acid?',
  'HI','HI (hydroiodic acid) is a strong acid. Among halogen acids, acidity increases: HF < HCl < HBr < HI.',
  185,options=['HF','HCl','HBr','HI'],correct='HI')

q(8,'A',5,'mcq','Liquid halogen at room temperature is:',
  'Br2','Bromine (Br2) is the only halogen that is liquid at room temperature. F2 and Cl2 are gases; I2 is solid.',
  185,options=['F2','Cl2','Br2','I2'],correct='Br2')

q(8,'A',6,'mcq','Non-metals that are gases belong to group:',
  'VIII-A','Group VIII-A (18) noble gases (He, Ne, Ar, Kr, Xe, Rn) are all gases at room temperature.',
  185,options=['VII-A','VI-A','VIII-A','V-A'],correct='VIII-A')

q(8,'A',7,'mcq','Which is a metalloid?',
  'Se','Selenium (Se) is a metalloid with properties between metals and non-metals.',
  185,options=['S','Se','Na','Ca'],correct='Se')

q(8,'A',8,'mcq','Which is an oxidizing agent?',
  'Cl','Chlorine is a strong oxidizing agent (accepts electrons easily due to high electronegativity).',
  185,options=['Na','Mg','Al','Cl'],correct='Cl')

q(8,'A',9,'mcq','Gas that turns lime water milky is:',
  'CO2','CO2 reacts with lime water (Ca(OH)2) to form white precipitate of CaCO3, making it milky.',
  185,options=['O2','H2','CO2','N2'],correct='CO2')

q(8,'A',10,'mcq','Lunar caustic is:',
  'AgNO3','Silver nitrate (AgNO3) is called lunar caustic. It was historically used in medicine and photography.',
  185,options=['AgCl','AgNO3','AgBr','AgI'],correct='AgNO3')

# Section B: Short Questions
q(8,'B',1,'short','Identify elements as Metals, Non-metals and Metalloids: C, Ca, Sb, S, Sr, Si, K, P, Ba, Ge.',
  'Metals: Ca, Sr, K, Ba. Non-metals: C, S, P. Metalloids: Sb, Si, Ge. Metals are on left side of periodic table, non-metals on right, metalloids along the staircase line.',
  'Classification based on position in periodic table and properties.',186)

q(8,'B',2,'short','What are Alkali metals? Write names and symbols.',
  'Alkali metals: Group IA elements. Highly reactive metals with 1 valence electron. Names and symbols: Lithium (Li), Sodium (Na), Potassium (K), Rubidium (Rb), Cesium (Cs), Francium (Fr). They react vigorously with water to form alkaline solutions.',
  'Alkali metals are the most reactive metals.',186)

q(8,'B',3,'short','What are Alkaline Earth Metals? Write names and symbols.',
  'Alkaline Earth Metals: Group IIA elements. Reactive metals with 2 valence electrons. Names and symbols: Beryllium (Be), Magnesium (Mg), Calcium (Ca), Strontium (Sr), Barium (Ba), Radium (Ra). Their oxides are alkaline (basic).',
  'Alkaline earth metals are less reactive than alkali metals.',186)

q(8,'B',4,'short','What are Halogens? Write names and symbols.',
  'Halogens: Group VIIA (17) elements. Non-metals with 7 valence electrons. Highly reactive. Names and symbols: Fluorine (F), Chlorine (Cl), Bromine (Br), Iodine (I), Astatine (At). Name means salt-formers.',
  'Halogens are the most reactive non-metals.',186)

q(8,'B',5,'short','Write names and symbols of any three metalloids.',
  'Metalloids: Elements with properties between metals and non-metals. Three examples: Silicon (Si) - used in semiconductors. Germanium (Ge) - used in electronics. Arsenic (As) - used in alloys. Others: Boron (B), Antimony (Sb), Tellurium (Te).',
  'Metalloids have intermediate properties and are used in semiconductors.',186)

q(8,'B',6,'short','Define Cation and Anion with examples.',
  'Cation: Positively charged ion formed by losing electrons. Example: Na+ (sodium ion), Ca2+ (calcium ion), Al3+ (aluminum ion). Anion: Negatively charged ion formed by gaining electrons. Example: Cl- (chloride ion), O2- (oxide ion), N3- (nitride ion).',
  'Cations are positive (metal ions); anions are negative (non-metal ions).',186)

q(8,'B',7,'short','Why do alkali metals not exist free in nature?',
  'Alkali metals are highly reactive (1 valence electron easily lost). They react vigorously with oxygen, water, and other substances. Therefore, they are always found in combined state (compounds) in nature, never as free elements.',
  'High reactivity prevents alkali metals from existing in free state.',186)

q(8,'B',8,'short','Explain inertness of noble metals.',
  'Noble metals (Au, Ag, Pt) are inert (unreactive) because they have high ionization energies and low reactivity. They do not easily react with oxygen, water, or acids. Gold does not tarnish; silver tarnishes slowly; platinum is very resistant to corrosion.',
  'Noble metals have stable electron configurations and high ionization energies.',186)

q(8,'B',9,'short','Write names and symbols of some noble metals.',
  'Noble metals: Gold (Au), Silver (Ag), Platinum (Pt), Palladium (Pd), Rhodium (Rh), Iridium (Ir), Osmium (Os), Ruthenium (Ru). They are resistant to corrosion and oxidation.',
  'Noble metals are valued for their resistance to corrosion.',186)

q(8,'B',10,'short','Explain electronegative character of non-metals.',
  'Non-metals have high electronegativity (tendency to attract electrons). They gain electrons to form anions. Electronegativity increases across a period and decreases down a group. Fluorine is the most electronegative element (4.0). This makes non-metals good oxidizing agents.',
  'High electronegativity makes non-metals electron acceptors.',186)

# Section C: Detailed Questions
q(8,'C',1,'detailed','Explain importance of Silver.',
  'Silver (Ag) importance: (1) Jewelry and decorative items. (2) Photography (AgBr, AgCl in film). (3) Electronics (conductors, switches). (4) Medicine (antimicrobial properties, wound dressings). (5) Coins and silverware. (6) Mirrors (silver coating). (7) Solar panels. (8) Water purification.',
  'Silver has diverse applications due to its conductivity and antimicrobial properties.',186)

q(8,'C',2,'detailed','Explain importance of Gold.',
  'Gold (Au) importance: (1) Jewelry and ornaments. (2) Currency and reserves (gold standard). (3) Electronics (connectors, circuits - does not corrode). (4) Dentistry (fillings, crowns). (5) Medicine (treatment of arthritis). (6) Aerospace (reflective coating). (7) Nanotechnology. Gold is valued for its inertness and malleability.',
  'Gold is valued for its inertness, malleability, and conductivity.',186)

q(8,'C',3,'detailed','Explain the experiment to test Cl- and I- ions.',
  'Test for Cl-: Add AgNO3 solution to sample. White precipitate of AgCl forms. AgCl dissolves in dilute NH3. Reaction: Ag+ + Cl- to AgCl (white). Test for I-: Add AgNO3 solution. Yellow precipitate of AgI forms. AgI does not dissolve in NH3. Reaction: Ag+ + I- to AgI (yellow).',
  'Silver nitrate test distinguishes halide ions by precipitate color.',186)

q(8,'C',4,'detailed','Explain electropositive character of metals.',
  'Electropositive character: Tendency to lose electrons and form positive ions (cations). Metals are electropositive. Increases down a group (easier to lose electrons). Decreases across a period (harder to lose electrons). Alkali metals are most electropositive. This makes metals good reducing agents.',
  'Metals lose electrons easily due to low ionization energy.',186)

q(8,'C',5,'detailed','Explain position of Magnesium in periodic table and its importance.',
  'Magnesium (Mg): Group IIA, Period 3. Atomic number 12. Electronic configuration: 2, 8, 2. Importance: (1) Lightweight structural material (aircraft, cars). (2) Chlorophyll in plants (photosynthesis). (3) Flares and fireworks (bright white light). (4) Antacids (Mg(OH)2). (5) Alloys (magnalium).',
  'Magnesium is essential in biology and industry.',186)

q(8,'C',6,'detailed','Explain position of Sodium in periodic table and its importance.',
  'Sodium (Na): Group IA, Period 3. Atomic number 11. Electronic configuration: 2, 8, 1. Importance: (1) Table salt (NaCl). (2) Soap manufacturing (NaOH). (3) Street lights (sodium vapor lamps - yellow light). (4) Heat transfer (liquid Na in nuclear reactors). (5) Biological functions (nerve impulses, fluid balance).',
  'Sodium is essential in daily life and biological systems.',186)

q(8,'C',7,'detailed','Arrange Halogen Acids in increasing order of acidic strength: HBr, HCl, HI, HF.',
  'Increasing acidic strength: HF < HCl < HBr < HI. Reason: As size of halogen increases down the group, H-X bond becomes weaker and longer, making it easier to release H+ ion. HI has weakest bond, so strongest acid. HF has strongest bond (and hydrogen bonding), so weakest acid.',
  'Acidic strength increases down the group as bond strength decreases.',186)

q(8,'C',8,'detailed','Explain electronegative character of non-metals.',
  'Non-metals have high electronegativity - strong tendency to attract shared electrons in covalent bonds. Fluorine is most electronegative (4.0). Electronegativity increases across period (more protons, smaller size) and decreases down group (larger size, more shielding). This makes non-metals good electron acceptors and oxidizing agents.',
  'High electronegativity is a defining characteristic of non-metals.',186)

q(8,'C',9,'detailed','Differentiate between sodium and iron as soft and hard metal.',
  'Sodium (soft metal): Can be cut with knife, low density (floats on water), low melting point (98 C), highly reactive, Group IA. Iron (hard metal): Cannot be cut with knife, high density, high melting point (1538 C), less reactive (rusts slowly), transition metal. Soft metals have weak metallic bonds; hard metals have strong metallic bonds.',
  'Metal hardness depends on strength of metallic bonding.',186)

q(8,'C',10,'detailed','Discuss the reactivity of Halogens.',
  'Halogens are highly reactive non-metals (7 valence electrons, need 1 electron). Reactivity decreases down the group: F > Cl > Br > I. Fluorine is most reactive (smallest size, highest electronegativity). Reactions: (1) With metals: form metal halides. (2) With hydrogen: form hydrogen halides. (3) Displacement: more reactive halogen displaces less reactive one. (4) With water: form acids.',
  'Halogens are reactive due to high electronegativity and need for one electron.',186)

# ============================================================
# OUTPUT JSON
# ============================================================
with open('D:/SubjectZone/public/data/class_ix_chemistry.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, indent=2, ensure_ascii=False)
print(f"Generated {len(items)} Chemistry IX exercise items")
