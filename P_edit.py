from tkinter import *
from tkinter import filedialog,messagebox,simpledialog

root = Tk()


class Pedit():
    of = 1
    def __init__(self,master):
        master.title("P_edit")
        self.text_area = Text(master, undo=True)
        self.text_area.pack(fill = BOTH , expand=1)
        self.m = Menu(master)
        self.fmenu= Menu(self.m, tearoff = False)
        self.m.add_cascade(label="File", menu=self.fmenu)
        self.fmenu.add_command(label="New", command=self.new)
        self.fmenu.add_command(label="Open", command=self.open_file)
        self.fmenu.add_separator()
        self.fmenu.add_command(label="Save", command=self.save_file)
        self.fmenu.add_command(label="Save As", command=self.save_as_file)
        self.fmenu.add_separator()
        self.fmenu.add_command(label="Exit", command=master.quit)
        self.emenu = Menu(self.m, tearoff = False)
        self.m.add_cascade(label="Edit", menu=self.emenu)
        self.emenu.add_command(label="Copy", command=self.copy)
        self.emenu.add_command(label="Cut", command=self.cut)
        self.emenu.add_command(label="Paste", command=self.paste)
        self.emenu.add_separator()
        self.emenu.add_command(label="Redo", command=self.text_area.edit_redo)
        self.emenu.add_command(label="Undo", command=self.text_area.edit_undo)
        self.a = Menu(self.m, tearoff=False)
        self.m.add_cascade(label="About Us", menu=self.a)
        self.a.add_command(label="Details" , command=self.new_win)

        master.bind("<Control-s>",self.save_file)
        master.bind("<Control-Shift-s>",self.save_as_file)
        master.bind("<Control-o>",self.open_file)
        master.bind("<Control-c>",self.copy)
        master.bind("<Control-x>", self.cut)
        master.bind("<Control-v>",self.paste)
        master.bind("<Control-n>",self.new)
        master.bind("<Control-y>",self.text_area.edit_redo)
        master.bind("<Control-z>",self.text_area.edit_undo)
        master.bind("<Control-q>",master.quit)
        master.config(menu=self.m)

    def save_file(self,event=""):
        if self.of==1:
            self.save_as_file()
        else:
            f = open(self.of, "w+")
            f.write(self.text_area.get(1.0, END))
            f.close()

    def open_file(self,event=""):
        self.f = filedialog.askopenfile(initialdir='D:\\', title="Open", filetypes=(("Text Files",".txt"),("All Files","*.*")))
        if self.f!=None:
            self.text_area.delete(1.0, END)
            self.of = self.f.name
            for i in self.f:
                self.text_area.insert(END, i)


    def save_as_file(self,event=""):
        try:
            self.f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
            self.f.write(self.text_area.get(1.0, END))
            self.of = self.f.name
            self.f.close()
        except:
            return


    def new(self,event=""):
        self.text_area.delete(1.0,END)
        self.of=1

    def copy(self,event=""):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())

    def cut(self,event=""):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())
        self.text_area.delete("sel.first","sel.last")

    def paste(self,event=""):
        self.text_area.insert(END,self.text_area.clipboard_get())




    def new_win(self):
        st = "This Is Basic Text Editor Made for practice of Programming.\nPlease Give Suggestions if Any Mistake in this App.\nBy:-Parag Bharadva"

        messagebox.showinfo("About Us",st)













pe = Pedit(root)
root.mainloop()



















