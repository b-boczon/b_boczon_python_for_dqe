import re

text = """homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""
# Split the text into sentences based on periods or new lines
sentences = re.split(r'[.\n]+', text)

# Initialize an empty list to store the last words of each sentence
last_words = [] 

# Loop through of the list excluding the first element - the title 'homework'
for sentence in sentences[1:]:
    last_word = sentence.split(' ')[-1]  # Extract the last word of the current sentence
    last_words.append(last_word) # Append the last word to the list 'last_words'

# Insert a new sentence made of the last words, into 'sentences' in the position pointed in the text 
sentences.insert(4, ' '.join(last_words))

# Reconstruct the text, capitalizing the first letter of each sentence
# The title is handled separately to ensure it's displayed correctly
normalized_text = sentences[0].capitalize() + ' \n' + '. '.join([i.strip().capitalize() for i in sentences[1:]])

# Replace incorrect usages of "iz" with "is" using a regular expression
final_text = re.sub(r'\biz\b', 'is', normalized_text)

# Count the number of whitespace characters in the original text
number_of_spaces = len(re.findall(r'\s', text))