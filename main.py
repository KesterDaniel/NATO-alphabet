import pandas

alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in alphabet_df.iterrows()}
