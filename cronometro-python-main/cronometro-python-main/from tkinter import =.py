from tkinter import *

# Cores
cor1 = "#0a0a0a"  # black / preta
cor2 = "#fafcff"  # white / branca
cor3 = "#21c25c"  # green / verde
cor4 = "#eb463b"  # red / vermelha
cor5 = "#dedcdc"  # gray / Cizenta
cor6 = "#3080f0"  # blue / azul

janela = Tk()
janela.title("")
janela.geometry('300x180')
janela.configure(bg=cor1)
janela.resizable(width=False, height=False)

global tempo
global rodar
global contador

tempo = "00:00:00"
rodar = False
contador = 0

def iniciar():
    global tempo
    global contador

    if rodar:
        if contador < 0:
            inicio = 'Começando em ' + str(-contador)
            label_tempo['text'] = inicio
            label_tempo['font'] = 'Arial 10'
        else:
            label_tempo['font'] = 'Times 50 bold'

            h, m, s = map(int, tempo.split(":"))
            s += 1
            if s == 60:
                s = 0
                m += 1
            if m == 60:
                m = 0
                h += 1

            h = str(h).zfill(2)
            m = str(m).zfill(2)
            s = str(s).zfill(2)

            temporario = f"{h}:{m}:{s}"
            label_tempo['text'] = temporario
            tempo = temporario

        label_tempo.after(1000, iniciar)
        contador += 1

def start():
    global rodar
    rodar = True
    iniciar()

def pausar():
    global rodar
    rodar = False

def reiniciar():
    global contador
    global tempo

    contador = 0
    tempo = "00:00:00"
    label_tempo['text'] = tempo

label_app = Label(janela, text='Cronômetro', font=('Arial 10'), bg=cor1, fg=cor2)
label_app.place(x=20, y=5)

label_tempo = Label(janela, text=tempo, font=('Times 50 bold'), bg=cor1, fg=cor6)
label_tempo.place(x=20, y=30)

botao_iniciar = Button(janela, command=start, text='Iniciar', width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
botao_iniciar.place(x=190, y=130)

botao_pausar = Button(janela, command=pausar, text='Pausar', width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
botao_pausar.place(x=105, y=130)

botao_reiniciar = Button(janela, command=reiniciar, text='Reiniciar', width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
botao_reiniciar.place(x=20, y=130)

janela.mainloop()v