import tkinter as tk


class Menu(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('500x500')
        self.title('Blackjack')


        first_label = tk.Label(self, text="Numero de Jugadores", font=30)
        first_label.pack(padx=3, pady=3)

        opcion = tk.StringVar(self, value='0')
        num_jugadores = tk.OptionMenu(self, opcion, '1','2','3','4','5')
        num_jugadores.pack(padx=3, pady=3)

        def start():
            print(opcion.get())
            if opcion.get() != '0':
                menu.destroy()
                game.deiconify()

        first_button = tk.Button(self, text="Jugar", command=start)
        first_button.pack(padx=5, pady=5)


class Game(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('500x500')
        self.title('Blackjack')

        first_label = tk.Label(self, text="Crupier", font=30)
        first_label.pack(padx=3, pady=3)

        first_button = tk.Button(self, text="Hello World")
        first_button.pack(padx=5, pady=5)




def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


menu = Menu()
game = Game()
center_window(menu)
center_window(game)
game.withdraw()

menu.mainloop()
game.mainloop()

