# --------------------------------------------------------------
# Author. Iván Gustavo Nieto
# --------------------------------------------------------------

# This module define some function to obtain csv files with the words of the english using web scraping.
# Each word will be extracted of links taken of the page 'https://www.mso.anu.edu.au/~ralph/OPTED/'.

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# This function receives two iterable objects and determines if their intersection is empty or not.
def empty_intersection(List, Word):
	set1 = set(List)
	set2 = set(Word)

	inter = list(set1 & set2)
	if (len(inter) == 0):
		return True
	else:
		return False

# The parameters of this function are the letter to search and the path
# of the controller to be used by selenium

def words_by_letter(Letter,controller_path):


	# ----------------------------------------------------------
	# Preparing tools to web scraping
	# ----------------------------------------------------------

	list_links = 'https://github.com/ivanc998/IN-Portfolio/blob/main/Project-Decrypt/csv-files/link_list.csv?raw=true'
	df = pd.read_csv(list_links)

	try:
		url = df.iloc[ord(Letter.lower()) - 97]['Links']
	except:
		raise Exception(f'{Letter} is not a valid character')

	service = Service(controller_path)

	options = Options()
	options.headless = True # Navigation on silence mode

	wd = webdriver.Chrome(service = service, options = options)
	wd.get(url)

	# ----------------------------------------------------------
	# Start the web scraping
	# ----------------------------------------------------------

	Lista = [] # Here will be saved the found words

	Words = wd.find_elements(by = 'xpath', value = '//b')

	for J in Words:
		aux = (J.text).lower()
		if (aux not in Lista) and  (empty_intersection(['-', '\'', ' '], aux)):
			Lista.append(aux) # Save words without repetions or spacial characters

		if len(Lista) > 4:
			break


	try:
		ind = Lista.index(Letter.lower()) # Erase elements containing only the word searched
		Lista.pop(ind)
	except:
		pass

	# ----------------------------------------------------------
	# Export the words found
	# ----------------------------------------------------------

	df = pd.DataFrame({Letter.upper() : Lista}) # Define the dictionary to create the csv file
	name = Letter.upper() + '_words.csv' # Define the file name

	df.to_csv(name) # Save the file created
	print(f'{len(Lista)} found of the letter {Letter}.') 

	wd.quit()



# -------------------------------------------------
# Suggestion to use the function 'words_by_letter'
# -------------------------------------------------

'''
Letters = [chr(x) for x in range(97, 123)]
 executable_path = ...

for Letter in Letters:
	words_by_letter(Letter = Letter,)

'''