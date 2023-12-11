import pandas


alphabet_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in alphabet_frame.iterrows()}

while True:
    user_input = input("Enter a word: ").strip().upper()
    try:
        phonetic_list = [alphabet_dict[char] for char in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(phonetic_list)
        break
