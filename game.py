#import libraries
import tkinter as tk

#initialize global variables
turn = 'x'
counter = 0
pos = ['topLeft','topCenter','topRight','midLeft','midCenter','midRight','botLeft','botCenter','botRight']
posX = [
    0.35,0.475,0.605,
    0.35,0.475,0.605,
    0.35,0.475,0.605
    ]
posY = [
    0.300,0.300,0.300,
    0.535,0.535,0.535,
    0.776,0.776,0.776
    ]


#game function for noticing the actual Xs and Os
def game(root, self, id):
    #initialize global variables
    global turn
    global pos
    global counter

    #if it is X's turn, then place an x where the mouse clicked and change the turn to O
    if turn == 'x':
        pos[id] = 'X'
        self.letter = tk.Label(root, text="x")
        self.letter.config(font=("Atomic Age",100),background="#8DB3C9", foreground="#00629B")
        self.letter.place(relx=posX[id],rely=posY[id])
        turn = 'o'
    #else, it is Os turn so place an O and change the turn to x
    else:
        pos[id] = 'O'
        self.letter = tk.Label(root, text="o")
        self.letter.config(font=("Atomic Age",100),background="#8DB3C9", foreground="#9B0000")
        self.letter.place(relx=posX[id],rely=posY[id])
        turn = 'x'

    #counter to detect when all squares are filled   
    counter += 1

    #check function to see if there is a win or a tie
    check(pos, counter, self.letter, root, self, id)




def check(pos, count, letter, root, self, id):
    #Check if there is 3 in a row
    if (pos[0] == pos[1] == pos[2]) or (pos[3] == pos[4] == pos[5]) or (pos[6] == pos[7] == pos[8]) or (pos[0] == pos[3] == pos[6]) or (pos[1] == pos[4] == pos[7]) or (pos[2] == pos[5] == pos[8]) or (pos[0] == pos[4] == pos[8]) or (pos[2] == pos[4] == pos[6]):
        #if there is 3 in a row, bring up win screen and prompt for new game
        self.coverImage = tk.PhotoImage(file="UI/cover.png")
        self.cover = tk.Label(root, image=self.coverImage, bg="#8DB3C9")
        self.cover.place(relx=0.5,rely=0.28, anchor="n")

        #win text
        if (pos[id] == 'X'):
            self.winImage = tk.PhotoImage(file="UI/xwin.png")
            self.win = tk.Label(root, image=self.winImage, bg="#8DB3C9")
            self.win.place(relx=0.325,rely=0.4)
        else:
            self.winImage = tk.PhotoImage(file="UI/owin.png")
            self.win = tk.Label(root, image=self.winImage, bg="#8DB3C9")
            self.win.place(relx=0.325,rely=0.4)

        #restart button
        self.restartImage = tk.PhotoImage(file="UI/restartButton.png")
        self.restart = tk.Button(root, image=self.restartImage, bg="#8DB3C9", border="0", command=lambda: restart(letter, self.cover, self.restart, self.win, self, root))
        self.restart.place(relx=0.5,rely=0.6,anchor="n")
  
    #Check if tie
    elif (count == 9):
        #same as above but for ties
        self.coverImage = tk.PhotoImage(file="UI/cover.png")
        self.cover = tk.Label(root, image=self.coverImage, bg="#8DB3C9")
        self.cover.place(relx=0.5,rely=0.28, anchor="n")

        self.tieImage = tk.PhotoImage(file="UI/tie.png")
        self.tie = tk.Label(root, image=self.tieImage, bg="#8DB3C9")
        self.tie.place(relx=0.35,rely=0.4)

        self.restartImage = tk.PhotoImage(file="UI/restartButton.png")
        self.restart = tk.Button(root, image=self.restartImage, bg="#8DB3C9", border="0", command=lambda: restart(letter, self.cover, self.restart, self.tie, self, root))
        self.restart.place(relx=0.5,rely=0.6,anchor="n")



#restart sequence
def restart(letter, cover, restart, win, self, root):
    #reset global variables
    global turn
    global pos
    global counter

    turn = 'x'
    pos = ['topLeft','topCenter','topRight','midLeft','midCenter','midRight','botLeft','botCenter','botRight']
    counter = 0

    #remove all unnecessary ui elements to allow for new game
    letter.place_forget()
    cover.place_forget()
    restart.place_forget()
    win.place_forget()

    #replace buttons to continue game
    self.buttonImage = tk.PhotoImage(file="UI/ticbutton.png")
    self.topLeft = tk.Button(root, image=self.buttonImage, bg="#8DB3C9", border="0", command=lambda: game(root, self, 0))
    self.topLeft.place(relx=0.365,rely=0.3,anchor="n")

    self.topCenter = tk.Button(root, image=self.buttonImage, bg="#8DB3C9", border="0", command=lambda: game(root, self, 1))
    self.topCenter.place(relx=0.5,rely=0.3,anchor="n")

    self.topRight = tk.Button(root, image=self.buttonImage, bg="#8DB3C9", border="0", command=lambda: game(root, self, 2))
    self.topRight.place(relx=0.635,rely=0.3,anchor="n")

    self.midLeft = tk.Button(root, image=self.buttonImage, bg="#8DB3C9", border="0", command=lambda: game(root, self, 3))
    self.midLeft.place(relx=0.365,rely=0.535,anchor="n")

    self.midCenter = tk.Button(root, image=self.buttonImage, bg="#8DB3C9", border="0", command=lambda: game(root, self, 4))
    self.midCenter.place(relx=0.5,rely=0.535,anchor="n")

    self.midRight = tk.Button(root, image=self.buttonImage, bg="#8DB3C9", border="0", command=lambda: game(root, self, 5))
    self.midRight.place(relx=0.635,rely=0.535,anchor="n")

    self.botLeft = tk.Button(root, image=self.buttonImage, bg="#8DB3C9", border="0", command=lambda: game(root, self, 6))
    self.botLeft.place(relx=0.365,rely=0.776,anchor="n")

    self.botCenter = tk.Button(root, image=self.buttonImage, bg="#8DB3C9", border="0", command=lambda: game(root, self, 7))
    self.botCenter.place(relx=0.5,rely=0.776,anchor="n")

    self.botRight = tk.Button(root, image=self.buttonImage, bg="#8DB3C9", border="0", command=lambda: game(root, self, 8))
    self.botRight.place(relx=0.635,rely=0.776,anchor="n")