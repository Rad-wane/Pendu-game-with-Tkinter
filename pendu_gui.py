#importations 
from tkinter import *
import tkinter.font as font
import tkinter as tk
from random_words import RandomWords
from tkinter import messagebox

#initializations and first screen
window = Tk()
c = tk.Canvas(window, width=300, height=400)
c.pack()
window.title("\"PENDU\" game")
window.geometry('300x400')
bg = PhotoImage(file = "C:/Users/radwa/Desktop/Code files/Pendu-game-with-Tkinter/img/bg.png") 
c.create_image(0, 0, image=bg, anchor="nw")
c.create_text(150, 50, text="PENDU", font=("Comic Sans MS", 30, "bold"))
mode_txt =c.create_text(145, 120, text="Choose your game mode :", font=("Comic Sans MS", 15, "italic"))

#uploading the photos 
photos = []
for i in range(7):
	path = "C:/Users/radwa/Desktop/Code files/Pendu-game-with-Tkinter/img/" +str(i+1)+str(i+1)+".png"
	photos.append(PhotoImage(file = path).subsample(4, 4) )

score =0

#First playing mode : single player
def spm ():
	#initializations 
	w_dict={}
	guess_dict = {}
	w_list=[]
	guess=''
	run = True
	typed =[]
	correct_in = []

	#second screen
	sp.destroy()
	mp.destroy()
	c.delete(mode_txt)
	r=c.create_text(147, 85, text="in single mode", font=("Comic Sans MS", 14, "italic"))
	
	#Choose a word randomely
	rw = RandomWords()
	word = rw.random_word()
	
	#filling the dicts and showing empty slots
	for i in range(len(word)):
		w_dict[i] = word[i]
		guess_dict[i] = '_'
		w_list.append(word[i])
	for key in guess_dict:
		guess += ' '+guess_dict[key]
	word_disp = c.create_text(145, 150, text=guess, font=("Comic Sans MS", 15, "bold"))	

	#Text entry for the guess 
	letter_in_disp = tk.Entry(window, font=("Comic Sans MS", 15, "bold"),justify='center',bg='#eec900')
	letter_in_disp.place(x=135,y=200, width = 30, height = 30)
	buttonFont = font.Font(family='Comic Sans MS', size=14, weight='bold')		
		
	#fonction for the entry's validation button
	def get_entry():
		
		in_letter = letter_in_disp.get()		
		letter_in_disp.delete(first=0)
		if (in_letter not in typed) and (in_letter not in correct_in) :
			typed.append(in_letter)
		
		#Check if the input is in the word, and updating the score accordingly
		b_letter = False
		for key in w_dict:
			if w_dict[key] == in_letter:
				b_letter = True
				guess_dict[key] = w_dict[key]
		
		#if the guessed letter is not in the word : showing a picture. If the game is lost, showing a
		#message box with the word, and a restart feature		
		if b_letter == False:
			global score
			cover=PhotoImage(file = "C:/Users/radwa/Desktop/Code files/Pendu-game-with-Tkinter/img/bg.png")
			c.create_image(198,170, image=cover, anchor="nw")
			curr_img = c.create_image(100, 160, image=photos[score], disabledimage=photos[score-1], anchor=NW)						
			score+=1		
			
			if score == 7:
				restart = messagebox.askquestion("You lost !", "You lost ! The word was \""+word+"\". Another word?")
				if restart =='yes':					
					score =0
					c.delete(word_disp)					
					c.create_image(0, 0, image=bg, anchor="nw")
					c.create_text(150, 50, text="PENDU", font=("Comic Sans MS", 30, "bold"))				
					r=c.create_text(147, 85, text="in single mode", font=("Comic Sans MS", 14, "italic"))					
					spm()
				else:
					window.quit()				
				
		#if the guessed letter is in the word, we append it to a list
		if b_letter :
			correct_in.append(in_letter)
		#print the remainig emplty slots 
		guess=''
		for key in guess_dict:
			guess += ' '+guess_dict[key]
		
		c.itemconfigure(word_disp, text=guess)
		
		#checking if the game is won, in this case showing a message box
		#with the word and a restarting feature
		won = True
		for key in guess_dict:
			if 	guess_dict[key] == '_':
				won =False
		if won :
			restart = messagebox.askquestion("You won !", "You won ! The word was \""+word+"\". Another word?")
			if restart =='yes':
				score =0
				c.delete(word_disp)					
				c.create_image(0, 0, image=bg, anchor="nw")
				c.create_text(150, 50, text="PENDU", font=("Comic Sans MS", 30, "bold"))				
				r=c.create_text(147, 85, text="in single mode", font=("Comic Sans MS", 14, "italic"))					
				spm()
			else:
				window.quit()
		
	#Entry's validation button 
	ok = Button(window, text="OK", bg='#ffe4b5',font=buttonFont, fg='#838b8b',command=get_entry).place(x=134,y=235, width = 30, height = 30)
	
		
