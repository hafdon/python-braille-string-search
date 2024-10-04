import argparse
import html

from config import HTML_FOOTER, HTML_HEADER, array_of_lists

from utils.compile_patterns import compile_patterns
from utils.create_annotated_line import create_annotated_line
from utils.find_matches import find_matches


# Main function to process the file and generate HTML output
# The bulk of the work is done by `compile_patterns` and `create_annotated_line`
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

    #####
    #####

    # Create regex patterns passed on configurations
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

            # Create a for loop with "line" as index
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
