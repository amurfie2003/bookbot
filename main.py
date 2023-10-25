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



#count each letter occurrence
def count_letters(search_list):
    result = {}
    content = get_book_content(book_path)
    for search in search_list:
        count = 0
        for i in range(0, len(content)):
            if search == content[i].lower():
                count += 1
        result[search] = count

    return result

#book report
def book_report():
    print()
    print(f"---Result of {book_path} analysis---")
    print(f"\t{word_count()} words found in the document")
    
    result = count_letters(search)
    for key, value in result.items():
        print(f"\tThe '{key}' character was found {value} times")
    
    print("---End Of Report---")
    return 





def main():
    book_report()
    return 

main()