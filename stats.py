def count_words_in_book(book_text):
    words = book_text.split()
    return len(words)

def count_characters_used_in_book(book_text):
    character_list = {}

    for char in book_text:
        char = char.lower()
        character_list[char] = character_list.get(char, 0) + 1
    return character_list

def sort_on(items):
    return items["num"]

def sort_characters_by_frequency(character_list):
    sorted_list = []
    for char in character_list:
        if char.isalpha():
            sorted_list.append({"char": char, "num": character_list[char]})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list