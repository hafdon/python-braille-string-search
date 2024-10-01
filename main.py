import re
import html

from config import array_of_lists


# Function to compile regex patterns based on match_type
def compile_patterns(array_of_lists):
    compiled = []
    for lst in array_of_lists:
        patterns = []
        for word in lst["strings"]:
            if lst["match_type"] == "full_word":
                # Match whole words using word boundaries
                pattern = re.compile(r"\b" + re.escape(word) + r"\b", re.IGNORECASE)
            elif lst["match_type"] == "substring":
                # Match any occurrence of the substring
                pattern = re.compile(re.escape(word), re.IGNORECASE)
            elif lst["match_type"] == "not_beginning":
                # Match substrings not at the beginning of a word
                pattern = re.compile(r"(?<!\b)" + re.escape(word), re.IGNORECASE)
            else:
                # Default to substring match if unspecified
                pattern = re.compile(re.escape(word), re.IGNORECASE)
            patterns.append((word, pattern))

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


# Function to find matches in a line for a specific list
def find_matches(line, compiled_list):
    matches = []
    for word, pattern in compiled_list["patterns"]:
        for match in pattern.finditer(line):
            start = match.start()
            matched_text = match.group(0)
            matches.append((start, matched_text, word))
    # Sort matches by starting index
    matches.sort(key=lambda x: x[0])
    return matches


# Helper function to convert style keywords to CSS properties
def styles_to_css(styles):
    css_styles = []
    for style in styles:
        if style.lower() == "bold":
            css_styles.append("font-weight: bold;")
        elif style.lower() == "italics":
            css_styles.append("font-style: italic;")
        elif style.lower() == "strikethrough":
            css_styles.append("text-decoration: line-through;")
        # Add more styles here if needed
    return " ".join(css_styles)


# Function to create an annotated line with colored and styled words
def create_annotated_line(line, matches, color, styles):
    annotated_line = [" " for _ in line]  # Initialize with spaces

    for start, matched_text, word in matches:
        for i, char in enumerate(matched_text):
            if start + i < len(annotated_line):
                annotated_line[start + i] = matched_text[i]

    # Now, build the HTML annotated line with colored and styled spans
    annotated_html = ""
    i = 0
    while i < len(line):
        char = annotated_line[i]
        if char != " ":
            # Find the full span of the word
            start = i
            word_chars = []
            while i < len(line) and annotated_line[i] != " ":
                word_chars.append(annotated_line[i])
                i += 1
            word = "".join(word_chars)
            # Escape HTML characters
            word_escaped = html.escape(word)
            # Build the style string
            style_string = f"color:{color}; {styles_to_css(styles)}"
            # Wrap the word in a styled span
            annotated_html += f'<span style="{style_string}">{word_escaped}</span>'
        else:
            # Preserve spaces using non-breaking spaces for HTML
            annotated_html += " "
            i += 1
    return annotated_html


# Main function to process the file and generate HTML output
def main():
    input_file = "sample.txt"  # Replace with your input file path
    output_file = "output.html"  # Replace with your desired output file path

    compiled_lists = compile_patterns(array_of_lists)

    # Determine the maximum identifier length for consistent width
    max_identifier_length = max(
        (len(lst["line_identifier"]) for lst in compiled_lists), default=0
    )
    # Estimate width based on character count (assuming monospace font)
    identifier_width = max(
        150, max_identifier_length * 10
    )  # Adjust multiplier as needed

    # HTML Header and Styles using CSS Grid
    html_header = f"""<!DOCTYPE html>
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
            line-height: 1; /* Adjust line height as needed */
        }}
    </style>
</head>
<body>
"""
    html_footer = """
</body>
</html>
"""

    try:
        with open(input_file, "r", encoding="utf-8") as infile, open(
            output_file, "w", encoding="utf-8"
        ) as outfile:

            # Write the HTML header
            outfile.write(html_header)

            for line_number, line in enumerate(infile, start=1):
                # Remove trailing newline characters
                line = line.rstrip("\n")
                # Escape HTML special characters
                line_escaped = html.escape(line)

                # Write the original line with an empty identifier
                outfile.write(
                    f'<div class="original"><span class="identifier"></span>'
                    f'<span class="original-content">{line_escaped}</span></div>\n'
                )

                # For each configured list, find matches and write annotated line
                for compiled_list in compiled_lists:
                    matches = find_matches(line, compiled_list)
                    if matches:
                        annotated_html = create_annotated_line(
                            line,
                            matches,
                            compiled_list["color"],
                            compiled_list.get("styles", []),
                        )
                        # Prepare the identifier for this list
                        identifier = compiled_list["line_identifier"]
                        identifier_html = (
                            f'<span class="identifier">{html.escape(identifier)}</span>'
                        )
                        # Write the annotated line with its identifier
                        outfile.write(
                            f'<div class="annotated">{identifier_html}'
                            f'<span class="annotated-content">{annotated_html}</span></div>\n'
                        )

                # Optional: Add a blank line for readability between original lines
                # outfile.write('<div>&nbsp;</div>\n')

            # Write the HTML footer
            outfile.write(html_footer)

        print(f"Processing complete. Output written to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
