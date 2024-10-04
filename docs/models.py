from typing import TypedDict, List, Literal, Union, Dict


# Exception format for specific cases
class ExceptionType(TypedDict):
    one: List[str]


# Format for objects that have "dots" attribute
class WordWithDots(TypedDict):
    word: str
    dots: str


# Main structure for each entry in the array
class Entry(TypedDict, total=False):
    line_identifier: (
        str  # Identifier for the line (e.g., "Full words only", "[5+]", etc.)
    )
    match_type: Literal[
        "full_word", "substring", "not_beginning"
    ]  # Defines matching criteria
    color: Literal[
        "fuchsia", "green", "blue", "red", "orange"
    ]  # Color coding for the entry
    strings: List[
        Union[str, WordWithDots]
    ]  # List of words or objects with word and dots info
    style: str  # Optional styling for the entry (e.g., "strikethrough")
    exeptions: List[
        ExceptionType
    ]  # Exceptions list if any (applicable for specific cases)


# The complete structure is an array of entries
ArrayOfLists = List[Entry]
