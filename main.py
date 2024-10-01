import re

# Define the array of lists containing strings to search for
from config import array_of_lists

# Compile regex patterns for each list for efficiency
# Each sublist in array_of_lists has its own dictionary of patterns
compiled_patterns = []
for sublist in array_of_lists:
    patterns = {s: re.compile(re.escape(s), re.IGNORECASE) for s in sublist}
    compiled_patterns.append(patterns)


# Function to find matches for a specific sublist in a given line
def find_matches(line, patterns):
    matches = []
    for s, pattern in patterns.items():
        for match in pattern.finditer(line):
            start_index = match.start()
            matched_substring = match.group(0)
            matches.append((start_index, s))
    # Sort matches based on starting index
    matches.sort(key=lambda x: x[0])
    return matches


# Function to create an annotated line with identified words aligned
def create_words_line(line, matches):
    # Initialize a list of spaces
    words_line = [" " for _ in line]

    for start, word in matches:
        # Place the word starting at the start index
        for i, char in enumerate(word):
            if start + i < len(words_line):
                # To handle overlapping, only place the first character if space is empty
                if words_line[start + i] == " ":
                    words_line[start + i] = word[i]
                else:
                    # If there's already a character, you can choose to overwrite or skip
                    # Here, we'll skip to prevent overlapping
                    pass
    return "".join(words_line)


# Main function to read the input file and write to the output file
def main():
    input_file = "sample.txt"  # Replace with your input file path
    output_file = "output.txt"  # Replace with your desired output file path

    try:
        with open(input_file, "r", encoding="utf-8") as infile, open(
            output_file, "w", encoding="utf-8"
        ) as outfile:

            for line_number, line in enumerate(infile, start=1):
                # Remove any trailing newline characters
                line = line.rstrip("\n")

                # Write the original line to the output file
                outfile.write(line + "\n")

                # For each sublist in array_of_lists, find matches and write annotated line
                for patterns in compiled_patterns:
                    matches = find_matches(line, patterns)
                    words_line = create_words_line(line, matches)
                    # Only write the words_line if any matches were found
                    if any(word_line.strip() for word_line in [words_line]):
                        outfile.write(words_line + "\n")

                # Optionally, add a blank line for readability between original lines
                # outfile.write('\n')

        print(f"Processing complete. Output written to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
