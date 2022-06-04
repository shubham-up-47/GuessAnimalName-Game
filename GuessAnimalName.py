from tkinter import *                           # importing all libraries of tkinter
from tkinter import messagebox
import random                                   # to get random words

root = Tk()                                     # getting tkinter window
root.geometry('800x500+300+100')                # setting position & size of tkinter window
root.configure(bg='olive')                       # setting background colour of tkinter window
img = PhotoImage(file='logo.png')
root.iconphoto(False, img)                    # setting icon of tkinter window
root.title('GuessAnimalName')


#----------------Checking Win, Loss or Continue----------------#

def GuessAnimalName():
    global currWord,starString,noOfChances,noOfLeftChances,spacedStarString,temp,currChar
    currChar = inputText1.get()
    inputBox1.delete(0,END)
    if(noOfLeftChances > 0):
        if(currChar in currWord):
            for i in range(noOfChances):
                if(currWord[i]==currChar and starString[i]=='*'):
                    starString.pop(i)
                    starString.insert(i,currWord[i])
                    currString = ''.join(starString)
                    currWord = list(currWord)
                    currWord.pop(i)
                    currWord.insert(i,"*")
                    wordlabel.configure(text=currString)
                    if(currString==temp):
                        ansText.configure(text='Well done, You won the game...')
                        result = messagebox.askyesno("Notification", 'Congratulations, You won...\nWant to play again ?')
                        if(result==True):
                            chooseword()
                        else:
                            root.destroy()
                    else:
                        break
        else:
            noOfLeftChances -= 1
            leftchances.configure(text='LeftChances = {}'.format(noOfLeftChances))
    if(noOfLeftChances <= 0):
        ansText.configure(text='Bad luck, You lost the game...')
        result = messagebox.askyesno("Notification", 'OOPs, You lost the game...\nWant to play again ?')
        if(result == True):
            chooseword()
        else:
            root.destroy()

def helper(event):
    GuessAnimalName()

#----------------Implementing Lebels of Tkinter Window----------------#

introlabel = Label(root,text='Welcome to GuessAnimalName Game',font=('arial',30,'underline bold'),bg='yellow',fg='maroon')
introlabel.place(x=35,y=0)                      # x = distanceFronLeft & y = distanceFromTop

wordlabel = Label(root,text='',font=('arial',55,'bold'),bg='olive')
wordlabel.place(x=210,y=150)

leftchances = Label(root,text='',font=('arial',25,'bold'),bg='wheat')
leftchances.place(x=500,y=90)

ansText = Label(root,text='',font=('arial',25,'bold'),bg='olive',fg='skyblue')
ansText.place(x=170,y=425)

#----------------Entry Box of Game-----------------#

inputText1 = StringVar()
inputBox1 = Entry(root,font=('arial',25,'bold'),relief=SUNKEN,bd=5,bg='green',justify='center',fg='white',textvariable=inputText1)
inputBox1.focus_set()
inputBox1.place(x=210,y=250)

#----------------Button of Game-----------------#

button1 = Button(root,text='Submit',font=('arial',15,'bold'),width=15,bd=5,bg='red',activebackground='blue',activeforeground='white',command=GuessAnimalName)
button1.place(x=300,y=350)
root.bind("<Return>",helper)

#----------------Word Selection Function----------------#

worldlist = ['lion','monkey','dog','elephant','deer','horse','tiger']

def chooseword():
    global currWord,starString,noOfChances,noOfLeftChances,spacedStarString,temp
    currWord = random.choice(worldlist)
    starString = ["*" for i in currWord]
    noOfChances = len(currWord)
    noOfLeftChances = noOfChances
    temp = currWord
    leftchances.configure(text='LeftChances = {}'.format(noOfLeftChances))
    spacedStarString = ''
    for i in starString:
        spacedStarString += i+' '
    wordlabel.configure(text=spacedStarString)
    ansText.configure(text='')

#----------------Main Function----------------#

chooseword()
root.mainloop()






