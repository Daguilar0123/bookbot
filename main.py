import sys
from stats import get_num_words, get_num_characters_dict, character_dict_to_sorted_list
def get_book_text(filepath):
    with open(filepath) as f:
        # do something with f (the file) here
        file_contents = f.read()
    return file_contents



def main():
    if len(sys.argv) != 2:
        print(f"Usage: python2 main.pyj <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    number_of_words = get_num_words(text)
    character_count_dictionary = get_num_characters_dict(text)
    sorted_char_list = character_dict_to_sorted_list(character_count_dictionary)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    #print(character_count_dictionary)
    #print(sorted_char_list)
    for item in sorted_char_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()