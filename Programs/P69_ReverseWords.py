(
def reverse_words(text):
    words = text.split()
    if not words:
        return ""
    return ' '.join(words[::-1])
|
def reverse_words(text):
    parts = text.split()
    if len(parts) == 0:
        return ""
    return ' '.join(reversed(parts))
)
