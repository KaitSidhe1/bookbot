from stats import get_num_words
from stats import get_per_char_count
from stats import get_sorted_count
from sys import argv
from sys import exit

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    path_to_file = argv[1]
    text = get_book_text(path_to_file)
    num_words = get_num_words(text)
    sorted_count = get_sorted_count(get_per_char_count(text))

    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {path_to_file}")
    print ("----------- Word Count ----------")
    print (f"Found {num_words} total words")
    print ("--------- Character Count -------")

    for count in sorted_count:
       if count["char"].isalpha():
           print (f"{count["char"]}: {count["num"]}")

    print("============= END ===============")    

    
main()