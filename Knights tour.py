import tkinter as tk
from tkinter import messagebox


class at_oyunu:
    def __init__(self):
        self.root = tk.Tk()
        self.level = 5
        self.root.title("At turu Oyunu")
        self.a = 1
        self.buttons = []
        self.next_move = []
        self.choose_move = []
        self.interface_olustur()
        self.difficult_selec()
        self.oyun_resetleme_butonu_ekle()
        
        self.root.mainloop()

    def interface_olustur(self):
        for i in range(self.level):
            row = []
            for j in range(self.level):
                if (i + j) % 2 == 0:
                    color = "white"
                else:
                    color = "gray"
                button = tk.Button(self.root, text="", width=5, height=2, bg=color)
                button.grid(row=i, column=j)  
                button["command"] = lambda button=button: self.on_button_click(button) 
                row.append(button)
            self.buttons.append(row)

    def on_button_click(self, button):
        button["text"] = str(self.a)
        self.a += 1
        for i in range(len(self.buttons)):
            if button in self.buttons[i]:
                row = i
                col = self.buttons[i].index(button)
                break
        self.next_move = [[row+1,col+2],[row+1,col-2],[row-1,col-2],[row-1,col+2],[row-2,col+1],[row-2,col-1],[row+2,col+1],[row+2,col-1]]
        self.choose_move.append([row,col])
        self.probability_move()

    def probability_move(self):
        for i in range(self.level):
            for j in range(self.level):
                if [i, j] in self.next_move and [i, j] not in self.choose_move :
                    self.buttons[i][j].config(background="red")
                    self.buttons[i][j].config(state="normal")
                else:
                    self.buttons[i][j].config(state="disabled")
                    if (i + j) % 2 == 0:
                        color = "white"
                    else:
                        color = "gray"
                    self.buttons[i][j].config(background=color)
                    
                    if len(self.choose_move) == self.level * self.level:
                        answer = messagebox.askquestion("Başlık", "Do you want to play again?")
                        if answer == "yes":
                            self.oyun_resetle()
                        else:
                            self.root.destroy()
                

    def oyun_resetleme_butonu_ekle(self):
        reset_button = tk.Button(self.root, text="Reset", command=self.oyun_resetle)
        reset_button.grid(row=8, column=0, columnspan=8)
        label = tk.Label(self.root, text="created by baturay incekara")
        label.grid(row=9, column=0,columnspan=8 )

    def oyun_resetle(self):
        for i in range(self.level):
            for j in range(self.level):
                self.buttons[i][j].config(text="")
                self.buttons[i][j].config(state="normal")
                if (i + j) % 2 == 0:
                    color = "white"
                else:
                    color = "gray"
                self.buttons[i][j].config(background=color)
        self.a = 1
        self.next_move = []
        self.choose_move = []
    def difficult_selec(self):
            
        # option menu oluşturulması
        options = ["4x4", "5x5", "6x6", "8x8"]
        self.selected_option = tk.StringVar()
        self.selected_option.set(options[1])
        option = tk.OptionMenu(self.root, self.selected_option, *options)
        option.grid(row=10, column=0, columnspan=8)

        # seçim butonu oluşturulması
        button = tk.Button(self.root, text="Zorluğu seç", command=self.get_selected_option)
        button.grid(row=11, column=0, columnspan=8)

        #get_selected_option()
    def get_selected_option(self):
        self.butonlari_sil()
        self.level = int(self.selected_option.get()[0])
        self.buttons = []
        self.next_move = []
        self.choose_move = []
        self.a=1
        self.interface_olustur()

    def butonlari_sil(self):
        for i in range(self.level):
            for j in range(self.level):
                self.buttons[i][j].destroy()
        self.buttons = []

    
dd = at_oyunu()