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

def sort_characters(characters):

    # Creating a list of dictionaries 
    list_of_characters = []

    # Iterating over the existing character dictionary 
        # "i" will take the value of each character (a, b, c, etc.) 
        # characters[i] will be the count of each character 
    for i in characters: 
        count = characters[i]

        # Creating a temporary dictionary to store the new values with the "char" and "count" keys 
        temp_characters = {}

            # Updating said dictionary: 
        temp_characters.update({"char": i, "count": count})

        # Adding the temp dictionary to the LIST of dictionaries 
        list_of_characters.append(temp_characters)

    # Defining function that takes a dictionary and returns the the value of the "count" key
    def sort_on(list_of_characters):
        return list_of_characters["count"]
    
    # Sorting the list of characters by the "count" key in each dictionary, in reverse order 
    list_of_characters.sort(reverse=True, key=sort_on)

    return list_of_characters

def generate_report(word_count, list_of_characters):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    #Iterating over the list of characters to go through each dictionary: 
    for i in list_of_characters: 
        if i["char"].isalpha(): 
            print(f"{i["char"]}: {i["count"]}")
        else: 
            pass 

    print("============= END ===============")

    
        

    

   