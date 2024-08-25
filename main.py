def main():
    path_to_frank = "./books/frankenstein.txt"
    frank_text = read_file(path_to_frank)
    # frank_word_count = count_words(frank_text)
    frank_dict = char_count(frank_text)
    print(frank_dict)


# reads a file and returns its text as a string
def read_file(path_name):
    with open(path_name) as f:
        return f.read()

# returns an int - count of words seperated by spaces
def count_words(text):
    text_list = text.split()
    return len(text_list)

# takes in a list of words, iterates through and counts each character, returns a dictionary
def char_count(list_of_words):
    char_dict = dict()
    for word in list_of_words:
        for letter in word:
            letter = letter.lower()
            if char_dict.get(letter) != None:
                char_dict[letter] += 1
            else:
                char_dict[letter] = 1

    return char_dict

main()
