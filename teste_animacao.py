# Teste de animação
from tkinter import *
import os
from time import sleep

pastaApp = os.path.dirname(__file__)
mov_x = -30 #posicação inicial
pst = "\\sprites\\" #pasta com os sprites

app = Tk()
app.title("Teste de animação")
app.geometry("500x250")
app.resizable(False, False)
# O resizable(False, False)impede que a janela seja redimencionada

while True:
    movimentos=["1.png", "2.png","3.png","4.png","5.png","6.png"]

    for i, mov in enumerate(movimentos, 0):
        imgPlayer= PhotoImage(file=pastaApp+f"{pst}{mov}")
        l_player = Label(app, image=imgPlayer)
        l_player.place(x=mov_x, y=10)
        app.update()
        sleep(0.05) # altera velocidade de transição
        if i == 1 or 4:
            mov_x += 17 # altera distância de percurso
    if mov_x >= 500:
        mov_x = -30 #vai para posição inicial

app.mainloop()