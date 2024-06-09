import re
#Check if the string starts with "The" and ends with "Spain":
"""

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")

"""

import re

def main():
    # Example string
    text = "The quick brown lion jumps over the lazy dog 1234567890"

    match = re.search(r'lion', text)
    if match:
        print("re.search() found:", match.group())

    match = re.match(r'The', text)
    if match:
        print("re.match() found:", match.group())

    matches = re.findall(r'\d', text)
    print("re.findall() found:", matches)

    matches_iter = re.finditer(r'\d', text)
    print("re.finditer() found:")
    for match in matches_iter:
        print(match.group())

    new_text = re.sub(r'\d', 'X', text)
    print("re.sub() result:", new_text)

    tokens = re.split(r'\s+', text)
    print("re.split() result:", tokens)

if __name__ == "__main__":
    main()

"""
re.search(): Searches for the first occurrence of a pattern within a string.
re.match(): Attempts to match the pattern at the beginning of the string.
re.findall(): Finds all occurrences of a pattern in a string and returns a list of all matches.
re.finditer(): Finds all occurrences of a pattern in a string and returns an iterator of match objects.
re.sub(): Replaces occurrences of a pattern in a string with a specified replacement.
re.split(): Splits a string by occurrences of a pattern into a list of substrings.
"""