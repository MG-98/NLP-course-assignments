import pickle
import helper
import numpy as np

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
for word in vocab:
    if word not in my_english_dictionary:
        misspelled_words.append(word)

# Find words with Min-edit distance
distances =np.zeros((len(misspelled_words) , len(my_english_dictionary)))
correct_wrd_dict ={}
for i in range(len(misspelled_words)):
    for j in range(len(my_english_dictionary)):
        distances[i,j]=helper.Edit_distance(misspelled_words[i] ,my_english_dictionary[j], len(misspelled_words[i]) , len(my_english_dictionary[j]))
    correct_wrd_dict[misspelled_words[i]] = ( my_english_dictionary[np.argmin(distances[i])] ,np.min(distances[i]))

print(correct_wrd_dict)