"""
#>>> main('caesar.txt')
The average word length is 5

"""

def main(file_name):
    txt_file_object = open(file_name, 'r')
    all_text_lstOfLines = txt_file_object.readlines()   # takes the whole text and creates a list where each position
                                                        # is a line
    data = get_data(all_text_lstOfLines)
    print('The average word length is %5.3f' % (data[1]))   # data[1] is average_size
    print('Word usage is as follows %s' % (data[0]))        # data[0] is word_count_dic
    #five_most_used(data[0])
    print(data[2])


def get_data(all_text_lstOfLines):
    count, total_size = 0, 0
    longest_word = ""
    word_count_dic = {}
    for line in all_text_lstOfLines:
        line = line.strip() # removes white space and newline characters
        word_list = line.split()    # word_list is a list with each word of the line in its own position
        for word in word_list:
            word = word.strip(',.:?!;')  # removes all specified characters
            count += 1
            total_size += int(len(word))
            if len(word) > len(longest_word):
                longest_word = word
            most_used_words(word,word_count_dic)
    average_size =  total_size/count
    return word_count_dic, average_size, longest_word


def most_used_words(word,word_count_dic):
    word = word.lower()
    if word in word_count_dic:
        word_count_dic[word] += 1
    else:
        word_count_dic[word] = 1

def five_most_used(dic):
    top_five = {}
    for x,y in dic.items():
        pass

# Assuming that file is small enough to read in completely and not need to read line by line
main('test.txt')


'''
Write a text analyzer. It should be in a form of a function that takes a file name as an argument. It should read and 
analyze a text file and then print:
- the top 5 most frequently used words in the file
- the number of times the top 5 words are used
- should be sorted by most frequently used count
- the longest word in the document
- the average size of each word'''

if __name__== "__main__":
    import doctest
    doctest.testmod()
