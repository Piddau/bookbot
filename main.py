from stats import count_words_in_book, count_characters_used_in_book, sort_characters_by_frequency
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def print_report(book_path, num_words, sorted_characters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_info in sorted_characters:
        print(f"{char_info['char']}: {char_info['num']}")
    print("============= END ===============")

def main(argv):
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = argv[1]
    book_text = get_book_text(book)
    num_words = count_words_in_book(book_text)
    character_count = count_characters_used_in_book(book_text)
    sorted_characters = sort_characters_by_frequency(character_count)
    print_report(book, num_words, sorted_characters)

main(sys.argv)