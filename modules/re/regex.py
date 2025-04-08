import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

# Function to print iterator
def find_matches(matches):
    for match in matches:
        print(match)
    print()

# The r string is the raw string, it will ignore the tab.
print(r'\tTab')
print()

# Compile method
pattern = re.compile(r'abc')  # This will search for this pattern. Case sensitive.
matches = pattern.finditer(text_to_search)  # Returns an iterator that returns all the matches
find_matches(matches)
print(text_to_search[1:4])

# To search for a period you must escape (MetaCharacters)
pattern = re.compile(r'\.')
matches = pattern.finditer(text_to_search)
find_matches(matches)

# To match a url you must escape the .
pattern = re.compile(r'coreyms\.com')
matches = pattern.finditer(text_to_search)
find_matches(matches)

# To match any digit use \d - see snippets.txt
pattern = re.compile(r'\d')
matches = pattern.finditer(text_to_search)
find_matches(matches)

# Anchors
# Using word boundaries
pattern = re.compile(r'\bHa') # This will match the word that has a word boundary (non-alphanumeric, before it)
matches = pattern.finditer(text_to_search)
find_matches(matches)

# Start of string (or end) - use ^ (or $)
pattern = re.compile(r'^Start') # This will match the word Start only if it is at the beginning of the string.
pattern_2 = re.compile(r'end$') # This will match the word end at the end of the string.
matches = pattern.finditer(sentence)
matches_2 = pattern_2.finditer(sentence)

find_matches(matches)
find_matches(matches_2)

# Find a phone number
pattern = re.compile(r'\d\d\d') # This will find three digits in a row
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') # The dot will match any character in between
matches = pattern.finditer(text_to_search)
find_matches(matches)

# Look for phone numbers in file
with open('data.txt', 'r') as f:
    contents = f.read()
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') # The dot will match any character in between
matches = pattern.finditer(contents)
find_matches(matches)

# Character sets []
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d') # The character set will match a - or a . (character sets do not need to be escaped)
matches = pattern.finditer(text_to_search)
find_matches(matches)

pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d') # To match 800 or 900 numbers
matches = pattern.finditer(text_to_search)
find_matches(matches)

pattern = re.compile(r'[1-5]') # The hyphen is a special character inside a character set. At start or end it matches -, else it specifies a range
pattern_2 = re.compile(r'[a-g]') # Also works on letters
pattern_3 = re.compile(r'[a-gA-G]') # Can match them back to back like this
matches = pattern.finditer(text_to_search)
matches_2 = pattern_2.finditer(sentence)
matches_3 = pattern_3.finditer(sentence)

find_matches(matches)
find_matches(matches_2)
find_matches(matches_3)

# The ^ is an another special character inside a character set
pattern = re.compile(r'[^a-zA-Z]') # The carrot ^ negates the search so this finds everything that is not in the character set.
matches = pattern.finditer(text_to_search)
find_matches(matches)

# Quantifiers - match multiple characters at a time
# Specify the number of multiple characters to match at a time using {}
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
matches = pattern.finditer(text_to_search)
find_matches(matches)

pattern = re.compile(r'Mr\.?\s[A-Z]\w*') # The \w* will match 0 or more of alpha characters after. If using the + Then Mr. T would not match.
matches = pattern.finditer(text_to_search)
find_matches(matches)

# Using a group use ()
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*') # The | will match the `or` values
matches = pattern.finditer(text_to_search)
find_matches(matches)

# Matching emails
emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)') 
matches = pattern.finditer(emails)
find_matches(matches)

# Matching urls
urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)') # Group the last two in () in order to later retrieve those values.
matches = pattern.finditer(urls)
subbed_urls = pattern.sub(r'\2\3', urls) # The 2 and 3 are the groups we want to sub into the pattern.and

for match in matches:
    print(match.group(2)) # This will print out the groups. Group 0 is every group is number in ordered.

print(subbed_urls)

# findall method
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
matches = pattern.findall(text_to_search) # This will only match the first group (Mr|Ms|Mrs)
find_matches(matches)

# match method - This will only search for this at the beginning of the string.
pattern = re.compile(r'Start') 
matches = pattern.match(sentence) # Does not return an iterable. Only the first value found or none. 
print(matches)

# search method - This will search over the entire string.
pattern = re.compile(r'sentence')
matches = pattern.search(sentence) # Only the first value found or none.
print(matches)

# Flags
pattern = re.compile(r'start', re.IGNORECASE) # The flag will ignore case. re.I is shorthand.
matches = pattern.search(sentence)
print(matches)