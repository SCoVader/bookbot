def get_book_text(filepath):
    content_string = ""
    with open(filepath) as f:
        content_string = f.read()

    return content_string

def count_words(text):
    count = 0
    count = len(text.split())
    return count

def main():
    path = "./books/frankenstein.txt"
    num_words = count_words(get_book_text(path))
    print(f"Found {num_words} total words")

if __name__ == "__main__":
    main()
