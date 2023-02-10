import pandas

alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in alphabet_df.iterrows()}

def generate_phonetic():
    try:
        user_word = input("Enter a word: ").upper()
        user_word_list = [alphabet_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(user_word_list)

generate_phonetic()