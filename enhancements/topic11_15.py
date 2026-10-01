# enhancements/topic11_15.py
# Q241 to Q360: Articles, Tenses, Voice, Speech, Sentence Types

TIPS = {
    # Topic 11: Articles (Q241 - Q264)
    241: {
        "hint": "Ordinal numbers (first, second, third) indicate a unique rank or position.",
        "memory_tip": "Article rule: Use definite article 'the' before ordinal numbers (the first, the second)."
    },
    242: {
        "hint": "When referring to playing a musical instrument, which article is used?",
        "memory_tip": "Article rule: Use 'the' before musical instruments when referring to playing them (play the flute/piano)."
    },
    243: {
        "hint": "Superlative adjectives (best, tallest, greatest) require a specific article.",
        "memory_tip": "Article rule: Always use 'the' before superlative degree adjectives (the best, the highest)."
    },
    244: {
        "hint": "Uncountable nouns used in a general sense do not take an article.",
        "memory_tip": "Article rule: Zero article before uncountable material nouns in general statements (Sugar is sweet)."
    },
    245: {
        "hint": "Names of materials, substances, and precious metals in general take no article.",
        "memory_tip": "Article rule: Omit articles before material nouns used generally (Gold is a precious metal)."
    },
    246: {
        "hint": "'Amazing' begins with a vowel sound /ə/.",
        "memory_tip": "Article rule: Use 'an' before words beginning with a vowel sound (a, e, i, o, u)."
    },
    247: {
        "hint": "'Assistant' starts with a vowel sound /ə/.",
        "memory_tip": "Article rule: Singular countable nouns starting with a vowel sound take 'an'."
    },
    248: {
        "hint": "Refers to a specific level of a building; check the official key option.",
        "memory_tip": "Article rule: Positions like 'the top floor' specify unique locations; note test key option (2)."
    },
    249: {
        "hint": "Superlatives like 'most industrial' require the definite article.",
        "memory_tip": "Article rule: 'One of the' is always followed by 'the' + superlative adjective."
    },
    250: {
        "hint": "'Very' begins with a consonant sound /v/.",
        "memory_tip": "Article rule: Use 'a' before singular countable noun phrases starting with a consonant sound."
    },
    251: {
        "hint": "'Island' begins with the diphthong vowel sound /aɪ/.",
        "memory_tip": "Article rule: Island begins with a vowel sound -> 'an island'."
    },
    252: {
        "hint": "Superlative adjective 'best' takes the definite article.",
        "memory_tip": "Article rule: Superlatives take 'the' (the best prize, the biggest award)."
    },
    253: {
        "hint": "'Owl' begins with the vowel sound /aʊ/.",
        "memory_tip": "Article rule: Vowel sound beginning requires 'an' (an owl, an eagle)."
    },
    254: {
        "hint": "'Umbrella' begins with the short vowel sound /ʌ/.",
        "memory_tip": "Article rule: Use 'an' before vowel sounds (an umbrella, an uncle)."
    },
    255: {
        "hint": "Superlative adjective 'longest' describes the river.",
        "memory_tip": "Article rule: 'The' is required before superlative adjectives (the longest, the deepest)."
    },
    256: {
        "hint": "'Easy' begins with the long vowel sound /iː/.",
        "memory_tip": "Article rule: Vowel sound beginning -> 'an easy language'."
    },
    257: {
        "hint": "'Hour' begins with a silent 'h', producing an initial vowel sound /aʊər/.",
        "memory_tip": "Article rule: Words with silent 'h' take 'an' (an hour, an honest man, an heir)."
    },
    258: {
        "hint": "'Wonderful' starts with the consonant sound /w/.",
        "memory_tip": "Article rule: Consonant sound beginning takes 'a' (a wonderful lamp)."
    },
    259: {
        "hint": "Unique celestial objects and natural bodies take the definite article.",
        "memory_tip": "Article rule: Use 'The' before unique celestial entities (The Sun, The Moon, The Earth)."
    },
    260: {
        "hint": "'Sacred' starts with the consonant sound /s/.",
        "memory_tip": "Article rule: Singular countable noun with consonant sound -> 'a sacred river'."
    },
    261: {
        "hint": "Expressions of payment method ('by cheque', 'by cash', 'by card') take no article.",
        "memory_tip": "Article rule: Fixed prepositional phrases like 'by cheque', 'by bus', 'by air' use zero article."
    },
    262: {
        "hint": "Singular profession, diet, or role starting with a consonant sound.",
        "memory_tip": "Article rule: Use 'a' before singular designations (a vegetarian, a doctor)."
    },
    263: {
        "hint": "'Photographer' begins with the consonant sound /f/.",
        "memory_tip": "Article rule: Use 'a' before names of occupations beginning with consonant sounds."
    },
    264: {
        "hint": "Superlative adjective 'youngest' requires the definite article.",
        "memory_tip": "Article rule: Superlative forms take 'The' (The youngest, The tallest)."
    },

    # Topic 12: Tenses (Q265 - Q288)
    265: {
        "hint": "Subject + base verb with '-s' expressing a general fact or habit.",
        "memory_tip": "Tense structure: Subject + V1(s/es) = Simple Present Tense."
    },
    266: {
        "hint": "Formed with 'is' + verb-ing, indicating an action happening right now.",
        "memory_tip": "Tense structure: am/is/are + V-ing = Present Continuous Tense."
    },
    267: {
        "hint": "Expresses a repeated, routine action occurring 'every hour'.",
        "memory_tip": "Tense rule: Regular habits and routines are expressed in Simple Present Tense."
    },
    268: {
        "hint": "The past verb 'bought' with the past time marker 'yesterday'.",
        "memory_tip": "Tense structure: Subject + V2 + past time adverb = Simple Past Tense."
    },
    269: {
        "hint": "'Was' + verb-ing represents an ongoing action in the past.",
        "memory_tip": "Tense structure: was/were + V-ing = Past Continuous Tense."
    },
    270: {
        "hint": "'Has' + past participle (V3) indicates an action completed with present relevance.",
        "memory_tip": "Tense structure: has/have + V3 = Present Perfect Tense."
    },
    271: {
        "hint": "'Will' + base verb (V1) refers to an action that will occur in future time.",
        "memory_tip": "Tense structure: will/shall + V1 = Simple Future Tense."
    },
    272: {
        "hint": "'Have been' + verb-ing with a duration phrase ('for a week').",
        "memory_tip": "Tense structure: has/have + been + V-ing = Present Perfect Continuous Tense."
    },
    273: {
        "hint": "The frequency adverb 'always' combined with third-person singular V1 'forgets'.",
        "memory_tip": "Tense rule: Habitual actions with 'always/often' use Simple Present Tense."
    },
    274: {
        "hint": "'Am not' + verb-ing expresses an action around the present time period.",
        "memory_tip": "Tense structure: am/is/are + not + V-ing = Present Continuous (negative)."
    },
    275: {
        "hint": "V2 verb 'left' with a specific past year 'in 1990'.",
        "memory_tip": "Tense rule: Specific completed past time points always take Simple Past Tense."
    },
    276: {
        "hint": "'Have' + V3 'spoken' indicates a completed action with present connection.",
        "memory_tip": "Tense structure: have + V3 (past participle) = Present Perfect Tense."
    },
    277: {
        "hint": "'Have been' + verb-ing ('travelling') indicating an ongoing activity over 6 hours.",
        "memory_tip": "Tense structure: have been + V-ing + for/since = Present Perfect Continuous."
    },
    278: {
        "hint": "'Are' + verb-ing ('looking') describes an action in progress right now.",
        "memory_tip": "Tense structure: are + V-ing = Present Continuous Tense."
    },
    279: {
        "hint": "Auxiliary 'did not' + V1 with past time marker 'yesterday'.",
        "memory_tip": "Tense structure: did + not + V1 = Simple Past Tense negative."
    },
    280: {
        "hint": "'Have been waiting' with time preposition 'since 9 o'clock'.",
        "memory_tip": "Tense structure: have been + V-ing + since = Present Perfect Continuous."
    },
    281: {
        "hint": "Interrogative starting with auxiliary 'Did' + subject + base verb.",
        "memory_tip": "Tense structure: Did + Subject + V1? = Simple Past Tense interrogative."
    },
    282: {
        "hint": "Interrogative starting with 'Do' + subject + base verb.",
        "memory_tip": "Tense structure: Do/Does + Subject + V1? = Simple Present Tense interrogative."
    },
    283: {
        "hint": "'Is' + subject + verb-ing ('listening') asks about an ongoing action.",
        "memory_tip": "Tense structure: Is/Are + Subject + V-ing? = Present Continuous interrogative."
    },
    284: {
        "hint": "Wh-word + 'did' + subject + base verb.",
        "memory_tip": "Tense structure: Question word + did + Subject + V1 = Simple Past interrogative."
    },
    285: {
        "hint": "'Was' + subject + verb-ing ('eating') asking about continuous past action.",
        "memory_tip": "Tense structure: was/were + V-ing = Past Continuous Tense."
    },
    286: {
        "hint": "'Have' + subject + V3 ('put') asks about a completed past action with present effect.",
        "memory_tip": "Tense structure: have/has + Subject + V3? = Present Perfect Tense."
    },
    287: {
        "hint": "'Have broken' expresses life experience up to the present.",
        "memory_tip": "Tense structure: have + V3 = Present Perfect Tense for lifetime experiences."
    },
    288: {
        "hint": "Subject 'Your dog' (singular) + V1-s 'eats' describes a regular tendency.",
        "memory_tip": "Tense structure: Singular Subject + V1-s = Simple Present Tense."
    },

    # Topic 13: Voice (Q289 - Q312)
    289: {
        "hint": "Simple Past active 'dusted' becomes 'was/were dusted' in passive voice.",
        "memory_tip": "Passive rule: Simple Past active (V2) -> was/were + V3."
    },
    290: {
        "hint": "Simple Present active 'writes' with plural object 'history books'.",
        "memory_tip": "Passive rule: Simple Present active (V1) -> am/is/are + V3 (are written)."
    },
    291: {
        "hint": "Present Perfect active 'have received' takes 'has/have been received'.",
        "memory_tip": "Passive rule: Present Perfect active -> has/have + been + V3."
    },
    292: {
        "hint": "Past Perfect active 'had bought' becomes 'had been bought'.",
        "memory_tip": "Passive rule: Past Perfect active -> had been + V3."
    },
    293: {
        "hint": "Simple Present active 'sell' with plural object 'toys'.",
        "memory_tip": "Passive rule: Object 'toys' + are + sold (V3) + by us."
    },
    294: {
        "hint": "Simple Past active 'took' with plural object 'some pictures'.",
        "memory_tip": "Passive rule: Plural object + were + taken (V3) + by Vamsi."
    },
    295: {
        "hint": "Present Continuous active 'are eating' with singular object 'food'.",
        "memory_tip": "Passive rule: Present continuous -> is/am/are + being + V3 (food is being eaten)."
    },
    296: {
        "hint": "Present Perfect active 'has painted' with plural object 'these doors'.",
        "memory_tip": "Passive rule: Plural object + have been + painted (V3)."
    },
    297: {
        "hint": "Simple Future active 'will praise' with object 'you'.",
        "memory_tip": "Passive rule: will/shall + be + V3 (You will be praised)."
    },
    298: {
        "hint": "Past Perfect active 'had caught' with object 'many snakes'.",
        "memory_tip": "Passive rule: had + been + caught (V3)."
    },
    299: {
        "hint": "Present Continuous active 'is drinking' with uncountable object 'milk'.",
        "memory_tip": "Passive rule: Singular/uncountable + is + being + drunk (V3)."
    },
    300: {
        "hint": "Past Continuous active 'was teaching' with singular object 'a poem'.",
        "memory_tip": "Passive rule: Past continuous -> was/were + being + V3 (was being taught)."
    },
    301: {
        "hint": "Simple Present active 'writes' with plural object 'books'.",
        "memory_tip": "Passive rule: Plural object 'Books' + are + written (V3) + by Pallavi."
    },
    302: {
        "hint": "Present Perfect active 'have played' with singular object 'cricket'.",
        "memory_tip": "Passive rule: Singular object + has been + played (V3) + by me."
    },
    303: {
        "hint": "Simple Present active 'repairs' with plural object 'air coolers'.",
        "memory_tip": "Passive rule: Plural object + are + repaired (V3) + by Kiran."
    },
    304: {
        "hint": "Imperative sentence of command is converted using 'Let + object + be + V3'.",
        "memory_tip": "Passive rule: Imperative command -> Let + Object + be + V3 (Let all the gates be closed)."
    },
    305: {
        "hint": "Simple Past active 'wrote' with singular object 'Geetanjali'.",
        "memory_tip": "Passive rule: Singular object + was + written (V3) + by Tagore."
    },
    306: {
        "hint": "Simple Past active 'ate' with singular object 'an apple'.",
        "memory_tip": "Passive rule: An apple + was + eaten (V3) + by Sudeep."
    },
    307: {
        "hint": "Simple Present active 'makes' with plural object 'machines'.",
        "memory_tip": "Passive rule: Plural object + are + made (V3) + by man."
    },
    308: {
        "hint": "Past Perfect active 'had bought' with plural object 'three books'.",
        "memory_tip": "Passive rule: Three books + had been + bought (V3) + by me."
    },
    309: {
        "hint": "Simple Past active 'saw' with plural object 'many animals'.",
        "memory_tip": "Passive rule: Many animals + were + seen (V3) + by us."
    },
    310: {
        "hint": "Imperative command 'Close the door' converts using 'Let'.",
        "memory_tip": "Passive rule: Let + the door + be + closed (V3)."
    },
    311: {
        "hint": "Present Continuous active 'are eating' with plural object 'bananas'.",
        "memory_tip": "Passive rule: Plural object + are being + eaten (V3) (Option 4; note key correction from 74 to 4)."
    },
    312: {
        "hint": "Simple Past active 'killed' with singular object 'the cat'.",
        "memory_tip": "Passive rule: The cat + was + killed (V3) + by the dog."
    },

    # Topic 14: Direct & Indirect Speech (Q313 - Q336)
    313: {
        "hint": "Present continuous 'are you doing' backshifts to past continuous 'he was doing'.",
        "memory_tip": "Speech rule: Present continuous (am/is/are) backshifts to Past continuous (was/were)."
    },
    314: {
        "hint": "Direct 'I am making' backshifts to indirect 'he was making'.",
        "memory_tip": "Speech rule: 1st person pronoun shifts to 3rd person; 'am' changes to 'was'."
    },
    315: {
        "hint": "Present 'is' in direct question backshifts to past in reported clause.",
        "memory_tip": "Speech rule: In indirect Wh-questions, 'is' shifts to 'was' and follows the subject."
    },
    316: {
        "hint": "Yes/No questions in reported speech are introduced by conjunction 'if' or 'whether'.",
        "memory_tip": "Speech rule: Yes/No interrogative -> conjunction 'if' or 'whether'."
    },
    317: {
        "hint": "Modal verb 'can' backshifts to 'could' in reported speech.",
        "memory_tip": "Speech rule: Modal backshift: can -> could, may -> might, will -> would."
    },
    318: {
        "hint": "Direct 'you are' spoken to Ravi becomes 'he was' in reported statement.",
        "memory_tip": "Speech rule: Second person pronoun refers to object (Ravi -> he); 'are' -> 'was'."
    },
    319: {
        "hint": "Simple Present question 'do they know' backshifts to Simple Past 'knew'.",
        "memory_tip": "Speech rule: Simple present verb (know) shifts to simple past (knew)."
    },
    320: {
        "hint": "Simple Past direct question 'did you find' backshifts to Past Perfect 'had found'.",
        "memory_tip": "Speech rule: Simple past (did find) shifts to Past Perfect (had found)."
    },
    321: {
        "hint": "Direct 1st person possessive 'my hands' spoken by the potter becomes 'his hands'.",
        "memory_tip": "Speech rule: Pronoun changes according to the speaker ('my' -> 'his')."
    },
    322: {
        "hint": "Imperative command converts to to-infinitive: 'to look at the paper'.",
        "memory_tip": "Speech rule: Imperative in reported speech uses 'to + base verb' (to look)."
    },
    323: {
        "hint": "Command 'Open the safe' converts into infinitive 'to open'.",
        "memory_tip": "Speech rule: Imperative orders take 'ordered/told + to + V1' (to open)."
    },
    324: {
        "hint": "Negative imperative 'Don't miss' converts into 'not to miss'.",
        "memory_tip": "Speech rule: Negative imperative becomes 'not to + V1' (not to miss)."
    },
    325: {
        "hint": "Present 'say' backshifts to past 'said' in the reported clause.",
        "memory_tip": "Speech rule: Subordinate clause verb backshifts from present to past (say -> said)."
    },
    326: {
        "hint": "Direct possessive 'my way' spoken by him changes to 'his way'.",
        "memory_tip": "Speech rule: 1st person possessive pronoun aligns with the speaker ('my' -> 'his')."
    },
    327: {
        "hint": "Direct question 'Do you like' backshifts to past 'liked'.",
        "memory_tip": "Speech rule: Simple present verb (like) backshifts to past (liked)."
    },
    328: {
        "hint": "Pronoun 'you' referring to 'her' in reported clause becomes 'her'.",
        "memory_tip": "Speech rule: Second person pronoun aligns with reported listener ('her')."
    },
    329: {
        "hint": "Exclamatory sentences in reported speech use the reporting conjunction 'that'.",
        "memory_tip": "Speech rule: Exclaimed with sorrow + that + clause."
    },
    330: {
        "hint": "Reported exclamations are connected to the reporting verb by 'that'.",
        "memory_tip": "Speech rule: Reporting clause connector for declarative and exclamatory = 'that'."
    },
    331: {
        "hint": "Direct 'are you all sitting' spoken to 'us' backshifts to 'we were all sitting'.",
        "memory_tip": "Speech rule: Present continuous auxiliary 'are' backshifts to past 'were'."
    },
    332: {
        "hint": "The connecting conjunction introducing the indirect statement clause.",
        "memory_tip": "Speech rule: Exclaimed with regret 'that' he was ruined."
    },
    333: {
        "hint": "Direct question 'what are you doing' spoken to 'me' becomes 'what I was doing'.",
        "memory_tip": "Speech rule: In indirect questions, subject precedes the verb: 'what I was doing'."
    },
    334: {
        "hint": "Direct question 'Are you planning' spoken to Henry backshifts to 'if he was planning'.",
        "memory_tip": "Speech rule: Present continuous (are planning) backshifts to past continuous (was planning)."
    },
    335: {
        "hint": "Direct modal 'will' backshifts to 'would' in indirect speech.",
        "memory_tip": "Speech rule: Modal backshift: will -> would."
    },
    336: {
        "hint": "Direct question 'Are you quite well' backshifts to 'if he was quite well'.",
        "memory_tip": "Speech rule: Present 'are' changes to past 'was' for singular subject 'he'."
    },

    # Topic 15: Types of Sentences (Q337 - Q360)
    337: {
        "hint": "Sentences that state facts, convey assertions, or make declarations.",
        "memory_tip": "Sentence types: Declarative sentences make statements and end with a period/full stop."
    },
    338: {
        "hint": "Look for the sentence that asks a question and ends with a question mark.",
        "memory_tip": "Sentence types: Interrogative sentences ask questions (?); Auxiliary/Wh-word fronted."
    },
    339: {
        "hint": "An imperative sentence can express an order, a polite request, or advice.",
        "memory_tip": "Sentence types: Imperative expresses command, request, advice, or instruction."
    },
    340: {
        "hint": "Look for the sentence expressing intense feeling and ending with an exclamation mark (!).",
        "memory_tip": "Sentence types: Exclamatory expresses sudden, strong emotion (starts with How/What, ends with !)."
    },
    341: {
        "hint": "A plain statement asserting a fact about Dr. Kalam.",
        "memory_tip": "Declarative = statement of fact or opinion."
    },
    342: {
        "hint": "Begins with a question word 'What' and seeks information.",
        "memory_tip": "Interrogative = asks a direct question."
    },
    343: {
        "hint": "Expresses a passionate longing/wish and ends with an exclamation point.",
        "memory_tip": "Exclamatory = expresses strong desire, surprise, or emotion."
    },
    344: {
        "hint": "Which option transforms the statement into a question?",
        "memory_tip": "Statement -> Interrogative transformation: 'Did he win the election?'"
    },
    345: {
        "hint": "States an assertion directly about a person.",
        "memory_tip": "Declarative = direct statement."
    },
    346: {
        "hint": "A declarative statement containing a negative marker (not).",
        "memory_tip": "Negative Declarative: Subject + does not + V1."
    },
    347: {
        "hint": "Transforms the statement into a negative interrogative question.",
        "memory_tip": "Negative Interrogative: Did + Subject + not + V1?"
    },
    348: {
        "hint": "Transforms 'He has a car' into its negative declarative form.",
        "memory_tip": "Negative form of has (possession): He does not have a car."
    },
    349: {
        "hint": "States a routine personal fact ending in a period.",
        "memory_tip": "Declarative = statement of habit or fact."
    },
    350: {
        "hint": "Narrates a past action as a direct statement.",
        "memory_tip": "Declarative = statement of fact."
    },
    351: {
        "hint": "Inquires about identity using the question word 'Who'.",
        "memory_tip": "Interrogative = question seeking an answer."
    },
    352: {
        "hint": "Begins with auxiliary 'Have' and asks a question.",
        "memory_tip": "Interrogative = Yes/No question."
    },
    353: {
        "hint": "Begins with 'What a...' expressing amazement with '!'.",
        "memory_tip": "Exclamatory: What + a/an + adjective + noun + subject + verb!"
    },
    354: {
        "hint": "Expresses admiration of beauty ending with an exclamation mark.",
        "memory_tip": "Exclamatory sentence expresses strong appreciation or wonder."
    },
    355: {
        "hint": "Look for the option that is a straightforward affirmative statement.",
        "memory_tip": "Declarative sentence asserts a fact or feeling directly."
    },
    356: {
        "hint": "Asks about location starting with 'Where'.",
        "memory_tip": "Interrogative sentence inquires about place."
    },
    357: {
        "hint": "Contains the joyful interjection 'Hurrah!' and an exclamation mark.",
        "memory_tip": "Exclamatory sentence communicates joy or triumph."
    },
    358: {
        "hint": "Narrates an action plainly and ends with a full stop.",
        "memory_tip": "Declarative sentence reports information."
    },
    359: {
        "hint": "Inquires about hearing capability starting with modal 'Can'.",
        "memory_tip": "Interrogative sentence begins with auxiliary/modal verb."
    },
    360: {
        "hint": "Contains a polite request with 'Please' directed at the listener.",
        "memory_tip": "Imperative sentence gives a command, direction, or makes a request."
    }
}
