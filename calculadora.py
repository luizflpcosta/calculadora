import tkinter as tk

# definição das cores

cores = {
    'preta' : '#3b3b3b',
    'branco' : '#feffff',
    'azul_escuro' : '#38576b',
    'cinzenta' : '#ECEFF1',
    'laranja' : '#FFAB40'
}

# armazena a expressão

expressao = ''

# atualiza entrada na calculadora

def atualizar_entrada(valor):
    global expressao
    expressao += str(valor)
    app_label.config(text=expressao)

# avalia a expressão matemática e mostra o resultado
def avaliar_expressao():
    global expressao
    try:
        resultado = (eval(expressao))
        if isinstance(resultado, float) and resultado.is_integer():
            resultado = int(resultado) # converte para inteiro se o resultado for inteiro
        app_label.config(text=resultado)
        expressao = resultado
    except Exception as e:
        app_label.config(text='Erro')
        expressao = ''

# função para limpar a entrada na calculadora
def limpar_entrada():
    global expressao
    expressao = ''
    app_label.config(text='')

# funcao para criar botoes de forma simplificada
def criar_botao(texto, linha, coluna, columnspan=1, comando=None, bg=cores['cinzenta'], fg=cores['preta']):
    botao = tk.Button(frame_corpo, text=texto, width=5, height=2, bg=bg, fg=fg, font=('Ivy 13 bold'), relief=tk.RAISED, overrelief=tk.RIDGE, command=comando)
    botao.grid(row=linha, column=coluna, columnspan=columnspan, sticky='nsew')
    return botao


# criando a janela principal
janela = tk.Tk()
janela.title('Calculadora')
janela.geometry('235x310')
janela.config(bg=cores['preta'])

# criando frames
frame_tela = tk.Frame(janela, width=235, height=50, bg=cores['azul_escuro'])
frame_tela.grid(row=0, column=0)

frame_corpo = tk.Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

# Criando o label para mostrar a expressão e o resultado
app_label = tk.Label(frame_tela, width=16, height=2, padx=7, relief=tk.FLAT, anchor='e', justify=tk.RIGHT, font=('Ivy 18'), bg=cores['azul_escuro'], fg=cores['branco'])
app_label.place(x=0, y=0)

# Criando os botões da calculadora
botoes = [
    ('C', 0, 0, 2, limpar_entrada),
    ('%', 0, 2, 1, lambda: atualizar_entrada('%')),
    ('/', 0, 3, 1, lambda: atualizar_entrada('/'), cores['laranja'], cores['branco']),
    ('7', 1, 0, 1, lambda: atualizar_entrada('7')),
    ('8', 1, 1, 1, lambda: atualizar_entrada('8')),
    ('9', 1, 2, 1, lambda: atualizar_entrada('9')),
    ('X', 1, 3,1, lambda: atualizar_entrada('*'), cores['laranja'], cores['branco']),
    ('4', 2, 0, 1, lambda: atualizar_entrada('4')),
    ('5', 2, 1, 1, lambda: atualizar_entrada('5')),
    ('6', 2, 2, 1, lambda: atualizar_entrada('6')),
    ('-', 2, 3, 1, lambda: atualizar_entrada('-'), cores['laranja'], cores['branco']),
    ('1', 3, 0, 1, lambda: atualizar_entrada('1')),
    ('2', 3, 1, 1, lambda: atualizar_entrada('2')),
    ('3', 3, 2, 1, lambda: atualizar_entrada('3')),
    ('+', 3, 3, 1, lambda: atualizar_entrada('+'), cores['laranja'], cores['branco']),
    ('0', 4, 0, 2, lambda: atualizar_entrada('0')),
    ('.', 4, 2, 1, lambda: atualizar_entrada('.')),
    ('=', 4, 3, 1, avaliar_expressao, cores['laranja'], cores['branco'])
]

# Iterando sobre a lista de botões e criando-os na interface
for botao in botoes:
    criar_botao(*botao)

janela.mainloop()