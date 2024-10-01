# Text Annotator

**Text Annotator** is a Python tool designed to search through text files for specified strings based on customizable matching rules. It generates an HTML output with color-coded annotations, making it easy to visualize and differentiate the identified words according to their respective categories.

## 📄 Table of Contents

- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Configuration](#-configuration)
- [Example](#-example)
- [Output](#-output)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

- **Configurable Search Lists:** Define multiple lists of strings, each with its own matching rules and color coding.
- **Flexible Matching Types:**
  - **Full Word Match:** Matches entire words using word boundaries.
  - **Substring Match:** Matches any occurrence of the string within words.
  - **Not at Beginning of Word:** Matches strings that do not start at a word boundary.
- **Color-Coded Annotations:** Generates an HTML file with colored lines to differentiate annotations based on their categories.
- **HTML Output:** Preserves text alignment and formatting using HTML's `<pre>` and `<span>` tags.
- **Efficient Processing:** Handles large text files by reading and processing them line by line.

## 🛠 Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/hafdon/python-braille-string-search.git
   cd python-braille-string-search
   ```

2. **Create a Virtual Environment (Optional but Recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   This project relies only on Python's standard library, so no additional packages are required.

## 🚀 Usage

1. **Prepare Your Text File:**

   Ensure you have a text file (e.g., `sample.txt`) that you want to annotate.

2. **Configure the Search Lists:**

   Open the `config.py` script and modify the `array_of_lists` variable to define your search strings, matching rules, and colors.

3. **Run the Script:**

   ```bash
   python annotate.py
   ```

4. **View the Output:**

   After running, an `output.html` file will be generated in the repository directory. Open this file in your web browser to view the annotated text.

## 📝 Configuration

The core of the tool is the `array_of_lists` variable within the `annotate.py` script. This array allows you to define multiple lists, each with its own set of strings, matching type, and annotation color.

### **Structure:**

```python
array_of_lists = [
    {
        "strings": ["string1", "string2"],
        "match_type": "full_word",  # Options: 'full_word', 'substring', 'not_beginning'
        "color": "red"
    },
    {
        "strings": ["string3", "string4"],
        "match_type": "substring",
        "color": "blue"
    },
    # Add more lists as needed
]
```

### **Parameters:**

- **`strings`:** A list of strings to search for in the text.
- **`match_type`:** Defines how the search is performed.
  - **`full_word`:** Matches entire words using word boundaries (`\b` in regex).
  - **`substring`:** Matches any occurrence of the string within words.
  - **`not_beginning`:** Matches strings that do not start at a word boundary.
- **`color`:** The color used to highlight the matched strings in the HTML output. Accepts any valid CSS color value (e.g., `"red"`, `"#FF5733"`, `"rgb(255,0,0)"`).

### **Example Configuration:**

```python
array_of_lists = [
    {
        "strings": ["dog", "cat"],
        "match_type": "full_word",
        "color": "red"
    },
    {
        "strings": ["ever", "father"],
        "match_type": "substring",
        "color": "blue"
    },
    {
        "strings": ["here", "there"],
        "match_type": "not_beginning",
        "color": "green"
    }
]
```

## 📖 Example

### **Input (`sample.txt`):**

```
The Dogged reporter ever wanted to father heretics here there.
A cat and a dog were here to see the heretics.
```

### **Configuration:**

```python
array_of_lists = [
    {
        "strings": ["dog", "cat"],
        "match_type": "full_word",
        "color": "red"
    },
    {
        "strings": ["ever", "father"],
        "match_type": "substring",
        "color": "blue"
    },
    {
        "strings": ["here", "there"],
        "match_type": "not_beginning",
        "color": "green"
    }
]
```

### **Generated `output.html`:**

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
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
    <div class="original">
      The Dogged reporter ever wanted to father heretics here there.
    </div>
    <div>dog</div>
    <div>ever father</div>
    <div>here there</div>
    <div class="original">A cat and a dog were here to see the heretics.</div>
    <div>cat dog</div>
    <div>here</div>
    <div>heretics</div>
  </body>
</html>
```

**Rendered Output:**

![Sample Output Screenshot](https://i.imgur.com/VqZtVPR.png)

_(The image shows the original lines with annotated lines colored accordingly.)_

## 📂 Output

The script generates an `output.html` file with the following structure:

- **Original Lines:** Displayed in black.
- **Annotated Lines:** Each corresponding to a configured list, with matched words colored based on their assigned colors.

### **HTML Structure:**

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
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
    <div class="original">Original text line here.</div>
    <div><span style="color:red;">matched_word</span>...</div>
    <div><span style="color:blue;">matched_word</span>...</div>
    <div><span style="color:green;">matched_word</span>...</div>
    <!-- More lines as needed -->
  </body>
</html>
```

## 🤝 Contributing

Contributions are welcome! If you'd like to enhance the functionality, fix bugs, or improve documentation, please follow these steps:

1. **Fork the Repository**
2. **Create a New Branch:**

   ```bash
   git checkout -b feature/YourFeatureName
   ```

3. **Commit Your Changes:**

   ```bash
   git commit -m "Add your message here"
   ```

4. **Push to the Branch:**

   ```bash
   git push origin feature/YourFeatureName
   ```

5. **Open a Pull Request**

Please ensure your contributions adhere to the project's coding standards and include appropriate documentation.

## 📝 License

This project is licensed under the [MIT License](LICENSE).
