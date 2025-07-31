def get_contents():
    with open("books/frankenstein.txt") as book:    # opens the file as a variable named 'book'
        book_contents = book.read()                 # book.read saves the contents of the 'book' file to 
        return(book_contents)          

def count_words(book_contents):
    words = book_contents.split()
    num_words = len(words)
    return num_words

def count_characters(book_contents): 
    characters = {}

    for c in book_contents:
        lowered_char = c.lower()

        if lowered_char in characters: 
            characters[lowered_char] += 1

        else: 
            characters[lowered_char] = 1
    
    return characters

    


# def count_characters(book_contents): 
#    characters = book_contents.lower()
#    print(characters)