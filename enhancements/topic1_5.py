# enhancements/topic1_5.py
# Q1 to Q120: Synonyms, Antonyms, Spellings, One-word substitutes, Idiomatic expressions

TIPS = {
    # Topic 1: Synonyms (Q1 - Q24)
    1: {
        "hint": "Think of a sound that causes intense fright, horror, or distress.",
        "memory_tip": "Root: Latin 'terrere' (to frighten) -> terrible, terror, terrify. Synonym: dreadful."
    },
    2: {
        "hint": "Describes food or drink that is extremely pleasing to the taste buds.",
        "memory_tip": "Delicious = highly pleasant to taste. Root 'delicacy' (fine food) -> tasty, appetizing."
    },
    3: {
        "hint": "A person who teaches, coaches, or trains someone in a specific practical skill.",
        "memory_tip": "Instructor = one who instructs/trains. Root: Latin 'instructus' (equipped/taught) -> trainer."
    },
    4: {
        "hint": "The inability or refusal to accept something as true; feeling skeptical.",
        "memory_tip": "Prefix 'dis-' (not) + 'belief' (faith) = lack of conviction or doubt."
    },
    5: {
        "hint": "A state of great suffering, distress, or difficult discomfort.",
        "memory_tip": "Misery = deep unhappiness or hardship. Root: Latin 'miser' (wretched) -> difficulty, sorrow."
    },
    6: {
        "hint": "Happening not often; on very rare occasions.",
        "memory_tip": "Seldom = rarely, scarcely ever. Mnemonic: 'Seldom seen = rarely green'."
    },
    7: {
        "hint": "The state of being destroyed, severely harmed, or wrecked.",
        "memory_tip": "Ruin = total destruction or severe damage. Think of ancient ruins (damaged structures)."
    },
    8: {
        "hint": "A sustained combat, clash, or violent struggle between opposing forces.",
        "memory_tip": "Battle = combat/fight. From Old French 'bataille' (clash/fight)."
    },
    9: {
        "hint": "Strikingly unusual, bizarre, uncanny, or unnatural.",
        "memory_tip": "Weird = uncanny, strange. Originally related to fate or destiny, now means unusual."
    },
    10: {
        "hint": "People who offer goods, commodities, or services for sale.",
        "memory_tip": "Vendor = seller. Root: Latin 'vendere' (to sell) -> vending machine, vendor."
    },
    11: {
        "hint": "Lacking confidence, certainty, or conviction in oneself.",
        "memory_tip": "Prefix 'un-' (not) + 'sure' (confident) = unconfident, hesitant."
    },
    12: {
        "hint": "An act, statement, or gift showing deep gratitude, honor, or respect.",
        "memory_tip": "Tribute = homage, honor, salute. Root: Latin 'tributum' (contribution/homage paid)."
    },
    13: {
        "hint": "A feeling of joyful satisfaction, enjoyment, or cheer.",
        "memory_tip": "Pleasure = delight, enjoyment. Root: Latin 'placere' (to please)."
    },
    14: {
        "hint": "Savage, unfeeling, or characteristic of an animal or beast.",
        "memory_tip": "Brute = beast, animal-like, lacking reason. 'Brute force' = savage/raw physical force."
    },
    15: {
        "hint": "A very brief, fleeting period of time.",
        "memory_tip": "Moment = a brief instant or short time. Root: Latin 'momentum' (movement/instant)."
    },
    16: {
        "hint": "To keep, value, protect, and hold dear over a long period.",
        "memory_tip": "Treasure (verb) = cherish, preserve, protect as precious."
    },
    17: {
        "hint": "Deeply affected by intense physical or emotional distress and shock.",
        "memory_tip": "Traumatised = greatly shocked. Greek 'trauma' = wound, damage."
    },
    18: {
        "hint": "Exceptionally large in scale, volume, intensity, or extent.",
        "memory_tip": "Massive = very big, heavy, bulky. Root: 'mass' + suffix '-ive'."
    },
    19: {
        "hint": "A place or condition providing safety, shelter, and security from danger.",
        "memory_tip": "Refuge = shelter, protection. Root: Latin 'refugium' (fleeing back for safety)."
    },
    20: {
        "hint": "Existing or acting entirely by oneself without companions.",
        "memory_tip": "Alone = all one; solo, unaccompanied. Root: Latin 'solus' (alone -> solo)."
    },
    21: {
        "hint": "Possessing outstanding quality, skill, or superior merit.",
        "memory_tip": "Excellent = extremely good, outstanding. Root: Latin 'excellere' (to surpass)."
    },
    22: {
        "hint": "The natural physical desire or craving for food.",
        "memory_tip": "Appetite = hunger or desire for food. Root: Latin 'appetere' (to crave/strive after)."
    },
    23: {
        "hint": "Physical or emotional injury, distress, or disadvantage.",
        "memory_tip": "Harm = damage, injury, hurt, pain."
    },
    24: {
        "hint": "Complete, total, full, with no part omitted.",
        "memory_tip": "Entire = whole, complete. Root: Latin 'integer' (untouched, complete)."
    },

    # Topic 2: Antonyms (Q25 - Q48)
    25: {
        "hint": "If an action happens 'usually' (customarily), its opposite is rarely or as an exception.",
        "memory_tip": "Antonym: Usually (customarily/regularly) <-> Exceptionally (rarely/unusually)."
    },
    26: {
        "hint": "Yelling means shouting loudly; think of speaking very softly using only breath.",
        "memory_tip": "Antonym: Yell (shout loudly) <-> Whisper (speak in a low voice)."
    },
    27: {
        "hint": "Muttering means complaining quietly under one's breath; the opposite is speaking out openly.",
        "memory_tip": "Antonym: Mutter (mumble in secret) <-> Speak out (express openly)."
    },
    28: {
        "hint": "Enormous means gigantic or massive; the opposite is miniature or minuscule.",
        "memory_tip": "Antonym: Enormous (colossal, huge) <-> Tiny (very small)."
    },
    29: {
        "hint": "Add the negative prefix that means not considerate or benevolent.",
        "memory_tip": "Prefix rule: 'kind' + negative prefix 'un-' forms 'unkind'."
    },
    30: {
        "hint": "To lead means going in front; the opposite action is going behind someone.",
        "memory_tip": "Antonym: Lead (guide in front) <-> Follow (come after behind)."
    },
    31: {
        "hint": "In reference to age, an elderly person is the opposite of someone in the early stage of life.",
        "memory_tip": "Antonym: Old (aged) <-> Young (youthful)."
    },
    32: {
        "hint": "A wise person exercises good judgment; the opposite lacks reason and discretion.",
        "memory_tip": "Antonym: Wise (judicious/prudent) <-> Foolish (lacking wisdom)."
    },
    33: {
        "hint": "To recall a memory is to remember; failing to recall is...",
        "memory_tip": "Antonym: Remember (recall to mind) <-> Forget (lose memory of)."
    },
    34: {
        "hint": "Experiencing joy and gladness vs. feeling sorrow or gloom.",
        "memory_tip": "Antonym: Happy (joyful) <-> Sad (sorrowful, depressed)."
    },
    35: {
        "hint": "To dispatch or cause to go away vs. to take in or acquire.",
        "memory_tip": "Antonym: Send (dispatch away) <-> Receive (accept/take in)."
    },
    36: {
        "hint": "Having small thickness or width vs. having heavy girth or width.",
        "memory_tip": "Antonym: Thin (slender, lean) <-> Thick (dense, wide)."
    },
    37: {
        "hint": "Snug means warm, comfortable, and cozy; the opposite is exposed, bare, and cold.",
        "memory_tip": "Antonym: Snug (cozy/sheltered) <-> Bleak (cold, bare, unwelcoming)."
    },
    38: {
        "hint": "Covetous means greedy and constantly desiring more; the opposite is being content with what one has.",
        "memory_tip": "Antonym: Covetous (avaricious/greedy) <-> Satisfied (contented)."
    },
    39: {
        "hint": "A stingy person hates spending money or sharing; the opposite gives freely.",
        "memory_tip": "Antonym: Stingy (miserly) <-> Generous (benevolent/giving freely)."
    },
    40: {
        "hint": "Valiant describes great courage and bravery; the opposite lacks courage in the face of danger.",
        "memory_tip": "Antonym: Valiant (brave/heroic) <-> Cowardly (timid/faint-hearted)."
    },
    41: {
        "hint": "Brave means ready to face danger; the opposite runs away from fear.",
        "memory_tip": "Antonym: Brave (courageous) <-> Cowardly (fearful, pusillanimous)."
    },
    42: {
        "hint": "Happening instantly in a moment vs. taking place step by step over time.",
        "memory_tip": "Antonym: Suddenly (abruptly) <-> Gradually (step by step, slowly)."
    },
    43: {
        "hint": "Costing a large amount of money vs. low in price.",
        "memory_tip": "Antonym: Expensive (costly/dear) <-> Cheap (inexpensive/low cost)."
    },
    44: {
        "hint": "Great in size, dimensions, or capacity vs. of limited dimensions.",
        "memory_tip": "Antonym: Large (immense/huge) <-> Small (little/compact)."
    },
    45: {
        "hint": "To take, agree to, or receive favorably vs. to turn down or decline.",
        "memory_tip": "Antonym: Accept (embrace/agree) <-> Reject (refuse/turn down)."
    },
    46: {
        "hint": "Misery is a state of deep anguish; the opposite is peace of mind and peaceful satisfaction.",
        "memory_tip": "Antonym: Misery (wretchedness/sorrow) <-> Contentment (peaceful happiness)."
    },
    47: {
        "hint": "Belonging to an individual privately vs. concerning the community or society as a whole.",
        "memory_tip": "Antonym: Personal (private/individual) <-> Public (civic/communal)."
    },
    48: {
        "hint": "Concerned with real-world application vs. confined to abstract concepts and speculation.",
        "memory_tip": "Antonym: Practical (hands-on/applied) <-> Theoretical (abstract/conceptual)."
    },

    # Topic 3: Spellings (Q49 - Q72)
    49: {
        "hint": "Spelled with a single 's' and ends with '-ery'.",
        "memory_tip": "Spelling: M-I-S-E-R-Y (from Latin 'miseria'). Do not double the 's'."
    },
    50: {
        "hint": "Notice British English spelling with '-our-'.",
        "memory_tip": "Spelling: F-A-V-O-U-R-I-T-E. Base word 'favour' + suffix '-ite'."
    },
    51: {
        "hint": "Ends in '-ible', not '-able', with double 's'.",
        "memory_tip": "Spelling: R-E-S-P-O-N-S-I-B-L-E. Mnemonic: 'Response' + '-ible'."
    },
    52: {
        "hint": "Contains 'ci' making the 'sh' sound, ending in '-ous'.",
        "memory_tip": "Spelling: D-E-L-I-C-I-O-U-S. Think of 'delic-i-ous'."
    },
    53: {
        "hint": "Begins with 'kitch-' containing a silent 't'.",
        "memory_tip": "Spelling: K-I-T-C-H-E-N. Notice the 't' before 'ch'."
    },
    54: {
        "hint": "A steep high rock face; spelled with a double 'f'.",
        "memory_tip": "Spelling rule: Short vowel followed by 'f' at the end doubles the 'f' -> C-L-I-F-F."
    },
    55: {
        "hint": "Contains 'ie' making the long 'ee' sound followed by 'k'.",
        "memory_tip": "Spelling rule: 'i before e except after c' -> S-H-R-I-E-K-E-D."
    },
    56: {
        "hint": "Contains double 't' and single 'd'.",
        "memory_tip": "Spelling: A-T-T-I-T-U-D-E. Double 't' after initial 'a'."
    },
    57: {
        "hint": "An advisory or legislative body ends with '-cil', not '-sel'.",
        "memory_tip": "Spelling: C-O-U-N-C-I-L (assembly) vs C-O-U-N-S-E-L (advice/lawyer)."
    },
    58: {
        "hint": "Contains 'qu', double 'r', and single 'l'.",
        "memory_tip": "Spelling: S-Q-U-I-R-R-E-L. Double 'r' with '-el' ending."
    },
    59: {
        "hint": "Derived from beg; ends in '-ar', not '-er'.",
        "memory_tip": "Spelling: B-E-G-G-A-R. Double 'g' and ends in '-ar' like 'liar' and 'scholar'."
    },
    60: {
        "hint": "An open, roofed porch; often spelled with '-ah' at the end.",
        "memory_tip": "Spelling: V-E-R-A-N-D-A-H (or veranda). Starts with 've-' and ends in '-dah'."
    },
    61: {
        "hint": "Base word 'comic' + suffix '-al'.",
        "memory_tip": "Spelling: C-O-M-I-C-A-L. No 'k' needed; single 'm'."
    },
    62: {
        "hint": "Means ungenerous or miserly; ends in '-gy'.",
        "memory_tip": "Spelling: S-T-I-N-G-Y. 'Sting' + '-y'."
    },
    63: {
        "hint": "Ends in '-itive' with single 's'.",
        "memory_tip": "Spelling: S-E-N-S-I-T-I-V-E. Root: 'sense' + '-itive'."
    },
    64: {
        "hint": "Starts with 'qua-' and ends in '-ity'.",
        "memory_tip": "Spelling: Q-U-A-L-I-T-Y. 'Q' is always followed by 'u'."
    },
    65: {
        "hint": "First light of day; spelled with 'aw'.",
        "memory_tip": "Spelling: D-A-W-N. Rhymes with lawn, fawn."
    },
    66: {
        "hint": "Past tense of insist; double 's' in the middle.",
        "memory_tip": "Spelling: I-N-S-I-S-T-E-D. Root: 'insist' + '-ed'."
    },
    67: {
        "hint": "The popular microblogging platform name; contains double 't'.",
        "memory_tip": "Spelling: T-W-I-T-T-E-R. Double 't' after short vowel 'i'."
    },
    68: {
        "hint": "Act of copying or mimicking; contains single 'm' and single 't'.",
        "memory_tip": "Spelling: I-M-I-T-A-T-I-O-N. Root: Latin 'imitari' (to copy)."
    },
    69: {
        "hint": "A sudden catastrophe or calamity; spelled with '-aster'.",
        "memory_tip": "Spelling: D-I-S-A-S-T-E-R. Root: Latin 'dis-' (bad) + 'astron' (star) -> ill-starred event."
    },
    70: {
        "hint": "One who works in a garden; ends with '-er'.",
        "memory_tip": "Spelling: G-A-R-D-E-N-E-R. 'Garden' + agent suffix '-er'."
    },
    71: {
        "hint": "Strong emotion or enthusiasm; spelled with double 's'.",
        "memory_tip": "Spelling: P-A-S-S-I-O-N. Double 's' makes the 'sh' sound."
    },
    72: {
        "hint": "A holiday or period of leisure; ends in '-tion'.",
        "memory_tip": "Spelling: V-A-C-A-T-I-O-N. Root: Latin 'vacare' (to be empty/free)."
    },

    # Topic 4: One-Word Substitutes (Q73 - Q96)
    73: {
        "hint": "A professional trained to plan, design, and oversee the construction of buildings.",
        "memory_tip": "Root: Greek 'arkhi-' (chief) + 'tekton' (builder) = Architect."
    },
    74: {
        "hint": "Someone skilled in decorative, ornamental, and artistic handwriting.",
        "memory_tip": "Root: Greek 'kallos' (beauty) + 'graphein' (to write) = Calligrapher."
    },
    75: {
        "hint": "A tradesperson whose occupation is mending, crafting, and repairing footwear.",
        "memory_tip": "Vocabulary: Cobbler = shoemaker/repairer. 'Cobble' originally meant to mend clumsily."
    },
    76: {
        "hint": "A person who cultivates flowers, plants, and grounds.",
        "memory_tip": "Agent noun: Garden + '-er' = Gardener."
    },
    77: {
        "hint": "An investigator whose job is to discover clues and solve crimes.",
        "memory_tip": "Root: Latin 'detectus' (uncovered) -> Detective (one who uncovers clues)."
    },
    78: {
        "hint": "A medical practitioner who specializes in the care and diseases of infants and children.",
        "memory_tip": "Root: Greek 'pais/paid-' (child) + 'iatros' (physician) = Pediatrician."
    },
    79: {
        "hint": "A scientist who studies the solid Earth, rocks, and the processes by which they change.",
        "memory_tip": "Root: Greek 'geo-' (earth) + '-logist' (one who studies) = Geologist."
    },
    80: {
        "hint": "A scientist who studies celestial objects, space, planets, and stars.",
        "memory_tip": "Root: Greek 'astron' (star) + 'nomos' (law/arranging) = Astronomer."
    },
    81: {
        "hint": "A person employed at railway stations, hotels, or airports to carry travelers' bags.",
        "memory_tip": "Root: Latin 'portare' (to carry) -> Porter (one who carries loads)."
    },
    82: {
        "hint": "An author who writes an account of someone else's life.",
        "memory_tip": "Root: Greek 'bios' (life) + 'grapher' (writer) = Biographer."
    },
    83: {
        "hint": "A written account of a person's life composed by that person themself.",
        "memory_tip": "Root: 'auto-' (self) + 'bio' (life) + 'graphy' (writing) = Autobiography."
    },
    84: {
        "hint": "A reckless person who wastes money and spends extravagantly.",
        "memory_tip": "Compound: 'Spend' + 'thrift' (thrifty/savings) = Spendthrift (one who spends all savings)."
    },
    85: {
        "hint": "Someone who believes that all events are predetermined by destiny and inevitable.",
        "memory_tip": "Root: 'fate' + '-ist' = Fatalist (one who surrenders to fate)."
    },
    86: {
        "hint": "A person who has reached or passed the age of one hundred years.",
        "memory_tip": "Root: Latin 'centum' (hundred) + 'annus' (year) = Centenarian."
    },
    87: {
        "hint": "Existing or present in all places at the same time.",
        "memory_tip": "Root: Latin 'omni-' (all) + 'present' = Omnipresent. (Omniscient = all-knowing)."
    },
    88: {
        "hint": "A soldier or person motivated purely by monetary gain and financial reward.",
        "memory_tip": "Root: Latin 'merces' (wages/reward) -> Mercenary (working only for money)."
    },
    89: {
        "hint": "A person who harbors hatred, dislike, or deep prejudice against women.",
        "memory_tip": "Root: Greek 'misein' (to hate) + 'gyne' (woman) = Misogynist."
    },
    90: {
        "hint": "The state or custom of having only one spouse at a given time.",
        "memory_tip": "Root: Greek 'monos' (single) + 'gamos' (marriage) = Monogamy. (Polygamy = many)."
    },
    91: {
        "hint": "A person who is fluent in or able to use several different languages.",
        "memory_tip": "Root: Greek 'poly-' (many) + 'glotta' (tongue/language) = Polyglot."
    },
    92: {
        "hint": "The scientific study of the interactions between living organisms and their environment.",
        "memory_tip": "Root: Greek 'oikos' (house/dwelling) + '-logy' (study) = Ecology."
    },
    93: {
        "hint": "A statement open to more than one interpretation; unclear or having double meaning.",
        "memory_tip": "Root: Latin 'ambi-' (both sides) + 'agere' (to drive) = Ambiguous (wavering meaning)."
    },
    94: {
        "hint": "A generous benefactor who donates time and wealth to promote human welfare.",
        "memory_tip": "Root: Greek 'philos' (loving) + 'anthropos' (humankind) = Philanthropist."
    },
    95: {
        "hint": "A forerunner or innovator who explores new territory or fields of knowledge first.",
        "memory_tip": "Vocabulary: Pioneer = first explorer/innovator who paves the way for others."
    },
    96: {
        "hint": "An advocate committed to protecting ecosystems and preventing pollution.",
        "memory_tip": "Root: 'Environment' + '-al' + '-ist' = Environmentalist."
    },

    # Topic 5: Idioms (Q97 - Q120)
    97: {
        "hint": "To face a grim, unavoidable situation with courage and fortitude.",
        "memory_tip": "Idiom: 'Bite the bullet' = endure a painful or difficult ordeal bravely."
    },
    98: {
        "hint": "Describes a person who is trustworthy and unfailingly keeps their promises.",
        "memory_tip": "Idiom: 'A man of his word' = someone who honors their commitments and promises."
    },
    99: {
        "hint": "A sharp, shrewd, and discerning person who is not easily tricked or deceived.",
        "memory_tip": "Idiom: 'Nobody's fool' = clever, astute, not easily fooled by deception."
    },
    100: {
        "hint": "Making rapid, remarkable, and dramatic progress in a short time.",
        "memory_tip": "Idiom: 'In leaps and bounds' = progressing very swiftly and dramatically."
    },
    101: {
        "hint": "Characterized by high speed, intense energy, wild excitement, and velocity.",
        "memory_tip": "Idiom: 'Fast and furious' = rapid, heated, and full of lively intensity."
    },
    102: {
        "hint": "To express one's thoughts, feelings, and beliefs directly and candidly.",
        "memory_tip": "Idiom: 'Speak your mind' = communicate honest thoughts without hesitation."
    },
    103: {
        "hint": "Achieving an objective by whatever means necessary, whether fair or foul.",
        "memory_tip": "Idiom: 'By hook or by crook' = by any available method, fair or unfair."
    },
    104: {
        "hint": "A treacherous, deceitful enemy pretending to be a trustworthy friend.",
        "memory_tip": "Idiom: 'A snake in the grass' = a hidden danger or treacherous person pretending loyalty."
    },
    105: {
        "hint": "To battle or struggle with all one's might, energy, and determination.",
        "memory_tip": "Idiom: 'Fight tooth and nail' = fight with fierce, relentless determination."
    },
    106: {
        "hint": "Miscellaneous remnants, assorted small items, or leftover pieces.",
        "memory_tip": "Idiom: 'Odds and ends' = various small miscellaneous bits and pieces."
    },
    107: {
        "hint": "To reveal an undisclosed secret unintentionally or prematurely.",
        "memory_tip": "Idiom: 'Let the cat out of the bag' = divulge a secret, often accidentally."
    },
    108: {
        "hint": "Very early in the morning, right as daylight begins to break.",
        "memory_tip": "Idiom: 'At the crack of dawn' = at the very first glimpse of morning light."
    },
    109: {
        "hint": "To state something clearly and frankly without hesitation, disguise, or embarrassment.",
        "memory_tip": "Idiom: 'Make no bones about' = acknowledge or express something completely directly."
    },
    110: {
        "hint": "The very beginning and the ultimate culmination; the essence of everything.",
        "memory_tip": "Idiom: 'The alpha and omega' = the start and the finish (first and last Greek letters)."
    },
    111: {
        "hint": "Taking excessive risks when already in an advantageous position.",
        "memory_tip": "Idiom: 'Push your luck' = risk losing success by taking unnecessary further chances."
    },
    112: {
        "hint": "A huge fuss, commotion, or excitement over a minor and trivial matter.",
        "memory_tip": "Idiom: 'A storm in a teacup' = great excitement or worry over something insignificant."
    },
    113: {
        "hint": "A very tiny, almost negligible contribution relative to what is needed.",
        "memory_tip": "Idiom: 'A drop in the ocean' = an insignificant amount compared with the huge total."
    },
    114: {
        "hint": "A controversial topic or dispute that is difficult, risky, or awkward to handle.",
        "memory_tip": "Idiom: 'A hot potato' = an issue so controversial that everyone wants to pass it on."
    },
    115: {
        "hint": "An ineffective or helpless individual or enterprise requiring constant assistance.",
        "memory_tip": "Idiom: 'A lame duck' = an ineffectual person, failed project, or official in final term."
    },
    116: {
        "hint": "An outcome that achieves immense, thunderous, and undisputed popularity and success.",
        "memory_tip": "Idiom: 'A roaring success' = a massive, booming, undisputed achievement."
    },
    117: {
        "hint": "A costly possession whose upkeep outweighs its practical usefulness.",
        "memory_tip": "Idiom: 'A white elephant' = an expensive, burdensome possession that is useless."
    },
    118: {
        "hint": "Living together within the same dwelling or shared household.",
        "memory_tip": "Idiom: 'Under one/a roof' = sharing the same house or domestic residence."
    },
    119: {
        "hint": "Having knowledge readily accessible and thoroughly mastered for immediate recall.",
        "memory_tip": "Idiom: 'At your fingertips' = readily available for immediate use or recall."
    },
    120: {
        "hint": "A general, comprehensive panoramic overview of something seen from above.",
        "memory_tip": "Idiom: 'A bird's eye view' = an overall panoramic view from a high vantage point."
    }
}
