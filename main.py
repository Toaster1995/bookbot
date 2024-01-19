def main():
    book_path = "books/frankenstein.txt"
    print_report(book_path)

def print_report(book_path):
    print(f"--- Begin report of {book_path} ---")
    print()
    text = get_book_text(book_path)
    words_cnt = count_words(text)
    print(f"{words_cnt} words found in the  given document")
    print()
    
    letters_dict = get_chars_dict(text)
    new_list = []
    for char in letters_dict:
        if char.isalpha():
            new_list.append(char)
            
    new_list.sort()
    for char in new_list:
        cnt = letters_dict[char]
        print(f"The '{char}' character was found {cnt} times")
    print()
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(book_text):
    words = book_text.split()
    return len(words)

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