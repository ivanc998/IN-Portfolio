# --------------------------------------------------------------
# Author. Iván Gustavo Nieto
# --------------------------------------------------------------

# This module define a function to obtain a csv file with the frecuency of each letter in english language.
# It will skip the words with characters different to to common alphabet

import pandas as pd 
from time import sleep

# The function recibes like a parameter the letter to study and the current frecuency to update.
# In the first iteration it must recibe a list with zeros.
def update_frecuency(Letter, frecuency_list):

	# ----------------------------------------------------------------------
	# Define the necessary elements to use the csv files with tords list
	# ----------------------------------------------------------------------

	Letter = Letter.upper()
	letter = Letter.lower()
	url = f'https://github.com/ivanc998/IN-Portfolio/blob/main/Project-Decrypt/csv-files/{Letter}_words.csv?raw=true'
	df = pd.read_csv(url, index_col = 0)

	n_rows = df.shape[0] # Obtain the amount fo rows on the dataframe

	# All words on the current file begin with 'letter', so it starts with this information
	frecuency_list[ord(Letter.lower()) - 97] += n_rows 

	# ----------------------------------------------------------------------
	# Count the ocurrences of each letter and update the result
	# ----------------------------------------------------------------------
	for i in range(0, n_rows):
		try:
			word = df.iloc[i][Letter].replace(letter, '') # Drop 'letter' to don't count it twice
			word = set(word) # Drop al duplicates

			if len(word) != 0: 

				for lt in word:
					try:
						frecuency_list[ord(lt) - 97] += 1 # Add 1 to each letter found
					except:
						# If it find a different character, show where is located
						print(f'\tLetter: {Letter}')
						print(f'\tRow: {i}')
						print(f'\tCharacter: {lt}')
						print('\t\t-----')
		except:
			# If find some element no iterable then show it
			print(f'Letter: {Letter}')
			print(f'Row: {i}')
		

	return frecuency_list # Return the frecuency list


# ----------------------------------------------------------------------
# Use the function to build the frecuency of each letter
# ----------------------------------------------------------------------

frecuency_list = [0] * 26 # Each index on the list represents a letter. A -> 0, b -> 1, ..., etc.
name = [chr(x) for x in range(97, 123)] # Build a list with all letters to study

for J in name:
	print('---------------------------')
	print(f'Letter: {J}')
	print('---------------------------')
	frecuency_list = update_frecuency(Letter = J, frecuency_list = frecuency_list) # Execute the function
	sleep(15) # Break to the system

# Create a excel file with the obtained information
pd.DataFrame({'Letter' : name,'stats' : frecuency_list}).to_excel('[E] Frecuency_letters.xlsx')