# # Define the array of lists with configuration for each list
# array_of_lists = [
#     {
#         "strings": ["error", "fail", "critical"],
#         "match_type": "full_word",
#         "color": "red",
#         "style": ["bold", "strikethrough"]  # Applying multiple styles
#     },
#     {
#         "strings": ["warning", "caution"],
#         "match_type": "substring",
#         "color": "orange",
#         "style": "italics"  # Single style as a string
#     },
#     {
#         "strings": ["info", "note"],
#         "match_type": "substring",
#         "color": "blue"
#         # No style applied
#     }
# ]

SEPARATOR = "."

# HTML Header and Styles using CSS Grid
HTML_HEADER = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Annotated Text Output</title>
    <style>
        body {{
            font-family: monospace;
            white-space: pre;
        }}
        .original, .annotated {{
            display: grid; /* Use CSS Grid for layout */
            grid-template-columns: 150px 1fr; /* Fixed width for identifier, flexible for content */
            align-items: flex-start; /* Align items at the start vertically */
            margin-bottom: 5px; /* Optional: Space between lines */
        }}
        .identifier {{
            text-align: right; /* Right-align the text within the identifier */
            font-weight: bold;
            padding-right: 10px; /* Space between identifier and content */
            white-space: nowrap; /* Prevent the identifier text from wrapping */
        }}
        .original-content {{
            color: black;
        }}
        .annotated-content {{
            margin: 0; /* Remove default margin */
            padding: 0; /* Remove default padding */
            line-height: .5; /* Adjust line height as needed */
        }}
    </style>
