# # Define the array of lists with configuration for each list
# array_of_lists = [
#     {
#         "strings": ["dog", "cat"],
#         "match_type": "full_word",  # Options: 'full_word', 'substring', 'not_beginning'
#         "color": "red",
#     },
#     {"strings": ["ever", "father"], "match_type": "substring", "color": "blue"},
#     {"strings": ["here", "there"], "match_type": "not_beginning", "color": "green"},
# ]

# Define the list of strings to search for
array_of_lists = [
    {
        "match_type": "substring",
        "color": "red",
        "strings": [
            "day",
            "ever",
            "father",
            "here",
            "know",
            "lord",
            "mother",
            "nam",
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
    },
    {
        # 45+
        "match_type": "full_word",
        "color": "red",
        "strings": ["upon", "word", "those", "whose", "these"],
    },
    {
        "match_type": "full_word",
        "color": "green",
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
        "match_type": "substring",
        "color": "blue",
        "strings": ["the", "and", "of", "with", "for"],
    },
    {
        "match_type": "not_beginning",
        "color": "purple",
        "strings": [
            "ound",
            "ance",
            "sion",
            "less",
            "ount",
            "ence",
            "ong",
            "ful",
            "tion",
            "ness",
            "ment",
            "ity",
        ],
    },
    {
        ###
        # SHORTFORMS used in braille.
        #
        # - With a few exceptions, shortforms can be used as both whole words and parts of longer words.
        # - Most shotforms can only be used within a longer word if the longer word is:
        #   - standing alone
        #   - appears on a definitive list of permitted words
        # - Do not use shortforms as partsof words if their use would violate a basic contraction rule.
        ###
        "match_type": "substring",
        "color": "black",
        "strings": [
            "about",
            "above",
            "according",
            "across",
            "also",
            "almost",
            "always",
            "braille",
            "first",
            "good",
            "great",
            "immediate",
            "letter",
            "little",
            "must",
            "necessary",
            "paid",
            "perhaps",
            "quick",
            "said",
            "children",
            "because",
            "below",
        ],
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
        ],
    },
    {
        "match_type": "substring",
        "color": "pink",
        "strings": ["dis", "con"],
    },
]
