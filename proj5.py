def generate_acronym(sentence):
    words = sentence.split()
    acronym = ''.join(word[0].upper() for word in words)
    return acronym
if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    acronym = generate_acronym(sentence)
    print(f"The acronym for '{sentence}' is: {acronym}")