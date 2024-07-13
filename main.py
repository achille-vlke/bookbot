def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    sorted_characters = sort_num_characters(num_characters)

    print(get_book_text(book_path))     # print the book
    print()
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")       # print words count
    print()
    for item in sorted_characters:
        print(f"The '{item['letter']}' character was found {item['count']} times")
    print()
    print("--- End report ---")
    
def sort_num_characters(dict):
    char_list = [{"letter": letter, "count": count} for letter, count in dict.items()] # creates a list of dictionaries
    sorted_num = sorted(char_list, key=lambda x: x["count"], reverse=True) # sorts the list using the value of each dictionary, in descending order
    return sorted_num

def get_num_characters(text):
    lowered_text = text.lower()
    char_count = {}
    for char in lowered_text:
        if char.isalpha(): # filters non alphabet words
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