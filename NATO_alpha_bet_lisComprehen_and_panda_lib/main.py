import pandas


alphabet_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in alphabet_frame.iterrows()}


user_input = input("Enter a word:").strip().upper()
phonetic_list = [alphabet_dict[char] for char in user_input]
print(phonetic_list)
