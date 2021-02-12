from random_words import RandomWords
from random import *
from definition import find


#Variables declaration and random word choice

SCORE = 7
w_dict={}
guess_dict = {}
w_list=[]
guess=''
run = True
typed =[]
correct_in = []

#Overall header
print('******** Pendu ********')

#choose the modes : single or multiplayer
print('Choose your game mode? (m/s) :')
mode = input()
while mode !='m' and mode !='s':		
	print('Incorrect input ! try again (m/s) : ')
	mode = input()

if mode =='m':
	print('Multiplayer mode choosen !')
	print('Enter a word : ')
	word = input()
	while word.isalpha() == False:		
		print('Incorrect input ! try again : ')
		word = input()
	word = word.lower()
	for i in range (10):
		print('\n')	
else :
	rw = RandomWords()
	word = rw.random_word()

#Filling the dicts and randomly showing one character 
for i in range(len(word)):
	w_dict[i] = word[i]
	guess_dict[i] = '_'
	w_list.append(word[i])

# rand_ind = randint(0,len(word)-1)

# while w_list.count(w_dict[rand_ind]) != 1 :
# 	rand_ind = randint(0,len(word)-1)

# guess_dict[rand_ind] = w_dict[rand_ind]

for key in guess_dict:
	guess += ' '+guess_dict[key]

print(guess)

#Finding the word definition using definition.py
definition_w=find(word)
if definition_w == False:
	definition_w = 'Not found'

#main loop
while run :
	#asking for a letter and runing checks and formating
	print('Enter a letter : ')
	in_letter = input()
	while len(in_letter) != 1 or not in_letter.isalpha() :
		print('Incorrect input, try again : ')
		in_letter = input()	
	in_letter = in_letter.lower()
	
	# append the already used letter in a list to display
	if (in_letter not in typed) and (in_letter not in correct_in) :
		typed.append(in_letter)
	
	#Check if the input is in the word, and updating the score accordingly
	b_letter = False
	for key in w_dict:
		if w_dict[key] == in_letter:
			b_letter = True
			guess_dict[key] = w_dict[key]
			
	if b_letter == False:
		SCORE -= 1

	if b_letter :
		correct_in.append(in_letter)
	
	#print the remainig emplty slots 
	guess=''
	for key in guess_dict:
		guess += ' '+guess_dict[key]	

	#headers and formating, with lives left, used letters, etc
	header=''
	space_bef =''
	for i in range(len('Used letters : '+str(typed)+ '  | Lives left : '+str(SCORE))):
		header+='_'
	for i in range(len('Used letters : '+str(typed)+ '  | Lives left : '+str(SCORE))//2 - len(guess)//2 - 2):
		space_bef+=' '
	print(header)
	print('Used letters : '+str(typed)+ '  | Lives left : '+str(SCORE))
	print(space_bef+guess)
	
	# Escaping the loop conditions
	won = True
	for key in guess_dict:
		if 	guess_dict[key] == '_':
			won =False

	if won :
		
		print('You won ! The word was : \"'+ word+'\"')
		print('Definition of \"'+ word+'\"' + ' : ' + definition_w)

	if SCORE == 0:
		SCORE == 7
		
		print('You lost ! The word was : \"'+ word+'\"')
		print('Definition of \"'+ word+'\"' + ' : ' + definition_w)

	# Asking for another game
	if SCORE==0 or won:
		
		print('Another word? (y/n) :')
		res = input()

		while res !='y' and res !='n':		
			print('Incorrect input ! Another word? (y/n) : ')
			res = input()

		if res == 'y':
			#choose the modes : single or multiplayer
			print('Choose your game mode? (m/s) :')
			mode = input()
			while mode !='m' and mode !='s':		
				print('Incorrect input ! try again (m/s) : ')
				mode = input()

			if mode =='m':
				print('Multiplayer mode choosen !')
				print('Enter a word : ')	
				word = input()
				while word.isalpha() == False:		
					print('Incorrect input ! try again : ')
					word = input()
				word = word.lower()
				for i in range (10):
					print('\n')	
			else :
				rw = RandomWords()
				word = rw.random_word()
			SCORE = 7
			definition_w=find(word)
			print('******** Pendu ********')

			w_dict={}
			guess_dict = {}
			w_list=[]
			guess=''

			for i in range(len(word)):
				w_dict[i] = word[i]
				guess_dict[i] = '_'
				w_list.append(word[i])

			# rand_ind = randint(0,len(word)-1)
			# while w_list.count(w_dict[rand_ind]) != 1 :
			# 	rand_ind = randint(0,len(word)-1)
			# guess_dict[rand_ind] = w_dict[rand_ind]


			for key in guess_dict:
				guess += ' '+guess_dict[key]

			print(guess)
			run = True
			typed =[]
			correct_in = []

			definition_w=find(word)
			if definition_w == False:
				definition_w = 'Not found'
		else:
			run = False
			print('Game over !')

