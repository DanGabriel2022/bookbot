from stats import get_contents
from stats import count_words
from stats import count_characters
from stats import sort_characters
from stats import generate_report
                                      
def main():
    book_content = get_contents()
    word_count = count_words(book_content)
    characters = count_characters(book_content)
    list_of_characters = sort_characters(characters)

    sort_characters(characters)

    generate_report(word_count, list_of_characters)
    
main()