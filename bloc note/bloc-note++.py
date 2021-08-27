
import tkinter
from tkinter import messagebox
from tkinter.filedialog import *
import os


class Fenetre:
    def __init__(self,geo,name):
        self.app = tkinter.Tk()
        self.name = name
        self.geometry = geo
        self.text = ""
        self.file = ""
        
    def creat_app(self):
 
        self.app.title(self.name)
        self.app.geometry(self.geometry)
        self.app.iconbitmap('bloc_note.ico')
        self.app.mainloop()


    def creat_text(self):
        self.saisie = tkinter.StringVar()
        self.text = tkinter.Text(self.app,height=700,width=600,bg="#e8e6e1",fg="#000",font ="arial")
        self.text.pack()

    def a_propos(self):

        
        messagebox.showinfo("bloc-note++","\nbloc-note++\n\n© Copyright PyDev\n\nle projet a débuté le 24/08/2021")

        


    def detete(self):
        self.text.delete("0.0","end")

    def save_as(self):
        filepath = asksaveasfilename(title="save as",filetypes=[('txt files','.txt')])
        self.file = filepath
        liste = self.file.split(".")
        if len(liste) - 1 == "txt":
            with open(filepath,"w") as file:
                file.write(str(self.text.get(index1="0.0",index2=tkinter.END)))
                file.close()
        elif self.file == "":
            messagebox.showwarning("error","please select a file .txt")
        else:
            try:
                with open(filepath + ".txt","w") as file:
                    file.write(str(self.text.get(index1="0.0",index2=tkinter.END)))
                    file.close()
            except:
                messagebox.showwarning("error","please select a file .txt")


    def save(self):
        if self.file == "":
            filepath = asksaveasfilename(title="save as",filetypes=[('txt files','.txt')])
            self.file = filepath
            liste = self.file.split(".")
            if len(liste) - 1 == "txt":
                with open(filepath,"w") as file:
                    file.write(str(self.text.get(index1="0.0",index2=tkinter.END)))
                    file.close()
            elif self.file == "":
                messagebox.showwarning("error","please select a file .txt")

            else:
                try:
                    with open(filepath + ".txt","w") as file:
                        file.write(str(self.text.get(index1="0.0",index2=tkinter.END)))
                        file.close()
                except:
                    messagebox.showwarning("error","veuillez donner un fichier .txt")
        else:
            with open(self.file,"w") as file:
                file.write(str(self.text.get(index1="0.0",index2=tkinter.END)))
                file.close()

    def open_file(self):
        filepath = askopenfilename(title="save as",filetypes=[('txt files','.txt')])
        self.file = filepath
        if self.file == "":
            messagebox.showwarning("error","please select a file .txt")
        try:
            with open(filepath,"r") as file:
                
                self.text.delete("0.0","end")
                self.text.insert("0.0",str(file.read()))
        except FileNotFoundError:
            messagebox.showerror("error",f"can not found this file  ")
            self.file = ""
            

    def copy(self):
        self.app.clipboard_append(str(self.text.get(index1="0.0",index2=tkinter.END)))
        
    def past(self):
        self.text.insert("0.0", self.app.clipboard_get())
        
            
           

    def creat_menu(self):
        menu = tkinter.Menu(self.app)
        first_menu = tkinter.Menu(menu)
        seconde_menu = tkinter.Menu(menu)
        seconde_menu.add_command(label="delete all", command=self.detete)
        seconde_menu.add_command(label="quit", command=self.app.destroy)
        seconde_menu.add_command(label="copy all", command=self.copy)
        seconde_menu.add_command(label="paste", command=self.past)
        seconde_menu.add_command(label="")
        seconde_menu.add_command(label="à propos", command=self.a_propos)
        first_menu.add_command(label="save as", command=self.save_as)
        first_menu.add_command(label="save", command=self.save)
        first_menu.add_command(label="open", command=self.open_file)
        menu.add_cascade(label="files",menu=first_menu)
        menu.add_cascade(label="tools",menu=seconde_menu)
        self.app.config(menu=menu)
        print(self.file)

fenetre = Fenetre("700x600","bloc-note++")
fenetre.creat_text()
fenetre.creat_menu()
print(fenetre.file)
fenetre.creat_app()
print(fenetre.file)
