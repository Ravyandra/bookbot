from stats import * 
import sys


def main():
    print(sys.argv)
    if len(sys.argv) != 2:
         print("Usage: python3 main.py <path_to_book>")
         sys.exit(1)
    
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    word_count = number_of_words(book_text)
    # number_of_characters(book_text)
    character_count = number_of_characters2(book_text)
    book_report_output(book_path, word_count, character_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()
        
"""def number_of_characters(book_content): # more complicated
    character_numbers = {}
    for character in book_content:
        character_numbers[character.lower()] = 0
    
    for key in character_numbers.keys():
        count = 0
        for character in book_content:
            if character.lower() == key:
                count += 1
        character_numbers[key] = count

    return character_numbers"""

def number_of_characters2(book_content): # optimized
    character_numbers = {}
    for character in book_content:
        if character.lower() not in character_numbers:
            character_numbers[character.lower()] = 1
        else:    
            # for key in character_numbers.keys():  not necessary
                # if character.lower() == key:
                    character_numbers[character.lower()] += 1

    return character_numbers

def book_report_output(path, words, characters):
    book_name = path.split("/")
    
    print(f"--- This is a book report of {book_name[1]} ---")
    print(f"{words} words found in the document")
    print("")
    for key in characters:
         if key.isalpha():
            print(f"{key}: {characters[key]}")


main()