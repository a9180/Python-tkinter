from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Título")
menu_inicial.geometry("500x300")


Label1 = Label(
    menu_inicial,
    text="frase de testes",
    font="Arial 20",
    bd=1,
    relief="solid"
)
Label1.pack()

menu_inicial.mainloop()