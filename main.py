search = ['a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z']
book_path = 'books/frankenstein.txt'

#Read the content of txt file
def get_book_content(book_path):
    with open(book_path, 'r') as file:
        content = file.read()
    return content

#Count words in text file
def word_count():
    content = get_book_content(book_path)
    words = content.split()
    return len(words)



