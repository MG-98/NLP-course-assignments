import pickle
import nltk


# Open the dictionary file (pickle format)
with open("/home/mg/ZC-SPRING21/NLP/Assignments/Assignment_2/assignment_2/vocab.pkl", 'rb') as vocab_file:
    my_english_dictionary = pickle.load(vocab_file)

# Open the test file (text format)
with open("/home/mg/ZC-SPRING21/NLP/Assignments/Assignment_2/assignment_2/doc.txt", 'r') as file_text:
    file = file_text.read()

# Removing punctuation as it results in some misleading results
punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

for char in file:
    if char in punctuation:
        file = file.replace(char, "")

# Checking for mis-spelled words
vocab = file.split()
misspelled_words = []
for i in range(len(vocab)):
    if vocab[i] not in my_english_dictionary:
        misspelled_words.append(vocab[i])
print(misspelled_words)

# Find words with Min-edit distance




