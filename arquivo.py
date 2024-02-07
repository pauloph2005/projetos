



from tkinter import *

def btn_click(num):
    current = entrada.get()
    entrada.delete(0, END)
    entrada.insert(0, current + str(num))

def btn_clear():
    entrada.delete(0, END)

def btn_equal():
    expression = entrada.get()
    result = eval(expression)
    entrada.delete(0, END)
    entrada.insert(0, result)

janela = Tk()
janela.title("Calculadora")

entrada = Entry(janela, width=25, borderwidth=5)
entrada.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Definindo os botões
btn_1 = Button(janela, text="1", padx=20, pady=10, command=lambda: btn_click(1))
btn_2 = Button(janela, text="2", padx=20, pady=10, command=lambda: btn_click(2))
btn_3 = Button(janela, text="3", padx=20, pady=10, command=lambda: btn_click(3))
btn_4 = Button(janela, text="4", padx=20, pady=10, command=lambda: btn_click(4))
btn_5 = Button(janela, text="5", padx=20, pady=10, command=lambda: btn_click(5))
btn_6 = Button(janela, text="6", padx=20, pady=10, command=lambda: btn_click(6))
btn_7 = Button(janela, text="7", padx=20, pady=10, command=lambda: btn_click(7))
btn_8 = Button(janela, text="8", padx=20, pady=10, command=lambda: btn_click(8))
btn_9 = Button(janela, text="9", padx=20, pady=10, command=lambda: btn_click(9))
btn_0 = Button(janela, text="0", padx=20, pady=10, command=lambda: btn_click(0))

btn_add = Button(janela, text="+", padx=19, pady=10, command=lambda: btn_click("+"))
btn_subtract = Button(janela, text="-", padx=20, pady=10, command=lambda: btn_click("-"))
btn_multiply = Button(janela, text="*", padx=20, pady=10, command=lambda: btn_click("*"))
btn_divide = Button(janela, text="/", padx=20, pady=10, command=lambda: btn_click("/"))
btn_clear = Button(janela, text="C", padx=19, pady=10, command=btn_clear)
btn_equal = Button(janela, text="=", padx=19, pady=10, command=btn_equal)

# Posicionando os botões na tela
btn_1.grid(row=1, column=0)
btn_2.grid(row=1, column=1)
btn_3.grid(row=1, column=2)

btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)

btn_7.grid(row=3, column=0)
btn_8.grid(row=3, column=1)
btn_9.grid(row=3, column=2)

btn_0.grid(row=4, column=0)
btn_add.grid(row=4, column=1)
btn_subtract.grid(row=4, column=2)

btn_multiply.grid(row=5, column=0)
btn_divide.grid(row=5, column=1)
btn_clear.grid(row=5, column=2)

btn_equal.grid(row=6, column=0)

janela.mainloop()

