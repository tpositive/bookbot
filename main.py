import string

def main():
    user_input = False
    while user_input == False:
        question1 = input("Do you want to search for specific words? (y/n): ")
        if question1 == 'y' or question1 == 'Y':
            user_keywords = input("Enter the word(s) you would like to search seperated by ',' if you would like to search multiple words:\n").split(',')
            user_input = True
        elif question1 == 'n' or question1 == 'N':
            user_keywords = ''
            user_input =True
        else:
            print("Please enter y or n")
    with open("books/frankenstein.txt") as file:
        contents = file.read()
        count,keyword_count = word_count(contents, user_keywords)
        letters = letter_count(contents)
        letter_list = []
        for letter in letters:
            letter_list.append({"letter": letter, "count": letters[letter]})
        letter_list.sort(reverse=True, key=dictionary_sort)
        if len(keyword_count) > 0:
            keyword_count.sort(reverse=True, key=dictionary_sort)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"Word Count: {count}\n")
        if user_keywords:
            print(f"User provided key words:\n {user_keywords}")
            for dictionary in keyword_count:
                print(f"The word '{dictionary['word']}' was found {dictionary['count']} in the text")

        for dictionary in letter_list:
            print(f"The '{dictionary['letter']}' character was found {dictionary['count']} times")
        print("--- End report ---")

def word_count(text, keywords=[]):
    words = text.split()
    count = len(words)
    new_keyword_list = []
    ##optional keyword search##
    if len(keywords) > 0:
        for item in keywords:
            item = str(item).lower()
            keyword_count = 0
            for word in words:
                if word == item:
                    keyword_count += 1
            new_keyword_list.append({'word': item, 'count': keyword_count})
    return count, new_keyword_list

def letter_count(text):
    text_lowered = text.lower()
    letter_dict=dict.fromkeys(string.ascii_lowercase, 0)
    for letter in text_lowered:
        if letter in letter_dict:
            letter_dict[letter] += 1
    return letter_dict

def dictionary_sort(dict):
    return dict["count"]
        
 
main()