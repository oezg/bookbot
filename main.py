import string


def get_content(filename: str) -> str:
    with open("books/"+filename) as f:
        content = f.read()
    return content


def word_count(text: str) -> int:
    words = text.split()
    return len(words)

def letter_frequency(text: str) -> dict:
    text = text.lower()
    return {letter: text.count(letter) for letter in string.ascii_lowercase}

def print_report(text: str):
    print(word_count(text), "words found")
    frequency = letter_frequency(text)
    for letter, freq in sorted(frequency.items(), key=lambda x: -x[1]):
        print(f"The '{letter}' character was found {freq} times")




def main():
    frankenstein = get_content("frankenstein.txt")
    print_report(frankenstein)

if __name__ == "__main__":
    main()
    