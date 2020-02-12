import tkinter as tk


HEIGHT = 800
WIDTH = 900
COLLORBUTTON='#bfbfbf'
COLORBACKGROUND='#333300'
COLORBUT1='#1a1a1a' # ta czern chyba lepsza #262626 ,a fiolet #1e0033
root = tk.Tk()

canvas=tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()


frameGeneruj=tk.Frame(root, bg=COLORBACKGROUND)
frameGeneruj.place(relwidth=1,relheight=0.3)
buttonGeneruj= tk.Button(frameGeneruj, text="Wygeneruj klucz", activebackground=COLLORBUTTON,bg=COLORBUT1,fg='white')
buttonGeneruj.place( rely=0.1, relx=0.4 , relheight=0.15, relwidth=0.2)


framelewa=tk.Frame(root, bg=COLORBACKGROUND)
framelewa.place(relx=0.0, rely=0.3, relwidth=0.5, relheight=0.7)
entrylewa=tk.Text(framelewa,bg='#bfbfbf')
entrylewa.place(rely=0.2, relx=0.1, relheight=0.7, relwidth=0.8)
buttonlewa= tk.Button(framelewa, text="Zaszyfruj", activebackground=COLLORBUTTON, bg=COLORBUT1,fg='white')
buttonlewa.place( rely=0.9, relx=0.35 , relheight=0.1, relwidth=0.3)
buttonczyta1= tk.Button(framelewa, text="Czytaj z pliku", activebackground=COLLORBUTTON, bg=COLORBUT1,fg='white')
buttonczyta1.place( rely=0.05, relx=0.15 , relheight=0.1, relwidth=0.3)
buttonpisze1= tk.Button(framelewa, text="Zapisz do pliku", activebackground=COLLORBUTTON, bg=COLORBUT1,fg='white')
buttonpisze1.place( rely=0.05, relx=0.55 , relheight=0.1, relwidth=0.3)

#photo = tk.PhotoImage(file = "pobrane.gif")
#w=tk.Label(framelewa,image=photo)
#w.pack()



frameprawa=tk.Frame(root, bg=COLORBACKGROUND)
frameprawa.place(relx=0.5, rely=0.3, relwidth=0.5, relheight=0.7)
entryprawa=tk.Text(frameprawa,bg='#bfbfbf')
entryprawa.place(rely=0.2, relx=0.1, relheight=0.7, relwidth=0.8)
buttonprawa= tk.Button(frameprawa, text="Odszyfruj", activebackground=COLLORBUTTON, bg=COLORBUT1,fg='white')
buttonprawa.place( rely=0.9, relx=0.35 , relheight=0.1, relwidth=0.3)
buttonczyta2= tk.Button(frameprawa, text="Czytaj z pliku", activebackground=COLLORBUTTON, bg=COLORBUT1,fg='white')
buttonczyta2.place( rely=0.05, relx=0.15 , relheight=0.1, relwidth=0.3)
buttonpisze2= tk.Button(frameprawa, text="Zapisz do pliku", activebackground=COLLORBUTTON, bg=COLORBUT1,fg='white')
buttonpisze2.place( rely=0.05, relx=0.55 , relheight=0.1, relwidth=0.3)


#label=tk.Label(frame, text="THIS IS A label", bg='yellow')
#label.pack()

#entry=tk.Entry(frame,bg='green')
#entry.pack()
root.mainloop()
