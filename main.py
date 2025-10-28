# Get book function

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def book_splitter(book_text):
    book_words = book_text.split() 
    num_words = len(book_words)
    print (f"Found {num_words} total words")

def main():
    book_splitter(get_book_text("books/frankenstein.txt"))

main()