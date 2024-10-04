# Function to compile regex patterns based on match_type
import re


def compile_patterns(array_of_lists):
    compiled = []
    for lst in array_of_lists:
        patterns = []
        for entry in lst["strings"]:
            if isinstance(entry, dict):
                actual_word = entry.get("word")
                dots = entry.get("dots")
            else:
                actual_word = entry
                dots = None

            if lst["match_type"] == "full_word":
                # Match whole words using word boundaries
                pattern = re.compile(
                    r"\b" + re.escape(actual_word) + r"\b", re.IGNORECASE
                )
            elif lst["match_type"] == "substring":
                # Match any occurrence of the substring
                pattern = re.compile(re.escape(actual_word), re.IGNORECASE)
            elif lst["match_type"] == "not_beginning":
                # Match substrings not at the beginning of a word
                pattern = re.compile(r"(?<!\b)" + re.escape(actual_word), re.IGNORECASE)
            else:
                # Default to substring match if unspecified
                pattern = re.compile(re.escape(actual_word), re.IGNORECASE)

            patterns.append((actual_word, pattern, dots))

        # Retrieve the 'style' key if it exists, else default to an empty list
        styles = lst.get("style", [])
        if isinstance(styles, str):
            styles = [styles]  # Convert to list if a single string is provided

        # Retrieve the 'line_identifier' key if it exists, else default to an empty string
        line_identifier = lst.get("line_identifier", "")

        compiled.append(
            {
                "patterns": patterns,
                "color": lst["color"],
                "styles": styles,  # Add styles to the compiled list
                "line_identifier": line_identifier,  # Add line_identifier to the compiled list
            }
        )
    return compiled
