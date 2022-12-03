import pandas as pd



for i in range(97, 123):
	Letter = chr(i)
	url = f'https://github.com/ivanc998/IN-Portfolio/blob/main/Project-Decrypt/csv-files/{Letter.upper()}_words.csv?raw=true'
	df = pd.read_csv(url, index_col = 0)

	df_size = df.shape[0]
	length_words = []

	for j in range(df_size):
		word = df.iloc[j][Letter.upper()]

		if (type(word) is str) and (len(word) > 1):
			length_words.append(len(word))
		else:
			length_words.append(None)


	df['Length'] = length_words
	df.dropna(inplace = True)
	df.reset_index(inplace = True,  drop = True)

	name = f'{Letter.upper()}_words.csv'
	df.to_csv(name)

