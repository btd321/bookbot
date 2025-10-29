# main
from stats import get_book
from stats import num_of_words
from stats import num_of_char
from stats import dict_sort
import sys

if len(sys.argv) !=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book_location = sys.argv[1]


    

num_char = num_of_char(get_book(book_location))
book = get_book(book_location)

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}")
    print("----------- Word Count ----------")
    num_of_words(book)
    print("--------- Character Count -------")
    dict_sort(num_char)

main()