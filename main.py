from stats import word_count

def main():
    #book_text = get_book_text('books/frankenstein.txt')
    #return print(book_text)
    words = word_count('books/frankenstein.txt')
    return print(f"Found {words} total words")


main()