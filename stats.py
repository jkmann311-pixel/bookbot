# takes a filepath as an input, specifically a filepath to a text file. then it opens and reads that text file to a string.
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def word_count(filepath):
    # takes the text from the book and stores it in a string
    book_text = get_book_text(filepath)
    # i want to get that string and count how many words there are. maybe len(split(book_text))
    number_of_words = len(book_text.split())
    
    return number_of_words
