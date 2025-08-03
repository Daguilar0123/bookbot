def get_num_words(text):
    number_of_words = len(text.split())
    return number_of_words

def get_num_characters_dict(text):
    lowered_text = text.lower()
    count_dictionary = {}
    for char in lowered_text:
        if char not in count_dictionary:
            count_dictionary[char] = 1
            #print(count_dictionary)
        elif char in count_dictionary:
            count_dictionary[char] += 1
            #print(count_dictionary)
    return count_dictionary

def sort_on(item):
    return item["num"]

def character_dict_to_sorted_list(count_dictionary):
    # Convert to list of dicts, only for alpha chars
    char_list = []
    for char, num in count_dictionary.items():
        if char.isalpha():
            char_list.append({"char": char, "num": num})
    char_list.sort(reverse=True, key=sort_on)
    return char_list


'''
def chars_to_sorted_list(char_count_dict):
    # Build a list of dictionaries: [{"char": "e", "num": 44538}, ...]
    char_list = []
    for char, count in char_count_dict.items():
        if char.isalpha():  # Only include alphabetical characters
            char_list.append({"char": char, "num": count})
    # Sort the list from greatest to least count
    char_list.sort(reverse=True, key=lambda item: item["num"])
    return char_list
'''