import pandas as pd 
from time import sleep

def update_frecuency(Letter, frecuency_list):

	Letter = Letter.upper()
	letter = Letter.lower()
	url = f"https://github.com/ivanc998/csv_files/blob/main/words_list/{Letter}_words.csv?raw=true"
	df = pd.read_csv(url, index_col = 0)

	n_rows = df.shape[0]

	frecuency_list[ord(Letter.lower()) - 97] += n_rows

	for i in range(0, n_rows):

		try:
			word = df.iloc[i][Letter].replace(letter, '')
			word = set(word)

			if len(word) != 0: 

				for lt in word:
					try:
						frecuency_list[ord(lt) - 97] += 1
					except:
						print(f'\tLetra: {Letter}')
						print(f'\tRegistro: {i}')
						print(f'\tCaaracter: {lt}')
						print('\t\t-----')
		except:
			print(f'Letra: {Letter}')
			print(f'Registro: {i}')
					

	return frecuency_list

frecuency_list = [0] * 26
name = [chr(x) for x in range(97, 123)]

for j in name:
	print('---------------------------')
	print(f'Letra: {j}')
	print('---------------------------')
	frecuency_list = update_frecuency(Letter = j, frecuency_list = frecuency_list)
	sleep(40)

pd.DataFrame({'Letter' : name,'stats' : frecuency_list}).to_excel('Frecuency_letters.xlsx')


