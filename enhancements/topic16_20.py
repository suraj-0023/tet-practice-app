# enhancements/topic16_20.py
# Q361 to Q480: Linkers, Language Functions, Concord / Agreement, Auxiliary Verbs, Order of Adjectives

TIPS = {
    # Topic 16: Linkers / Conjunctions (Q361 - Q384)
    361: {
        "hint": "Used as an adverb to mean 'in place of the person or thing mentioned'.",
        "memory_tip": "Linker: 'Instead' denotes an alternative chosen in place of something else."
    },
    362: {
        "hint": "Introduces a logical consequence or deduction from what was stated.",
        "memory_tip": "Linker: 'Therefore' = for that reason / consequently (cause -> effect)."
    },
    363: {
        "hint": "Signals the outcome or effect produced by heavy rain.",
        "memory_tip": "Linker: 'As a result' introduces the direct consequence of an event."
    },
    364: {
        "hint": "Used to introduce a new, incidental topic or question into a conversation.",
        "memory_tip": "Discourse marker: 'By the way' transitions to a new or incidental point."
    },
    365: {
        "hint": "Used when introducing a specific person or thing as an illustrative example.",
        "memory_tip": "Linker: 'For instance' = for example (illustrating a general statement)."
    },
    366: {
        "hint": "Used to dismiss previous points and move on to what is most essential.",
        "memory_tip": "Discourse marker: 'Anyway' = in any case / regardless of other factors."
    },
    367: {
        "hint": "Used at the end of a clause to mean 'in addition' or 'also'.",
        "memory_tip": "Linker: 'As well' comes at the end of a clause to mean also/too."
    },
    368: {
        "hint": "Used to emphasize that the exact opposite of what was suggested is true.",
        "memory_tip": "Linker: 'On the contrary' introduces the opposite reality to dispel a false assumption."
    },
    369: {
        "hint": "Placed before the main verb to mean in addition.",
        "memory_tip": "Adverb linker: 'Also' precedes the main verb (has also been)."
    },
    370: {
        "hint": "Used to introduce an extra, reinforcing piece of information.",
        "memory_tip": "Linker: 'In addition to that' adds extra supporting information."
    },
    371: {
        "hint": "Means 'moreover' or 'in addition to'; provides an extra justification.",
        "memory_tip": "Linker: 'Besides' = moreover / furthermore / in addition to that."
    },
    372: {
        "hint": "Contrasts a negative claim with its direct positive opposite.",
        "memory_tip": "Linker: 'Not X; on the contrary, Y' asserts the complete opposite truth."
    },
    373: {
        "hint": "Sequential linkers used to list points in a numbered order.",
        "memory_tip": "Sequence linkers: 'Firstly' begins the list; 'Then' introduces subsequent points."
    },
    374: {
        "hint": "Introduces a contrasting statement or concession.",
        "memory_tip": "Linker: 'However' introduces a contrast with a previous clause."
    },
    375: {
        "hint": "Dismisses unimportant details to conclude a practical stance.",
        "memory_tip": "Discourse marker: 'Anyway' sums up an argument dismissively."
    },
    376: {
        "hint": "Signals a direct result or outcome of a preceding circumstance.",
        "memory_tip": "Linker: 'Consequently' = as a result / hence."
    },
    377: {
        "hint": "Presents an opposite point of view or balancing perspective.",
        "memory_tip": "Linker: 'On the other hand' introduces an alternative or contrasting perspective."
    },
    378: {
        "hint": "Means 'except if' or 'if not' in a conditional clause.",
        "memory_tip": "Conditional conjunction: 'Unless' = If ... not (Unless you apologize = If you do not apologize)."
    },
    379: {
        "hint": "Introduces a concessive clause contrasting two surprising facts.",
        "memory_tip": "Concession conjunction: 'Although' connects contrasting unexpected truths."
    },
    380: {
        "hint": "Connects two independent sentences with a contrast in outcome.",
        "memory_tip": "Adversative linker: 'However' signals contrast across sentences."
    },
    381: {
        "hint": "Denies the preceding popular assumption by asserting the reverse.",
        "memory_tip": "Linker: 'On the contrary' asserts the direct reverse."
    },
    382: {
        "hint": "Preposition expressing the reason or charge for an arrest.",
        "memory_tip": "Preposition: 'Arrested for' + crime/offense."
    },
    383: {
        "hint": "Subordinating conjunction of reason meaning 'because' or 'since'.",
        "memory_tip": "Conjunction of cause: 'As' = because / since."
    },
    384: {
        "hint": "Prepositional phrase meaning 'because of' or 'due to'.",
        "memory_tip": "Preposition of cause: 'Owing to' = because of (followed by noun phrase)."
    },

    # Topic 17: Language Functions (Q385 - Q408)
    385: {
        "hint": "'Can' expresses physical or learned capability.",
        "memory_tip": "Language function: 'Can' + V1 for general capability = Expressing Ability."
    },
    386: {
        "hint": "'Could you... please?' is a courteous way of asking someone to do something.",
        "memory_tip": "Language function: 'Could you... please?' = Polite Request."
    },
    387: {
        "hint": "'May' indicates a chance that an event will occur.",
        "memory_tip": "Language function: 'May / Might' + V1 = Expressing Possibility."
    },
    388: {
        "hint": "Expresses a future likelihood or chance of a career choice.",
        "memory_tip": "Language function: 'May become' = Expressing Possibility."
    },
    389: {
        "hint": "Expresses the likelihood of a late arrival.",
        "memory_tip": "Language function: 'May arrive' = Expressing Possibility."
    },
    390: {
        "hint": "States physical stamina and capacity to dance for hours.",
        "memory_tip": "Language function: 'Can' expressing capacity = Ability."
    },
    391: {
        "hint": "'May I...?' is a polite and formal way of asking to borrow or do something.",
        "memory_tip": "Language function: 'May I...?' = Seeking/Asking for Permission."
    },
    392: {
        "hint": "Traditional classroom query asking for authorization to enter.",
        "memory_tip": "Language function: 'May I come in?' = Seeking Permission."
    },
    393: {
        "hint": "Expresses artistic talent and capability using 'can'.",
        "memory_tip": "Language function: 'Can' = Ability."
    },
    394: {
        "hint": "'Would you like...?' politely invites or offers someone food or drink.",
        "memory_tip": "Language function: 'Would you like...?' = Making an Offer."
    },
    395: {
        "hint": "'Should' conveys a recommendation or moral obligation.",
        "memory_tip": "Language function: 'Should' + V1 = Giving Advice / Recommendation."
    },
    396: {
        "hint": "'Could you lend me...?' is a polite plea asking for assistance.",
        "memory_tip": "Language function: 'Could you...?' = Polite Request."
    },
    397: {
        "hint": "Inviting someone to partake of tea.",
        "memory_tip": "Language function: 'Would you like to have...?' = Making an Offer."
    },
    398: {
        "hint": "'Will you join us...?' invites someone to take part.",
        "memory_tip": "Language function: 'Will you join...?' = Making an Offer / Invitation."
    },
    399: {
        "hint": "'You may leave' grants authorization to depart.",
        "memory_tip": "Language function: 'You may' spoken by authority = Giving Permission."
    },
    400: {
        "hint": "'Should' is used to suggest a beneficial habit.",
        "memory_tip": "Language function: 'You should' = Giving Advice."
    },
    401: {
        "hint": "'Must' indicates strong obligation or non-negotiable duty.",
        "memory_tip": "Language function: 'Must' = Compulsion / Strong Obligation."
    },
    402: {
        "hint": "'Can drive' describes practical skill and qualification.",
        "memory_tip": "Language function: 'Can' = Ability."
    },
    403: {
        "hint": "'Could you... please?' requests an action politely.",
        "memory_tip": "Language function: 'Could you... please?' = Polite Request."
    },
    404: {
        "hint": "'May become' points to a future contingency or possibility.",
        "memory_tip": "Language function: 'May' = Possibility."
    },
    405: {
        "hint": "'May be delayed' communicates potential weather impact.",
        "memory_tip": "Language function: 'May be' = Possibility."
    },
    406: {
        "hint": "'Should not' warns against an unwise course of action.",
        "memory_tip": "Language function: 'Should not' = Advice / Admonition."
    },
    407: {
        "hint": "'Would you like to have...?' offers refreshment or rest.",
        "memory_tip": "Language function: 'Would you like...?' = Making an Offer."
    },
    408: {
        "hint": "'May get' indicates a hopeful possibility.",
        "memory_tip": "Language function: 'May' = Possibility."
    },

    # Topic 18: Subject-Verb Concord (Q409 - Q432)
    409: {
        "hint": "Two singular pronouns joined by 'and' require a plural verb.",
        "memory_tip": "Concord rule: Singular + and + Singular takes a plural verb (He and I were playing)."
    },
    410: {
        "hint": "Two distinct entities joined by 'and' take a plural verb (do, not does).",
        "memory_tip": "Concord rule: Two subjects joined by 'and' take plural verb (Fire and water do not agree)."
    },
    411: {
        "hint": "Gold and silver are two separate precious metals -> plural verb 'are'.",
        "memory_tip": "Concord rule: Plural subject requires plural verb 'are'."
    },
    412: {
        "hint": "Subjects ending in '-ics' (Mathematics, Physics) denoting a single field of study take a singular verb.",
        "memory_tip": "Concord rule: Names of academic subjects ending in '-ics' take singular verb 'is'."
    },
    413: {
        "hint": "Two nouns expressing a single compound unit or idea take a singular verb.",
        "memory_tip": "Concord rule: Unit pairs (horse and carriage, bread and butter) take singular verb 'is'."
    },
    414: {
        "hint": "When two singular subjects are connected by 'neither... nor', the verb is singular.",
        "memory_tip": "Concord rule: Neither S1 nor S2 (both singular) takes singular verb ('seems')."
    },
    415: {
        "hint": "Subjects joined by 'either... or' with singular nouns take a singular verb.",
        "memory_tip": "Concord rule: Either... or connecting singular nouns takes singular verb ('has been')."
    },
    416: {
        "hint": "'Many a' is always followed by a singular countable noun and singular verb.",
        "memory_tip": "Concord rule: 'Many a + singular noun' takes singular verb ('Many a man has')."
    },
    417: {
        "hint": "'Each of...' takes a singular verb in prescriptive grammar; check test key option.",
        "memory_tip": "Concord rule: 'Each of' formally takes singular, but check test paper matching option."
    },
    418: {
        "hint": "When joined by 'as well as', the verb agrees with the first subject (Sanskrit).",
        "memory_tip": "Concord rule: S1 + 'as well as' + S2 agrees with S1 (Sanskrit was taught)."
    },
    419: {
        "hint": "When joined by 'with', the verb agrees with the principal subject (The ship).",
        "memory_tip": "Concord rule: Expressions like 'with/together with' do not change the number of the subject."
    },
    420: {
        "hint": "Parenthetical phrase 'with his councillors' does not affect singular subject 'The Mayor'.",
        "memory_tip": "Concord rule: The Mayor (singular) with... -> singular verb 'is'."
    },
    421: {
        "hint": "A title of a book, though plural in form, represents a single work and takes a singular verb.",
        "memory_tip": "Concord rule: Book titles take singular verb ('Gulliver's Travels was written by Swift')."
    },
    422: {
        "hint": "The true subject is 'The formation' (singular), not 'paragraphs'.",
        "memory_tip": "Concord rule: The head noun determines agreement: 'The formation of paragraphs is...'."
    },
    423: {
        "hint": "Fractions of a singular entity take a singular verb ('city is').",
        "memory_tip": "Concord rule: Fraction of singular noun -> singular verb ('Two-thirds of the city is')."
    },
    424: {
        "hint": "In dummy 'there' sentences, the verb agrees with the delayed plural subject 'many objections'.",
        "memory_tip": "Concord rule: There + are + plural noun phrase ('many objections')."
    },
    425: {
        "hint": "Neither mother nor father (both singular) takes singular verb 'is'.",
        "memory_tip": "Concord rule: Neither... nor with singular subjects takes singular verb ('is alive')."
    },
    426: {
        "hint": "'As well as' leaves agreement with the initial singular subject 'The cow'.",
        "memory_tip": "Concord rule: The cow as well as the horse eats (singular V1-s)."
    },
    427: {
        "hint": "'Each of' followed by a plural noun takes a singular verb 'was arrested'.",
        "memory_tip": "Concord rule: 'Each' is inherently singular -> 'was arrested'."
    },
    428: {
        "hint": "Single article 'The' before two titles indicates they refer to the same individual.",
        "memory_tip": "Concord rule: One article for two titles = one person -> singular verb 'is unwell'."
    },
    429: {
        "hint": "Single article 'A' indicates both adjectives qualify the same individual.",
        "memory_tip": "Concord rule: 'A good man and useful citizen' = one person -> 'has passed away'."
    },
    430: {
        "hint": "Two articles ('The accountant and the cashier') indicate two separate people -> plural verb.",
        "memory_tip": "Concord rule: Two separate articles = two people -> plural verb 'have absconded'."
    },
    431: {
        "hint": "'News' is an uncountable noun singular in construction and takes a singular verb.",
        "memory_tip": "Concord rule: 'News' is always singular -> 'No news is good news'."
    },
    432: {
        "hint": "The head noun is 'The cost' (singular), which governs 'has risen'.",
        "memory_tip": "Concord rule: Head noun 'The cost' (singular) governs verb: 'has risen'."
    },

    # Topic 19: Agreement & Auxiliary Verbs (Q433 - Q456)
    433: {
        "hint": "Past time marker 'yesterday' with singular subject 'she'.",
        "memory_tip": "Auxiliary rule: 3rd person singular past of be = 'was'."
    },
    434: {
        "hint": "Second person subject 'you' in past tense takes 'were'.",
        "memory_tip": "Auxiliary rule: 'You' always takes 'were' in the past."
    },
    435: {
        "hint": "Compound plural subject 'Raphel and I' in past tense takes 'were'.",
        "memory_tip": "Auxiliary rule: Plural subject in past takes 'were'."
    },
    436: {
        "hint": "Second person 'you' takes plural past form.",
        "memory_tip": "Auxiliary rule: 'You were' for questions and statements."
    },
    437: {
        "hint": "Plural subject takes plural past auxiliary.",
        "memory_tip": "Auxiliary rule: Plural subject + 'were'."
    },
    438: {
        "hint": "Plural subject 'they' takes 'were'.",
        "memory_tip": "Auxiliary rule: 'They were' in the past tense."
    },
    439: {
        "hint": "Singular subject in past tense takes 'was'.",
        "memory_tip": "Auxiliary rule: He/She/It + was."
    },
    440: {
        "hint": "Plural subject in past interrogative takes 'were'.",
        "memory_tip": "Auxiliary rule: Plural past = were."
    },
    441: {
        "hint": "Future auxiliary used for expressing decision or prediction.",
        "memory_tip": "Auxiliary rule: 'Will' + base verb indicates future time."
    },
    442: {
        "hint": "Singular third person subject in past tense.",
        "memory_tip": "Auxiliary rule: Singular subject takes 'was'."
    },
    443: {
        "hint": "Singular third person subject in present tense.",
        "memory_tip": "Auxiliary rule: Singular subject takes 'is'."
    },
    444: {
        "hint": "Singular subject referring to a past condition.",
        "memory_tip": "Auxiliary rule: Singular past = was."
    },
    445: {
        "hint": "Future auxiliary paired with bare infinitive.",
        "memory_tip": "Auxiliary rule: Modal 'will' for future tense."
    },
    446: {
        "hint": "Singular subject past tense.",
        "memory_tip": "Auxiliary rule: Singular subject + was."
    },
    447: {
        "hint": "Past singular auxiliary for third person.",
        "memory_tip": "Auxiliary rule: 3rd person singular past = was."
    },
    448: {
        "hint": "First person singular pronoun 'I' in present tense takes 'am'.",
        "memory_tip": "Auxiliary rule: 'I' pairs exclusively with 'am' in present tense."
    },
    449: {
        "hint": "Subject 'I' in present tense.",
        "memory_tip": "Auxiliary rule: 'I am'."
    },
    450: {
        "hint": "Third person singular subject in present tense.",
        "memory_tip": "Auxiliary rule: He/She/It pairs with 'is'."
    },
    451: {
        "hint": "Singular subject present tense takes 'is'.",
        "memory_tip": "Auxiliary rule: Singular subject takes 'is'."
    },
    452: {
        "hint": "Correlative 'either... or' / 'neither... nor': verb agrees with nearest subject 'I' -> 'am'.",
        "memory_tip": "Concord rule: With or/nor, verb agrees with the nearest subject ('I am')."
    },
    453: {
        "hint": "Plural subject takes the base form of the verb (V1) without '-s'.",
        "memory_tip": "Subject-verb agreement: Plural subject + V1 (open)."
    },
    454: {
        "hint": "Plural subject takes base verb form.",
        "memory_tip": "Subject-verb agreement: They/We + watch (V1)."
    },
    455: {
        "hint": "Plural/First/Second person negative auxiliary 'don't'.",
        "memory_tip": "Auxiliary rule: I/You/We/They take 'do/don't'."
    },
    456: {
        "hint": "Auxiliary used for question with plural subject.",
        "memory_tip": "Auxiliary rule: 'Do' with plural subjects."
    },

    # Topic 20: Order of Adjectives (Q457 - Q480)
    457: {
        "hint": "Opinion/Quality (smart) precedes size (little).",
        "memory_tip": "Adjective order: Opinion -> Size -> Noun (a smart little boy)."
    },
    458: {
        "hint": "Number (three) -> Opinion (lovely) -> Size (tiny) -> Color (yellow) -> Noun.",
        "memory_tip": "Adjective order: Number -> Opinion -> Size -> Color (three lovely tiny yellow flowers)."
    },
    459: {
        "hint": "Size (big) -> Color (white) -> Material (leather) -> Noun.",
        "memory_tip": "Adjective order: Size -> Color -> Material (a big white leather bag)."
    },
    460: {
        "hint": "Opinion (beautiful) -> Size (big) -> Material/Type (diamond) -> Noun.",
        "memory_tip": "Adjective order: Opinion -> Size -> Material (a beautiful big diamond necklace)."
    },
    461: {
        "hint": "Size/Shape (fat) -> Age (old) -> Color (white) -> Noun.",
        "memory_tip": "Adjective order: Size -> Age -> Color (a fat old white horse)."
    },
    462: {
        "hint": "Size (big) -> Color (grey) -> Material (woolen) -> Noun.",
        "memory_tip": "Adjective order: Size -> Color -> Material (a big grey woolen sweater)."
    },
    463: {
        "hint": "Size (small) -> Shape (round) -> Material (leather) -> Noun.",
        "memory_tip": "Adjective order: Size -> Shape -> Material (a small round leather handbag)."
    },
    464: {
        "hint": "Color (brown) -> Origin (German) -> Material (glass) -> Noun.",
        "memory_tip": "Adjective order: Color -> Origin -> Material (a brown German glass mug)."
    },
    465: {
        "hint": "Size (little) -> Shape (square) -> Material (brick) -> Noun.",
        "memory_tip": "Adjective order: Size -> Shape -> Material (a little square brick house)."
    },
    466: {
        "hint": "Size (big) -> Age (new) -> Purpose/Type (car) -> Noun.",
        "memory_tip": "Adjective order: Size -> Age -> Purpose (a big new car factory)."
    },
    467: {
        "hint": "Size (enormous) -> Color (black) -> Material (iron) -> Noun.",
        "memory_tip": "Adjective order: Size -> Color -> Material (enormous black iron gates)."
    },
    468: {
        "hint": "Size (small) -> Shape (oval) -> Color (white) -> Noun.",
        "memory_tip": "Adjective order: Size -> Shape -> Color (small oval white pearls)."
    },
    469: {
        "hint": "Age (old) -> Material (wooden) -> Purpose (serving) -> Noun.",
        "memory_tip": "Adjective order: Age -> Material -> Purpose (old wooden serving spoons)."
    },
    470: {
        "hint": "Quality/Condition (fresh) -> Color (red) -> Type (organic) -> Noun.",
        "memory_tip": "Adjective order: Quality -> Color -> Type (fresh red organic tomatoes)."
    },
    471: {
        "hint": "Size (small) -> Color (black) -> Material (tin) -> Noun.",
        "memory_tip": "Adjective order: Size -> Color -> Material (a small black tin box)."
    },
    472: {
        "hint": "Size (small) -> Color (green) -> Noun (insect).",
        "memory_tip": "Adjective order: Size -> Color (a small green insect)."
    },
    473: {
        "hint": "Opinion (wonderful) -> Age (new) -> Purpose (face) -> Noun.",
        "memory_tip": "Adjective order: Opinion -> Age -> Purpose (a wonderful new face cream)."
    },
    474: {
        "hint": "Opinion (beautiful) -> Material (wooden) -> Purpose (picture) -> Noun.",
        "memory_tip": "Adjective order: Opinion -> Material -> Purpose (a beautiful wooden picture frame)."
    },
    475: {
        "hint": "Origin (Japanese) -> Type (industrial) -> Noun (designers).",
        "memory_tip": "Adjective order: Origin -> Type (Japanese industrial designers)."
    },
    476: {
        "hint": "Opinion (useful) -> Color (black) -> Purpose (laptop) -> Noun.",
        "memory_tip": "Adjective order: Opinion -> Color -> Purpose (a useful black laptop bag)."
    },
    477: {
        "hint": "Size (big) -> Age (new) -> Material/Type (chocolate) -> Noun.",
        "memory_tip": "Adjective order: Size -> Age -> Type (a big new chocolate bar)."
    },
    478: {
        "hint": "Opinion (terrific) -> Origin (American) -> Purpose (television) -> Noun.",
        "memory_tip": "Adjective order: Opinion -> Origin -> Purpose (A terrific American television comedy)."
    },
    479: {
        "hint": "Opinion (wonderful) -> Age (modern) -> Purpose (sports) -> Noun.",
        "memory_tip": "Adjective order: Opinion -> Age -> Purpose (Wonderful modern sports shoes)."
    },
    480: {
        "hint": "Color (red) -> Material (metal) -> Purpose (kitchen) -> Noun.",
        "memory_tip": "Adjective order: Color -> Material -> Purpose (red metal kitchen chairs)."
    }
}
