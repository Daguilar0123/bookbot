def get_book_text(filepath):
    with open(filepath) as f:
        # do something with f (the file) here
        file_contents = f.read()
    return file_contents

def count_words(text):
    return len(text.split())

def main():
    print(f"{count_words(get_book_text("books/frankenstein.txt"))} words found in the document")

main()