from config import SEPARATOR
from utils.styles_to_css import styles_to_css


import html

# Function to create an annotated line with colored and styled words


def create_annotated_line(line, matches, color, styles):
    # Initialize the annotated_line with SEPARATORs
    annotated_line = [SEPARATOR for _ in line]

    # Replace SEPARATORs with actual characters for matched words
    for match in matches:
        start, matched_text, word, dots = match
        end = start + len(matched_text)
        for i in range(start, end):
            if i < len(annotated_line):
                annotated_line[i] = line[i]

    # Build the HTML annotated line with colored and styled spans
    annotated_html = ""
    i = 0
    while i < len(line):
        char = annotated_line[i]
        if char != SEPARATOR:
            # Find the full span of the word
            start = i
            word_chars = []
            while i < len(line) and annotated_line[i] != SEPARATOR:
                word_chars.append(annotated_line[i])
                i += 1
            word = "".join(word_chars)

            # Find the corresponding dots for this word
            # Assuming matches are sorted and non-overlapping
            dots = None
            for match in matches:
                match_start, matched_text, _, match_dots = match
                if match_start == start:
                    dots = match_dots
                    break

            # Escape HTML characters
            word_escaped = html.escape(word)

            # Build the style string
            style_string = f"color:{color}; {styles_to_css(styles)}"

            # Wrap the word in a styled span with tooltip if dots exist
            if dots:
                # annotated_html += f'<span style="{style_string}" title="{html.escape(dots)}">{word_escaped}</span>'
                span = (
                    f'<span class="tooltip" style="{style_string}">'
                    f"{word_escaped}"
                    f'<span class="tooltiptext">{html.escape(dots)}</span>'
                    f"</span>"
                )

            else:
                # annotated_html += f'<span style="{style_string}">{word_escaped}</span>'
                span = f'<span style="{style_string}">{word_escaped}</span>'
            annotated_html += span

        else:
            # Replace non-matched characters with SEPARATOR
            annotated_html += SEPARATOR
            i += 1
    return annotated_html
