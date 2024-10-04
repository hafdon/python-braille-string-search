import re
import argparse
import html

from config import HTML_FOOTER, HTML_HEADER, SEPARATOR, array_of_lists


# Function to compile regex patterns based on match_type
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


# Function to find matches in a line for a specific list
def find_matches(line, compiled_list):
    matches = []
    for word, pattern, dots in compiled_list["patterns"]:
        for match in pattern.finditer(line):
            start = match.start()
            matched_text = match.group(0)
            matches.append((start, matched_text, word, dots))
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
                annotated_html += f'<span style="{style_string}" title="{html.escape(dots)}">{word_escaped}</span>'
            else:
                annotated_html += f'<span style="{style_string}">{word_escaped}</span>'
        else:
            # Replace non-matched characters with SEPARATOR
            annotated_html += SEPARATOR
            i += 1
    return annotated_html


# Main function to process the file and generate HTML output
def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="Process input and output file paths.")

    # Add arguments for input and output files
    parser.add_argument("input_file", type=str, help="Path to the input file.")
    parser.add_argument("output_file", type=str, help="Path to the output file.")

    # Parse the arguments
    args = parser.parse_args()

    # Assign the arguments to variables
    input_file = args.input_file
    output_file = args.output_file

    # Now you can use input_file and output_file as needed
    print(f"Input File: {input_file}")
    print(f"Output File: {output_file}")

    compiled_lists = compile_patterns(array_of_lists)

    # Determine the maximum identifier length for consistent width
    max_identifier_length = max(
        (len(lst["line_identifier"]) for lst in compiled_lists), default=0
    )
    # Estimate width based on character count (assuming monospace font)
    identifier_width = max(
        150, max_identifier_length * 10
    )  # Adjust multiplier as needed

    try:
        with open(input_file, "r", encoding="utf-8") as infile, open(
            output_file, "w", encoding="utf-8"
        ) as outfile:

            # Write the HTML header
            outfile.write(HTML_HEADER)

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
                            f'<div class="annotated"><span class="identifier">{html.escape(identifier)}</span>'
                            f'<span class="annotated-content">{annotated_html}</span></div>\n'
                        )

                # Optional: Add a blank line for readability between original lines
                # outfile.write('<div>&nbsp;</div>\n')

            # Write the HTML footer
            outfile.write(HTML_FOOTER)

        print(f"Processing complete. Output written to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
