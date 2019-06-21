import tkinter

main_window = tkinter.Tk()


def event_hitung():
    label2 = tkinter.Label(main_window, text= "Saya dicari")
    label2.pack()

label = tkinter.Label(main_window, text="Halo saya \n adalah program sederhana")
tombol = tkinter.Button(main_window, text="Cari hasil", command = event_hitung)

label.pack()
tombol.pack()

main_window.mainloop()