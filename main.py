from stats import get_contents
from stats import count_words
from stats import count_characters
                                      
def main():
    book_content = get_contents()
    word_count = count_words(book_content)
    characters = count_characters(book_content)

    print(f"{word_count} words found in the document")

    print(characters)


main()