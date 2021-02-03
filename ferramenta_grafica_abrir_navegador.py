import webbrowser  # interface de alto nivel para exibir documentos web
from tkinter import *      # interface padrao python para ferramentas graficas

root = Tk( )  # nome do sistema
root.title('Abrir Browser')
root.geometry('300x200') # tamanho do sistema

def google():
    webbrowser.open('www.google.com')


mygoogle = Button(root, text='Abrir o Google', command=google).pack(pady=20)
root.mainloop()

