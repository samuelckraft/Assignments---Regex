#Task 1
import re

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"

def extract(text,key):
    pattern = r"\b" + key + r":\s*([^;]+)"

    match = re.search(pattern, text)
    if match:
        return match.group(1)
    else:
        return None

print(extract(text, "Occupation"))