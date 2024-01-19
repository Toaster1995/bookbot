def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(get_chars_dict(text))

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(book_text):
    words = book_text.split()
    print(len(words))

def get_chars_dict(book_text):
    res = {}
    for letter in book_text:
        letter = letter.lower()
        if letter in res:
            res[letter.lower()] += 1
            continue
        res[letter.lower()] = 1
    return res

main()