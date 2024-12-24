def main():
    book_folder = "books/"
    book_file_name = "frankenstein.txt"
    book_path = book_folder + book_file_name
    
    text = get_file_contents(book_path)

    print(f"--- Report generated from {book_path} ---")

    word_count = get_word_count(text)

    print(f"Document contains {word_count} words.")
    
    chars = get_char_dict(text)
    

    print("Here are the character counts:")
    print_char_dict(chars)

    print("--- End of report ---")


def get_file_contents(file_path):
    with open(file_path) as f:
        return f.read()

def get_word_count(text):
   return len(text.split())

def get_char_dict(text):
    res = {}

    for char in text.lower():
        if char in "abcdefghijklmnopqrstuvwxyz":
            res[char] = res.get(char, 0) + 1

    return res

def print_char_dict(char_dict):
    for char, value in sorted(char_dict.items(), key=lambda item: item[1], reverse=True):
        print(f"The '{char}' character was found {value} times")

main()
