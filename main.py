import sys
from stats import get_num_words
from stats import sym_count
from stats import prettify_sym_count

report_header = "============ BOOKBOT ============"
report_word_count = "----------- Word Count ----------"
report_character_stat = "--------- Character Count -------"
report_footer = "============= END ==============="

def get_book_text(filepath):
    content_string = ""
    with open(filepath) as f:
        content_string = f.read()

    return content_string

def main():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_num_words(text)
    sym_stat_list=prettify_sym_count(sym_count(text))
    print(report_header)
    print(f"Analyzing book found at {path}...")
    print(report_word_count)
    print(f"Found {num_words} total words")
    print(report_character_stat)
    for line in sym_stat_list:
        if line["char"].isalpha():
            print(f"{line["char"]}: {line["num"]}")
    print(report_footer)

if __name__ == "__main__":
    main()
