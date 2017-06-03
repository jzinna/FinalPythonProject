'''
Write a text analyzer. It should be in a form of a function that takes a file name as an argument. It should read and
analyze a text file and then print:
- the top 5 most frequently used words in the file
- the number of times the top 5 words are used
- should be sorted by most frequently used count
- the longest word in the document
- the average size of each word'''

import re

def main(file_name):
    txt_file_object = open(file_name, 'r')
    all_text_lstOfLines = txt_file_object.readlines()   # assuming text is short enough to avoid memory problems, takes the whole text and creates a list where each position is a line
    data = get_data(all_text_lstOfLines)
    print('The five most common words and the number of times they occur are %s' % (data[0]))
    print('The longest word is \"%s\"' % (data[2]))
    print('The average word length is %5.3f' % (data[1]))   # data[1] is average_size




def get_data(all_text_lstOfLines):
    count, total_size = 0, 0
    longest_word = ""
    word_count_dic = {}
    for line in all_text_lstOfLines:
        line = re.sub(r'[^\w\s]','',line) # removes white space, punctuation, and newline characters
        word_list = line.split()    # word_list is a list with each word of the line in its own position
        for word in word_list:
            count += 1
            total_size += int(len(word))
            if len(word) > len(longest_word):
                longest_word = word
            most_used_words(word,word_count_dic)
    top_five = five_most_used(word_count_dic)
    average_size =  total_size/count
    return top_five, average_size, longest_word


def most_used_words(word,word_count_dic):
    word = word.lower()
    if word in word_count_dic:
        word_count_dic[word] += 1
    else:
        word_count_dic[word] = 1

def five_most_used(dic):
    word_number_pairs = list(dic.items())
    ordered_most_common = sorted(word_number_pairs, key=lambda word_number_pairs: word_number_pairs[1], reverse=True)
    ordered_five_most_common = ordered_most_common[:5]
    return ordered_five_most_common




main('macbeth.txt')
