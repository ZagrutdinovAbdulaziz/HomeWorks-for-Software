import tkinter as tk
from tkinter import messagebox

font_header = ('Arial', 15)
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
entry_font = ('Arial', 12, 'bold')
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}

class Hotel(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)


        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)



        self.frames = {}
        for F in (MainPage, LoginPage, ):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame


            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainPage")

    def show_frame(self, page_name):

        frame = self.frames[page_name]
        frame.tkraise()


class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame = tk.Frame
        self.frame.configure(self, background='#536872')

        self. main_lbl= tk.Label(self,text='Капсула отель', font=label_font, **base_padding,
                                  bg='#CEBCE6')
        self.main_lbl.place(y=5, height=25, width=400)

        self.info = tk.Label(self, text="Стоимость за одну ночь 30$. В стоимость входит завтрак",
                             bg='#FFE042', fg='#2A502A')
        self.info.place(y=25, width=400, height=15)

        self.one_btn = tk.Button(self, text='Капсула1', font='bold', bg='#318FE7',
                                 activebackground='#20B2AA', width=10,
                                 command=lambda: self.basket_ent.insert(0, "Капсула1"))
        self.one_btn.place(y=70, width=150, height=25)

        self.two_btn = tk.Button(self, text='Капсула2', font='bold', bg='#318FE7',
                                 activebackground='#20B2AA', width=10,
                                 command=lambda: self.basket_ent.insert(0, "Капсула2"))
        self.two_btn.place(x=200, y=70, width=150, height=25)

        self.three_btn = tk.Button(self, text='Капсула3', font='bold', bg='#318FE7',
                                   activebackground='#20B2AA', width=10,
                                   command=lambda: self.basket_ent.insert(0, "Капсула3"))
        self.three_btn.place(y=110, width=150, height=25)

        self.fore_btn = tk.Button(self, text='Капсула4', font='bold', bg='#318FE7',
                                  activebackground='#20B2AA', width=10,
                                  command=lambda: self.basket_ent.insert(0, "Капсула4"))
        self.fore_btn.place(x=200, y=110, width=150, height=25)

        self.five_btn = tk.Button(self, text='Капсула5', font='bold', bg='#318FE7',
                                  activebackground='#20B2AA', width=10,
                                  command=lambda: self.basket_ent.insert(0, "Капсула5"))
        self.five_btn.place(y=170, width=150, height=25)

        self.six_btn = tk.Button(self, text='Капсула6', font='bold', bg='#318FE7',
                                 activebackground='#20B2AA', width=10,
                                 command=lambda: self.basket_ent.insert(0, "Капсула6"))
        self.six_btn.place(x=200, y=170, width=150, height=25)

        self.seven_btn = tk.Button(self, text='Капсула7', font='bold', bg='#318FE7',
                                   activebackground='#20B2AA', width=10,
                                   command=lambda: self.basket_ent.insert(0, "Капсула7"))
        self.seven_btn.place( y=220, width=150, height=25)

        self.seven_btn = tk.Button(self, text='Капсула8', font='bold', bg='#318FE7',
                                   activebackground='#20B2AA', width=10,
                                   command=lambda: self.basket_ent.insert(0, "Капсула8"))
        self.seven_btn.place(x=200, y=220, width=150, height=25)

        self.basket_ent = tk.Entry(self, font=label_font,
                                   bg='#3591CD')
        self.basket_ent.place(x=20, y=270, width=350, height=50)



        self.delet_btn = tk.Button(self, text="Удалить", font='bold', bg='#3591CD',
                                   activebackground='#20B2AA', width=20,
                                   command=lambda: self.Delete())
        self.delet_btn.place(x=50, y=400, width=100, height=25)

        self.delet_btn = tk.Button(self, text="Регистрация", font='bold', bg='#3591CD',
                                   activebackground='#20B2AA', width=20,
                                   command=lambda: self.Regist())
        self.delet_btn.place(x=250, y=400, width=100, height=25)

    def Delete(self):
        self.basket_ent.delete(0, tk.END)

    def Regist(self):
        self.controller.show_frame("LoginPage")

class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame = tk.Frame
        self.frame.configure(self, background='#536872')


        self.firstname_label = tk.Label(self, text='Имя', font=label_font, **base_padding,
                                  bg='#F4D000')
        self.firstname_label.place(x=130,y=100,width=150,height=20)
        self.controller.configure(background='#334353')

        self.firstname_entry = tk.Entry(self, bg='#838996', fg='#FDF5E6', font=font_entry)
        self.firstname_entry.place(x=130,y=120,width=150,height=20)


        self.secondname_label = tk.Label(self, text='Фамилия', font=label_font, **base_padding,
                                  bg='#F4D000')
        self.secondname_label.place(x=130,y=200,width=150,height=20)


        self.secondname_entry = tk.Entry(self,  bg='#838996', fg='#FDF5E6', font=font_entry)
        self.secondname_entry.place(x=130,y=220,width=150,height=20)


        self.send_btn = tk.Button(self, text='Забронировать', font='bold',  bg='#318FE7',
                                  activebackground='#20B2AA', width=10,
                                  command=lambda: self.MsgBox())
        self.send_btn.place(x=100,y=300,width=200,height=25)

    def MsgBox(self):
        messagebox.showinfo("Успешно!")


if __name__ == "__main__":
    app = Hotel()

    app.title("Отель")
    app.geometry("400x500")
    app.resizable(False, False)

    app.grid_columnconfigure(0, minsize=100)
    app.mainloop()