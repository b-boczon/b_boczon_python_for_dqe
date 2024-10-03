import re
text = """homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

target_paragraph = "also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph."

def split_paragraphs(t):
    """Split the text into paragraphs based on new lines"""
    return re.split(r'(\n)', t)

def split_sentences(paragraphs):
    """Split paragraphs into individual sentences based on punctuation marks or indents"""
    all_sentences = []  # List to hold sentences from all paragraphs
    for paragraph in paragraphs:
        new_sentences = [sentence for sentence in re.split(r'(\xa0\s*|[.!?]\s*)', paragraph)]
        all_sentences.extend(new_sentences)  # Append sentences from the current paragraph
    return all_sentences

def normalize_case(sentences):
    """Capitalize each item in the provided object"""
    return [sentence.capitalize() for sentence in sentences]

def last_words(sentences):
    """Extract the last word from each sentence if it is alphabetical or alphanumeric and creates a new sentence from them"""
    words = []
    for sentence in sentences:
        # Split the sentence into words, filter out empty strings
        words_in_sentence = [word for word in sentence.split() if word.strip()]
        if words_in_sentence:  # Ensure the list isn't empty to avoid IndexError
            last_word = words_in_sentence[-1]
            if last_word.isalpha() or last_word.isalnum():
                words.append(last_word)
    return ' '.join(words).capitalize() + '.'

def append_new_sentence(new_paragraphs, new_sentence, target):
    """Append a new sentence created from the last words to the specified paragraph"""
    final_paragraphs = []
    for paragraph in new_paragraphs:
        if target.lower() in paragraph.lower():
            modified_paragraph = paragraph + " " + new_sentence
            final_paragraphs.append(modified_paragraph)
        else:
            final_paragraphs.append(paragraph)
    return final_paragraphs

def build_final_text(txt):
    """Join given object"""
    return ''.join(txt)

def fix_spelling_mistakes(txt):
    """Fix spelling mistakes within the text"""
    return re.sub(r'(?<!“)\biz\b(?!”)', 'is', txt)

def count_whitespaces(txt):
    """Count all whitespaces in the text"""
    return len(re.findall(r'\s', txt))


par = split_paragraphs(text)
sent = split_sentences(par)
norm = normalize_case(sent)
wrd = last_words(norm)
new_text = append_new_sentence(par, wrd, target_paragraph)
new_sent = split_sentences(new_text)
new_norm = normalize_case(new_sent)
new_norm_text = build_final_text(new_norm)
new_fixed = fix_spelling_mistakes(new_norm_text)
cnt = count_whitespaces(text)

print(par)
print(sent)
print(norm)
print(wrd)
print(new_text)
print(new_sent)
print(new_norm)
print(new_norm_text)
print(new_fixed)
print(cnt)
