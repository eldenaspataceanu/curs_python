import tkinter as tk
from tkinter import ttk, Canvas, Frame
from sqlalchemy import create_engine
from PIL import Image, ImageTk

engine = create_engine('mysql+mysqldb://root:Python123!@localhost:3306/proiect_final')


class Application:
    def __init__(self):
        self._window = tk.Tk()
        self._window.geometry('800x600')
        self._window.winfo_toplevel().title('User App')
        self._cursor = engine.execute('SELECT * FROM users')
        self._canvas = Canvas(self._window)
        self._frame = Frame(self._canvas)
        self._header = ['Id', 'Name', 'Address', 'Postcode', 'Location',
                        'Date of birth', 'Professional activities', 'Telefone',
                        'Constituency', 'Political party', 'email', 'Image']
        self._scrollbar = None
        self._img = []

    def _draw(self):

        self._scrollbar = ttk.Scrollbar(self._window, orient='horizontal', command=self._canvas.xview)
        self._scrollbar.pack(side='bottom', fill='x')
        self._canvas.configure(xscrollcommand=self._scrollbar.set)

        self._scrollbar = ttk.Scrollbar(self._window, orient='vertical', command=self._canvas.yview)
        self._scrollbar.pack(side='right', fill='y')
        self._canvas.configure(yscrollcommand=self._scrollbar.set)
        self._canvas.bind('<Configure>', lambda e: self._canvas.configure(scrollregion=self._canvas.bbox("all")))
        self._canvas.create_window((0, 0), window=self._frame, anchor='nw')
        self._canvas.pack(side="top", fill="both", expand=True)

    def _table(self):
        i = 0
        for j, title in enumerate(self._header):
            header = tk.Label(self._frame, text=title, anchor='center', fg='red')
            header.grid(row=i, column=j)
        for user in self._cursor:
            for j in range(len(user)):
                if j == 11:
                    img = Image.open(user[j])
                    resized = img.resize((70, 80))
                    self._img.append(ImageTk.PhotoImage(resized))
                    imagine = tk.Label(self._frame, image=self._img[-1])
                    imagine.grid(row=i + 1, column=j)
                else:
                    label = tk.Label(self._frame, text=user[j], anchor='center')
                    label.grid(row=i + 1, column=j)
            i = i + 1

    def run(self):
        self._draw()
        self._table()
        self._window.mainloop()

#
# with Image.open("images/06fdbbe7-823e-457c-9cf6-3e70964706f9.jpg") as im:
#     im.rotate(0).show()
