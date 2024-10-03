import re

text = """homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# Specify the pointer to the paragraph where the new sentence should be added
target_paragraph = "also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph."

# Initialize an empty lists to store interim results
new_paragraphs = []
last_words = [] 

# Change letter case to lower and split the text into paragraphs based on new lines
paragraphs = re.split(r'(\n)', text.lower())

for paragraph in paragraphs:
    # Split each paragraph into sentences based on indent or punctuation marks, capitalize and join into normalized sentences
    new_sentences = [sentence.capitalize() for sentence in re.split(r'(\xa0\s*|[.!?]\s*)', paragraph)]
    # Create normalized paragraphs
    new_paragraphs.append(''.join(new_sentences))


# Loop through new_sentences and extract last word of each sentence
    for sentence in new_sentences:
        last_word = sentence.split(' ')[-1]
        # Ensure last word is either alphabetical or alphanumeric
        if last_word.isalpha() or last_word.isalnum(): 
            last_words.append(last_word) # Append the last word to the list 'last_words'

# Create a sentence from last words and capitalize
new_sentence = ' '.join(last_words).capitalize() + '.'

# Initialize a list to hold the final modified paragraphs
final_paragraphs = []

# Loop through normalized paragraphs
for paragraph in new_paragraphs:
    # Check if the current paragraph contains the target phrase.
    if target_paragraph.lower() in paragraph.lower():
        # Append the new sentence to the targeted paragraph
        modified_paragraph = paragraph + " " + new_sentence
        final_paragraphs.append(modified_paragraph)
    else:
        # If the current paragraph does not contain target paragraph, it is added as it is
        final_paragraphs.append(paragraph)

# Join all final paragraphs to form a normalized text
normalized_text = ''.join(final_paragraphs)

# Replace incorrect usages of "iz" with "is" using a regular expression
final_text = re.sub(r'(?<!“)\biz\b(?!”)', 'is', normalized_text)

# Count the number of whitespace characters in the original text
number_of_spaces = len(re.findall(r'\s', text))

# print(normalized_text)
print(final_text)
print(number_of_spaces)