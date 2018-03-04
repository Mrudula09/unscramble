import time
import itertools
import inspect
import os

def meaning_full_words(word,size_of_words):
    starting_time=time.time()
    #Opening dict_words.txt file.
    dictionary = open_input_file("dictionary.txt", 'r')

    #Getting the words as set.
    words = set(map("".join, itertools.permutations(word,size_of_words)))

    #Getting first letters in all the words:
    unique_letters=set(word)
    #Meaning full words.
    m_words=[]

    #Logic
    for line in dictionary:
        #Checking whether first letter of a line is in unique_letters.
        if line[0] in unique_letters:

            #Stripping the line.
            line=line.strip()

            #checking whether the length of line is equal to the size of the word.
            if len(line)==size_of_words:

            #Checking whether the line is in words or not.
            # If line is in words we append it to a list of meaning full words.
            # Remove the meaning line from the words. To reduce the searching time of a next line in
            #words.
                if line in words:
                    m_words.append(line)
                    words= words - {line}
    #If words is empty i.e If there are no words in 'words' we can simply terminate it. No need of going
    #to *end of file*
        if not words:
            break

    print("Time Taken: ",time.time()-starting_time)
    return m_words

def open_input_file(file, mode="rt"):
    mod_dir = get_module_dir()
    test_file = os.path.join(mod_dir, file)
    return open(test_file, mode)

def get_module_dir():
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    return mod_dir

print(meaning_full_words("out",2))
print(meaning_full_words("python",5))
print(meaning_full_words("python",4))