import sys
from stats import get_num_words
from stats import split_book_text
from stats import get_book_text
from stats import character_count
from stats import get_sorted_list
from stats import print_sorted_list
def main():
    print(sys.argv)
    #Starting If statement
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    ##Variables and functions

    book_location = sys.argv[1]
    book_contents = get_book_text(book_location)
    words = split_book_text(book_contents)
    num_words = get_num_words(words)
    letter_dict = character_count(book_contents)
    sorted_list = get_sorted_list(letter_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("-------- Character Count --------")
    print_sorted_list(sorted_list)
main()