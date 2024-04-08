def count_word(file_path):
    word_counts = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.strip('.,?!;:"\'').lower()
                word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

def display_word(word_counts):
    sorted_words = sorted(word_counts.keys())
    for word in sorted_words:
        print(f"{word}: {word_counts[word]}")

def main():
    file_path = input("Enter the path of the text file: ")
    try:
        word_counts = count_word(file_path)
        print("\nWord counts in alphabetical order:")
        display_word(word_counts)
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()
