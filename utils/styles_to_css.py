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
