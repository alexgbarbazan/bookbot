import sys
from stats import get_num_words, get_count_by_letter, get_char_dictionary

def get_book_test(file_path):
    with open(file_path) as f:
        return(f.read())

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    text = get_book_test(sys.argv[1])
    print(
            "============ BOOKBOT ============\n"
            "Analyzing book found at books/frankenstein.txt...\n"
            "----------- Word Count ----------"
        )
    get_num_words(text)
    print("----------- Character Count ----------")
    dic = get_char_dictionary(text)
    print("============= END ===============")
    
main()

