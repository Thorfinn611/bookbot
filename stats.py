def read_text(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def count_words(filepath: str) -> int:
    text = read_text(filepath)
    return len(text.split())  # simple whitespace tokenization

def char_counts(filepath: str) -> dict[str, int]:
    """
    Counts only alphabetic characters (Unicode-aware).
    """
    text = read_text(filepath).lower()
    counts: dict[str, int] = {}
    for ch in text:
        if ch.isalpha():  # keeps a–z and letters like æ, â, ê, etc.
            counts[ch] = counts.get(ch, 0) + 1
    return counts

def sort_on(item: dict) -> int:
    return item["num"]

def char_sort(counts: dict[str, int]) -> list[dict]:
    # Return a list of {"char": <letter>, "num": <count>} sorted by count (desc)
    items = [{"char": ch, "num": n} for ch, n in counts.items()]
    items.sort(reverse=True, key=sort_on)
    return items

