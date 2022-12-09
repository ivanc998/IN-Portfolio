# ---------------------------------------------------
# Author. Iván Gustavo Nieto
# ---------------------------------------------------

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# ---------------------------------------------------
# Create the real texts field with web scrap
# ---------------------------------------------------

# Set the webdriver
executable_path = # add the path of the chromedriver as str 
service = Service(executable_path)
options = Options()
options.headless = True

# Create the webdriver with the previous settings
wd = webdriver.Chrome(service = service, options = options)
url = "https://en.wikipedia.org/wiki/Computer_programming"

wd.get(url) # Open the website

paragraphs = wd.find_elements(By.XPATH , '//p')
paragraphs = [x.text for x in paragraphs] # Extract the text of each element found

wd.quit() # Close the webdriver

for i in range(len(paragraphs)):
	row = ''
	for j in paragraphs[i]:
		if (97 <= ord(j.lower()) and ord(j.lower()) <= 122) or (j == ' '): # Delete the elements out the alphabet
			row += j

	paragraphs[i] = row


# ---------------------------------------------------
# Create fake texts using affine encrypt
# ---------------------------------------------------

# Define a function to encrypt  the given text
def affine_taransformation_encypt(a, b, text, tabs):

	# a and b are the paramethers on the transformation
	# text is the objecto encrypt 
	# tabs the length of each block of letters on the encrypt text

	text = text.replace(' ','').lower() # Drop the spaces and the capital letters on the text
	encypt_text = '' # Create the variable to save the text encrypt 

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

	return encypt_text
