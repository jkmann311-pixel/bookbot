from stats import word_count, character_count, sort_characters
import sys

def main():
    filepath = sys.argv[1]
    words = word_count(filepath)
    ch = character_count(filepath)
    new_list = sort_characters(ch)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for d in new_list:
        ch_key = list(d.keys())[0]
        count = list(d.values())[0]
        print(f"{ch_key}: {count}")

    print("============= END ===============")

    return

if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

else:
    main()