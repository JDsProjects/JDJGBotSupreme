import os
import json
from .config import PROFANE_WORD_LIST_PATH

# Convert profane word list from json to array
with open(os.path.join(os.path.dirname(__file__), PROFANE_WORD_LIST_PATH), "r") as _profane_word_list:
    PROFANE_WORD_LIST = json.load(_profane_word_list)


def censor_profanity(text: str, censor: str = "*") -> str:
    """Censors all profane words with the provided censor"""

    split_text: list = text.split()
    final_text: str = " ".join(split_text)

    if len(split_text) < len(PROFANE_WORD_LIST):
        for word in split_text:
            if word.lower() in PROFANE_WORD_LIST:
                final_text = final_text.replace(word, censor * len(word))
    else:
        for word in PROFANE_WORD_LIST:
            if word in split_text:
                final_text = final_text.replace(word, censor * len(word))

    return final_text


def has_profanity(text: str) -> bool:
    """Checks if the text contains any profane content and returns a boolean accordingly"""

    split_text: list = text.lower().split()

    if len(split_text) < len(PROFANE_WORD_LIST):
        for word in split_text:
            if word.lower() in PROFANE_WORD_LIST:
                return True
    else:
        for word in PROFANE_WORD_LIST:
            if word in split_text:
                return True

    return False


def get_profanity(text: str, duplicates=False) -> list:
    """Gets all profane words and returns them in a list"""

    text: str = text.lower()
    additional: list = []
    profane: list = [word for word in PROFANE_WORD_LIST if word in text]
    if duplicates:
        for word in profane:
            c: int = text.count(word)
            if c > 1:
                x: list = [word for _ in range(c - 1)]
                additional.extend(list(x))
    profane.extend(additional)
    return profane
