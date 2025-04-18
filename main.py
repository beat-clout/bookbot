from stats import get_num_words
from stats import letter_count
from stats import transform_and_sort
import sys

def get_book_text(filepath):
        with open(filepath) as f:
                return f.read() 
             
def main():
        if len(sys.argv) != 2:
                print("Usage: python3 main.py <path_to_book>")
                sys.exit(1)
        filepath = sys.argv[1]
        text = get_book_text(filepath)
        num_words=get_num_words(text)
        letter_dict = letter_count(text)
        sorted_letters = transform_and_sort(letter_dict)
        # Print header and word count
        print(f"============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
    
        # Print character count
        print("--------- Character Count -------")
        for item in sorted_letters:
                print(f"{item['char']}: {item['count']}")
    
        # Print footer
        print("============= END ===============")

main()

