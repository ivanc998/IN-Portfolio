# ---------------------------------------------------
# Author. Iván Gustavo Nieto
# ---------------------------------------------------

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random
import pandas as pd

# ---------------------------------------------------
# Create the real texts field with web scrap
# ---------------------------------------------------

# Set the webdriver
executable_path = 'C:\\Users\\ivang\\OneDrive\\Documentos\\Ciencia de datos\\chromedriver.exe'
service = Service(executable_path)
options = Options()
options.headless = True

# Create the webdriver with the previous settings
wd = webdriver.Chrome(service = service, options = options)
url = "https://homepage.cs.uri.edu/faculty/wolfe/book/Readings/Reading13.htm"

wd.get(url) # Open the website

paragraphs = wd.find_elements(By.XPATH , '//body') # Find the tags 'body' on the page
paragraphs = paragraphs[0].get_attribute("innerText").split('.') # Extract the text and split using '.'

wd.quit() # Close the webdriver

paragraphs = list(map(lambda x: x + '.' ,list(filter(lambda x: len(x) > 1, paragraphs)))) # Filter and add '.'' to each text 

# ---------------------------------------------------
# Create fake texts using affine encrypt
# ---------------------------------------------------

# Define a function to encrypt  the given text
def affine_taransformation_encypt(a, b, text, tabs):

	# a and b are the paramethers on the transformation
	# text is the objecto encrypt 
	# tabs the length of each block of letters on the encrypt text
	# If tabs is 'random' then the systen will assign the spaces randomly between 1 and 9

	text = text.replace(' ','').lower() # Drop the spaces and the capital letters on the text
	encypt_text = '' # Create the variable to save the text encrypt 

	if tabs == 'random':
		key = True 
		tabs = random.randint(1,9)
	else:
		key = False

	cont_tabs = 0 # Variable to cont each block of the text

	for i in text:

		P = ord(i) - 97

		if 0 <= P and P <= 25: # Aply the tansformation only to letters on the alphabet
			C = ((a*P) + b) % 26 
			encypt_text += chr(C + 97)

			cont_tabs += 1
			if cont_tabs == tabs: 
				encypt_text += ' '
				cont_tabs = 0

				if key:
					tabs = random.randint(1,9)


	return encypt_text

a, b = 5, 8

affine_field = [affine_taransformation_encypt(a, b, x, 'random') for x in paragraphs] # Encrypt each text

# ---------------------------------------------------
# Create fake texts using letters exchange
# ---------------------------------------------------

# Define a function to exchange the letters with a dictionary having as keys the letters
# and as values the letter to assign.

def exchange_letters(dict_exchange, text, tabs):

	text = text.replace(' ','').lower()

	encypt_text = ''

	if tabs == 'random':
		key = True 
		tabs = random.randint(1,9)
	else:
		key = False

	cont_tabs = 0

	for i in text:
		if i in dict_exchange:
			encypt_text += dict_exchange[i]
			cont_tabs += 1

			if cont_tabs == tabs:
				encypt_text += ' '
				cont_tabs = 0

				if key:
					tabs = random.randint(1,9) 


	return encypt_text		

Keys = list(set([chr(x) for x in range(97, 123)])) # Generate a random sort on the alphabet letters
dict_exchange = {chr(x + 97) : Keys[x] for x in range(26)}

exchange_field = [exchange_letters(dict_exchange, x, 'random') for x in paragraphs] # Encrip each text

# ---------------------------------------------------
# Create fake texts using random values
# ---------------------------------------------------

# Define a function to create a text with length given
def random_text(len_t):
	created_text = ''

	for i in range(len_t):
		
		# Add a tab or letter depending of the obtained number
		ch = random.randint(97, 123) 
		if ch == 123:
			created_text += ' '
		else:
			created_text += chr(ch)

	return created_text 

random_text_field = [random_text(len(j) + 2) for j in paragraphs]

df_dict = {'Real text' : paragraphs,
			'Affine encrypt' : affine_field,
			'Exchange encrypt' : exchange_field,
			'random_text' : random_text_field}


df = pd.DataFrame(df_dict)
df.to_csv('Test_recognize_words.csv')
