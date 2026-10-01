# enhancements/topic6_10.py
# Q121 to Q240: Phrasal verbs, Confused words / Homophones, Affixes / Word formation, Collocations, Parts of speech

TIPS = {
    # Topic 6: Phrasal Verbs (Q121 - Q144)
    121: {
        "hint": "To cease doing an activity or habit permanently.",
        "memory_tip": "Phrasal verb: 'Give up' = surrender, abandon, or stop a habit (e.g. give up smoking)."
    },
    122: {
        "hint": "To distribute items or pass them to members of a group.",
        "memory_tip": "Phrasal verb: 'Hand out' = distribute copies, books, or papers to a group."
    },
    123: {
        "hint": "To provide something good to balance or reduce the bad effect of damage or loss.",
        "memory_tip": "Phrasal verb: 'Make up for' = compensate for a loss, mistake, or deficiency."
    },
    124: {
        "hint": "To officially or legally transfer ownership of property or possessions.",
        "memory_tip": "Phrasal verb: 'Make over' = legally transfer title or property to someone."
    },
    125: {
        "hint": "To reconcile and become friendly again after a dispute or fight.",
        "memory_tip": "Phrasal verb: 'Make up' = resolve differences, forgive, and restore harmony."
    },
    126: {
        "hint": "Diving into an activity recklessly without prior thought or planning.",
        "memory_tip": "Phrasal verb: 'Plunge in' = jump into an action hastily without careful forethought."
    },
    127: {
        "hint": "Continuing to talk or write at great length in a wandering, unstructured way.",
        "memory_tip": "Phrasal verb: 'Ramble on' = speak or write endlessly without a clear, concise focus."
    },
    128: {
        "hint": "Remaining inside one's house rather than venturing outside.",
        "memory_tip": "Phrasal verb: 'Stay in' = remain indoors (opposite of go out)."
    },
    129: {
        "hint": "Remaining awake and not retiring to bed until very late.",
        "memory_tip": "Phrasal verb: 'Stay up' = remain awake past one's normal bedtime."
    },
    130: {
        "hint": "Maintaining a safe physical distance; restraining oneself from moving closer.",
        "memory_tip": "Phrasal verb: 'Keep back' = stay at a safe distance; remain behind."
    },
    131: {
        "hint": "Preventing oneself or others from approaching or touching something.",
        "memory_tip": "Phrasal verb: 'Keep away' = maintain distance, avoid contact."
    },
    132: {
        "hint": "Departing or leaving a location, especially to make a move.",
        "memory_tip": "Phrasal verb: 'Get along' (in context) = leave or be on one's way."
    },
    133: {
        "hint": "To return to a place after going elsewhere.",
        "memory_tip": "Phrasal verb: 'Get back' = return to a starting point or home."
    },
    134: {
        "hint": "A person's face or eyes suddenly showing intense delight, excitement, or joy.",
        "memory_tip": "Phrasal verb: 'Light up' (past 'lit up') = radiate happiness, brighten with joy."
    },
    135: {
        "hint": "To draw attention to, emphasize, or emphasize something significant.",
        "memory_tip": "Phrasal verb: 'Point up' = emphasize, accentuate, or highlight a key feature."
    },
    136: {
        "hint": "To direct someone's attention to a particular fact or detail by mentioning it.",
        "memory_tip": "Phrasal verb: 'Point out' = draw attention to or state/mention a specific fact."
    },
    137: {
        "hint": "To provide care, protection, and supervision for someone or something.",
        "memory_tip": "Phrasal verb: 'Look after' = take care of, attend to the needs of."
    },
    138: {
        "hint": "Glancing in different directions in search of something misplaced or needed.",
        "memory_tip": "Phrasal verb: 'Look around for' = search or seek in surrounding areas."
    },
    139: {
        "hint": "Thinking about or reviewing past events and memories.",
        "memory_tip": "Phrasal verb: 'Look back' = reflect upon past experiences; review history."
    },
    140: {
        "hint": "Deriding or mocking someone with laughter.",
        "memory_tip": "Phrasal verb: 'Laugh at' = ridicule, mock, or chuckle derisively at."
    },
    141: {
        "hint": "To start out on an expedition, trip, or voyage.",
        "memory_tip": "Phrasal verb: 'Set off' = begin a journey or voyage."
    },
    142: {
        "hint": "To stop employing someone or to cease using something.",
        "memory_tip": "Phrasal verb: 'Lay off' = dismiss employees or stop using/bothering something."
    },
    143: {
        "hint": "To attack someone physically or verbally with fierce aggression.",
        "memory_tip": "Phrasal verb: 'Lay into' = attack vigorously with fists or angry words."
    },
    144: {
        "hint": "To establish, construct, or erect a structure, organization, or business.",
        "memory_tip": "Phrasal verb: 'Set up' = erect, build, or establish."
    },

    # Topic 7: Homophones / Confused Words (Q145 - Q168)
    145: {
        "hint": "'Hear' refers to auditory perception; 'here' refers to location.",
        "memory_tip": "Mnemonic: You 'hear' with your 'EAR'; 'here' is near 'there'."
    },
    146: {
        "hint": "'Week' is seven days; 'weak' is lacking strength.",
        "memory_tip": "Mnemonic: 'Seven days make one week; no strength makes one weak'."
    },
    147: {
        "hint": "'Buy' means purchase; 'by' denotes proximity or agency.",
        "memory_tip": "Usage: 'Buy' (purchase with money) vs. 'By' (beside, according to)."
    },
    148: {
        "hint": "'Peace' means calm/tranquility; 'piece' means a section or part.",
        "memory_tip": "Mnemonic: Have a 'piece of pie' (both spelled with 'pie')."
    },
    149: {
        "hint": "'Sun' is the solar star; 'son' is a male offspring.",
        "memory_tip": "Usage: The 'sun' shines in the sky; a parents' male child is their 'son'."
    },
    150: {
        "hint": "'Scent' is a fragrance/smell; 'sent' is the past tense of send.",
        "memory_tip": "Usage: 'Scent' (aroma with 'sc') vs 'Sent' (dispatched)."
    },
    151: {
        "hint": "A monarch's period of rule is spelled with a silent 'g'.",
        "memory_tip": "Homophones: 'Reign' (rule of king) vs 'Rain' (water) vs 'Rein' (horse strap)."
    },
    152: {
        "hint": "'Two' is the number 2; 'to' is the preposition.",
        "memory_tip": "Usage: 'Two' (number 2), 'to' (preposition/direction), 'too' (also/excessive)."
    },
    153: {
        "hint": "'Sight' refers to vision; 'site' refers to a physical location or area.",
        "memory_tip": "Usage: 'Sight' (eyesight, view) vs 'Site' (building/construction site)."
    },
    154: {
        "hint": "'Hare' is a rabbit-like animal; 'hair' grows on the head.",
        "memory_tip": "Usage: 'Hare' (animal in the race) vs 'Hair' (strands on the scalp)."
    },
    155: {
        "hint": "'Write' is composing text with a pen; 'right' means correct or opposite of left.",
        "memory_tip": "Usage: 'Write' with a pen; 'Right' answer."
    },
    156: {
        "hint": "'Saw' functions both as the past of see and as a cutting tool.",
        "memory_tip": "Homonym: 'Saw' (past tense of see) and 'saw' (carpenter's toothed tool)."
    },
    157: {
        "hint": "'See' means to perceive with eyes; 'sea' is a large body of saltwater.",
        "memory_tip": "Mnemonic: 'See' with double 'ee' (eyes); 'Sea' has 'a' for aquatic."
    },
    158: {
        "hint": "The base verb for discovering or locating something.",
        "memory_tip": "Vocabulary: 'Find' (discover) vs 'Fined' (penalized with fee)."
    },
    159: {
        "hint": "'Advise' (with 's') is the verb; 'advice' (with 'c') is the noun.",
        "memory_tip": "Grammar rule: 'Advise' = verb (action); 'Advice' = noun (counsel given)."
    },
    160: {
        "hint": "'Meat' is animal flesh used as food; 'meet' is encountering someone.",
        "memory_tip": "Mnemonic: 'Meat' has 'eat'; 'meet' has two people meeting ('ee')."
    },
    161: {
        "hint": "The cardinal number following three is spelled 'four'.",
        "memory_tip": "Homophones: 'Four' (number 4) vs 'Fore' (in front)."
    },
    162: {
        "hint": "'Fair' means just/equitable or a carnival; 'fare' is transport fee.",
        "memory_tip": "Usage: 'Fair' play / book fair vs bus 'fare'."
    },
    163: {
        "hint": "Cutting into something with teeth is spelled 'bite'.",
        "memory_tip": "Homophones: 'Bite' (chew with teeth) vs 'Byte' (unit of digital data)."
    },
    164: {
        "hint": "To receive willingly is 'accept'; excluding something is 'except'.",
        "memory_tip": "Usage: 'Accept' (agree/take in) vs 'Except' (excluding/leaving out)."
    },
    165: {
        "hint": "Blood vessels carrying blood back to the heart are 'veins'.",
        "memory_tip": "Homophones: 'Vein' (blood vessel), 'Vain' (conceited/futile), 'Vane' (weather vane)."
    },
    166: {
        "hint": "As a noun, 'present' means a gift; as a verb, it means to exhibit or introduce.",
        "memory_tip": "Word class shift: 'Present' (noun: gift/now) vs 'Present' (verb: display/introduce)."
    },
    167: {
        "hint": "Contraction of 'they are' contains an apostrophe.",
        "memory_tip": "Rule: 'They're' = they are; 'Their' = possessive; 'There' = place."
    },
    168: {
        "hint": "A maker or builder (such as a playwright or wheelwright) is spelled with 'w-r'.",
        "memory_tip": "Vocabulary: 'Wright' = builder/maker (from Old English 'wyrhta', worker)."
    },

    # Topic 8: Word Formation / Affixes (Q169 - Q192)
    169: {
        "hint": "Add the Latin suffix '-tion' to form the noun of process or result.",
        "memory_tip": "Suffix rule: Verb 'estimate' + '-ion' -> Noun 'estimation'."
    },
    170: {
        "hint": "The base noun referring to harm or damage from which 'injurious' derives.",
        "memory_tip": "Word families: 'Injury' (noun) -> 'Injurious' (adjective)."
    },
    171: {
        "hint": "The suffix that forms a noun denoting an outcome or result (e.g. findings).",
        "memory_tip": "Suffix '-ing' on 'find' creates the collective noun 'finding(s)'."
    },
    172: {
        "hint": "The standard suffix added to adjectives to convert them into adverbs of manner.",
        "memory_tip": "Adverb rule: Adjective + '-ly' forms an adverb of manner (e.g. quick -> quickly)."
    },
    173: {
        "hint": "Suffix added to scientific field names ending in '-y' to create an adjective.",
        "memory_tip": "Suffix rule: 'Botany' -> 'Botanical' (-ical suffix)."
    },
    174: {
        "hint": "Words starting with 'l' take the assimilated negative prefix 'il-'.",
        "memory_tip": "Prefix rule: 'il-' attaches before stems starting with 'l' (legal -> illegal, logical -> illogical)."
    },
    175: {
        "hint": "Words beginning with 'p' or 'm' take the negative prefix 'im-'.",
        "memory_tip": "Prefix rule: 'im-' attaches before 'p' and 'm' (polite -> impolite, possible -> impossible)."
    },
    176: {
        "hint": "The reversible prefix added to verbs to reverse an action (pack -> unpack).",
        "memory_tip": "Prefix rule: 'un-' denotes reversal of an action (pack -> unpack, tie -> untie)."
    },
    177: {
        "hint": "The prefix meaning 'again' or 'back' (e.g. write again = rewrite).",
        "memory_tip": "Prefix rule: 're-' signifies repetition or doing again (write -> rewrite)."
    },
    178: {
        "hint": "Suffix added to verbs to form abstract nouns indicating the action or state.",
        "memory_tip": "Suffix rule: Verb 'improve' + '-ment' -> Noun 'improvement'."
    },
    179: {
        "hint": "Suffix added to adjectives to form abstract nouns of condition or state.",
        "memory_tip": "Suffix rule: Adjective 'weak' + '-ness' -> Noun 'weakness'."
    },
    180: {
        "hint": "Suffix meaning 'full of' added to nouns to form adjectives.",
        "memory_tip": "Suffix rule: Noun + '-ful' = Adjective (beauty -> beautiful, care -> careful)."
    },
    181: {
        "hint": "Suffix meaning 'without' or lacking vigilance and caution.",
        "memory_tip": "Suffix rule: 'Care' + '-less' = careless (lacking care/reckless)."
    },
    182: {
        "hint": "Hyphenated compound words, closed compound words, and open compounds.",
        "memory_tip": "Compound words: Can be closed (notebook), hyphenated (son-in-law), or open (post office)."
    },
    183: {
        "hint": "The primary intermediate base before the final noun suffix '-ness' was added.",
        "memory_tip": "Morphology: 'Forget' (root) -> 'forgetful' (stem/adjective) -> 'forgetfulness' (noun)."
    },
    184: {
        "hint": "The stem left after removing the adverbial suffix '-ly'.",
        "memory_tip": "Morphology: 'Hope' (root) -> 'hopeful' (stem) + '-ly' -> 'hopefully'."
    },
    185: {
        "hint": "The irreducible root verb before adding '-able' and '-ly'.",
        "memory_tip": "Morphology: Root word = 'understand' in 'understandably'."
    },
    186: {
        "hint": "The negative prefix added to 'efficient'.",
        "memory_tip": "Prefix rule: 'in-' attaches to 'efficient' -> 'inefficient'."
    },
    187: {
        "hint": "The negative prefix attached to 'justice' to denote lack of fairness.",
        "memory_tip": "Prefix rule: 'in-' + 'justice' = 'injustice'."
    },
    188: {
        "hint": "Suffix added to adjectives ending in '-y' (y changes to i).",
        "memory_tip": "Spelling rule: 'lazy' + '-ness' -> 'laziness' (y changes to i before suffix)."
    },
    189: {
        "hint": "Suffix meaning 'capable of being' or worthy of.",
        "memory_tip": "Suffix rule: '-able' forms adjectives meaning capable of (enjoy -> enjoyable)."
    },
    190: {
        "hint": "Look for the single base word that is not combined from two separate words.",
        "memory_tip": "Compound words combine two free morphemes (sun+flower). 'School' is a single simplex word."
    },
    191: {
        "hint": "Suffix added to the verb 'act' to form the noun of deed or process.",
        "memory_tip": "Suffix rule: 'Act' + '-ion' = 'action' (noun)."
    },
    192: {
        "hint": "'Wind' and 'mill' are both naming words for things.",
        "memory_tip": "Compound structure: 'Wind' (Noun) + 'mill' (Noun) = Noun + Noun."
    },

    # Topic 9: Collocations (Q193 - Q216)
    193: {
        "hint": "Which verb naturally pairs with 'attention' when listening closely?",
        "memory_tip": "Collocation: 'Pay attention' (never make or give attention)."
    },
    194: {
        "hint": "Which verb naturally pairs with 'a decision' when reaching a conclusion?",
        "memory_tip": "Collocation: 'Make a decision' (we make decisions, not do them)."
    },
    195: {
        "hint": "Which verb is used with 'a mistake'?",
        "memory_tip": "Collocation: 'Make a mistake' (past: 'made a mistake')."
    },
    196: {
        "hint": "Which verb pairs with 'homework' or 'chores'?",
        "memory_tip": "Collocation: 'Do homework' / 'Do chores' (use 'do' for routine work)."
    },
    197: {
        "hint": "Which verb is used for presenting a public speech or lecture?",
        "memory_tip": "Collocation: 'Deliver a speech' (or give a speech)."
    },
    198: {
        "hint": "Which verb combines with 'an effort' to mean attempting hard?",
        "memory_tip": "Collocation: 'Make an effort' = try hard."
    },
    199: {
        "hint": "Which verb pairs with 'a vital/important role'?",
        "memory_tip": "Collocation: 'Play a role' in something."
    },
    200: {
        "hint": "Which verb pairs with 'a risk' or 'a chance'?",
        "memory_tip": "Collocation: 'Take a risk' = accept the possibility of danger/failure."
    },
    201: {
        "hint": "Adjective commonly paired with 'competition' to mean intense rivalry.",
        "memory_tip": "Collocation: 'Fierce competition' (or stiff/keen competition)."
    },
    202: {
        "hint": "Adjective paired with 'exercise' to mean routine physical workout.",
        "memory_tip": "Collocation: 'Regular exercise' = consistent workout routine."
    },
    203: {
        "hint": "Adjective used with 'range' or 'variety' to denote broad diversity.",
        "memory_tip": "Collocation: 'A wide range' of products/options."
    },
    204: {
        "hint": "Adjective collocated with 'influence' or 'impact' to mean powerful.",
        "memory_tip": "Collocation: 'A strong influence' / 'strong impression'."
    },
    205: {
        "hint": "Adjective paired with 'communication' to mean achieving desired results.",
        "memory_tip": "Collocation: 'Effective communication' = producing intended clarity."
    },
    206: {
        "hint": "Verb pairing with 'skills' to mean improving or cultivating them.",
        "memory_tip": "Collocation: 'Develop skills' = acquire and sharpen abilities."
    },
    207: {
        "hint": "Noun paired with 'keep one's' to mean honoring a promise.",
        "memory_tip": "Collocation: 'Keep one's word' = uphold a promise."
    },
    208: {
        "hint": "Adjective paired with 'importance' or 'respect'.",
        "memory_tip": "Collocation: 'Of great importance' = extremely significant."
    },
    209: {
        "hint": "Verb paired with 'a book' or 'the news'.",
        "memory_tip": "Collocation: 'Read a book' / 'Read the instructions'."
    },
    210: {
        "hint": "Verb naturally paired with 'a question' or 'for advice'.",
        "memory_tip": "Collocation: 'Ask a question' (never say a question)."
    },
    211: {
        "hint": "Verb paired with 'a meal' or 'lunch/dinner'.",
        "memory_tip": "Collocation: 'Have a meal' / 'Have lunch' (past: 'had a meal')."
    },
    212: {
        "hint": "Adverb paired with 'moved' or 'sorry' to express intense feeling.",
        "memory_tip": "Collocation: 'Deeply moved' / 'Deeply concerned'."
    },
    213: {
        "hint": "Adjective paired with 'habits' or 'intervals'.",
        "memory_tip": "Collocation: 'Regular intervals' / 'Regular hours'."
    },
    214: {
        "hint": "Verb paired with 'a career' or 'a goal' meaning to actively follow.",
        "memory_tip": "Collocation: 'Pursue a career' = follow a professional path."
    },
    215: {
        "hint": "Adjective paired with 'pleasure' to mean immense satisfaction.",
        "memory_tip": "Collocation: 'Great pleasure' = utmost joy or delight."
    },
    216: {
        "hint": "Verb paired with 'a promise' or 'arrangements'.",
        "memory_tip": "Collocation: 'Make a promise' / 'Make arrangements'."
    },

    # Topic 10: Parts of Speech (Q217 - Q240)
    217: {
        "hint": "'She' is a word used in place of a female person's name.",
        "memory_tip": "Part of speech: Pronoun replaces a noun (I, you, he, she, it, we, they)."
    },
    218: {
        "hint": "'Wiped' is an action word denoting cleaning by rubbing.",
        "memory_tip": "Part of speech: Verb expresses action, state, or occurrence."
    },
    219: {
        "hint": "'And' joins words, phrases, or clauses together.",
        "memory_tip": "Part of speech: Conjunction joins words or clauses (FANBOYS: For, And, Nor, But, Or, Yet, So)."
    },
    220: {
        "hint": "'In' shows spatial or temporal position before a noun.",
        "memory_tip": "Part of speech: Preposition shows relationship in time, space, or direction."
    },
    221: {
        "hint": "'Controlled' describes the action of directing or regulating.",
        "memory_tip": "Part of speech: Verb describes what the subject did."
    },
    222: {
        "hint": "'Kabaddi' is the specific name of a sport.",
        "memory_tip": "Part of speech: Proper Noun names a specific person, place, or game."
    },
    223: {
        "hint": "'He' stands in place of a male noun.",
        "memory_tip": "Part of speech: Personal Pronoun substitutes for a third-person singular male noun."
    },
    224: {
        "hint": "'Into' shows motion toward the inside of something.",
        "memory_tip": "Part of speech: Preposition indicating movement or direction inward."
    },
    225: {
        "hint": "'Small' describes the size or dimension of a noun.",
        "memory_tip": "Part of speech: Adjective modifies or qualifies a noun."
    },
    226: {
        "hint": "'Regularly' describes how often the action occurs (frequency).",
        "memory_tip": "Part of speech: Adverb of frequency modifies a verb, adjective, or another adverb."
    },
    227: {
        "hint": "'Saw' is the past form of the action see.",
        "memory_tip": "Part of speech: Verb (irregular past tense of see)."
    },
    228: {
        "hint": "'Brown' describes the color attribute of an object.",
        "memory_tip": "Part of speech: Color words modifying nouns are Adjectives."
    },
    229: {
        "hint": "'Oh' is an exclamation expressing surprise, realization, or emotion.",
        "memory_tip": "Part of speech: Interjection conveys sudden emotion or exclamation."
    },
    230: {
        "hint": "'Tailor' is a naming word for an occupation/person.",
        "memory_tip": "Part of speech: Common Noun names a person or trade."
    },
    231: {
        "hint": "'Under' indicates lower vertical position beneath something.",
        "memory_tip": "Part of speech: Preposition indicating location beneath."
    },
    232: {
        "hint": "'On' indicates contact with a surface.",
        "memory_tip": "Part of speech: Preposition indicating position atop a surface."
    },
    233: {
        "hint": "'Meat' is a naming word for a physical substance or food.",
        "memory_tip": "Part of speech: Material/Mass Noun naming a substance."
    },
    234: {
        "hint": "'We' refers to the speaker and one or more others.",
        "memory_tip": "Part of speech: First-person plural Personal Pronoun."
    },
    235: {
        "hint": "'Father' is a naming word; 'and' connects two elements.",
        "memory_tip": "'Father' = Noun (person); 'And' = Coordinating Conjunction."
    },
    236: {
        "hint": "One is an action word; the other describes how the action was done.",
        "memory_tip": "Action word = Verb; '-ly' word describing the action = Adverb of manner."
    },
    237: {
        "hint": "'Sachin' is an individual person's name; 'on' expresses location.",
        "memory_tip": "'Sachin' = Proper Noun; 'On' = Preposition."
    },
    238: {
        "hint": "'Want' expresses a desire (action/state); 'palace' is a grandiose building.",
        "memory_tip": "'Want' = Verb; 'Palace' = Noun (place/building)."
    },
    239: {
        "hint": "'And' joins sentences or phrases; 'at' pinpoints location or time.",
        "memory_tip": "'And' = Conjunction; 'At' = Preposition."
    },
    240: {
        "hint": "'Spent' is the past action of spend; 'gardening' here functions as an activity/noun.",
        "memory_tip": "'Spent' = Verb; 'Gardening' = Gerund functioning as a Noun."
    }
}
