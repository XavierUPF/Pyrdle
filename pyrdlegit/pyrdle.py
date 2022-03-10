import enum
from tkinter import *
from tkinter import messagebox
import words
import wordscat
import wordscas

word = words.get_word()
dicwords = words.words

window = Tk(className='Pyrdle')

def catala():
	global word
	global dicwords
	word = wordscat.get_catword()
	dicwords = wordscat.wordscat
	return word
	return dicwords

def castellano():
	global word
	global dicwords
	word = wordscas.get_casword()
	dicwords = wordscas.wordscas
	return word
	return dicwords

def english():
	global word
	global dicwords
	word = words.get_word()
	dicwords = words.words
	return word
	return dicwords

Font_tuple = ('Courier', 60, "bold")

window.config(bg="white")
window.geometry("400x450")

photo = PhotoImage(file='pyrdleico.png')
window.wm_iconphoto(False, photo)

menubar = Menu(window)
window.config(menu=menubar)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="English", command=english)
filemenu.add_command(label="Català", command=catala)
filemenu.add_command(label="Castellano", command=castellano)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="Language", menu=filemenu)

###

guessnum = -1

wordInput = Entry(window)
wordInput.grid(row=6, column=0, padx=10, pady=10, columnspan=3)

for i in range(5):
	window.columnconfigure(i, weight=1, minsize=75)
	window.rowconfigure(i, weight=1, minsize=75)

	for j in range(0, 5):
		frame = Frame(
			master=window,
			relief=RAISED,
			borderwidth=1
		)
		frame.grid(row=i, column=j, padx=5, pady=5)
		label = Label(master=frame, text=" ", bg="white", width=2, height=1)
		label.pack(padx=5, pady=5)

def getGuess():

	guess = wordInput.get().lower()

	global guessnum
	guessnum += 1

	if guessnum <= 4:

		if len(guess) == 5:
			if guess in dicwords:

				if word == guess:
					messagebox.showinfo("Great!", f"The word was {word.title()}!")
					guessnum -= 1
					for i, letter in enumerate(guess):

						label = Label(window, text=letter.upper())
						label.grid(row=guessnum+1, column=i, padx=10, pady=10)
						if letter == word[i]:
							label.config(bg="#6AAA64", fg="white")
				else:
					for i, letter in enumerate(guess):

						label = Label(window, text=letter.upper())
						label.grid(row=guessnum, column=i, padx=10, pady=10)

						if letter == word[i]:
							label.config(bg="#6AAA64", fg="white")

						if letter in word and not letter == word[i]:
							label.config(bg="#C9B458", fg="white")
                    
						if letter not in word:
								label.config(bg="#787C7E", fg="white")
			else:
				messagebox.showwarning("Oops!", "Ooops! The word you used is not in this dictionary")
				guessnum -= 1 
		else:
			messagebox.showwarning("Please use 5 characters", "Please use 5 characters in your guess")
			guessnum -= 1

	else:
		messagebox.showerror("You lose!", f"You Lose! The word was {word}!")                                                

wordGuessButton = Button(window, text="             Guess             ", command=getGuess)
wordGuessButton.grid(row=6, column=3, columnspan=6)

window.mainloop()
