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
