import json

batch5 = {
    401: {
        "hint": "Because the organism's behavior is instrumental in securing the reinforcement reward, it is also called this.",
        "memory_tip": "Operant Conditioning = Instrumental Conditioning (B.F. Skinner; behavior is instrumental in getting rewarded)."
    },
    402: {
        "hint": "Skinner famously placed hungry white rats into an operant chamber equipped with a lever that dispensed food pellets.",
        "memory_tip": "Skinner experimented on White Rats (lever press) and Pigeons (key peck)."
    },
    403: {
        "hint": "Unlike Pavlov's stimulus-elicited (S-type) reflex, Skinner's operant behavior is emitted voluntarily by the organism.",
        "memory_tip": "Operant Conditioning = R-Type Conditioning (Response-governed; behavior operates on the environment)."
    },
    404: {
        "hint": "In operant conditioning, the reinforcing pellet or praise is delivered strictly following the emission of the target correct response.",
        "memory_tip": "Operant Contingency: Response -> Reinforcing Stimulus (Reinforcement depends on correct response)."
    },
    405: {
        "hint": "Reinforcing a behavior only after a set, predictable amount of time has elapsed (e.g. weekly quiz, monthly salary).",
        "memory_tip": "Fixed Interval (FI) Schedule = Reinforcement given after a fixed, unchanging passage of time."
    },
    406: {
        "hint": "Analyze the core differences between classical stimulus association and operant response reinforcement.",
        "memory_tip": "Classical = S-R association; Operant = R-S reinforcement contingency."
    },
    407: {
        "hint": "Evaluate the theoretical assertions regarding Pavlov's respondent vs Skinner's operant paradigms.",
        "memory_tip": "Respondent Behavior = Involuntary reflex elicited by stimulus; Operant Behavior = Voluntary action emitted by organism."
    },
    408: {
        "hint": "Both connectionist and operant behavioral frameworks agree that reinforcement strengthens behavioral probability.",
        "memory_tip": "Behavioral Principle: Reinforcement increases the probability of a response recurring."
    },
    409: {
        "hint": "Providing reinforcement immediately every single time the learner executes the desired correct response.",
        "memory_tip": "Continuous Reinforcement Schedule (CRF) = Every single correct response is reinforced (best for initial acquisition)."
    },
    410: {
        "hint": "Reinforcing a student after a fixed, unchanging number of completed problems or responses (e.g. reward after every 5 tasks).",
        "memory_tip": "Fixed Ratio (FR) Schedule = Reinforcement delivered after a predetermined fixed number of responses."
    },
    411: {
        "hint": "The humanistic psychotherapist who developed non-directive, client-centered therapy emphasizing unconditional positive regard.",
        "memory_tip": "Carl Rogers = Client-Centered Therapy / Person-Centered Approach (Empathy, Congruence, Unconditional Positive Regard)."
    },
    412: {
        "hint": "The humanistic psychologist who arranged human motives into a 5-tier pyramid from physiological needs to self-actualization.",
        "memory_tip": "Abraham Maslow = Hierarchy of Needs (1943; Physiological -> Safety -> Belongingness -> Esteem -> Self-Actualization)."
    },
    413: {
        "hint": "Review Maslow's hierarchical levels: lower deficiency needs must be met before higher growth needs emerge.",
        "memory_tip": "Maslow's Pyramid: Deficiency Needs (D-needs: Physical, Safety, Love, Esteem) -> Being Needs (B-needs: Self-Actualization)."
    },
    414: {
        "hint": "The foundational survival necessities required to sustain biological life: air, food, water, and sleep.",
        "memory_tip": "Maslow's 1st Tier = Physiological Needs (Food, water, shelter, oxygen, sleep)."
    },
    415: {
        "hint": "Having a safe roof over one's head, physical protection from harm, and economic stability fulfills this second tier.",
        "memory_tip": "Maslow's 2nd Tier = Safety and Security Needs (Protection from danger, physical shelter, stability)."
    },
    416: {
        "hint": "Longing for friendship, romantic intimacy, acceptance in a peer group, and familial warmth belongs to this third level.",
        "memory_tip": "Maslow's 3rd Tier = Love and Belongingness Needs (Friendship, family, affiliation, affection)."
    },
    417: {
        "hint": "Love belongs to the 3rd tier of belongingness; Self-actualization is the apex 5th tier of fulfilling one's fullest creative potential.",
        "memory_tip": "Self-Actualization = Apex tier (realizing personal potential); Love = 3rd tier (social belongingness)."
    },
    418: {
        "hint": "Hands-on experiential learning (Kolb) actively energizes, motivates, and delights students; claiming they are unhappy is false.",
        "memory_tip": "Experiential Learning (David Kolb) = Learning through reflective action; produces high learner satisfaction."
    },
    419: {
        "hint": "Abraham Maslow's theory fundamentally explains how human behavior is driven and energized by hierarchical needs.",
        "memory_tip": "Maslow's Theory = Theory of Human Motivation and Needs."
    },
    420: {
        "hint": "The base foundation of the pyramid that demands immediate biological satisfaction before any psychological need can be felt.",
        "memory_tip": "Lowest Order Need = Physiological Needs (Foundational survival drives)."
    },
    421: {
        "hint": "The Stanford psychologist who formulated Social Learning Theory demonstrating that humans learn by observing models.",
        "memory_tip": "Albert Bandura = Social Learning Theory / Social Cognitive Theory (Observational Learning & Modeling)."
    },
    422: {
        "hint": "Children observe the actions of parents, teachers, and heroes and reproduce those behaviors through imitation.",
        "memory_tip": "Bandura: Learning occurs through Observational Modeling and Imitation of social models."
    },
    423: {
        "hint": "Bandura's paradigm is known as Social Learning, Observational Learning, and Modeling; 'Association' belongs to Pavlov/Thorndike.",
        "memory_tip": "Bandura's Theory = Observational Learning / Vicarious Learning / Social Cognitive Theory (NOT association)."
    },
    424: {
        "hint": "Bandura's observational modeling sequence consists of Attention, Retention, Reproduction, and Motivation (ARRM); Generalization is Pavlovian.",
        "memory_tip": "Bandura's 4 Modeling Steps: ARRM = Attention -> Retention -> Reproduction -> Motivation."
    },
    425: {
        "hint": "Storing the model's observed performance in memory through verbal coding or visual mental imagery for later retrieval.",
        "memory_tip": "Retention = Bandura's 2nd step (encoding and remembering the observed modeled behavior)."
    },
    426: {
        "hint": "A pupil closely attending to a teacher's procedural demonstration to replicate the steps exemplifies vicarious learning.",
        "memory_tip": "Observational Learning = Acquiring skills by carefully observing a competent model."
    },
    427: {
        "hint": "Before any modeling can take place, the learner must actively notice, focus upon, and perceive the model's behavior.",
        "memory_tip": "Attention = Bandura's 1st Step of Modeling (Focusing sensory perception on the model)."
    },
    428: {
        "hint": "Bandura's classic 1961 experiment where nursery children watched an adult beat an inflatable plastic clown doll.",
        "memory_tip": "Bobo Doll Experiment (Bandura, 1961) = Demonstrated that aggressive behavior is learned through observation."
    },
    429: {
        "hint": "Observational learning requires paying attention, retaining mental images, motor execution capability, and reinforcement incentive.",
        "memory_tip": "Bandura's Requirements = Attention + Retention + Motor Reproduction + Motivation."
    },
    430: {
        "hint": "The seminal 1963 volume by Albert Bandura and Richard Walters introducing observational modeling and personality development.",
        "memory_tip": "Bandura & Walters authored 'Social Learning and Personality Development' (1963)."
    },
    431: {
        "hint": "The influential 1960 book by Jerome Bruner that emerged from the Woods Hole Conference championing spiral curriculum.",
        "memory_tip": "Jerome Bruner authored 'The Process of Education' (1960; Spiral Curriculum & Discovery Learning)."
    },
    432: {
        "hint": "Constructivist instruction relies on active student exploration, intrinsic curiosity, and scaffolding, rejecting punitive coercion.",
        "memory_tip": "Bruner's Constructivism emphasizes discovery, intrinsic motivation, and exploration, opposing punishment."
    },
    433: {
        "hint": "Bruner stressed that learning driven by innate curiosity, wonder, and joy of mastery is far more potent than external grades.",
        "memory_tip": "Intrinsic Motivation (internal drive, curiosity, mastery) is central to Bruner's Discovery Learning."
    },
    434: {
        "hint": "Meaningful learning naturally ignites from the student's inner inquisitiveness and natural urge to explore.",
        "memory_tip": "Bruner: Instruction must tap into the child's natural curiosity and readiness to learn."
    },
    435: {
        "hint": "Bruner's pedagogical model where students actively uncover concepts, relationships, and principles on their own.",
        "memory_tip": "Bruner's Model = Discovery Learning Theory (Inquiry-based constructivist learning)."
    },
    436: {
        "hint": "Rather than passively receiving teacher lectures, students construct knowledge through active autonomous exploration.",
        "memory_tip": "Discovery learning places primary value on Self-Learning and learner autonomy."
    },
    437: {
        "hint": "Revisiting foundational ideas at increasing levels of depth and complexity across school grades.",
        "memory_tip": "Spiral Curriculum (Bruner) = Revisiting concepts with increasing depth and cognitive sophistication."
    },
    438: {
        "hint": "The famous educational hypothesis asserted by Jerome Bruner in 'The Process of Education' regarding developmental teachability.",
        "memory_tip": "Jerome Bruner: 'Any subject can be taught effectively in some intellectually honest form to any child at any stage of development.'"
    },
    439: {
        "hint": "Bruner's developmental progression of cognitive representation: hands-on action first, then visual images, then abstract symbols.",
        "memory_tip": "Bruner's 3 Modes of Representation: EIS = 1. Enactive (action), 2. Iconic (images), 3. Symbolic (words/symbols)."
    },
    440: {
        "hint": "In discovery learning, the instructor steps off the stage to facilitate, scaffold, observe, and guide students' inquiries.",
        "memory_tip": "Constructivist Teacher Role = Facilitator / Monitor / Scaffolder (Guide on the side, not sage on the stage)."
    },
    441: {
        "hint": "Representing information through mental pictures, schematic diagrams, illustrations, and visual imagery.",
        "memory_tip": "Iconic Mode (Bruner) = Visual sensory representation (diagrams, pictures, models)."
    },
    442: {
        "hint": "The pioneering developmental psychologist who worked in Moscow and founded the socio-historical school of psychology.",
        "memory_tip": "Lev Semyonovich Vygotsky was a Russian/Soviet developmental psychologist."
    },
    443: {
        "hint": "The developmental perspective arguing that cognitive growth is co-constructed through social interaction within a cultural context.",
        "memory_tip": "Lev Vygotsky = Socio-Cultural Theory of Cognitive Development."
    },
    444: {
        "hint": "Vygotsky's central construct describing the gap between what a child can do alone versus with adult assistance.",
        "memory_tip": "ZPD (Zone of Proximal Development) = Concept formulated by Lev Vygotsky."
    },
    445: {
        "hint": "The term 'schema' was coined by Bartlett and popularized by Jean Piaget; Vygotsky used ZPD, MKO, and Scaffolding.",
        "memory_tip": "Schemata = Piaget's concept; Vygotsky's concepts = ZPD, MKO, Scaffolding, Cultural Tools, Private Speech."
    },
    446: {
        "hint": "The acronym for the fertile developmental distance between independent problem-solving and potential guided capability.",
        "memory_tip": "ZPD = Zone of Proximal Development."
    },
    447: {
        "hint": "Abstract logical reasoning, metacognition, and deductive thinking are Higher Mental Functions (HMFs), not lower ones.",
        "memory_tip": "Vygotsky's Mental Functions: Lower (elementary sensation, simple reflexes) -> Higher (logical reasoning, selective attention, abstract thought)."
    },
    448: {
        "hint": "Elementary instinctive inquiries, basic perceptual grasping, and simple questioning originate as baseline biological functions.",
        "memory_tip": "Lower mental functions are innate, unmediated biological capacities (elementary perception and reactive questioning)."
    },
    449: {
        "hint": "Higher mental functions involve cultural signs, language mediation, and deliberate self-regulation.",
        "memory_tip": "Higher Mental Functions (HMF) = Language-mediated, culturally transmitted advanced cognitive processes."
    },
    450: {
        "hint": "Vygotsky posited that higher mental faculties are developed through internalizing social speech and cultural mediation.",
        "memory_tip": "Higher Mental Functions develop through social dialogue, collaborative peer interaction, and language."
    },
    451: {
        "hint": "ZPD equals the difference between Potential Performance Level with guidance (B) and Actual Independent Performance Level (A).",
        "memory_tip": "ZPD Formula: ZPD = Level of Potential Development (B) - Level of Actual Development (A) [ZPD = B - A]."
    },
    452: {
        "hint": "Jerome Bruner introduced the term 'Scaffolding' to operationalize Vygotsky's ZPD, providing temporary supportive assistance.",
        "memory_tip": "Scaffolding = Temporary support provided by a More Knowledgeable Other (MKO) until child achieves mastery."
    },
    453: {
        "hint": "Vygotsky viewed this cultural sign system as the supreme psychological tool for mediating and transforming human thought.",
        "memory_tip": "Language is the primary vehicle of thought and cognitive development according to Vygotsky."
    },
    454: {
        "hint": "Around age 7, external private speech (talking aloud to oneself during play) gets internalized into silent mental verbal thought.",
        "memory_tip": "Speech Evolution (Vygotsky): Social Speech (0-2 yrs) -> Private Speech (3-6 yrs) -> Inner Speech / Thought (7+ yrs)."
    },
    455: {
        "hint": "B.F. Skinner is a radical behaviorist; the Gestalt school was founded by Max Wertheimer, Wolfgang Köhler, and Kurt Koffka.",
        "memory_tip": "Gestalt Psychologists = Wertheimer, Köhler, Koffka, Lewin (Skinner is a Behaviorist)."
    },
    456: {
        "hint": "Wolfgang Köhler documented his Tenerife primate experiments on chimpanzee problem-solving in this famous 1925 book.",
        "memory_tip": "Wolfgang Köhler authored 'The Mentality of Apes' (1925; Insight Learning)."
    },
    457: {
        "hint": "Köhler conducted his classic stick and box problem-solving experiments on these intelligent primates on Tenerife island.",
        "memory_tip": "Köhler's Subjects = Chimpanzees (Insightful learning using sticks and boxes to reach bananas)."
    },
    458: {
        "hint": "The German word 'Gestalt' has no direct English equivalent, roughly meaning whole, shape, configuration, or total form.",
        "memory_tip": "Gestalt = German word meaning 'Unified Whole' / 'Configuration' ('The whole is greater than the sum of its parts')."
    },
    459: {
        "hint": "The brightest of Köhler's chimpanzees who demonstrated insightful problem-solving by joining two sticks together.",
        "memory_tip": "Sultan = Köhler's famous chimpanzee that discovered solutions through sudden insight."
    },
    460: {
        "hint": "The cognitive mode of learning where the solution to a complex problem appears suddenly in conscious awareness.",
        "memory_tip": "Insight Learning (Köhler) = Sudden perceptual restructuring of the problem situation ('Aha!' experience)."
    },
    461: {
        "hint": "Rather than seeing isolated pieces, the animal perceived boxes, sticks, and bananas as a complete, unified perceptual field.",
        "memory_tip": "Insight occurs when the problem situation is perceived and grasped as an 'Organized Whole'."
    },
    462: {
        "hint": "Mechanical conditioning is Thorndikian or Pavlovian association; insight is cognitive, thoughtful, and understanding-based.",
        "memory_tip": "Insight Learning features: Suddenness, cognitive restructuring, transferability to new tasks (NOT conditioning)."
    },
    463: {
        "hint": "Action research systematically begins when a classroom teacher perceives a specific localized educational difficulty.",
        "memory_tip": "Step 1 of Action Research = Identification and delimitation of the classroom problem."
    },
    464: {
        "hint": "Robert K. Greenleaf's philosophy of leadership where the primary calling of the leader is to serve and empower team members.",
        "memory_tip": "Servant Leadership (Greenleaf) = Leading by serving others, showing humility, and putting team welfare first."
    },
    465: {
        "hint": "Without clear classroom expectations and consistent norms, confusion and behavioral disruption inevitably occur.",
        "memory_tip": "Effective Classroom Management = Clear rules, predictable routines, fair consistency, and mutual respect."
    },
    466: {
        "hint": "After data collection and testing interventions, the action researcher summarizes findings in a structured written document.",
        "memory_tip": "Final Step of Action Research = Preparation of the Action Research Report / Reflective Dissemination."
    },
    467: {
        "hint": "Curriculum and lesson design are pedagogical matters, whereas seating, lighting, ventilation, and acoustics are physical factors.",
        "memory_tip": "Physical Classroom Environment = Seating arrangements, lighting, ventilation, room display (Lesson plan is pedagogical)."
    },
    468: {
        "hint": "The social process of inspiring, guiding, motivating, and directing a group toward achieving shared educational goals.",
        "memory_tip": "Leadership = The dynamic art of influencing and directing a group toward common objectives."
    },
    469: {
        "hint": "An emotionally erratic, volatile, and unpredictable person cannot provide steady direction or earn trust.",
        "memory_tip": "Qualities of an Effective Leader = Emotional stability, vision, integrity, empathy, and decisive clarity."
    },
    470: {
        "hint": "The authoritarian style where a leader dictates all directives and policies unilaterally without team input.",
        "memory_tip": "Autocratic (Authoritarian) Leadership = Unilateral control, strict obedience, no member participation."
    },
    471: {
        "hint": "The German-American social psychologist who originated Field Theory and coined the term 'Action Research' in 1944.",
        "memory_tip": "Kurt Lewin = Father of Action Research (Spiral cycle: Plan, Act, Observe, Reflect)."
    },
    472: {
        "hint": "Arranging desks in straight parallel columns facing forward toward the teacher's podium.",
        "memory_tip": "Traditional Row Seating = Straight rows facing blackboard; ideal for lecture and individual seatwork."
    },
    473: {
        "hint": "Clustering student desks in small circular pods of 4-5 enables face-to-face interaction, peer sharing, and group discussion.",
        "memory_tip": "Small Group Clusters / Pods = Best seating arrangement for collaborative and cooperative group work."
    },
    474: {
        "hint": "A digitally integrated modern learning space utilizing computers, interactive smart boards, internet, and multimedia.",
        "memory_tip": "E-Classroom = Utilizes digital multimedia, projectors, smart interactive screens, and online resources."
    },
    475: {
        "hint": "An effective classroom environment accommodates differentiated instruction, student diversity, and psychological safety.",
        "memory_tip": "Effective Classrooms = Learner-centered, supportive of diverse student needs, and actively engaging."
    },
    476: {
        "hint": "The ultimate aim of classroom management is establishing an orderly, positive, and engaging climate for learning.",
        "memory_tip": "Primary Goal of Classroom Management = Creating a positive, orderly, and productive learning environment."
    },
    477: {
        "hint": "Managing through unconditional positive regard, empathy, and emotional warmth originates from Carl Rogers' perspective.",
        "memory_tip": "Humanistic Approach (Rogers/Maslow) = Respect, empathy, dignity, and positive student-teacher relationships."
    },
    478: {
        "hint": "A constructive teacher-leader tirelessly nurtures student self-efficacy, courage, and confidence, never shattering it.",
        "memory_tip": "Teacher as Leader = Builds student self-confidence, models integrity, and empowers autonomous learning."
    },
    479: {
        "hint": "Kurt Lewin's classic Action Research cycle consists strictly of Planning, Acting, Observing, and Reflecting.",
        "memory_tip": "Lewin's Action Research Spiral = Plan -> Act -> Observe -> Reflect (PAOR)."
    },
    480: {
        "hint": "The leadership style that actively invites team input, consensus building, and shared participatory decision-making.",
        "memory_tip": "Democratic (Participative) Leadership = Shared decision-making, mutual consultation, and collaborative respect."
    },
    481: {
        "hint": "When a teacher enters the room without a clear lesson objective or timetable, instructional time is wasted aimlessly.",
        "memory_tip": "Poor Time Management = Lack of clear instructional objectives and structured lesson pacing."
    },
    482: {
        "hint": "Direct lecture delivery with unbroken eye contact on the teacher is best served by conventional row seating.",
        "memory_tip": "Teacher-Centered Seating = Traditional straight rows facing front."
    },
    483: {
        "hint": "The French term describing complete non-intervention, hands-off delegation, and total freedom granted to subordinates.",
        "memory_tip": "Laissez-Faire Leadership = Delegative, hands-off leadership with minimum leader interference."
    },
    484: {
        "hint": "Guidance is not an isolated one-off event; it is an ongoing developmental journey assisting personal growth across life.",
        "memory_tip": "Guidance is a continuous, pervasive, and lifelong developmental process."
    },
    485: {
        "hint": "The intensive, professional face-to-face interpersonal relationship that forms the heart of guidance services.",
        "memory_tip": "Counseling = The specialized, personal, face-to-face dynamic core of Guidance."
    },
    486: {
        "hint": "A psychologically healthy person possesses realistic self-esteem, resilience against adversity, and emotional balance.",
        "memory_tip": "Hallmarks of Mental Health = Emotional stability, realistic self-concept, social adaptability, and resilience."
    },
    487: {
        "hint": "Specialized guidance assisting students to discover their vocational aptitudes, select careers, and prepare for work.",
        "memory_tip": "Vocational Guidance = Assisting individuals to choose, prepare for, and progress in an occupational career."
    },
    488: {
        "hint": "Assisting an individual to resolve private emotional, behavioral, marital, or interpersonal family distress.",
        "memory_tip": "Personal Guidance = Assistance with private emotional, psychological, and behavioral challenges."
    },
    489: {
        "hint": "Ego defense mechanisms operate unconsciously to protect the self-concept from overwhelming anxiety, guilt, and stress.",
        "memory_tip": "Defense Mechanisms (Freud) = Unconscious ego strategies to reduce anxiety and psychological stress."
    },
    490: {
        "hint": "An adjusted person maintains an accurate assessment of their strengths, weaknesses, and realistic possibilities.",
        "memory_tip": "Good Adjustment = Realistic self-knowledge, emotional maturity, and harmony with environmental realities."
    },
    491: {
        "hint": "The primitive defense mechanism of flatly refusing to accept or acknowledge the existence of an unpleasant, painful reality.",
        "memory_tip": "Denial = Refusing to acknowledge an objective painful reality or truth (e.g. denying a fatal diagnosis)."
    },
    492: {
        "hint": "E.G. Williamson's counselor-centered approach where the counselor diagnoses, analyzes, and prescribes the solution.",
        "memory_tip": "Directive Counseling (E.G. Williamson) = Counselor-centered, diagnostic, prescriptive, and intellectual."
    },
    493: {
        "hint": "Standardized psychological tests (IQ, aptitude, personality) provide crucial objective diagnostic insight in counseling.",
        "memory_tip": "Psychological testing is an invaluable objective assessment tool in counseling."
    },
    494: {
        "hint": "Involuntarily forcing traumatic memories, unacceptable impulses, and agonizing feelings into the unconscious mind.",
        "memory_tip": "Repression = Unconscious motivated forgetting of painful or unacceptable thoughts."
    },
    495: {
        "hint": "Holistic well-being requires harmonious alignment across biological health, emotional balance, and social integration.",
        "memory_tip": "Holistic Well-being = Integration of Physical, Mental, Emotional, and Social Health."
    },
    496: {
        "hint": "Group guidance sessions bring together students experiencing identical developmental, study, or career challenges.",
        "memory_tip": "Group Guidance = Addressing common, shared developmental or informational concerns in groups."
    },
    497: {
        "hint": "Regular physical exercise releases endorphins, reduces cortisol stress levels, and revitalizes brain functioning.",
        "memory_tip": "Physical Fitness = Directly enhances neuro-cognitive functioning and mental well-being."
    },
    498: {
        "hint": "Possessing a warm network of supportive family and peer friendships is the greatest buffer against mental illness.",
        "memory_tip": "Mental Health Pillar = Warm, supportive, and trusting social relationships."
    },
    499: {
        "hint": "The harmonious state of equilibrium achieved between one's internal desires and the practical demands of society.",
        "memory_tip": "Adjustment = Harmonious compromise and balance between personal needs and environmental demands."
    },
    500: {
        "hint": "Retreating from painful reality into an imaginary mental world where all unfulfilled desires are miraculously satisfied.",
        "memory_tip": "Fantasy (Daydreaming) = Defense mechanism escaping real frustration through imaginary wish-fulfillment."
    }
}

with open("cdp_enhancer/batch_5.json", "w") as f:
    json.dump(batch5, f, indent=2)
print("Batch 5 generated successfully! Total:", len(batch5))
