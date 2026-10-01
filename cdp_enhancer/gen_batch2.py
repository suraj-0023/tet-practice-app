import json

batch2 = {
    101: {
        "hint": "In middle age (40-65 yrs), adults focus on guiding the younger generation through work and family; failure brings stagnation.",
        "memory_tip": "Erikson's 7th Stage (40-65 yrs) = Generativity vs Stagnation (Virtue: Care)."
    },
    102: {
        "hint": "Check Erikson's developmental stage pairs: Young Adulthood matches Intimacy vs Isolation.",
        "memory_tip": "Erikson's Sequence: Trust -> Autonomy -> Initiative -> Industry -> Identity -> Intimacy -> Generativity -> Integrity."
    },
    103: {
        "hint": "Check the matching between the lifespan phase and its associated psychosocial conflict.",
        "memory_tip": "Erikson Stages: Infancy (Trust/Mistrust), Early Childhood (Autonomy/Doubt), Adolescence (Identity/Confusion)."
    },
    104: {
        "hint": "The final stage where elderly seniors over 60 reflect back on their life achievements with satisfaction or regret.",
        "memory_tip": "Late Adulthood (> 60 years) = Integrity vs Despair (Virtue: Wisdom)."
    },
    105: {
        "hint": "During young adulthood (twenties and early thirties), the primary developmental task is establishing deep loving relationships.",
        "memory_tip": "Young Adulthood (20-30/39 yrs) = Intimacy vs Isolation (Virtue: Love)."
    },
    106: {
        "hint": "At this highest pinnacle of moral development, actions are guided by self-chosen universal ethical principles and human dignity.",
        "memory_tip": "Kohlberg's Stage 6 = Universal Ethical Principles Orientation (Highest post-conventional stage)."
    },
    107: {
        "hint": "The ultimate 6th stage in Kohlberg's taxonomy where conscience and universal ethical equality transcend written law.",
        "memory_tip": "Kohlberg's 6th and Final Stage = Universal Ethical Principles (Level 3: Post-conventional)."
    },
    108: {
        "hint": "Pre-teens and early adolescents (11-13 yrs) reason predominantly based on social conventions, peer expectations, and societal rules.",
        "memory_tip": "Conventional Morality (10-13 yrs) = Conformity to social rules (Stage 3: Good Boy/Girl, Stage 4: Law & Order)."
    },
    109: {
        "hint": "Conforming to rules specifically to earn approval and praise from authority figures represents interpersonal concordance.",
        "memory_tip": "Kohlberg's Stage 3 = 'Good Boy - Good Girl' Orientation (Seeking social approval and maintaining positive interpersonal relations)."
    },
    110: {
        "hint": "This developmental psychologist developed the moral dilemmas (e.g. Heinz dilemma) at Harvard and Chicago in the United States.",
        "memory_tip": "Lawrence Kohlberg was an American psychologist (Harvard University)."
    },
    111: {
        "hint": "The theorist who formulated the three-level, six-stage framework of moral dilemmas based on Piaget's moral foundations.",
        "memory_tip": "Lawrence Kohlberg = Proponent of the Theory of Moral Development (Heinz Dilemma)."
    },
    112: {
        "hint": "Kohlberg structured moral reasoning into three overarching hierarchical levels, each containing exactly two stages.",
        "memory_tip": "Kohlberg's Structure = 3 Levels (Pre-conventional, Conventional, Post-conventional) & 6 Stages."
    },
    113: {
        "hint": "The initial moral level where rules are external to the self and judged solely by physical consequences (punishment/reward).",
        "memory_tip": "Level 1 = Pre-Conventional Morality (Stages 1 & 2; external rewards and punishments)."
    },
    114: {
        "hint": "The highest moral tier where principles are defined by self-chosen ethical values independent of group authority.",
        "memory_tip": "Level 3 = Post-Conventional Morality (Stages 5 & 6; social contract and universal ethics)."
    },
    115: {
        "hint": "Pleasing others, winning approval, and living up to family and peer expectations defines this 3rd stage.",
        "memory_tip": "Stage 3 = Interpersonal Conformity ('Good Boy - Nice Girl' orientation)."
    },
    116: {
        "hint": "Obeying laws strictly to maintain social order, duty, and avoid chaos represents this 4th stage.",
        "memory_tip": "Stage 4 = Law and Order Orientation (Social-Order-Maintaining Morality)."
    },
    117: {
        "hint": "Children below age 9-10 judge moral rightness strictly through physical reward, punishment, or immediate mutual exchange.",
        "memory_tip": "Pre-Conventional Level (ages 4-10 yrs) = Morality judged by external consequences."
    },
    118: {
        "hint": "At Stage 1, an action is perceived as wrong solely if the perpetrator gets caught and physically punished.",
        "memory_tip": "Stage 1 = Punishment and Obedience Orientation (Heteronomous Morality)."
    },
    119: {
        "hint": "Believing in the universal dignity of all human beings, equality, and justice even if society's laws conflict defines this stage.",
        "memory_tip": "Stage 6 = Universal Ethical Principles (Conscience driven; self-chosen ethical values)."
    },
    120: {
        "hint": "The quantitative measure corresponding to an individual's emotional and social intelligence quotient.",
        "memory_tip": "EQ = Emotional Quotient (measuring emotional intelligence; Daniel Goleman)."
    },
    121: {
        "hint": "A person with high emotional intelligence is deeply empathetic and acutely sensitive to the feelings and perspectives of others.",
        "memory_tip": "Core Components of EI (Goleman) = Self-awareness, Self-regulation, Motivation, Empathy, Social skills."
    },
    122: {
        "hint": "According to William McDougall's theory of instincts, running away or escaping from danger generates this primal emotion.",
        "memory_tip": "McDougall's 14 Instincts: Instinct of Escape corresponds to the Emotion of Fear."
    },
    123: {
        "hint": "Nurturing, protecting, and cherishing an infant originates from the biological parental instinct.",
        "memory_tip": "McDougall's Instincts: Parental instinct corresponds to the Emotion of Tender Emotion / Love."
    },
    124: {
        "hint": "The instinct of combat, fighting, or overcoming an obstacle gives rise to this intense emotional outburst.",
        "memory_tip": "McDougall's Instincts: Instinct of Pugnacity / Combat corresponds to the Emotion of Anger."
    },
    125: {
        "hint": "The psychological term emotion comes from a classical ancient Roman verb meaning to shake, stir up, or agitate.",
        "memory_tip": "Emotion is derived from Latin 'Emovere' (to stir up, agitate, or excite)."
    },
    126: {
        "hint": "Positive emotions foster flourishing and joy; anger is an intense unpleasant distress state associated with threat or frustration.",
        "memory_tip": "Positive Emotions = Joy, Love, Hope, Contentment; Negative Emotions = Anger, Fear, Jealousy, Sadness."
    },
    127: {
        "hint": "This developmental psychologist defined social development as the progressive attainment of maturity in social relationships.",
        "memory_tip": "Elizabeth B. Hurlock: 'Social development means the attaining of maturity in social relationships.'"
    },
    128: {
        "hint": "This psychologist defined socialization as transforming an instinctual biological infant into an integrated social personality.",
        "memory_tip": "H.E. Garrett: 'Socialization is the process whereby a biological individual is converted into a social person.'"
    },
    129: {
        "hint": "A socially mature person acts with high civic integrity and never manipulates mass media for dishonest or selfish ends.",
        "memory_tip": "Social Maturity = Altruism, empathy, ethical civic duty, and cooperative social responsibility."
    },
    130: {
        "hint": "Socially mature individuals possess strong communication, empathy, and active constructive leadership in group life.",
        "memory_tip": "Social Maturity includes leadership, interpersonal harmony, emotional stability, and civic cooperation."
    },
    131: {
        "hint": "Mildred Parten classified play into Unoccupied, Solitary, Onlooker, Parallel, Associative, and Cooperative; 'Correlation play' is fictitious.",
        "memory_tip": "Parten's 6 Stages of Play: Unoccupied, Solitary, Onlooker, Parallel, Associative, Cooperative."
    },
    132: {
        "hint": "Social maturity is characterized by obedience to constructive laws, empathy, and refusal to engage in anti-social disruptions.",
        "memory_tip": "Socially mature behavior strictly refrains from antisocial, destructive, or delinquent acts."
    },
    133: {
        "hint": "Engaging in antisocial, violent, or delinquent vandalism is a classic hallmark of social maladjustment, not maturity.",
        "memory_tip": "Antisocial conduct signifies emotional and social immaturity."
    },
    134: {
        "hint": "A mature social member puts community welfare and mutual collaboration above narrow selfish greed.",
        "memory_tip": "Social Maturity = Selfless collaboration, empathy, and tolerance of differences."
    },
    135: {
        "hint": "An effective educator actively creates collaborative learning environments, team projects, and cooperative group assignments.",
        "memory_tip": "Teacher's Role in Socialization = Encouraging group activities, democratic participation, and peer cohesion."
    },
    136: {
        "hint": "In solitary independent play, the toddler plays alone with their own toys and shows no inclination to share or invite others.",
        "memory_tip": "Solitary Play (Parten) = Child plays alone with own toys, paying little attention to nearby children."
    },
    137: {
        "hint": "The fundamental goal of socialization is shaping the raw biological child into a productive, cultured, and ethical citizen.",
        "memory_tip": "Ultimate Goal of Social Development = Transforming the biological child into an active, adjusted social member."
    },
    138: {
        "hint": "When children organize themselves into groups, communicate, and share materials, it constitutes active social play.",
        "memory_tip": "Social Play = Group play involving interpersonal communication and shared fun."
    },
    139: {
        "hint": "Playing side by side with similar toys without direct interaction or influence is the classic pre-school play pattern.",
        "memory_tip": "Parallel Play (Mildred Parten) = Playing alongside other children without direct interaction (2-3 yrs)."
    },
    140: {
        "hint": "The highest form of social play involves structured teamwork, division of labor, shared goals, and adherence to rules.",
        "memory_tip": "Cooperative Play (Parten) = Highly organized group play with common goals and mutual roles (4-6+ yrs)."
    },
    141: {
        "hint": "Socially developed persons exhibit high civic altruism, community involvement, and enthusiasm for social service.",
        "memory_tip": "Social Development is manifested through community service, empathy, and social cooperation."
    },
    142: {
        "hint": "Teenagers prioritize the rules, styles, opinions, and approval of their peer group above almost everything else.",
        "memory_tip": "Adolescence Social Trait = Intense Group Loyalty / Peer Conformity."
    },
    143: {
        "hint": "During late childhood (8-11 yrs), boys prefer playing strictly with boys and girls with girls, avoiding the other sex.",
        "memory_tip": "Sexual Cleavage = Gender segregation during late childhood (boys and girls avoid playing together)."
    },
    144: {
        "hint": "Both family parenting practices and school environment are powerful foundational agencies of socialization.",
        "memory_tip": "Agencies of Socialization = Primary (Family) + Secondary (School, Peer Group, Media)."
    },
    145: {
        "hint": "Socialization is an ongoing interactive dynamic shaped by institutional rules and cultural transmission.",
        "memory_tip": "Socialization is a comprehensive cultural transmission process."
    },
    146: {
        "hint": "The home, neighborhood peers, classroom teachers, and digital media all actively mold human social personality.",
        "memory_tip": "Major Socialization Agents = Family + School + Peer Group + Society + Media."
    },
    147: {
        "hint": "Healthy social maturity reflects warm, respectful, and constructive rapport with parents, peers, teachers, and society.",
        "memory_tip": "Social Maturity = Harmonious relationships across all social spheres."
    },
    148: {
        "hint": "Like many biological and psychological lifespan terms, adolescence traces its linguistic origin to classical Rome.",
        "memory_tip": "Adolescence is derived from the Latin verb 'Adolescere'."
    },
    149: {
        "hint": "The Latin verb 'adolescere' literally translates to 'to grow into maturity' or 'to ripen into adulthood'.",
        "memory_tip": "Adolescere = Latin meaning 'To grow into maturity / to ripen into adulthood'."
    },
    150: {
        "hint": "The World Health Organization (WHO) formally defines the adolescent demographic age bracket as spanning the second decade.",
        "memory_tip": "WHO definition of Adolescence = 10 to 19 years."
    },
    151: {
        "hint": "Teenagers are caught in a developmental no-man's-land: expected to act as adults yet denied adult privileges.",
        "memory_tip": "Adolescence = Transitional period where individuals are treated as neither child nor full adult."
    },
    152: {
        "hint": "Adolescence encompasses rapid physiological transformation, sexual maturity, and psychological identity consolidation.",
        "memory_tip": "Adolescence = Period of rapid physical, emotional, and social change (Storm and Stress)."
    },
    153: {
        "hint": "The central developmental struggle of the teenage years is discovering one's authentic identity, values, and life philosophy.",
        "memory_tip": "Adolescence = Search for Ego Identity (Erikson) and bridge to adulthood."
    },
    154: {
        "hint": "Adolescents seek autonomy, freedom, belonging, and respect; compulsory subservience or slavery directly opposes development.",
        "memory_tip": "Adolescent Needs = Autonomy, Peer Acceptance, Emotional Security, Self-expression."
    },
    155: {
        "hint": "Youth require security, emotional affection, constructive guidance, and healthy social avenues for self-expression.",
        "memory_tip": "Comprehensive Adolescent Needs = Physical, Emotional, Social, and Intellectual opportunities."
    },
    156: {
        "hint": "Due to hormonal shifts, identity confusion, and peer pressures, adolescence is renowned as a problem-laden stage.",
        "memory_tip": "Adolescence is termed a 'Period of Problems' (Stanley Hall: Storm & Stress); claiming it lacks problems is incorrect."
    },
    157: {
        "hint": "Successfully navigating the physiological and psychological transitions of adolescence leads directly into adult status.",
        "memory_tip": "Adolescence = The developmental gateway / bridge to Adulthood."
    },
    158: {
        "hint": "Adolescents require psychological reassurance, meaningful social status, vocational clarity, and constructive independence.",
        "memory_tip": "Core Adolescent Needs = Security, Identity, Independence, and Social Status."
    },
    159: {
        "hint": "Teenagers naturally form cliques with peers who share identical clothing styles, music tastes, slang, and attitudes.",
        "memory_tip": "'Birds of a feather flock together' exemplifies adolescent peer conformity and clique formation."
    },
    160: {
        "hint": "The renowned textbook author who synthesized empirical lifespan research across developmental milestones.",
        "memory_tip": "Elizabeth B. Hurlock wrote 'Developmental Psychology: A Life-Span Approach' and 'Child Development'."
    },
    161: {
        "hint": "Hurlock's adolescent peer group classification explicitly includes Chums, Cliques, and Crowds, not 'Old Friends'.",
        "memory_tip": "Hurlock's Adolescent Peer Groups: Chums (1-2 close friends), Cliques (small circle), Crowds (large group)."
    },
    162: {
        "hint": "In sociological analysis of youth crowds, partyers are primarily focused on social gatherings and leisure rather than academic work.",
        "memory_tip": "Adolescent crowds reflect diverse behavioral subcultures: Jocks, Nerds, Partiers, Freaks."
    },
    163: {
        "hint": "This author compiled the definitive reference work defining fundamental psychological, behavioral, and clinical terminology.",
        "memory_tip": "J.P. Chaplin authored the acclaimed 'Dictionary of Psychology'."
    },
    164: {
        "hint": "Healthy leadership training involves sports, student councils, and community volunteering, never illegal or antisocial actions.",
        "memory_tip": "Cultivating Student Leadership = Democratic participation, community projects, student council."
    },
    165: {
        "hint": "The leadership approach where all power and decisions are centralized in the leader without any subordinate input.",
        "memory_tip": "Authoritarian (Autocratic) Leadership = Unilateral top-down decisions; strict control."
    },
    166: {
        "hint": "Adolescents vigorously demand independence and emancipation from parental control; lacking need for freedom is false.",
        "memory_tip": "Adolescent Hallmark = Strong drive for Independence and autonomy from parental supervision."
    },
    167: {
        "hint": "Adolescent group behavior manifests in peer conformity, dress uniformity, slang, and shared leisure activities.",
        "memory_tip": "Adolescent Group Dynamics = Peer culture, shared identity, and mutual social support."
    },
    168: {
        "hint": "Essential 21st-century youth training involves decision-making, critical thinking, stress management, and interpersonal communication.",
        "memory_tip": "WHO 10 Core Life Skills: Self-awareness, Empathy, Critical Thinking, Decision Making, Stress Coping, etc."
    },
    169: {
        "hint": "Intelligence is an unobservable psychological construct inferred from problem-solving and adaptive behavior.",
        "memory_tip": "Intelligence = An abstract construct (hypothetical construct inferred from observable performance)."
    },
    170: {
        "hint": "Differences in speed of learning, abstract reasoning, and problem solving among individuals are dictated by this trait.",
        "memory_tip": "Intelligence is the primary cognitive factor accounting for individual academic differences."
    },
    171: {
        "hint": "A person's intelligence is determined by genetic endowment operating within a supportive or deprived environment.",
        "memory_tip": "Intelligence = Result of dynamic interaction between Heredity (limits) and Environment (fulfillment)."
    },
    172: {
        "hint": "The calendar age of an individual counted in solar years, months, and days starting from the date of physical birth.",
        "memory_tip": "Chronological Age (CA) = Calendar age from date of birth (biological age)."
    },
    173: {
        "hint": "The intellectual maturity level reached by an individual as measured by standardized intelligence test performance.",
        "memory_tip": "Mental Age (MA) = Concept introduced by Alfred Binet (1908) representing level of intellectual maturity."
    },
    174: {
        "hint": "Evaluate the formula for Intelligence Quotient comparing Mental Age to Chronological Age multiplied by 100.",
        "memory_tip": "IQ = (Mental Age / Chronological Age) × 100 [MA/CA × 100]."
    },
    175: {
        "hint": "The practical ability to manipulate tools, machinery, apparatus, and physical equipment effectively.",
        "memory_tip": "Thorndike's 3 Types of Intelligence: Mechanical/Concrete, Abstract, Social. Manipulating objects = Mechanical."
    },
    176: {
        "hint": "The capacity to comprehend words, mathematical notations, geometric graphs, and conceptual scientific formulae.",
        "memory_tip": "Abstract Intelligence (Thorndike/Terman) = Ability to deal with verbal, mathematical, and conceptual symbols."
    },
    177: {
        "hint": "Lewis Terman defined intelligence concisely as the capacity of an individual to carry on abstract thinking.",
        "memory_tip": "Lewis Terman: 'An individual is intelligent in proportion to his ability to carry on abstract thinking.'"
    },
    178: {
        "hint": "William Stern and Lewis Terman developed the IQ formula to measure and express human intellectual capacity.",
        "memory_tip": "IQ (Intelligence Quotient) measures an individual's relative cognitive ability compared to peers."
    },
    179: {
        "hint": "The ratio of Mental Age to Chronological Age scaled by one hundred to eliminate decimals.",
        "memory_tip": "IQ Formula = (Mental Age / Chronological Age) × 100 [(MA / CA) × 100]."
    },
    180: {
        "hint": "Calculating IQ requires two distinct age parameters: intellectual performance age and actual calendar age.",
        "memory_tip": "IQ computation requires both Mental Age (MA from test) and Chronological Age (CA from birthdate)."
    },
    181: {
        "hint": "When a child's mental age precisely matches their chronological age, MA/CA equals 1, resulting in 100.",
        "memory_tip": "If MA = CA, IQ = (MA / CA) × 100 = (1) × 100 = 100 (Exact Average Intelligence)."
    },
    182: {
        "hint": "David Wechsler defined intelligence as the global capacity of an individual to act purposefully and think rationally.",
        "memory_tip": "David Wechsler: 'Intelligence is the aggregate or global capacity to act purposefully, think rationally and deal effectively with environment.'"
    },
    183: {
        "hint": "Thorndike categorized intelligence into Concrete/Mechanical, Abstract, and Social; 'Environmental' is not part of his triad.",
        "memory_tip": "Thorndike's Intelligence Triad = Concrete/Mechanical + Abstract + Social."
    },
    184: {
        "hint": "The capacity to understand, interact with, and build harmonious relationships with people in human society.",
        "memory_tip": "Social Intelligence (Thorndike) = Ability to understand and manage men and women, boys and girls."
    },
    185: {
        "hint": "Charles Spearman identified the underlying general mental energy that participates in all relational reasoning.",
        "memory_tip": "Spearman's 'g' factor = General cognitive energy underlying all intellectual tasks."
    },
    186: {
        "hint": "The cognitive capability to discern logical relationships, patterns, and principles to acquire new knowledge.",
        "memory_tip": "Intelligence = The capacity to learn through understanding relationships and patterns."
    },
    187: {
        "hint": "Cognitive variance and learning pace are fundamentally explained by differences in intellectual potential.",
        "memory_tip": "Variations in student academic achievement are primarily rooted in differences in Intelligence."
    },
    188: {
        "hint": "The standardized numerical index representing an individual's level of mental development relative to their age group.",
        "memory_tip": "IQ = Intelligence Quotient (coined by William Stern in 1912, popularized by Terman)."
    },
    189: {
        "hint": "William Stern and S.S. Colvin emphasized intelligence as the ability of an organism to adjust itself to new situations.",
        "memory_tip": "William Stern: 'Intelligence is a general capacity of an individual consciously to adjust his thinking to new requirements.'"
    },
    190: {
        "hint": "The American psychologist who opposed Spearman's 'g' factor and proposed the Multi-Factor (synthetic) Theory (CAVD test).",
        "memory_tip": "E.L. Thorndike = Multi-Factor Theory of Intelligence (CAVD: Completion, Arithmetic, Vocabulary, Directions)."
    },
    191: {
        "hint": "Spearman posited that this universal innate mental capacity enters into every single intellectual activity.",
        "memory_tip": "Charles Spearman's Two-Factor Theory = General factor ('g') + Specific factors ('s'). 'g' is universal."
    },
    192: {
        "hint": "L.L. Thurstone identified seven distinct primary factors and developed the PMA test battery.",
        "memory_tip": "L.L. Thurstone = Group Factor Theory of Intelligence (Primary Mental Abilities: V, W, N, S, M, P, R)."
    },
    193: {
        "hint": "Guilford's SI cube expanded: Operations (5) × Contents (5) × Products (6) = 150 factors (initially 120, revised to 150 & 180).",
        "memory_tip": "J.P. Guilford's Structure of Intellect (SI) Model = 5 Operations × 5 Contents × 6 Products = 150 cells."
    },
    194: {
        "hint": "Howard Gardner presented his groundbreaking Theory of Multiple Intelligences in this landmark 1983 book.",
        "memory_tip": "Howard Gardner wrote 'Frames of Mind: The Theory of Multiple Intelligences' (1983)."
    },
    195: {
        "hint": "Individuals possessing rich vocabulary, rhetorical persuasion, and verbal dexterity are colloquially called this.",
        "memory_tip": "Linguistic Intelligence = 'Word Smart' (Gardner's Multiple Intelligences)."
    },
    196: {
        "hint": "Authors, orators, attorneys, and poets rely predominantly on phonological sensitivity and grammatical mastery.",
        "memory_tip": "Linguistic Intelligence = Sensitivity to spoken and written language (Poets, writers, lawyers)."
    },
    197: {
        "hint": "Mathematicians, physicists, and computer programmers excel in inductive-deductive reasoning and numerical computation.",
        "memory_tip": "Logical-Mathematical Intelligence = 'Number/Logic Smart' (Scientists, Mathematicians)."
    },
    198: {
        "hint": "People who visualize 3D spaces, navigate accurately, and mentally rotate figures are categorized with this label.",
        "memory_tip": "Spatial Intelligence = 'Picture Smart' (Architects, sculptors, navigators)."
    },
    199: {
        "hint": "The mental capability to visualize spatial configurations, transform mental images, and create fine art.",
        "memory_tip": "Spatial Intelligence = Ability to perceive visual-spatial world accurately (Artists, Architects, Surgeons)."
    },
    200: {
        "hint": "Athletes, gymnasts, dancers, and surgeons possess exquisite fine and gross motor dexterity and body control.",
        "memory_tip": "Bodily-Kinesthetic Intelligence = 'Body Smart' (Dancers, Athletes, Surgeons, Yoga masters)."
    }
}

with open("cdp_enhancer/batch_2.json", "w") as f:
    json.dump(batch2, f, indent=2)
print("Batch 2 generated successfully! Total:", len(batch2))
