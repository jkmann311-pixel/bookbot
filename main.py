# figure out how to open the frankenstein text file
def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

#def main():
    #return get_book_text(~/bookbot/books/frankenstain.txt)

#main