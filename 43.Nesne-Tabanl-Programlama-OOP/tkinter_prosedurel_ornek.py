## Tkinter

import tkinter

pencere = tkinter.Tk()
pencere.geometry("400x400")

etiket = tkinter.Label(text = 'merhaba Zalim Dünya !!!')
etiket.pack()

dugme = tkinter.Button(text = 'Tamam', command = pencere.destroy)
dugme.pack()

pencere.mainloop()
