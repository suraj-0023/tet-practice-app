# enhancements/topic26_30.py
# Q601 to Q720: Written Discourse, Alphabetical Order, Silent Letters, Reading Comprehension (Prose & Poetry)

TIPS = {
    # Topic 26: Letter Writing & Discourse (Q601 - Q624)
    601: {
        "hint": "The heading of a letter establishes origin and date of writing.",
        "memory_tip": "Letter format: The Heading includes the writer's address and the date."
    },
    602: {
        "hint": "Standard British and American date styles are all acceptable in letter writing.",
        "memory_tip": "Letter format: Dates may be written as 15 August 2024, August 15, 2024, or 15th August 2024."
    },
    603: {
        "hint": "The polite closing phrase before the signature (e.g. Yours sincerely).",
        "memory_tip": "Letter format: 'Yours sincerely / Yours faithfully' is called the Subscription (Leave-taking)."
    },
    604: {
        "hint": "The traditional subscription used by a student writing to a teacher or principal.",
        "memory_tip": "Letter format: Students addressing headmasters use 'Yours obediently' (no apostrophe in Yours)."
    },
    605: {
        "hint": "A paragraph giving a detailed sensory picture of a person, place, or event.",
        "memory_tip": "Writing discourse: Descriptive paragraph paints vivid details of a person, place, or thing."
    },
    606: {
        "hint": "An invitation card must state key event details concisely without lengthy text.",
        "memory_tip": "Discourse rule: Invitations prioritize brevity, clarity of venue, date, and host."
    },
    607: {
        "hint": "Electronic correspondence demands concise, direct, and brief communication.",
        "memory_tip": "Email feature: Brevity and clear subject lines are essential in email etiquette."
    },
    608: {
        "hint": "A conversation consists fundamentally of alternating speech turns between speakers.",
        "memory_tip": "Discourse: Conversations are structured around dialogue exchanges / turns."
    },
    609: {
        "hint": "The standard expansion of the technological abbreviation 'e-mail'.",
        "memory_tip": "Vocabulary: 'E-mail' stands for Electronic mail."
    },
    610: {
        "hint": "An informal or inappropriate salutation for professional corporate correspondence.",
        "memory_tip": "Email etiquette: 'My Dear Manager' is overly familiar; use 'Dear Sir/Madam' or 'Dear Mr. Rao'."
    },
    611: {
        "hint": "Delaying email replies shows unprofessionalism and disregard.",
        "memory_tip": "Email etiquette: Prompt replies are expected; replying late violates professional etiquette."
    },
    612: {
        "hint": "Any well-written biographical sketch requires logical flow and connection.",
        "memory_tip": "Discourse: Coherence is essential for all biographical sketches."
    },
    613: {
        "hint": "Biographies recount another person's life and use 'he/she/they'.",
        "memory_tip": "Discourse: A biographical sketch is written in the Third Person ('he/she'); Autobiography is 1st person."
    },
    614: {
        "hint": "A public announcement giving formal information about an upcoming event or instruction.",
        "memory_tip": "Discourse: A Notice is a formal public display for communicating information to a group."
    },
    615: {
        "hint": "Personal diaries record reflections, mistakes, and aspirations for tomorrow.",
        "memory_tip": "Discourse: Diary entries contain personal reflections, self-evaluation, and future plans."
    },
    616: {
        "hint": "A private record of daily events, feelings, and thoughts.",
        "memory_tip": "Discourse: A Diary records daily personal experiences and reflections."
    },
    617: {
        "hint": "Reflecting honestly in a diary helps a person improve constructively.",
        "memory_tip": "Discourse: Self-reflection in diary writing serves as constructive self-criticism."
    },
    618: {
        "hint": "A diary writer speaks about their own personal life experiences.",
        "memory_tip": "Discourse: A diary entry is written in First Person narrative ('I / we')."
    },
    619: {
        "hint": "Natural dialogue uses cohesive devices and transition words to connect ideas.",
        "memory_tip": "Discourse: Natural conversations require cohesive devices; avoiding them is incorrect."
    },
    620: {
        "hint": "The polite conventional opening exchange between speakers.",
        "memory_tip": "Conversation structure: Conversations typically open with Greetings (Hello, Good morning)."
    },
    621: {
        "hint": "Words like 'well', 'you know', 'actually' that manage the flow of conversation.",
        "memory_tip": "Linguistics: Discourse markers indicate transitions, attitudes, and turn-taking in talk."
    },
    622: {
        "hint": "Words that join and link thoughts across conversational exchanges.",
        "memory_tip": "Discourse: Linkers connect sentences and conversational thoughts."
    },
    623: {
        "hint": "The polite greeting at the beginning of a letter (e.g. Dear Sir).",
        "memory_tip": "Letter format: 'Dear Sir/Madam' is called the Salutation (greeting)."
    },
    624: {
        "hint": "An invitation must feature attractive presentation, clear layout, and appropriate structure.",
        "memory_tip": "Discourse: A successful invitation features an apt format and clear visual layout."
    },

    # Topic 27: Alphabetical Order & Reference Skills (Q625 - Q648)
    625: {
        "hint": "Compare letters position by position: a-b-r comes after a-b-i and a-b-o.",
        "memory_tip": "Alphabetical order: Check letter by letter (a-b-r comes after a-b-a, a-b-i)."
    },
    626: {
        "hint": "Compare letters: a-g-e comes after a-c-..., a-d-..., and a-f-...",
        "memory_tip": "Alphabetical order: 'g' comes after 'c', 'd', and 'f' -> 'agent' is last."
    },
    627: {
        "hint": "Compare 'adm-' with other 'ad-' prefixes; 'm' comes later than 'd', 'e', 'j'.",
        "memory_tip": "Alphabetical order: 'admittance' comes after 'address', 'adept', etc."
    },
    628: {
        "hint": "Compare 'b-o-o' with 'b-a-...', 'b-e-...', 'b-i-...'.",
        "memory_tip": "Alphabetical order: 'o' comes after 'a', 'e', 'i' -> 'boon' is last."
    },
    629: {
        "hint": "First word in alphabetical order: compare second and third letters of 'b-'.",
        "memory_tip": "Alphabetical order: Sort alphabetically to find the earliest entry."
    },
    630: {
        "hint": "Compare 'c-i-r-' with words having later letters.",
        "memory_tip": "Alphabetical order: 'ci-' precedes 'cl-', 'co-', 'cu-'."
    },
    631: {
        "hint": "Compare 'col-' with 'com-', 'con-', 'cor-'.",
        "memory_tip": "Alphabetical order: 'collaboration' comes earliest among 'co-' words."
    },
    632: {
        "hint": "Compare 'dep-' with other 'de-' words.",
        "memory_tip": "Alphabetical order: Check letter by letter from left to right."
    },
    633: {
        "hint": "Find the word with the latest alphabetical position starting with 'd-'.",
        "memory_tip": "Alphabetical order: 'disuse' appears after 'distance', 'disaster', etc."
    },
    634: {
        "hint": "Compare 'dr-' with 'da-', 'de-', 'di-'.",
        "memory_tip": "Alphabetical order: 'r' comes later in the alphabet than 'a', 'e', 'i' -> 'drink'."
    },
    635: {
        "hint": "Compare 'em-' with earlier 'e-' words.",
        "memory_tip": "Alphabetical order: 'emigration' comes after 'element', 'embargo'."
    },
    636: {
        "hint": "Compare 'ev-' with earlier 'e-' words.",
        "memory_tip": "Alphabetical order: 'v' is near the end of the alphabet -> 'evolve' is last."
    },
    637: {
        "hint": "Compare 'fe-' words; 'feminine' comes after 'fear', 'feeble'.",
        "memory_tip": "Alphabetical order: 'feminine' is placed after earlier 'fe-' entries."
    },
    638: {
        "hint": "Find the earliest word beginning with 'g-'.",
        "memory_tip": "Alphabetical order: 'ge-' precedes 'gi-', 'gl-', 'gr-'."
    },
    639: {
        "hint": "Earliest word starting with 'h-': 'ha-n-' precedes 'ha-r-', 'he-', 'ho-'.",
        "memory_tip": "Alphabetical order: 'handbag' comes first among the set."
    },
    640: {
        "hint": "Earliest word starting with 'j-': compare 'j-o-i-' with other 'j-' entries.",
        "memory_tip": "Alphabetical order: 'joint' comes first in alphabetical sequence."
    },
    641: {
        "hint": "Alphabetical ordering for 'j-' words.",
        "memory_tip": "Alphabetical order: Compare subsequent letters systematically."
    },
    642: {
        "hint": "Alphabetical ordering for 'l-' words.",
        "memory_tip": "Alphabetical order: 'local' position in sequence."
    },
    643: {
        "hint": "Alphabetical ordering for 'm-' words.",
        "memory_tip": "Alphabetical order: 'merciless' positioning."
    },
    644: {
        "hint": "Alphabetical ordering for 'n-' words.",
        "memory_tip": "Alphabetical order: 'nurture' positioning."
    },
    645: {
        "hint": "Alphabetical ordering for 'o-' words.",
        "memory_tip": "Alphabetical order: 'omnipresent' positioning."
    },
    646: {
        "hint": "Latest word alphabetically among 'p-' entries.",
        "memory_tip": "Alphabetical order: 'paralyse' appears last in this set."
    },
    647: {
        "hint": "Alphabetical sequence for 'p-' words.",
        "memory_tip": "Alphabetical order: 'plant' positioning."
    },
    648: {
        "hint": "Alphabetical sequence for 's-' words.",
        "memory_tip": "Alphabetical order: 'scholarship' positioning."
    },

    # Topic 28: Silent Letters (Q649 - Q672)
    649: {
        "hint": "Pronounced /ˈsʌt.əl/; the letter before 't' is not voiced.",
        "memory_tip": "Silent letter: 'b' is silent before 't' in subtle, doubt, debt."
    },
    650: {
        "hint": "Pronounced /əˈlaɪn/; the letter before 'n' is unvoiced.",
        "memory_tip": "Silent letter: 'g' is silent before 'n' in align, sign, reign, foreign."
    },
    651: {
        "hint": "Pronounced /tuːm/; the final letter after 'm' is silent.",
        "memory_tip": "Silent letter: 'b' is silent after 'm' in tomb, bomb, comb, lamb."
    },
    652: {
        "hint": "In non-rhotic standard British/Indian pronunciation, 'r' after a vowel is unpronounced.",
        "memory_tip": "Silent letter: 'r' is silent before consonants in non-rhotic pronunciation (Saturday)."
    },
    653: {
        "hint": "Pronounced /ʃɔːl/; the 'w' merges into the vowel sound.",
        "memory_tip": "Phonetics: 'w' in 'shawl' serves as vowel digraph spelling."
    },
    654: {
        "hint": "Pronounced /ˈpɑːsl/; the 'r' before 'c' is silent in standard non-rhotic speech.",
        "memory_tip": "Silent letter: 'r' before consonants is silent in non-rhotic RP."
    },
    655: {
        "hint": "Pronounced /det/; the letter 'b' before 't' is not articulated.",
        "memory_tip": "Silent letter: 'b' is silent before 't' in debt, doubt, subtle."
    },
    656: {
        "hint": "Pronounced /saɪð/; the letter 'c' following 's' is silent.",
        "memory_tip": "Silent letter: 'c' is silent after 's' in scythe, scene, muscle, scent."
    },
    657: {
        "hint": "Pronounced /sɑːm/; initial 'p' before 's' is not voiced.",
        "memory_tip": "Silent letter: 'p' is silent before 's' in psalm, psychology, psychic."
    },
    658: {
        "hint": "Pronounced /læm/; the final letter after 'm' is silent.",
        "memory_tip": "Silent letter: 'b' is silent at the end of words after 'm' (lamb, thumb, crumb)."
    },
    659: {
        "hint": "Pronounced /leŋθ/; the letter 'g' is part of the velar nasal digraph.",
        "memory_tip": "Phonetics: 'g' in 'length' is not pronounced as a hard /g/ sound."
    },
    660: {
        "hint": "Pronounced /ˈmɒn.ək/; 'r' is silent in non-rhotic pronunciation.",
        "memory_tip": "Phonetics: Non-rhotic silence of 'r' in final unstressed syllables."
    },
    661: {
        "hint": "Pronounced /ˈdeɪ.briː/ or /ˈdeb.riː/ from French; the final letter is silent.",
        "memory_tip": "Silent letter: French loanwords retain silent final 's' (debris, rendezvous)."
    },
    662: {
        "hint": "Pronounced /ˈmɒd.ən/; 'r' before 'n' is not voiced in non-rhotic pronunciation.",
        "memory_tip": "Silent letter: Post-vocalic 'r' is silent in non-rhotic English (modern, pattern)."
    },
    663: {
        "hint": "Pronounced /skɑːf/; 'r' is silent in non-rhotic pronunciation.",
        "memory_tip": "Silent letter: 'r' before consonants is unpronounced (scarf, car)."
    },
    664: {
        "hint": "Pronounced /ˈaɪ.ən/; the letter 'r' is completely silent.",
        "memory_tip": "Silent letter: 'r' is silent in 'iron' (/ˈaɪən/), not pronounced 'eye-ron'."
    },
    665: {
        "hint": "Pronounced /buˈkeɪ/ from French; final 't' is silent.",
        "memory_tip": "Silent letter: Final 't' is silent in French loanwords (bouquet, ballet, buffet)."
    },
    666: {
        "hint": "Pronounced /raɪm/; the letter 'h' after 'r' is silent.",
        "memory_tip": "Silent letter: 'h' is silent after 'r' in rhyme, rhythm, rhetoric."
    },
    667: {
        "hint": "Pronounced /ˈaʊ.ərz/; the initial 'h' is completely silent.",
        "memory_tip": "Silent letter: Initial 'h' is silent in hour, heir, honest, honor."
    },
    668: {
        "hint": "Pronounced /daʊt/; the letter 'b' before 't' is unvoiced.",
        "memory_tip": "Silent letter: 'b' is silent before 't' in doubt and debt."
    },
    669: {
        "hint": "Pronounced /saɪˈkɒl.ə.dʒi/; the Greek initial 'p' is silent.",
        "memory_tip": "Silent letter: Initial 'p' is silent before 's' in psychology, psychiatrist."
    },
    670: {
        "hint": "Pronounced /reɪn/; the letter 'g' before 'n' is silent.",
        "memory_tip": "Silent letter: 'g' is silent before 'n' in reign, feign, sovereign."
    },
    671: {
        "hint": "Pronounced /ˈdeɪ.bjuː/ or /deɪˈbjuː/ from French; final 't' is silent.",
        "memory_tip": "Silent letter: Final 't' is silent in debut, depot, chalet."
    },
    672: {
        "hint": "Pronounced /ˈkɑːs.əl/; the letter 't' in '-stle' is silent.",
        "memory_tip": "Silent letter: 't' is silent in '-stle' words (castle, whistle, rustle, listen)."
    },

    # Topic 29: Reading Comprehension - Prose (Q673 - Q696)
    673: {
        "hint": "Recall the story of the Golden Fish: why did the fisherman release it?",
        "memory_tip": "Comprehension: The kind fisherman felt pity and spared the talking golden fish."
    },
    674: {
        "hint": "What miraculous ability surprised the fisherman at the seashore?",
        "memory_tip": "Comprehension: The supernatural element was the golden fish speaking with human words."
    },
    675: {
        "hint": "Consider Swami Vivekananda's (Narendra's) courage, knowledge, and dedication.",
        "memory_tip": "Comprehension: Great spiritual leadership arose from combined virtues (All of the above)."
    },
    676: {
        "hint": "Why was Narendranath abbreviated to Narendra in childhood?",
        "memory_tip": "Comprehension: His original full name was too long for everyday calling."
    },
    677: {
        "hint": "Which traditional acrobatic performance was described in the passage?",
        "memory_tip": "Comprehension: The passage highlights the thrilling street art of rope walking."
    },
    678: {
        "hint": "How did Tenali Rama trick the thieves into watering his garden?",
        "memory_tip": "Comprehension: Tenali tricked the thieves into pulling all the water out of the well."
    },
    679: {
        "hint": "Review the exact sequence of ingredients in the tea-making recipe.",
        "memory_tip": "Comprehension: Steps in practical procedure texts must follow chronological order."
    },
    680: {
        "hint": "Which picturesque river valley is Dindi nestled beside in Andhra Pradesh?",
        "memory_tip": "Comprehension: Dindi is famous as a scenic village in the lap of the Godavari River."
    },
    681: {
        "hint": "What memorable musical contribution did Margaret Cousins make in Madanapalle?",
        "memory_tip": "Comprehension: Margaret Cousins set Tagore's 'Jana Gana Mana' to its musical tune in Madanapalle."
    },
    682: {
        "hint": "Opponents were amazed by Major Dhyan Chand's supernatural ball control.",
        "memory_tip": "Comprehension: People inspected his hockey stick suspecting magnets were concealed inside."
    },
    683: {
        "hint": "Identify the character who helped wash clothes in the textbook tale.",
        "memory_tip": "Comprehension: Identify specific character occupations stated in the narrative."
    },
    684: {
        "hint": "What colored container did Mia discover in the story?",
        "memory_tip": "Comprehension: Details in stories: Mia discovered a blue box."
    },
    685: {
        "hint": "Which predator threatened the infant in the forest story?",
        "memory_tip": "Comprehension: A wolf tried to attack the defenseless baby."
    },
    686: {
        "hint": "What was the brave mongoose's noble motive in fighting the serpent?",
        "memory_tip": "Comprehension: The loyal mongoose fought and killed the snake to protect the child."
    },
    687: {
        "hint": "What obstacle hindered the farmer from plowing his plot of land?",
        "memory_tip": "Comprehension: The farmer's field was heavily covered with large stones."
    },
    688: {
        "hint": "Recall the classic Aesop fable about the farmer and his miraculous bird.",
        "memory_tip": "Comprehension: The farmer's fortune changed because his goose laid golden eggs."
    },
    689: {
        "hint": "What greedy thought caused the farmer to ruin his blessing?",
        "memory_tip": "Comprehension: Greed prompted him to try to get all the golden eggs at once."
    },
    690: {
        "hint": "Why did the personified river weep in the environmental story?",
        "memory_tip": "Comprehension: The river was drying up and dying due to excessive human pollution."
    },
    691: {
        "hint": "In Maupassant's famous story 'The Necklace', what made Matilda discontented?",
        "memory_tip": "Comprehension: Matilda Loisel grieved that she owned no expensive jewellery."
    },
    692: {
        "hint": "What milestone made the morning extraordinary for wheelchair-using Mallika?",
        "memory_tip": "Comprehension: It was Mallika's long-awaited first day attending school."
    },
    693: {
        "hint": "What does genuine parity between genders provide to all individuals?",
        "memory_tip": "Comprehension: Gender equality guarantees equal rights, resources, and opportunities."
    },
    694: {
        "hint": "In democratic and fair households, who shares equal rights to make decisions?",
        "memory_tip": "Comprehension: Equal partnership means both men and women have equal voice."
    },
    695: {
        "hint": "What role was assigned to the little girl at the entry gate?",
        "memory_tip": "Comprehension: Her duty was admitting visitors who held valid tickets."
    },
    696: {
        "hint": "What is the recurring schedule of the hot air balloon festival mentioned?",
        "memory_tip": "Comprehension: Look for frequency keywords in informational texts: once every year."
    },

    # Topic 30: Reading Comprehension - Poetry (Q697 - Q720)
    697: {
        "hint": "The poem explores the physical structure made of brick, stone, and wood.",
        "memory_tip": "Poetry: A 'house' is the physical building; a 'home' is built of loving family relationships."
    },
    698: {
        "hint": "The second stanza contrasts physical bricks with love, unselfish acts, and family warmth.",
        "memory_tip": "Poetry: A home is defined by caring relationships, affection, and togetherness."
    },
    699: {
        "hint": "In the poem 'The Kite', how does a new kite look against the clear blue sky?",
        "memory_tip": "Poetry: 'How bright on the blue / Is a kite when it's new!'."
    },
    700: {
        "hint": "Find words that share matching final sounds in the kite poem.",
        "memory_tip": "Poetic device: Rhyme scheme pairs words ending in identical sounds (tides / rides)."
    },
    701: {
        "hint": "What flying object climbs, dives, and rides upon the wind?",
        "memory_tip": "Poetry: Pronoun reference: 'it' refers back to the soaring kite."
    },
    702: {
        "hint": "Who are the two family members engaged in the playful quarrel?",
        "memory_tip": "Poetry: The poem 'The Quarrel' depicts the poet and her brother."
    },
    703: {
        "hint": "Identify the pair of words with the identical rhyming ending sound /-aɪt/.",
        "memory_tip": "Rhyming pair: 'slight' and 'right' share the rhyme /-aɪt/."
    },
    704: {
        "hint": "Why did the brother suddenly hit the poet's back and admit fault?",
        "memory_tip": "Poetry: To break the tense silence and end the quarrel playfully for fun's sake."
    },
    705: {
        "hint": "In the poem celebrating harvest, what gives the villagers cause to dance?",
        "memory_tip": "Poetry: Harvest songs celebrate gratitude for abundant crop harvest."
    },
    706: {
        "hint": "What does the poet encourage us to continually renew in our hearts?",
        "memory_tip": "Poetry: Noble deeds and happy, virtuous thoughts should repeat constantly."
    },
    707: {
        "hint": "The joyful word game of language and thoughts can be enjoyed by everybody.",
        "memory_tip": "Poetry: 'The Wonderful Words' affirms anyone can participate in expressing ideas."
    },
    708: {
        "hint": "What serves as the garment and nourishment giving life to thoughts?",
        "memory_tip": "Poetry: 'Words are the food and dress of thought' (metaphor for expression)."
    },
    709: {
        "hint": "Thoughts remain trapped prisoners in our minds until liberated by what tool?",
        "memory_tip": "Poetry: Only articulate words can liberate and express an imprisoned thought."
    },
    710: {
        "hint": "In the poem 'The Ant and the Cricket', what tragedy faces the cricket in winter?",
        "memory_tip": "Poetry: Without stored food, the starving cricket risks dying of cold and starvation."
    },
    711: {
        "hint": "Which proverbially industrious insects are praised for diligence and hard work?",
        "memory_tip": "Poetry: Ants are famously hardworking; calling them lazy is completely incorrect."
    },
    712: {
        "hint": "In Rabindranath Tagore's poem 'The Last Bargain', what weapon did the King hold?",
        "memory_tip": "Poetry: 'With sword in hand, the King came in his chariot' (symbolizing worldly power)."
    },
    713: {
        "hint": "In William Blake's 'The School Boy', what creature symbolizes the constrained student?",
        "memory_tip": "Poetry: 'How can the bird that is born for joy / Sit in a cage and sing?' -> caged bird."
    },
    714: {
        "hint": "Under strict surveillance at school, where does the unhappy boy fail to find joy?",
        "memory_tip": "Poetry: The schoolboy finds joy neither in dull textbooks nor in the classroom bower."
    },
    715: {
        "hint": "How does the melancholy child endure the oppressive hours of the schoolday?",
        "memory_tip": "Poetry: He spends the school hours in sorrow, sighing, and dismay."
    },
    716: {
        "hint": "In Robert Frost's 'Dust of Snow', on what poisonous tree did the crow sit?",
        "memory_tip": "Poetry: A poisonous 'hemlock tree' with small white flowers."
    },
    717: {
        "hint": "In 'A Tiger in the Zoo', what vehicle sounds echo through the night?",
        "memory_tip": "Poetry: The trapped tiger hears the distant sirens and sounds of patrolling cars."
    },
    718: {
        "hint": "Where is the proud wild predator confined against his nature?",
        "memory_tip": "Poetry: The magnificent beast is locked inside a concrete cage/cell."
    },
    719: {
        "hint": "What emotional condition characterizes the restricted, caged child?",
        "memory_tip": "Poetry: Blake shows the child feels suffocated, controlled, and denied natural freedom."
    },
    720: {
        "hint": "In Adrienne Rich's 'The Trees', where are the indoor trees breaking out toward?",
        "memory_tip": "Poetry: The captive trees are moving back into their natural home, the forest."
    }
}
