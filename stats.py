def get_num_words(words):
    num_words = len(words)
    return num_words
def get_book_text(book):
    book_contents = ""
    with open(book) as file:
        book_contents = file.read()
    return book_contents
def split_book_text(file_contents):
    words = list()
    words = file_contents.split()
    return words
def character_count(book_contents):
    letter_dict = {}
    for character in book_contents:
        lower_character = character.lower()
        if lower_character in letter_dict:
            letter_dict[lower_character] += 1
        else:
            letter_dict[lower_character] = 1
    return letter_dict
def sort_on(letter_dict):
    return letter_dict["num"]
def get_sorted_list(letter_dict):
    sorted_list = list()
    for char, num in letter_dict.items():
        item_to_append = {"char": char, "num": num}
        sorted_list.append(item_to_append)
    #print(f"Sorted List Test: {sorted_list}")
    sorted_list.sort(reverse=True,key=sort_on)
    return sorted_list
def print_sorted_list(sorted_list):
    for item in sorted_list:
        print_char = item["char"]
        print_num = item["num"]
        if print_char.isalpha():
            print(f"{print_char}: {print_num}")
