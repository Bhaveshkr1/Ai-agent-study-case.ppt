def summarize_text(text):
    return text[:50] + "..." if len(text) > 50 else text
