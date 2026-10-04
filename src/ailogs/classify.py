import re

OOM = {"oom", "killed"}
TIMEOUT = {"timeout", "deadline"}
AUTH = {"401", "403", "unauthorized"}


class InputError(ValueError):
    pass


def classify(text):
    if not isinstance(text, str) or not text.strip():
        raise InputError("Text is empty.")
    tokens = re.findall(r"[a-z0-9]+", text.lower())
    counts = {}
    counts['oom'] = sum(token in OOM for token in tokens)
    counts['timeout'] = sum(token in TIMEOUT for token in tokens)
    counts['auth'] = sum(token in AUTH for token in tokens)
    label = max(counts, key=lambda name: (counts[name], name))
    if all(value == 0 for value in counts.values()):
        label = "unknown"
    return {"label": label, "counts": counts, "tokens": len(tokens)}
