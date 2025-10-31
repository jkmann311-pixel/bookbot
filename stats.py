def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def word_count(filepath):
    book_text = get_book_text(filepath)
    number_of_words = len(book_text.split())
    return number_of_words

def character_count(filepath):
    characters = {}
    book_text = get_book_text(filepath).lower()
    for ch in book_text:
        if ch.isalpha():
            if ch in characters:
                characters[ch] += 1
            else:
                characters[ch] = 1
        else:
            pass
    return characters

def sort_on(d):
    return list(d.values())[0]

def sort_characters(characters):
    char_list = [{key: value} for key, value in characters.items()]
    char_list.sort(key=sort_on, reverse=True)

    return char_list