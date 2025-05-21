#modulo tkinter sempre que precisarmos
# de interface de usuario
from tkinter import *

#class Gui (Graphical User Interface)
# se refere a interface do usuario
class Gui():
    """Classe da Interface Gráfica
    """
    #3 variaveis referidas ao padding
    # que estabelece o distanciamento
    # entre o conteudo de um elemento
    # e sua borda
    x_pad = 5
    y_pad = 3
    width_entry = 30 #define a largura da janela

    #Para Criar uma Janela
    #PYSQL sera o nome fantasia da aplicacao
    window = Tk()
    window.wm_title("PYSQL versao 1.0")

    #Definicao das variaveis que recebem
    # os dados inseridos pelo User
    txtNome = StringVar()
    txtSobrenome = StringVar()
    txtEmail = StringVar()
    txtCPF = StringVar()

    #Criando os objetos que farao parte das janelas
    lblnome = Label(window, text="Nome")
    lblsobrenome = Label(window, text="Sobrenome")
    lblemail = Label(window, text="Email")
    lblcpf = Label(window, text="CPF")

    entNome = Entry(window, textvariable=txtNome, width=width_entry)
    entSobrenome = Entry(window, textvariable=txtSobrenome, width=width_entry)
    entEmail = Entry(window, textvariable=txtEmail, width=width_entry)
    entCPF = Entry(window, textvariable=txtCPF, width=width_entry)

    listClientes = Listbox(window, width=100)
    scrollClientes = Scrollbar(window)
    btnViewAll = Button(window, text="Ver Todos")
    btnBuscar = Button(window, text="Buscar")
    btnInserir = Button(window, text="Inserir")
    btnUpdate = Button(window, text="Atualizar Selecionados")
    btnDelete = Button(window, text="Deletar Selecionados")
    btnClose = Button(window, text="Fechar")

    #Agora associamos os objetos ao Grid da janela
    lblnome.grid(column=0, row=0)
    lblsobrenome.grid(column=0, row=1)
    lblemail.grid(column=0, row=2)
    lblcpf.grid(column=0, row=3)

    entNome.grid(column=1, row=0, padx=50, pady=50)
    entSobrenome.grid(column=1, row=1)
    entEmail.grid(column=1, row=2)
    entCPF.grid(column=1, row=3)

    listClientes.grid(column=2, row=0, rowspan=10)
    scrollClientes.grid(column=6, row=1, rowspan=10)

    btnViewAll.grid(column=0, row=4, columnspan=2)
    btnBuscar.grid(column=0, row=5, columnspan=2)
    btnInserir.grid(column=0, row=6, columnspan=2)
    btnUpdate.grid(column=0, row=7, columnspan=2)
    btnDelete.grid(column=0, row=8, columnspan=2)
    btnClose.grid(column=0, row=9, columnspan=2)

    #Uniao do Scrollbar com a Listbox
    listClientes.configure(yscrollcommand=scrollClientes.set)
    scrollClientes.configure(command=listClientes.yview)

    #Adicionar SWAG (aparencia) para a interface
    for child in window.winfo_children():
        widget_class =child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
        elif widget_class == "Listbox":
                child.grid_configure(padx=0, pady=0, sticky='NS')
        elif widget_class == "Scrollbar":
                child.grid_configure(padx=0, pady=0, sticky='NS')
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='NS')
    def run(self):
        Gui.window.mainloop()
if __name__ == "__main__":
    gui = Gui()
    gui.run()
