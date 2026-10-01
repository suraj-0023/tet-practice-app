import json

batch1 = {
    1: {
        "hint": "Educational psychology centers on the learner, teacher, learning process, and classroom environment, not educational administration.",
        "memory_tip": "Skinner's Scope of Ed Psych = Learner + Teacher + Learning Experiences + Learning Process + Learning Situation (MEO is administrative)."
    },
    2: {
        "hint": "Development involves qualitative, internal, structural, and behavioral transformations rather than mere physical enlargement.",
        "memory_tip": "Growth = Quantitative & External; Development = Qualitative, Internal, Continuous & Integrated (Lifelong)."
    },
    3: {
        "hint": "The term is derived from two ancient classical terms meaning 'soul' or 'mind' and 'study' or 'science'.",
        "memory_tip": "Psychology = Greek: 'Psyche' (Soul/Mind) + 'Logos' (Study/Science)."
    },
    4: {
        "hint": "This specialized applied branch applies psychological findings directly to instruction and classroom learning.",
        "memory_tip": "Educational Psychology = Scientific study of teaching-learning processes & human behavior in educational settings."
    },
    5: {
        "hint": "Educational psychology deals with psychological and cognitive development, leaving economic and monetary matters to economics.",
        "memory_tip": "Educational Psychology focuses on Cognitive, Affective, and Psychomotor domains, not Financial development."
    },
    6: {
        "hint": "Measurable, physical, and quantitative bodily changes like increase in height, weight, and size indicate this concept.",
        "memory_tip": "Growth = Quantitative bodily changes (measurable in cm/kg); Development = Qualitative functional changes."
    },
    7: {
        "hint": "Wilhelm Wundt founded the world's first formal laboratory for psychological research in Germany in 1879.",
        "memory_tip": "Wilhelm Wundt established 1st Experimental Psychology Lab at Leipzig University, Germany in 1879."
    },
    8: {
        "hint": "Educational psychology is meant for pedagogical enhancement, understanding learner differences, and improving teaching, not personal career politics.",
        "memory_tip": "Purpose of Ed Psych for teachers = Understanding learners, individualized instruction, guidance & evaluation (not securing promotions)."
    },
    9: {
        "hint": "Human development is not merely an addition but an interactive multiplicative outcome of nature and nurture.",
        "memory_tip": "Woodworth's Formula: Development = Heredity × Environment (D = H × E; Nature × Nurture)."
    },
    10: {
        "hint": "This American psychologist rejected introspection and declared psychology as the science of observable behavior in 1913.",
        "memory_tip": "J.B. Watson = Father of Behaviorism ('Give me a dozen healthy infants...')."
    },
    11: {
        "hint": "Physical changes like height and weight can be objectively quantified using standard physical measuring tools.",
        "memory_tip": "Growth can be measured accurately and stops at maturity; Development is assessed through observation and continues lifelong."
    },
    12: {
        "hint": "This Swiss educational reformer founded schools emphasizing 'head, heart, and hands' (Pestalozzi method) at Yverdon.",
        "memory_tip": "Johann Heinrich Pestalozzi founded the famous Yverdon Boarding School based on natural child-centered education."
    },
    13: {
        "hint": "This pioneer wrote the monumental two-volume book 'Adolescence' (1904) and coined the phrase 'Storm and Stress'.",
        "memory_tip": "G. Stanley Hall = Father of Adolescence ('Period of Storm and Stress' / 'Sturm und Drang')."
    },
    14: {
        "hint": "He established the first laboratory dedicated to psychological experiments and separated psychology from philosophy.",
        "memory_tip": "Wilhelm Wundt = Father of Experimental Psychology (Leipzig, 1879; Structuralism)."
    },
    15: {
        "hint": "In Greek, the prefix represents life, breath, or soul, while the suffix denotes systematic discourse or knowledge.",
        "memory_tip": "Greek origin: Psyche = Soul / Mind, Logos = Knowledge / Study / Discourse."
    },
    16: {
        "hint": "This psychologist defined development as the complex process of integrating various emerging bodily structures and functions.",
        "memory_tip": "John E. Anderson: 'Development is the complex process of integrating different structures and functions.'"
    },
    17: {
        "hint": "Development is a product of biological maturation and purposeful interaction with the environment through practice.",
        "memory_tip": "Development Formula: D = f(Maturation × Learning) [Gesell & McGeoch]."
    },
    18: {
        "hint": "The pioneer who published 'Educational Psychology' (1903) and formulated the fundamental Laws of Learning.",
        "memory_tip": "E.L. Thorndike = Father of Educational Psychology (Connectionism, Trial & Error, Laws of Learning)."
    },
    19: {
        "hint": "The ancient Greek philosopher who founded the Academy and emphasized holistic education in his Republic.",
        "memory_tip": "Plato established the 'Gymnasia' system and the Academy in classical Athens."
    },
    20: {
        "hint": "The French philosopher who championed Naturalism in education in his celebrated book 'Emile'.",
        "memory_tip": "Rousseau's Slogan: 'Go back to nature' (Naturalism in Education, Emile)."
    },
    21: {
        "hint": "Physical growth ceases once the organism reaches full biological maturity and adulthood.",
        "memory_tip": "Growth stops at physical maturity (puberty/early adulthood); Development is continuous from womb to tomb."
    },
    22: {
        "hint": "An individual develops as an integrated whole; impairment in one domain adversely affects emotional, intellectual, and motor spheres.",
        "memory_tip": "Principle of Interrelation: Physical, cognitive, emotional, and social development are interdependent."
    },
    23: {
        "hint": "Because growth rates follow standard developmental trends, future status can be forecast with reasonable certainty.",
        "memory_tip": "Principle of Predictability: Early developmental milestones allow prediction of adult traits."
    },
    24: {
        "hint": "Gross and fine motor skills build progressively step by step upon preceding neuro-muscular achievements.",
        "memory_tip": "Principle of Cumulative Development: Major skills are the culmination of previously mastered sub-skills."
    },
    25: {
        "hint": "Responses are initially undifferentiated and broad, gradually becoming precise, fine-tuned, and discriminating.",
        "memory_tip": "Principle of General to Specific: Responses start generalized and progress toward specialized discrimination."
    },
    26: {
        "hint": "Motor control begins with head holding, followed by torso balance, and lastly leg and foot coordination.",
        "memory_tip": "Cephalocaudal Rule: Head-to-toe progression (Cephalo = Head, Caudal = Tail/Foot)."
    },
    27: {
        "hint": "Even identical twins have unique developmental tempos, emotional styles, and skill levels due to genetic-environmental interplay.",
        "memory_tip": "Principle of Individual Differences: Each learner develops at their own unique pace and rhythm."
    },
    28: {
        "hint": "Development begins right from conception (zygote) and carries on continuously through life till biological cessation.",
        "memory_tip": "Principle of Continuity: Development is an unbroken process from conception to death (womb to tomb)."
    },
    29: {
        "hint": "Motor and drawing abilities follow a universal chronological pattern of geometric shape reproduction.",
        "memory_tip": "Principle of Orderly Sequence: Developmental progress follows an orderly, invariant developmental sequence."
    },
    30: {
        "hint": "A generalized verbal label is initially applied to all adult males, then narrowed down specifically to the biological father.",
        "memory_tip": "General to Specific Progression: Broad over-extension narrows down to precise classification."
    },
    31: {
        "hint": "Current performance and learning rate in middle school provide reliable indices for projecting high school outcomes.",
        "memory_tip": "Principle of Predictability: Past and present achievement curves forecast future developmental trajectory."
    },
    32: {
        "hint": "Moral reasoning depends closely upon cognitive maturation and the ability to evaluate intent and consequence.",
        "memory_tip": "Principle of Interrelation: Cognitive deficits hinder higher-order moral reasoning (Piaget & Kohlberg)."
    },
    33: {
        "hint": "Two children of the exact same chronological age possess distinct profiles of academic and artistic proficiencies.",
        "memory_tip": "Principle of Individual Differences: Intra-individual and inter-individual variance in aptitudes and strengths."
    },
    34: {
        "hint": "Across every human culture, infants acquire gross motor milestones in the exact same sequential order.",
        "memory_tip": "Principle of Uniform Pattern: Invariant developmental stages across all normal individuals."
    },
    35: {
        "hint": "A physical orthopedic limitation frequently triggers emotional frustration, demonstrating interconnected development.",
        "memory_tip": "Principle of Interrelation: Physical hurdles directly influence emotional stability and behavioral adjustment."
    },
    36: {
        "hint": "Control of proximal muscles (shoulders/arms) develops earlier than fine control of distal muscles (wrists/fingers).",
        "memory_tip": "Proximodistal Rule: Center-outward development (Proximal = near the axis, Distal = extremities)."
    },
    37: {
        "hint": "Growth does not occur at a constant uniform speed; it spurts dramatically in infancy, plateaus in middle childhood, and surges in puberty.",
        "memory_tip": "Principle of Non-Uniform Pattern: Variable growth rates across different developmental phases."
    },
    38: {
        "hint": "Noticing special vocal talent in early childhood allows teachers to forecast outstanding adult musical competence.",
        "memory_tip": "Principle of Predictability: Aptitude displayed early indicates probable adult attainment."
    },
    39: {
        "hint": "One child walking at 10 months and another at 14 months represents standard natural biological variation.",
        "memory_tip": "Principle of Individual Differences: Every child follows their own developmental clock."
    },
    40: {
        "hint": "The spinal cord and torso develop and strengthen before the extremities and peripheral digits.",
        "memory_tip": "Principle of Proximodistal Development: Central axis to outer limbs."
    },
    41: {
        "hint": "Milestone acquisition intervals vary naturally from baby to baby without signaling developmental pathology.",
        "memory_tip": "Principle of Individual Differences: Variation in milestone onset times is normative."
    },
    42: {
        "hint": "Children who understand and regulate their emotions effectively form warmer, cooperative peer friendships.",
        "memory_tip": "Principle of Interrelation: Emotional intelligence directly fosters pro-social competence."
    },
    43: {
        "hint": "Puberty is primarily marked by rapid somatic growth and secondary sexual maturation, whereas ego-identity and self-consciousness consolidate in adolescence.",
        "memory_tip": "Puberty = Biological sexual maturation phase; Self-concept & identity crisis belong to Adolescence (Erikson)."
    },
    44: {
        "hint": "This developmental psychologist outlined the classic 10-stage lifespan model in 'Developmental Psychology: A Life-Span Approach'.",
        "memory_tip": "Elizabeth B. Hurlock classified human lifespan into 10 distinct developmental stages."
    },
    45: {
        "hint": "Between ages 2 and 6, young children relentlessly explore their environment, ask 'why', and dismantle toys.",
        "memory_tip": "Early Childhood (2-6 yrs) = Age of Exploration / Toy Age / Questioning Age / Pre-gang Age."
    },
    46: {
        "hint": "The critical transition period covering the first fourteen days after birth where the newborn adjusts to extrauterine life.",
        "memory_tip": "Neonatal Stage = First 2 weeks after birth (infant adjusting to respiration, feeding & temperature)."
    },
    47: {
        "hint": "The stage of babyhood extending from the end of the second week until the child turns two years old.",
        "memory_tip": "Infancy (Babyhood) = 2 weeks to 2 years (rapid physical growth and sensorimotor development)."
    },
    48: {
        "hint": "The pre-school stage from 2 to 6 years characterized by active language acquisition and symbolic play.",
        "memory_tip": "Early Childhood = 2 to 6 years (pre-school age, pre-gang age, language explosion)."
    },
    49: {
        "hint": "The elementary school years from 6 to 10-12 years where peer group bonding and concrete thinking flourish.",
        "memory_tip": "Late Childhood = 6 to 10/12 years (Elementary school age, Gang Age, play age)."
    },
    50: {
        "hint": "The transitional bio-maturational bridge connecting late childhood and adolescence, usually between 10/12 and 13/14 years.",
        "memory_tip": "Puberty (Pre-adolescence) = 10/12 to 13/14 years (period of sexual maturation and growth spurt)."
    },
    51: {
        "hint": "The phase of life from 18 to 40 years focusing on career establishment, marriage, and family life.",
        "memory_tip": "Early Adulthood = 18 to 40 years (Settling down, reproductive age, career consolidation)."
    },
    52: {
        "hint": "The middle-aged period from 40 to 60 years characterized by empty nest transitions, career peak, and physical climacteric.",
        "memory_tip": "Middle Adulthood / Middle Age = 40 to 60 years (Generativity vs Stagnation, mid-life transition)."
    },
    53: {
        "hint": "The concluding developmental epoch after age 60 characterized by retirement, biological decline, and life review.",
        "memory_tip": "Old Age (Late Adulthood) = 60+ years (Integrity vs Despair, physical decline)."
    },
    54: {
        "hint": "During elementary school years, peer conformity peaks and children form tightly knit play groups.",
        "memory_tip": "Late Childhood (6-12 yrs) = Gang Age; Early Childhood (2-6 yrs) = Pre-gang Age."
    },
    55: {
        "hint": "The Latin term 'pubertas' etymologically refers to the age of manhood or biological capability of procreation.",
        "memory_tip": "Pubertas = Latin term meaning 'Age of Manhood' / 'Age of Maturity'."
    },
    56: {
        "hint": "Because puberty bridges the closing phase of childhood and the opening phase of adolescence, it intersects both stages.",
        "memory_tip": "Puberty = 'Period of Overlapping' (Hurlock: overlaps late childhood and early adolescence)."
    },
    57: {
        "hint": "During the first two weeks of life, language, social gangs, and peer play do not exist.",
        "memory_tip": "Neonatal Stage (0-14 days) focuses on physiological stabilization, not social or cognitive tasks."
    },
    58: {
        "hint": "Abstract logical operations and peer gang participation are absent during the first two years of life.",
        "memory_tip": "Infancy (0-2 yrs) = Sensorimotor exploration & physical helplessness (not gang age or formal operations)."
    },
    59: {
        "hint": "Many biological and developmental terms regarding maturity are borrowed from ancient Roman civilization.",
        "memory_tip": "Puberty is derived from Latin 'Pubertas' (hair/manhood)."
    },
    60: {
        "hint": "Entering adulthood entails assuming career, familial, civic, and financial responsibilities.",
        "memory_tip": "Adulthood = Stage of social responsibility, settling down, and career stability."
    },
    61: {
        "hint": "The single diploid cell created at the exact moment of fertilization by the fusion of sperm and ovum.",
        "memory_tip": "Zygote = Fertilized ovum formed by sperm (23 chromosomes) + egg (23 chromosomes) = 46 chromosomes (23 pairs)."
    },
    62: {
        "hint": "Facial hair, voice deepening in boys, and breast development in girls emerge during this hormonal awakening.",
        "memory_tip": "Secondary Sexual Characteristics = Hallmarks of Puberty / Early Adolescence (gonadal hormones)."
    },
    63: {
        "hint": "The approximate 280-day biological period elapsed from conception until parturition inside the uterus.",
        "memory_tip": "Pre-natal Stage = 9 months / 40 weeks / 280 days gestation inside mother's womb."
    },
    64: {
        "hint": "Attributing human emotions, intentions, and living feelings to inanimate dolls or stones is animism.",
        "memory_tip": "Piaget's Pre-operational Stage (2-7 yrs) = Animism (believing non-living things have feelings) & Egocentrism."
    },
    65: {
        "hint": "The highest Piagetian stage allows adolescents to construct hypothetical propositions and test them systematically.",
        "memory_tip": "Formal Operational Stage (11-15+ yrs) = Hypothetico-deductive reasoning & Abstract thinking."
    },
    66: {
        "hint": "Piaget organized cognitive growth into sensorimotor, pre-operational, concrete operational, and formal operational stages.",
        "memory_tip": "Piaget's 4 Cognitive Stages: SPCF (Sensorimotor, Pre-operational, Concrete, Formal)."
    },
    67: {
        "hint": "Piaget's core constructs include Schema, Assimilation, Accommodation, and Equilibration; 'Incorporation' is not his key concept.",
        "memory_tip": "Piagetian Concepts = Schema, Assimilation, Accommodation, Equilibration, Adaptation, Centration, Conservation."
    },
    68: {
        "hint": "Piaget used this term to designate mental representations or organized cognitive building blocks of knowledge.",
        "memory_tip": "Schemata (Schema) = Cognitive structures / mental frameworks used to organize and interpret information."
    },
    69: {
        "hint": "Deductive understanding of abstract causal links and systematic experimental hypotheses manifests at the final Piagetian stage.",
        "memory_tip": "Formal Operational Stage = Understanding abstract cause-effect relationships and scientific logic."
    },
    70: {
        "hint": "The final stage of Piaget's theory appearing around age 11 onwards and persisting into adulthood.",
        "memory_tip": "Piaget's 4th and Final Stage = Formal Operational Stage (11 years and above)."
    },
    71: {
        "hint": "The initial Piagetian stage where learning is achieved purely through sensory impressions and physical reflexes.",
        "memory_tip": "Piaget's 1st Stage = Sensorimotor Stage (Birth to 2 years; senses and motor coordination)."
    },
    72: {
        "hint": "Before roughly 8 to 9 months, an infant acts as though an object hidden behind a screen ceases to exist ('out of sight, out of mind').",
        "memory_tip": "Sensorimotor Stage: Object Permanence lacks initially and develops around 8-9 months of age."
    },
    73: {
        "hint": "Jean Piaget was born in Neuchâtel and conducted his world-renowned genetic epistemology studies in this European nation.",
        "memory_tip": "Jean Piaget was a Swiss psychologist / genetic epistemologist (Switzerland)."
    },
    74: {
        "hint": "The Swiss psychologist renowned for studying his own children to chart the universal development of human intellect.",
        "memory_tip": "Jean Piaget = Proponent of Cognitive Developmental Theory (Genetic Epistemology)."
    },
    75: {
        "hint": "When incoming data cannot fit into existing schemas, the child must modify or construct new schemas to adapt.",
        "memory_tip": "Accommodation = Altering existing schemas or creating new ones in response to new environmental demands."
    },
    76: {
        "hint": "The comprehensive mental evolution encompassing memory, thinking, reasoning, perception, and self-awareness.",
        "memory_tip": "Cognitive Development = Evolution of mental abilities by which a person knows themselves and the world."
    },
    77: {
        "hint": "Incorporating new perceptual experiences into already existing mental schemas without changing the schema.",
        "memory_tip": "Assimilation = Fitting new information into existing cognitive schemas (Schema unchanged)."
    },
    78: {
        "hint": "The stage spanning from birth to age two where infant coordinates motor actions with sensory inputs.",
        "memory_tip": "Piaget Stage 1 = Sensorimotor (0 to 2 years)."
    },
    79: {
        "hint": "The stage spanning ages 2 to 7 years marked by symbolic play, language burst, egocentrism, and centration.",
        "memory_tip": "Piaget Stage 2 = Pre-operational Stage (2 to 7 years)."
    },
    80: {
        "hint": "The elementary school stage (7 to 11 years) characterized by logical operations applied to tangible physical objects.",
        "memory_tip": "Piaget Stage 3 = Concrete Operational Stage (7 to 11 years; Conservation & Reversibility)."
    },
    81: {
        "hint": "The stage commencing around puberty (11 years onwards) enabling abstract propositions and hypothetical deduction.",
        "memory_tip": "Piaget Stage 4 = Formal Operational Stage (11 years to adulthood)."
    },
    82: {
        "hint": "Conservation of volume, reversibility of thought, and classification develop during this middle childhood stage.",
        "memory_tip": "Concrete Operational Stage (7-11 yrs) = Conservation, Decentration, Reversibility, Seriation."
    },
    83: {
        "hint": "Inability to take another person's perspective (three-mountain task) and believing dolls are alive are hallmarks here.",
        "memory_tip": "Pre-operational Stage (2-7 yrs) = Egocentrism, Animism, Irreversibility, Centration."
    },
    84: {
        "hint": "Realizing that an object continues to exist even when concealed or removed from vision is acquired during this period.",
        "memory_tip": "Sensorimotor Stage (0-2 yrs) = Object Permanence ('Out of sight is NOT out of mind' by 8-12 months)."
    },
    85: {
        "hint": "Industry is paired with Inferiority in school age; Guilt is paired with Initiative during play age.",
        "memory_tip": "Erikson's Stage 4: Industry vs Inferiority (6-12 yrs). Stage 3: Initiative vs Guilt (3-5 yrs)."
    },
    86: {
        "hint": "Intimacy is paired with Isolation in young adulthood; Stagnation is paired with Generativity in middle adulthood.",
        "memory_tip": "Erikson's Stage 6: Intimacy vs Isolation (20-39 yrs). Stage 7: Generativity vs Stagnation (40-59 yrs)."
    },
    87: {
        "hint": "Identity vs Role Confusion occurs during adolescence (12-18 yrs), not in early childhood.",
        "memory_tip": "Adolescence Crisis = Identity vs Role Confusion (5th psychosocial stage)."
    },
    88: {
        "hint": "Preschoolers between 3 and 5 years eagerly initiate activities and imaginative games; criticism fosters guilt.",
        "memory_tip": "Initiative vs Guilt = Erikson's 3rd Stage (Ages 3 to 5 years, Play age)."
    },
    89: {
        "hint": "The infant's first social crisis depends entirely on the reliability, warmth, and consistency of the primary caregiver.",
        "memory_tip": "Erikson's 1st Crisis = Trust vs Mistrust (Infancy: 0 to 1/1.5 years; Virtue: Hope)."
    },
    90: {
        "hint": "In late adulthood, seniors reflect on their life accomplishments with contentment or face despair over missed choices.",
        "memory_tip": "Erikson's 8th & Final Stage = Ego Integrity vs Despair (Maturity / 65+ years; Virtue: Wisdom)."
    },
    91: {
        "hint": "The tumultuous transitional teenage stage where youth struggle to answer 'Who am I?' and find their social role.",
        "memory_tip": "Erikson coined 'Identity Crisis' specifically for Adolescence (Identity vs Role Confusion)."
    },
    92: {
        "hint": "Erikson shifted focus away from Freud's biological sexual instincts toward societal interactions and interpersonal crises across life.",
        "memory_tip": "Freud = Psychosexual (Id & Libido); Erikson = Psychosocial (Ego identity & Social interaction across 8 stages)."
    },
    93: {
        "hint": "The German-American developmental theorist who formulated the Eight Ages of Man spanning the entire lifespan.",
        "memory_tip": "Erik Erikson = Proponent of the Theory of Psychosocial Development (8 Life Stages)."
    },
    94: {
        "hint": "During early adulthood, individuals seek deeply committed romantic relationships or risk emotional isolation.",
        "memory_tip": "Young Adulthood Crisis (20-39 yrs) = Intimacy vs Isolation (Virtue: Love)."
    },
    95: {
        "hint": "Preschool children undertaking self-directed games and creative plans resolve this specific crisis.",
        "memory_tip": "Play Age Crisis (3-5 yrs) = Initiative vs Guilt (Virtue: Purpose)."
    },
    96: {
        "hint": "Looking back upon one's full life journey with acceptance leads to wholeness; regrets bring despair.",
        "memory_tip": "Old Age Crisis (60+ yrs) = Ego Integrity vs Despair (Virtue: Wisdom)."
    },
    97: {
        "hint": "Toddlers learning toilet training and motor self-control assert independence or suffer doubt in their abilities.",
        "memory_tip": "Toddlerhood Crisis (1-3 yrs) = Autonomy vs Shame & Doubt (Virtue: Will)."
    },
    98: {
        "hint": "Adolescents experimenting with peer roles, career goals, and ideological beliefs face this crisis.",
        "memory_tip": "Adolescence Crisis (12-18 yrs) = Identity vs Role Confusion (Virtue: Fidelity)."
    },
    99: {
        "hint": "During the first year of life, responsive parenting builds fundamental confidence in the world.",
        "memory_tip": "First Year Crisis (0-1 yr) = Trust vs Mistrust."
    },
    100: {
        "hint": "Elementary school children mastering reading, writing, and arithmetic strive for competence against feeling inferior.",
        "memory_tip": "School Age Crisis (6-12 yrs) = Industry vs Inferiority (Virtue: Competence)."
    }
}

with open("cdp_enhancer/batch_1.json", "w") as f:
    json.dump(batch1, f, indent=2)
print("Batch 1 generated successfully! Total:", len(batch1))
