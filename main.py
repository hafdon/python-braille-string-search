import re

# Define the list of strings to search for
from config import strings_to_look_for

# Compile regex patterns for each string for efficiency
patterns = {s: re.compile(re.escape(s), re.IGNORECASE) for s in strings_to_look_for}


# Function to search for strings in a given line and record their positions
def find_matches(line):
    matches = []
    for s, pattern in patterns.items():
        for match in pattern.finditer(line):
            start_index = match.start()
            matched_substring = match.group(0)
            matches.append((start_index, s))
    # Sort matches based on starting index to handle alignment properly
    matches.sort(key=lambda x: x[0])
    return matches


# Function to create the annotated line with identified words aligned
def create_annotated_line(line, matches):
    # Initialize a list of spaces
    annotated = [" " for _ in line]

    for start, word in matches:
        # Insert the word at the starting index
        # Ensure that we don't go out of bounds
        for i, char in enumerate(word):
            if start + i < len(annotated):
                annotated[start + i] = char if char != " " else " "
    # Join the list into a string
    annotated_line = "".join(annotated)

    # Now, to list the words under their positions, we can place them starting at their start indices
    # To make the words readable, we can overwrite the spaces with the word, separated by spaces
    # Alternatively, list the words separated by tabs or specific spacing
    # Here, we'll place each word at its starting position
    # To prevent overlapping, we'll skip positions already filled
    word_line = [" " for _ in line]
    for start, word in matches:
        for i, char in enumerate(word):
            if start + i < len(word_line):
                word_line[start + i] = word[i]
    return "".join(word_line)


# Alternative approach: Instead of overlapping characters, list the words with spaces aligned to their start positions
def create_words_line(line, matches):
    # Initialize a list of spaces
    words_line = [" " for _ in line]

    for start, word in matches:
        # Place the word starting at the start index
        for i, char in enumerate(word):
            if start + i < len(words_line):
                words_line[start + i] = word[i]
    return "".join(words_line)


def create_words_line_separated(line, matches):
    # Initialize a list of spaces
    words_line = [" " for _ in line]

    for start, word in matches:
        # Place the word starting at the start index
        for i, char in enumerate(word):
            if start + i < len(words_line):
                words_line[start + i] = word[i]
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

                # Find all matches in the line
                matches = find_matches(line)

                # Create the words line with identified words aligned
                words_line = create_words_line(line, matches)

                # Write the original line and the words line to the output file
                outfile.write(line + "\n")
                outfile.write(words_line + "\n")

        print(f"Processing complete. Output written to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

# Compile regex patterns for each string for efficiency
# The regex is case-insensitive and uses word boundaries to match substrings within words
patterns = {s: re.compile(re.escape(s), re.IGNORECASE) for s in strings_to_look_for}


# Function to search for strings in a given line
def search_line(line, line_number):
    found = []
    for s, pattern in patterns.items():
        # Find all non-overlapping matches in the line
        matches = pattern.finditer(line)
        for match in matches:
            # Extract the exact substring from the line where the match was found
            matched_substring = match.group(0)
            found.append((s, matched_substring))
    if found:
        print(f"Line {line_number}:")
        for s, substr in found:
            print(f'  "{s}" found in "{substr}"')
        print()  # Add a blank line for readability


# Main function to read the file and process each line
def main():
    file_path = "sample.txt"  # Replace with your file path
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for idx, line in enumerate(file, start=1):
                # Remove any trailing newline characters
                line = line.rstrip("\n")
                search_line(line, idx)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")


if __name__ == "__main__":
    main()
