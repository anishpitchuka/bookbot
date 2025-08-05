import sys
from stats import count_words,count_characters,sort_characters_by_count

def get_books_txt(filepath):

    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
   
    book_text = get_books_txt(filepath)
    word_count = count_words(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    character_count = count_characters(book_text)
    sorted_characters = sort_characters_by_count(character_count)

    for entry in sorted_characters:
        print(f"{entry['char']}: {entry['count']}")
  


if __name__ == '__main__':
    main()