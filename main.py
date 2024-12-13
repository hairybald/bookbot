def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters_count = get_characters_count(text)

    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()

    for letter, count in characters_count:
        print(f"The {letter} character was found {count} times")
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)

def get_characters_count(text):
    characters = {}

    for letter in text:
        lowered = letter.lower()
        if lowered.isalpha():
            if lowered not in characters:
                characters[lowered] = 1
            else:
                characters[lowered] += 1

    sorted_characters = sorted(characters.items(), key=lambda x: x[1], reverse=True)

    return sorted_characters


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
