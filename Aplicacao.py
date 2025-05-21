from GUI import *
import Backend as core
from tkinter import messagebox

core.TransactionObject().initDB()

app = None
selected = None

def view_command():
    rows = core.TransactionObject.view()
    app.listClientes.delete(0,END)
    for r in rows:
        app.listClientes.insert(END,r)

def search_command():
    app.listClientes.delete(0, END)

    db = core.TransactionObject()
    rows = db.search(
        app.txtNome.get(),
        app.txtSobrenome.get(),
        app.txtEmail.get(),
        app.txtCPF.get()
    )

    for r in rows:
        app.listClientes.insert(END, r)

def insert_command():
    core.TransactionObject.insert(
        app.txtNome.get(),
        app.txtSobrenome.get(),
        app.txtEmail.get(),
        app.txtCPF.get())
    view_command()

def update_command():
    if selected is not None:
        core.TransactionObject.update(
            selected[0],
            app.txtNome.get(),
            app.txtSobrenome.get(),
            app.txtEmail.get(),
            app.txtCPF.get()
        )
        view_command()
    else:
        messagebox.showwarning("Aviso", "Nenhum cliente selecionado para atualizar.")

def del_command():
    id = selected[0]
    core.TransactionObject.delete(id)
    view_command()

def getSelectedRow(event):
    global selected

    selection = app.listClientes.curselection()
    if not selection:
        messagebox.showwarning("Aviso", "Nenhum cliente selecionado!")
        selected = None
        return

    index = selection[0]
    selected = app.listClientes.get(index)

    app.entNome.delete(0, END)
    app.entNome.insert(END, selected[1])
    app.entSobrenome.delete(0, END)
    app.entSobrenome.insert(END, selected[2])
    app.entEmail.delete(0, END)
    app.entEmail.insert(END, selected[3])
    app.entCPF.delete(0, END)
    app.entCPF.insert(END, selected[4])

if __name__=='__main__':
    app = Gui()
    app.listClientes.bind('<<ListboxSelect>>', getSelectedRow)

    app.btnViewAll.configure(command=view_command)
    app.btnBuscar.configure(command=search_command)
    app.btnInserir.configure(command=insert_command)
    app.btnUpdate.configure(command=update_command)
    app.btnDelete.configure(command=del_command)
    app.btnClose.configure(command=app.window.destroy)
    app.run()