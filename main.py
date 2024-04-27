def count_letters(file_content):
    counts_dict = dict()
    text = file_content.lower()
    for ch in text:
        if ch in counts_dict:
            counts_dict[ch] +=1
        else:
            counts_dict[ch] = 1
    return counts_dict

def count_words(file_content):
    words = file_content.split()
    return len(words)

def print_report(file_path, word_count, letters_count):

    letters_count = dict(sorted(letters_count.items(), key=lambda item: item[1], reverse=True))

    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} found in the document")
    print("\n")
    for pair in letters_count.items():
        if pair[0].isalpha():
            print(f"The character '{pair[0]}' was found {pair[1]} times")
        
    print("--- End report ---")


def main():
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()
    
    word_count = count_words(file_contents)

    letters_count = count_letters(file_contents)

    print_report(file_path, word_count, letters_count)

main()
