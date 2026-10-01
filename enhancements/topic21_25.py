# enhancements/topic21_25.py
# Q481 to Q600: Transitive/Intransitive verbs, Question Tags, Sentence Correction, Clauses, Punctuation/Capitalization

TIPS = {
    # Topic 21: Types of Verbs (Q481 - Q504)
    481: {
        "hint": "The verb 'used' transfers action directly to the direct object 'candles'.",
        "memory_tip": "Verb type: Transitive verb requires a direct object (Subject + Verb + Object)."
    },
    482: {
        "hint": "'Lifted' takes the direct object 'its nose' (What did it lift?).",
        "memory_tip": "Verb type: If you can answer 'What?' or 'Whom?' after the verb, it is Transitive."
    },
    483: {
        "hint": "'Hung' has no direct object; 'limply' is an adverb answering 'How?'.",
        "memory_tip": "Verb type: Intransitive verb does not take a direct object (cannot be made passive)."
    },
    484: {
        "hint": "'Followed' takes the direct object pronoun 'him'.",
        "memory_tip": "Verb type: Followed + whom? (him) = Transitive verb."
    },
    485: {
        "hint": "'Found' takes the direct object pronoun 'him'.",
        "memory_tip": "Verb type: Found + whom? (him) = Transitive verb."
    },
    486: {
        "hint": "'Turned' takes the direct object 'its head'.",
        "memory_tip": "Verb type: Turned + what? (its head) = Transitive verb."
    },
    487: {
        "hint": "'Tumbled' has no object; 'backward' is an adverb of direction.",
        "memory_tip": "Verb type: Action confined to the subject without an object = Intransitive verb."
    },
    488: {
        "hint": "'Went' is followed by a prepositional phrase of place ('to the kitchen'), not a direct object.",
        "memory_tip": "Verb type: Verbs of movement (go, come, walk) followed by prepositions are Intransitive."
    },
    489: {
        "hint": "'Changes' takes the direct object 'you'.",
        "memory_tip": "Verb type: Transitive verb carries action over to an object ('changes you')."
    },
    490: {
        "hint": "'Stood' is followed by a prepositional phrase ('beside him'); no direct object.",
        "memory_tip": "Verb type: Intransitive verb indicates posture/position without an object."
    },
    491: {
        "hint": "'Held' acts directly upon 'the coffee pot'.",
        "memory_tip": "Verb type: Held + what? (the coffee pot) = Transitive verb."
    },
    492: {
        "hint": "'Lifted' takes the direct object 'its nose'.",
        "memory_tip": "Verb type: Transitive verb requires an object receiver."
    },
    493: {
        "hint": "'Picked up' acts upon the object pronoun 'it'.",
        "memory_tip": "Verb type: Phrasal verb with direct object 'it' = Transitive."
    },
    494: {
        "hint": "'Spotted' refers to catching sight of something (transitive sense).",
        "memory_tip": "Verb type: Spotted requires an object in meaning = Transitive verb."
    },
    495: {
        "hint": "'Sat down' takes no direct object; 'beside her' is a prepositional phrase.",
        "memory_tip": "Verb type: Sit/sat is inherently Intransitive (cannot take an object; contrast with 'set')."
    },
    496: {
        "hint": "'Came' is followed by a prepositional phrase ('out of the station').",
        "memory_tip": "Verb type: 'Come' expresses motion without a direct object = Intransitive."
    },
    497: {
        "hint": "'Dipped' acts directly upon the object 'his fingers'.",
        "memory_tip": "Verb type: Dipped + what? (his fingers) = Transitive verb."
    },
    498: {
        "hint": "'Bleated' has no object; 'frantically' is an adverb.",
        "memory_tip": "Verb type: Animal vocalizations (bleat, bark, roar) without objects = Intransitive."
    },
    499: {
        "hint": "'Sucked' acts directly on 'his fingers'.",
        "memory_tip": "Verb type: Sucked + what? (his fingers) = Transitive verb."
    },
    500: {
        "hint": "'Lowered' takes the direct object 'his fingers'.",
        "memory_tip": "Verb type: Lowered + what? (his fingers) = Transitive verb."
    },
    501: {
        "hint": "'Stamped' acts directly upon 'its small hoofs'.",
        "memory_tip": "Verb type: Stamped + what? (its small hoofs) = Transitive verb."
    },
    502: {
        "hint": "'Held' takes the direct object 'his fingers'.",
        "memory_tip": "Verb type: Held + what? (his fingers) = Transitive verb."
    },
    503: {
        "hint": "'Walked' here has no direct object; 'all day' is an adverbial of duration.",
        "memory_tip": "Verb type: Walk used without an object = Intransitive verb."
    },
    504: {
        "hint": "'Stroked' acts directly upon 'its sides'.",
        "memory_tip": "Verb type: Stroked + what? (its sides) = Transitive verb."
    },

    # Topic 22: Question Tags (Q505 - Q528)
    505: {
        "hint": "Positive statement with 'is' takes a negative tag 'isn't it?'.",
        "memory_tip": "Tag rule: Positive statement -> Negative tag; auxiliary 'is' -> 'isn't it?'."
    },
    506: {
        "hint": "Positive statement 'She is' takes negative tag 'isn't she?'.",
        "memory_tip": "Tag rule: Positive auxiliary 'is' + subject pronoun 'she' -> 'isn't she?'."
    },
    507: {
        "hint": "An imperative request takes 'will you?' or 'won't you?'.",
        "memory_tip": "Tag rule: Imperative sentences take 'will you?' as the question tag."
    },
    508: {
        "hint": "Positive statement with past auxiliary 'was' takes negative tag 'wasn't it?'.",
        "memory_tip": "Tag rule: 'was' (positive) -> 'wasn't it?'."
    },
    509: {
        "hint": "Negative statement with 'isn't' takes a positive tag 'is she?'.",
        "memory_tip": "Tag rule: Negative statement -> Positive tag ('isn't she' -> 'is she?')."
    },
    510: {
        "hint": "Positive statement 'He is' takes negative tag 'isn't he?'.",
        "memory_tip": "Tag rule: 'He is' -> 'isn't he?'."
    },
    511: {
        "hint": "Statement with main verb 'have' (British style) takes 'haven't you?'.",
        "memory_tip": "Tag rule: 'You have' -> 'haven't you?' (or don't you?)."
    },
    512: {
        "hint": "Positive statement 'It is' takes negative tag 'isn't it?'.",
        "memory_tip": "Tag rule: 'It is' -> 'isn't it?'."
    },
    513: {
        "hint": "Positive statement with modal 'can' takes negative tag 'can't we?'.",
        "memory_tip": "Tag rule: Modal 'can' -> 'can't we?'."
    },
    514: {
        "hint": "Positive statement 'I am' takes the anomalous tag 'aren't I?'.",
        "memory_tip": "Tag rule: 'I am' always takes the tag 'aren't I?' in standard English."
    },
    515: {
        "hint": "Negative statement with 'haven't' takes positive tag 'have you?'.",
        "memory_tip": "Tag rule: Negative auxiliary 'haven't' -> Positive tag 'have you?'."
    },
    516: {
        "hint": "Negative modal 'can't' takes positive tag 'can they?'.",
        "memory_tip": "Tag rule: 'can't' -> 'can they?'."
    },
    517: {
        "hint": "Statement with 'That was' takes 'wasn't that?' or 'wasn't it?'.",
        "memory_tip": "Tag rule: Check test key option: 'That was' -> 'wasn't that?'."
    },
    518: {
        "hint": "Negative statement 'isn't coming' takes positive tag 'is she?'.",
        "memory_tip": "Tag rule: 'isn't' -> 'is she?'."
    },
    519: {
        "hint": "Positive statement 'You have waited' takes negative tag 'haven't you?'.",
        "memory_tip": "Tag rule: 'You have' -> 'haven't you?'."
    },
    520: {
        "hint": "Plural subject with 'are' takes negative tag 'aren't they?'.",
        "memory_tip": "Tag rule: 'are rising' (positive) -> 'aren't they?'."
    },
    521: {
        "hint": "Positive future modal 'will' takes negative tag 'won't she?'.",
        "memory_tip": "Tag rule: 'will' (positive) -> 'won't she?' (will not contracted)."
    },
    522: {
        "hint": "Simple present 3rd person singular 'draws' (positive) takes 'doesn't she?'.",
        "memory_tip": "Tag rule: V1-s requires dummy auxiliary 'does' -> 'doesn't she?'."
    },
    523: {
        "hint": "Simple past 'went' (positive) takes past tag 'didn't they?'.",
        "memory_tip": "Tag rule: Simple past verb (V2) takes dummy auxiliary 'didn't' -> 'didn't they?'."
    },
    524: {
        "hint": "Negative modal 'can't' takes positive tag 'can you?'.",
        "memory_tip": "Tag rule: 'can't' -> 'can you?'."
    },
    525: {
        "hint": "Negative future modal 'won't' takes positive tag 'will they?'.",
        "memory_tip": "Tag rule: 'won't' -> 'will they?'."
    },
    526: {
        "hint": "Statement with 'have got'; check test key option.",
        "memory_tip": "Tag rule: Note official key selection for 'have' auxiliary tag."
    },
    527: {
        "hint": "Positive statement 'She is' takes negative tag 'isn't she?'.",
        "memory_tip": "Tag rule: 'is' -> 'isn't she?'."
    },
    528: {
        "hint": "Positive statement 'will be' takes negative tag 'won't he?'.",
        "memory_tip": "Tag rule: 'will' -> 'won't he?'."
    },

    # Topic 23: Sentence Correction (Q529 - Q552)
    529: {
        "hint": "Suggestions starting with 'Let's' are followed directly by the base verb (meet).",
        "memory_tip": "Grammar rule: 'Let's' + V1 bare infinitive (Let's meet tomorrow)."
    },
    530: {
        "hint": "Actions continuing from past to present with 'since' require Present Perfect Continuous.",
        "memory_tip": "Error correction: Use 'have been teaching' instead of 'am teaching' with 'since 2009'."
    },
    531: {
        "hint": "A period or duration of time takes 'for', not 'since'.",
        "memory_tip": "Grammar rule: Use 'for' for duration (for two days) and 'since' for starting point."
    },
    532: {
        "hint": "'Honest' begins with a silent 'h' and vowel sound /ɒ/, requiring 'an'.",
        "memory_tip": "Error correction: 'an honest man', never 'a honest man'."
    },
    533: {
        "hint": "Past time marker 'last year' requires Simple Past Tense 'left'.",
        "memory_tip": "Grammar rule: Specific past time references take Simple Past (left the school last year)."
    },
    534: {
        "hint": "Universal scientific truths and celestial facts take Simple Present Tense.",
        "memory_tip": "Grammar rule: Universal truths use Simple Present ('The earth moves round the sun')."
    },
    535: {
        "hint": "'Home' used as an adverb of direction does not take the preposition 'to'.",
        "memory_tip": "Grammar rule: Say 'going home' (not 'going to home')."
    },
    536: {
        "hint": "Correct prepositional phrase for regular morning times.",
        "memory_tip": "Grammar rule: 'goes to temple in the mornings' shows customary action."
    },
    537: {
        "hint": "Stative verbs of possession like 'own' are not used in continuous tenses.",
        "memory_tip": "Stative verb rule: Say 'I own a car', never 'I am owning a car'."
    },
    538: {
        "hint": "'Neither of' followed by plural noun takes a singular verb ('looks').",
        "memory_tip": "Concord rule: 'Neither of my daughters looks like me' (singular verb)."
    },
    539: {
        "hint": "'One of + plural noun' takes a singular verb ('works').",
        "memory_tip": "Grammar rule: 'One of my uncles works in Delhi' (uncles is plural, works is singular)."
    },
    540: {
        "hint": "Useful begins with the semi-vowel consonant sound /j/, taking 'a'.",
        "memory_tip": "Article rule: 'a useful metal' (starts with 'yu' consonant sound)."
    },
    541: {
        "hint": "Time expressions with 'next' do not take prepositions like 'on' or 'at'.",
        "memory_tip": "Preposition rule: Say 'See you next Friday' (no preposition before next/last)."
    },
    542: {
        "hint": "Routine habitual action in Simple Present with third person singular 'goes'.",
        "memory_tip": "Grammar rule: 'goes for a walk every day' (every day is two words as adverbial)."
    },
    543: {
        "hint": "Pronoun 'one' must be maintained consistently with possessive 'one's'.",
        "memory_tip": "Pronoun concord: 'One should love one's own country' (not his own country)."
    },
    544: {
        "hint": "In formal comparison, subjective pronoun follows 'than' (worse than I [am]).",
        "memory_tip": "Pronoun case: 'He is worse than I' (formal subjective complement)."
    },
    545: {
        "hint": "'Advice' is an uncountable noun and cannot be preceded by 'an' or pluralized.",
        "memory_tip": "Noun rule: 'some advice' or 'a piece of advice' (never an advice / advices)."
    },
    546: {
        "hint": "Question tag matches auxiliary 'are' with negative tag 'aren't you?'.",
        "memory_tip": "Tag rule: 'You are..., aren't you?'."
    },
    547: {
        "hint": "Superlative degree takes 'the' and no double comparative/superlative.",
        "memory_tip": "Degree rule: 'the cleverest girl' (not most cleverest)."
    },
    548: {
        "hint": "'Children' is an irregular plural countable noun taking 'How many'.",
        "memory_tip": "Quantifier rule: 'How many children' (children is plural of child; takes many, not much)."
    },
    549: {
        "hint": "'Information' is an uncountable noun and never takes '-s'.",
        "memory_tip": "Noun rule: 'some information' (never informations)."
    },
    550: {
        "hint": "Predicate adjective 'successful' follows linking verb 'is'.",
        "memory_tip": "Adjective rule: Subject + is + adjective ('Meena is successful')."
    },
    551: {
        "hint": "Verb 'depend' takes the preposition 'on' or 'upon'.",
        "memory_tip": "Preposition: 'depends on' (never depends at/in)."
    },
    552: {
        "hint": "Past time adverb 'yesterday' requires Simple Past 'saw'.",
        "memory_tip": "Tense rule: 'I saw Bhaskar yesterday' (Simple Past V2 with past time marker)."
    },

    # Topic 24: Clauses & Conditionals (Q553 - Q576)
    553: {
        "hint": "If + Simple Present (play), will + V1 (will win) represents an open real condition.",
        "memory_tip": "Conditional rule: If + V1, will + V1 = First Conditional (probable condition)."
    },
    554: {
        "hint": "The clause 'which is badly needed' modifies the preceding noun 'money'.",
        "memory_tip": "Clause type: A clause modifying a noun is an Adjective (Relative) Clause."
    },
    555: {
        "hint": "The clause 'what he says' functions as the direct object of the verb 'believe'.",
        "memory_tip": "Clause type: A clause functioning as subject or object of a verb is a Noun Clause."
    },
    556: {
        "hint": "Functions as the object of the verb.",
        "memory_tip": "Noun Clause acts as the object of the main verb."
    },
    557: {
        "hint": "Modifies the noun immediately preceding it.",
        "memory_tip": "Adjective Clause qualifies a noun or pronoun."
    },
    558: {
        "hint": "Tells time, reason, condition, or manner of the main verb.",
        "memory_tip": "Adverb Clause answers when, where, why, or how the action occurred."
    },
    559: {
        "hint": "Modifies the verb indicating time or condition.",
        "memory_tip": "Adverb Clause modifies a verb, adjective, or adverb."
    },
    560: {
        "hint": "Begins with relative pronoun and describes an antecedent noun.",
        "memory_tip": "Adjective Clause describes an antecedent noun."
    },
    561: {
        "hint": "Acts as the object or complement of the verb.",
        "memory_tip": "Noun Clause completes the meaning of the transitive verb."
    },
    562: {
        "hint": "Acts as the direct object of the verb.",
        "memory_tip": "Noun Clause answers 'What?' after the verb."
    },
    563: {
        "hint": "Relative clause giving information about a person or thing.",
        "memory_tip": "Adjective Clause functions like an adjective qualifying a noun."
    },
    564: {
        "hint": "Indicates the circumstance, condition, or cause of the action.",
        "memory_tip": "Adverb Clause provides circumstantial context (cause, time, place)."
    },
    565: {
        "hint": "Indicates time or reason modifying the predicate.",
        "memory_tip": "Adverb Clause functions as an adverbial modifier."
    },
    566: {
        "hint": "Specifies when or under what condition the action takes place.",
        "memory_tip": "Adverb Clause of time/condition."
    },
    567: {
        "hint": "Shows reason, condition, or time of the main action.",
        "memory_tip": "Adverb Clause modifies the main clause verb."
    },
    568: {
        "hint": "Answers 'what' was said, thought, or believed.",
        "memory_tip": "Noun Clause functions as object of reporting/thinking verb."
    },
    569: {
        "hint": "Describes or identifies the noun that comes right before it.",
        "memory_tip": "Adjective Clause functions as a post-modifier for a noun."
    },
    570: {
        "hint": "Qualifies the antecedent noun in the main clause.",
        "memory_tip": "Adjective Clause (Relative Clause) qualifies the antecedent."
    },
    571: {
        "hint": "Acts as the subject or object clause.",
        "memory_tip": "Noun Clause replaces a noun phrase."
    },
    572: {
        "hint": "Introduced by a relative pronoun describing a person or object.",
        "memory_tip": "Adjective Clause describes an antecedent."
    },
    573: {
        "hint": "Functions as the object of the verb.",
        "memory_tip": "Noun Clause acts as the complement/object."
    },
    574: {
        "hint": "Completes the transitive verb as its object.",
        "memory_tip": "Noun Clause functions as direct object."
    },
    575: {
        "hint": "Relative clause that tells us which person or thing is meant.",
        "memory_tip": "Adjective Clause modifies the preceding noun."
    },
    576: {
        "hint": "Tells when, where, why, or how the event took place.",
        "memory_tip": "Adverb Clause modifies the action of the verb."
    },

    # Topic 25: Punctuation & Capitalization (Q577 - Q600)
    577: {
        "hint": "The pronoun 'I' is always capitalized, and days of the week begin with capital letters.",
        "memory_tip": "Capitalization: 'I' is always uppercase; days of the week (Monday) start with a capital."
    },
    578: {
        "hint": "Titles of films/books are enclosed in quotation marks and capitalized.",
        "memory_tip": "Punctuation: Proper names and movie titles ('The Lion King') require initial capitals."
    },
    579: {
        "hint": "Two complete sentences must be separated by a full stop and followed by a capital letter.",
        "memory_tip": "Punctuation: End complete thoughts with a period (.) and start next sentence with a capital."
    },
    580: {
        "hint": "Proper noun of city 'Vijayawada' must start with a capital letter and end with a full stop.",
        "memory_tip": "Punctuation: City names are Proper Nouns and must be capitalized."
    },
    581: {
        "hint": "Direct speech begins with a comma before the opening quotes and ends with a period inside.",
        "memory_tip": "Direct speech rule: Comma after reporting verb + opening quotation marks + capital letter."
    },
    582: {
        "hint": "Indirect questions end with a full stop (period), not a question mark.",
        "memory_tip": "Punctuation: Reported/indirect questions end with a full stop, never a question mark."
    },
    583: {
        "hint": "Items in a list must be separated by commas.",
        "memory_tip": "Punctuation: Commas are required between series of list items (peas, carrots, beans and...)."
    },
    584: {
        "hint": "Check correct use of comma before quotation and quotation marks enclosing direct words.",
        "memory_tip": "Punctuation: Mahita said to Lakshmi, “You are late.”"
    },
    585: {
        "hint": "Series of items separated by commas with 'and' before the last item.",
        "memory_tip": "Punctuation: Comma series: 'apples, grapes and nuts.'."
    },
    586: {
        "hint": "Multiple items listed with commas separating them.",
        "memory_tip": "Punctuation: 'knives, forks, spoons and glasses.'."
    },
    587: {
        "hint": "Exclamatory sentence ending with an exclamation mark (!).",
        "memory_tip": "Punctuation: Exclamatory sentences must end with an exclamation mark (!)."
    },
    588: {
        "hint": "Comma placed inside quotation marks before the attribution.",
        "memory_tip": "Punctuation: “We're too late,” Hemanth said."
    },
    589: {
        "hint": "Quotation ends with question mark inside the quotation marks.",
        "memory_tip": "Punctuation: Direct question inside quotes retains question mark."
    },
    590: {
        "hint": "'It's' requires an apostrophe for contraction of 'it is'.",
        "memory_tip": "Punctuation: 'It's' = It is (apostrophe of contraction)."
    },
    591: {
        "hint": "Possessive apostrophe after plural noun 'children' is 'children's'.",
        "memory_tip": "Punctuation: Irregular plurals without 's' take '’s' for possession (children's books)."
    },
    592: {
        "hint": "Exclamation mark inside quotation marks expressing sudden wonder.",
        "memory_tip": "Punctuation: “How beautiful this child is!” Geeta exclaimed."
    },
    593: {
        "hint": "Names of specific individuals (Babu, Swamy) must begin with capital letters.",
        "memory_tip": "Capitalization: All proper names of persons begin with uppercase letters."
    },
    594: {
        "hint": "Both first name and surname of a person must be capitalized.",
        "memory_tip": "Capitalization: First name and surname are capitalized (Virat Kohli)."
    },
    595: {
        "hint": "Brand names and proper nouns are capitalized.",
        "memory_tip": "Capitalization: Commercial brand names (Samsung) must be capitalized."
    },
    596: {
        "hint": "Title of famous artwork and artist name are capitalized.",
        "memory_tip": "Capitalization: Famous art titles (Mona Lisa) and historical names (Da Vinci) take capitals."
    },
    597: {
        "hint": "Months of the year and states begin with capital letters.",
        "memory_tip": "Capitalization: Months (May) and State names (Andhra Pradesh) are capitalized."
    },
    598: {
        "hint": "Proper names of people and nations begin with capital letters.",
        "memory_tip": "Capitalization: Person names and country names (India) take initial capitals."
    },
    599: {
        "hint": "Names of cities and states require capital initial letters.",
        "memory_tip": "Capitalization: Geographical locations (Amaravati, Andhra Pradesh) take capitals."
    },
    600: {
        "hint": "Sentence start, acronyms (TET), and month names (October) take capital letters.",
        "memory_tip": "Capitalization: First word, acronyms, and months are capitalized."
    }
}