</head>
<body>
"""
HTML_FOOTER = """
</body>
</html>
"""

# Define the list of strings to search for
array_of_lists = [
    {
        ###
        # Single-letter
        # Has to be full word
        ###
        "line_identifier": "Full words only",
        "match_type": "full_word",
        "color": "fuchsia",
        "strings": [
            "but",
            "can",
            "do",
            "every",
            "from",
            "go",
            "have",
            "just",
            "knowledge",
            "like",
            "more",
            "not",
            "people",
            "quite",
            "rather",
            "so",
            "that",
            "us",
            "very",
            "will",
            "it",
            "you",
            "as",
            "child",
            "shall",
            "this",
            "which",
            "out",
            "still",
            "in",
            "enough",
            "his",
            "was",
            "be",
            "were",
        ],
    },
    {
        # 5+
        "line_identifier": "[5+]",
        "match_type": "substring",
        "color": "green",
        "strings": [
            "day",
            "ever",
            "father",
            "here",
            "know",
            "lord",
            "mother",
            "name",
            "one",
            "part",
            "question",
            "right",
            "some",
            "time",
            "under",
            "work",
            "young",
            "character",
            "through",
            "where",
            "ought",
            "there",
        ],
        "exeptions": [
            {
                "one":
                # Use the strong and loewr groupsigns in preference to the initial and final letter contractions
                # except as noted in (5) above (referring to "ence" groupsign) so long as the strong and lower groupsigns do not take up more space
                # e.g. telephon(ed) [not] teleph(one)d
                ["poisoned"]
            }
        ],
    },
    {
        # 45+
        "line_identifier": "[45+]",
        "match_type": "substring",
        "color": "green",
        "strings": ["upon", "word", "those", "whose", "these"],
    },
    {
        # 456+
        "line_identifier": "[456+]",
        "match_type": "substring",
        "color": "green",
        "strings": [
            {"word": "cannot", "dots": "14"},
            {"word": "had", "dots": "125"},
            "many",
            "spirit",
            "world",
            "their",
        ],
    },
    {
        # 46+
        # Cannot be at the beginning of a word
        "line_identifier": "[46+]",
        "match_type": "not_beginning",
        "color": "green",
        "strings": [
            "ound",
            "ance",
            "sion",
            "less",
            "ount",
        ],
    },
    {
        # 56+
        # Cannot be at the beginning of a word
        "match_type": "not_beginning",
        "line_identifier": "[56+]",
        "color": "green",
        "strings": ["ong", "ful", "tion", "ness", "ment", "ity", "ence"],
    },
    {
        "match_type": "substring",
        "color": "blue",
        "strings": ["the", "and", "of", "with", "for"],
    },
    {
        ###
        # These words contain shortforms, but they are brailled as though they do not have a shortform in them
        ###
        "match_type": "full_word",
        "color": "red",
        "style": "strikethrough",
        "strings": ["abouts", "almosts", "hims", "hims"],  # ab(ou)ts  # almo(st)s
    },
    {
        ###
        # the 75 SHORTFORMS used in braille.
        #
        # - With a few exceptions, shortforms can be used as both whole words and parts of longer words.
        # - Most shotforms can only be used within a longer word if the longer word is:
        #   - standing alone
        #   - appears on a definitive list of permitted words
        # - Do not use shortforms as partsof words if their use would violate a basic contraction rule.
        ###
        "match_type": "substring",
        "color": "red",
        "strings": [
            "about",
            "above",
            "according",
            "across",
            "after",
            "afternoon",
            "afterward",
            "again",
            "against",
            "almost",
            "already",
            "also",
            "although",
            "altogether",
            "always",
            "because",
            "before",
            "behind",
            "below",
            "beneath",
            "beside",
            "between",
            "beyond",
            "blind",
            "braille",
            "children",
            "conceive",
            "conceiving",
            "could",
            "deceive",
            "deceiving",
            "declare",
            "declaring",
            "either",
            "first",
            "friend",
            "good",
            "great",
            "herself",
            "him",
            "himself",
            "immediate",
            "its",
            "itself",
            "letter",
            "little",
            "much",
            "must",
            "myself",
            "necessary",
            "neither",
            "oneself",
            "ourselves",
            "paid",
            "perceive",
            "perceiving",
            "perhaps",
            "quick",
            "receive",
            "receiving",
            "rejoice",
            "rejoicing",
            "said",
            "should",
            "such",
            "themselves",
            "thyself",
            "today",
            "together",
            "tomorrow",
            "tonight",
            "would",
            "your",
            "yourself",
            "yourselves",
        ],
    },
    {
        ###
        # Allowed shortforms in longer words.
        # These are listed in Appendix 1 of Rules of Unified English Braille.
        # When a shortform is part of a longer word, add the longer word to
        # the Shortforms List provided that:
        # (a) the longer word retains an original meaning and the original
        # spelling of the shortform; and
        # (b) use of the shortform is not prohibited by rules 3–5 which follow
        ###
        "match_type": "full_word",
        "color": "red",
        "strings": [
            "aboutface",
            "aboutfaced",
            "aboutfacer",
            "aboutfacing",
            "aboutturn",
            "aboutturned",
            "aboveboard",
            "aboveground",
            "abovementioned",
            "accordingly",
            "afterbattle",
            "afterbirth",
            "afterbreakfast",
            "afterburn",
            "afterburned",
            "afterburner",
            "afterburning",
            "aftercare",
            "afterclap",
            "aftercoffee",
            "afterdamp",
            "afterdark",
            "afterdeck",
            "afterdinner",
            "afterflow",
            "aftergame",
            "afterglow",
            "afterguard",
            "afterhatch",
            "afterhatches",
            "afterhour",
            "afterlife",
            "afterlight",
            "afterlives",
            "afterlunch",
            "afterlunches",
            "aftermarket",
            "aftermatch",
            "aftermatches",
            "aftermath",
            "aftermeeting",
            "aftermidday",
            "aftermidnight",
            "aftermost",
            "afternoontea",
            "afterpain",
            "afterparties",
            "afterparty",
            "afterpiece",
            "afterplay",
            "aftersale",
            "afterschool",
            "aftersensation",
            "aftershave",
            "aftershock",
            "aftershow",
            "aftershower",
            "aftersupper",
            "aftertaste",
            "aftertax",
            "aftertaxes",
            "aftertea",
            "aftertheatre",
            "afterthought",
            "aftertime",
            "aftertreatment",
            "afterword",
            "afterwork",
            "afterworld",
            "beforehand",
            "behindhand",
            "belowdeck",
            "belowground",
            "belowmentioned",
            "beneathdeck",
            "beneathground",
            "betweendeck",
            "betweentime",
            "betweenwhile",
            "eastabout",
            "gadabout",
            "goodafternoon",
            "hereabout",
            "hereafter",
            "hereagain",
            "hereagainst",
            "hereinabove",
            "hereinafter",
            "hereinagain",
            "knockabout",
            "layabout",
            "midafternoon",
            "morningafter",
            "northabout",
            "readacross",
            "rightabout",
            "roundabout",
            "roustabout",
            "runabout",
            "southabout",
            "stirabout",
            "thereabout",
            "thereafter",
            "thereagain",
            "thereagainst",
            "thereinafter",
            "thereinagain",
            "turnabout",
            "unaccording",
            "unaccordingly",
            "walkabout",
            "westabout",
            "whereabout",
            "whereafter",
            "whereagain",
            "whereagainst",
            "whereinafter",
            "whereinagain",
        ],
    },
    {
        ###
        # Can only go at the beginning
        ###
        "match_type": "substring",
        "color": "orange",
        "strings": ["dis", "con"],
    },
    {
        "match_type": "substring",
        "color": "orange",
        "strings": [
            "ch",
            "sh",
            "th",
            "wh",
            "ou",
            "st",
            "in",
            "en",
            "be",
            "gh",
            "ar",
            "ed",
            "er",
            "ing",
            "ow",
            "bb",
            "gg",
            "ea",
            "ff",
            "cc",
        ],
    },
]
