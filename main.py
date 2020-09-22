#import libraries
import tkinter as tk
from game import *

#set up application to have all files
class StartApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #set title and screen size
        self.title("Tuq Tac Toe")
        self.geometry("1440x1024")

        #create a virtual grid to hold all app pages for use at different times
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        #Initialize each frame using a blank dictionary and for loop to add it to the grid
        #the frame on the top of the grid will be the one that is visible to the user
        self.frames = {}
        for frameGrid in (Menu,Game):
            page_name = frameGrid.__name__
            frame = frameGrid(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        #show the menu page to let users choose modules
        self.show("Menu")

    #function that changes which frame is visible by raising the previous one
    def show(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

#Menu page
class Menu(tk.Frame):
    #initialization step of menu
    def __init__(self, parent, controller):
        #initialize canvas to store all ui options
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame1 = (self)
        self.frame1.place(relheight=1, relwidth=1)

        #place background image
        self.bgImage = tk.PhotoImage(file="UI/background.png")
        self.background = tk.Label(self.frame1, image=self.bgImage)
        self.background.place(relwidth=1, relheight=1)

        #place title
        self.titleImage = tk.PhotoImage(file="UI/title.png")
        self.title = tk.Label(self.frame1, image=self.titleImage, bg="#8DB3C9")
        self.title.place(relx=0.15,rely=0.04)

        #place start button
        self.startImage = tk.PhotoImage(file="UI/startButton.png")
        self.start = tk.Button(self.frame1, image=self.startImage, bg="#8DB3C9", border="0", command=lambda: controller.show("Game"))
        self.start.place(relx=0.5,rely=0.5,anchor="n")

class Game(tk.Frame):
    #initialization of Game screen
    def __init__(self, parent, controller):
        #initialize canvas to store all ui options
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frameGame = tk.Frame(self, bg="#FFFFFF", border="0")
        self.frameGame.place(relheight=1, relwidth=1)

        #place background
        self.bgImageGame = tk.PhotoImage(file="UI/background.png")
        self.backgroundGame = tk.Label(self.frameGame, image=self.bgImageGame, bg="#8DB3C9")
        self.backgroundGame.place(relwidth=1, relheight=1)

        #place title
        self.titleImageGame = tk.PhotoImage(file="UI/title.png")
        self.titleGame = tk.Label(self.frameGame, image=self.titleImageGame, bg="#8DB3C9")
        self.titleGame.place(relx=0.15,rely=0.04)

        #place game board
        self.boardImage = tk.PhotoImage(file="UI/board.png")
        self.board = tk.Label(self.frameGame, image=self.boardImage, bg="#8DB3C9")
        self.board.place(relx=0.5,rely=0.28, anchor="n")
        
        #button placement for all sections to record where user clicks in tic tac toe
        self.buttonImage = tk.PhotoImage(file="UI/ticbutton.png")
        self.topLeft = tk.Button(self.frameGame, image=self.buttonImage, bg="#8DB3C9", border="0", command=lambda: game(self.frameGame, self, 0))
        self.topLeft.place(relx=0.365,rely=0.3,anchor="n")

        self.topCenter = tk.Button(self.frameGame, image=self.buttonImage, bg="#8DB3C9", border="0", command=lambda: game(self.frameGame, self, 1))
        self.topCenter.place(relx=0.5,rely=0.3,anchor="n")

        self.topRight = tk.Button(self.frameGame, image=self.buttonImage, bg="#8DB3C9", border="0", command=lambda: game(self.frameGame, self, 2))
        self.topRight.place(relx=0.635,rely=0.3,anchor="n")

        self.midLeft = tk.Button(self.frameGame, image=self.buttonImage, bg="#8DB3C9", border="0", command=lambda: game(self.frameGame, self, 3))
        self.midLeft.place(relx=0.365,rely=0.535,anchor="n")

        self.midCenter = tk.Button(self.frameGame, image=self.buttonImage, bg="#8DB3C9", border="0", command=lambda: game(self.frameGame, self, 4))
        self.midCenter.place(relx=0.5,rely=0.535,anchor="n")

        self.midRight = tk.Button(self.frameGame, image=self.buttonImage, bg="#8DB3C9", border="0", command=lambda: game(self.frameGame, self, 5))
        self.midRight.place(relx=0.635,rely=0.535,anchor="n")

        self.botLeft = tk.Button(self.frameGame, image=self.buttonImage, bg="#8DB3C9", border="0", command=lambda: game(self.frameGame, self, 6))
        self.botLeft.place(relx=0.365,rely=0.776,anchor="n")

        self.botCenter = tk.Button(self.frameGame, image=self.buttonImage, bg="#8DB3C9", border="0", command=lambda: game(self.frameGame, self, 7))
        self.botCenter.place(relx=0.5,rely=0.776,anchor="n")

        self.botRight = tk.Button(self.frameGame, image=self.buttonImage, bg="#8DB3C9", border="0", command=lambda: game(self.frameGame, self, 8))
        self.botRight.place(relx=0.635,rely=0.776,anchor="n")
        

#loop so that the app stays open
if __name__ == "__main__":
    app = StartApp()
    app.mainloop()