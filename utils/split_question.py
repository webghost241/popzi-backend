import re

def extract_info(content, starter, ender):
    pattern = re.compile(rf"{starter}(.*?){ender}", re.S)
    matches = pattern.findall(content)
    return [match.strip() for match in matches]


def split_options(question):
    parts = re.split(r"\n(A\)|B\)|C\)|D\))", question)
    question_text = parts[0].strip()
    options = parts[1:]
    # Combine option lead (e.g., "A)") with option text, considering options array is split into ['A)', 'option text', ...]
    options = [f"{options[i + 1]}" for i in range(0, len(options), 2)]
    return question_text, options


def split_index(sent):
    match = re.match('([A-Z]\\)) (.*)', sent)
    return match.group(2)