#Second playing mode : multi-player
def mpm ():
	#initializations 
	sp.destroy()
	mp.destroy()
	c.delete(mode_txt)
	r=c.create_text(147, 85, text="in multi-player mode", font=("Comic Sans MS", 14, "italic"))	
	buttonFont = font.Font(family='Comic Sans MS', size=14, weight='bold')
	word_dis = tk.Entry(window, font=("Comic Sans MS", 15, "bold"),justify='center',bg='#eec900')
	word_dis.place(x=70,y=180, width = 150, height = 30)
	
	#function to run when multi-player mode choosen
	def enter_word():
		#initializations and removing the screen where second player entred his word
		w_dict={}
		guess_dict = {}
		w_list=[]
		guess=''
		run = True
		typed =[]
		correct_in = []
		word = word_dis.get()
		word=word.lower()
		done.destroy()
		word_dis.destroy()
		#filling dicts, and showing empty slots
		for i in range(len(word)):
			w_dict[i] = word[i]
			guess_dict[i] = '_'
			w_list.append(word[i])
		for key in guess_dict:
			guess += ' '+guess_dict[key]
		word_disp = c.create_text(145, 150, text=guess, font=("Comic Sans MS", 15, "bold"))
		
		#text entry for the 2nd player to guess
		letter_in_disp = tk.Entry(window, font=("Comic Sans MS", 15, "bold"),justify='center',bg='#eec900')
		letter_in_disp.place(x=135,y=200, width = 30, height = 30)			
			
		#function to run when a second player guess a letter a press the OK button
		def get_entry():
			
			in_letter = letter_in_disp.get()		
			letter_in_disp.delete(first=0)
			if (in_letter not in typed) and (in_letter not in correct_in) :
				typed.append(in_letter)
			
			#Check if the input is in the word, with exit options as in spm()
			b_letter = False
			for key in w_dict:
				if w_dict[key] == in_letter:
					b_letter = True
					guess_dict[key] = w_dict[key]
					
			if b_letter == False:
				global score
				cover=PhotoImage(file = "C:/Users/radwa/Desktop/Code files/Pendu-game-with-Tkinter/img/bg.png")
				f=c.create_image(198,170, image=cover, anchor="nw")
				curr_img = c.create_image(100, 160, image=photos[score], disabledimage=photos[score-1], anchor=NW)						
				score+=1		
				if score == 7:
					restart = messagebox.askquestion("You lost !", "You lost ! The word was \""+word+"\". Another word?")
					if restart =='yes':						
						score =0
						c.delete(word_disp)
						c.delete(curr_img)
						c.delete(f)						
						letter_in_disp.destroy()
						ok.destroy()
						score =0
						c.delete(word_disp)					
						c.create_image(0, 0, image=bg, anchor="nw")
						c.create_text(150, 50, text="PENDU", font=("Comic Sans MS", 30, "bold"))				
						r=c.create_text(147, 85, text="in multi-player mode", font=("Comic Sans MS", 14, "italic"))					
						
						mpm()
					else:
						window.quit()					

			if b_letter :
				correct_in.append(in_letter)
			
			#print the remainig emplty slots 
			guess=''
			for key in guess_dict:
				guess += ' '+guess_dict[key]
			
			c.itemconfigure(word_disp, text=guess)
			
			won = True
			for key in guess_dict:
				if 	guess_dict[key] == '_':
					won =False
			if won :
				restart = messagebox.askquestion("You won !", "You won ! The word was \""+word+"\". Another word?")
				if restart =='yes':
					score =0
					c.delete(word_disp)					
					letter_in_disp.destroy()
					ok.destroy()
					c.delete(word_disp)					
					c.create_image(0, 0, image=bg, anchor="nw")
					c.create_text(150, 50, text="PENDU", font=("Comic Sans MS", 30, "bold"))				
					r=c.create_text(147, 85, text="in multi-player mode", font=("Comic Sans MS", 14, "italic"))						
					mpm()
				else:
					window.quit()
			
		#Entry's validation button
		ok = Button(window, text="OK", bg='#ffe4b5',font=buttonFont, fg='#838b8b',command=get_entry)
		ok.place(x=134,y=235, width = 30, height = 30)		

	# 1st player entry's (word) validation button
	done = Button(window, text="Done", bg='#ffe4b5',font=buttonFont, fg='#901020',command = enter_word )
	done.place(x=115,y=230)

#Fisrt screen buttons to choose the playing mode
buttonFont = font.Font(family='Comic Sans MS', size=14, weight='bold')
sp = Button(window, text="Single player", bg='#ffe4b5',font=buttonFont, fg='#901020',command = spm )
mp = Button(window, text="Multi-player",font=buttonFont, bg='#ffe4b5', fg='#901020', command = mpm) 
sp.place(x=80, y=165)
mp.place(x=82, y=220)

#main loop
window.mainloop()