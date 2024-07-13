def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)

    print(get_book_text(book_path))     # print the book
    print()
    print(f"{num_words} words found in the document")       # print words count
    print()
    sorted_characters = dict(sorted(num_characters.items()))        # sorts the characters in the dictionary
    print("Number of each character in the text:")
    for char, count in sorted_characters.items():
        print(f"{char}: {count}")       # print number of each character


def get_num_characters(text):
    lowered_text = text.lower()
    char_count = {}
    for char in lowered_text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

if __name__ == "__main__":      # ensure execution only if called
    main()