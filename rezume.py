from tkinter import *
 
root = Tk()
root.title("Резюме")
root.geometry("400x200")
 
name = StringVar()
surname = StringVar()
midname = StringVar()
town = StringVar()
 
name_label = Label(text="Введите имя:")
surname_label = Label(text="Введите фамилию:")
midname_label = Label(text="Введите отчество:")
town_label = Label(text="Введите город:") 

name_label.grid(row=0, column=0, sticky="w")
surname_label.grid(row=1, column=0, sticky="w")
midname_label.grid(row=2, column=0, sticky="w")
town_label.grid(row=3, column=0, sticky="w")
 
name_entry = Entry(textvariable=name)
surname_entry = Entry(textvariable=surname)
midname_entry = Entry(textvariable=midname)
town_entry = Entry(textvariable=town)
 
name_entry.grid(row=0, column=1, padx=5, pady=5)
surname_entry.grid(row=1, column=1, padx=5, pady=5)
midname_entry.grid(row=2, column=1, padx=5, pady=5)
town_entry.grid(row=3, column=1, padx=5, pady=5)
 
header = Label(text="Выберите возраст:", padx=15, pady=10)
header.grid(row=0, column=30, sticky=W)

lang = IntVar()

age1 = Radiobutton(text="5-10", value=1, variable=lang, padx=15, pady=10)
age1.grid(row=1, column=30, sticky=W)

age2 = Radiobutton(text="10-16", value=2, variable=lang, padx=15, pady=10)
age2.grid(row=2, column=30, sticky=W)

age3 = Radiobutton(text="16-25", value=3, variable=lang, padx=15, pady=10)
age3.grid(row=3, column=30, sticky=W)

root.mainloop()