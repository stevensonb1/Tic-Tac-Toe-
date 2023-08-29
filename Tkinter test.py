from tkinter import *
root = Tk()
root.title("Tic Tac Toe")
root.geometry('700x500')

frame = LabelFrame(root)
frame.pack()
w = Label(frame, text="Welcome to Tic Tac Toe!")
w.pack()

game_slots = {}
button_count = 0 

def button_clicked():
    print(button_count)

def create_buttons():
    global button_count
    for i in range(3):
        for j in range(3):
            button_count = button_count + 1
            frame = Frame(
                master=root,
                relief=RAISED,
                borderwidth=1,
            )
            frame.grid(row=i, column=j, padx=5, pady=5)
            btn = Button(master=frame, width=17, height=7, command = lambda c = button_count: button_clicked(c))
            btn.pack()

def start_game_interface(self):
    frame.pack_forget()
    self.pack_forget()
    create_buttons()

def create_start_buttons():
    start_btn = Button(
        root,
        text="Start game",
        bg="light green",
        width=30,
        height=3,
        command = lambda: start_game_interface(start_btn)
    )
    start_btn.pack()

create_start_buttons()
#create_buttons()
root.mainloop()