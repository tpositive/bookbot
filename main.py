import string

def main():
    with open("books/frankenstein.txt") as file:
        contents = file.read()
        count = word_count(contents)
        letters = letter_count(contents)
        letter_list = []
        for letter in letters:
            letter_list.append({"letter": letter, "count": letters[letter]})
        letter_list.sort(reverse=True, key=dictionary_sort)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{count}\n")
        for dictionary in letter_list:
            print(f"The '{dictionary['letter']}' character was found {dictionary['count']} times")
        print("--- End report ---")

def word_count(text):
    words = text.split()
    count = len(words)
    return count

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