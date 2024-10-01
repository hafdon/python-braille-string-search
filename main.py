import re
import html

from config import array_of_lists


# Function to compile regex patterns based on match_type
def compile_patterns(array_of_lists):
    compiled = []
    for lst in array_of_lists:
        patterns = []
        print(lst)
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
        compiled.append({"patterns": patterns, "color": lst["color"]})
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


# Function to create an annotated line with colored words
def create_annotated_line(line, matches, color):
    annotated_line = [" " for _ in line]  # Initialize with spaces
    spans = []  # To store span information

    for start, matched_text, word in matches:
        for i, char in enumerate(matched_text):
            if start + i < len(annotated_line):
                annotated_line[start + i] = matched_text[i]

    # Now, build the HTML annotated line with colored spans
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
            # Wrap the word in a colored span
            annotated_html += f'<span style="color:{color};">{word_escaped}</span>'
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

    # HTML Header and Styles
    html_header = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Annotated Text Output</title>
    <style>
        body {
            font-family: monospace;
            white-space: pre;
        }
        .original {
            color: black;
        }
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

                # Write the original line
                outfile.write(f'<div class="original">{line_escaped}</div>\n')

                # For each configured list, find matches and write annotated line
                for compiled_list in compiled_lists:
                    matches = find_matches(line, compiled_list)
                    if matches:
                        annotated_html = create_annotated_line(
                            line, matches, compiled_list["color"]
                        )
                        outfile.write(f"<div>{annotated_html}</div>\n")

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
