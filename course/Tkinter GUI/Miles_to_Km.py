import tkinter

window = tkinter.Tk()
window.title("Mile to KM converter")
# window.minsize(300, 300)
window.config(padx=20,pady=20)

label_1 = tkinter.Label(window, text="Miles")
label_1.grid(row=0, column=2)
window.config(padx=20,pady=20)

label_2 = tkinter.Label(window, text="Km")
label_2.grid(row=1, column=2)
window.config(padx=20,pady=20)

label_3 = tkinter.Label(window, text="is equal to")
label_3.grid(row=1, column=0)
window.config(padx=20,pady=20)

KM_value = tkinter.Label(window, text="0")
KM_value.grid(row=1, column=1)
window.config(padx=20,pady=20)

#input
input = tkinter.Entry(window, width=30)
input.grid(row=0, column=1)
window.config(padx=20,pady=20)

#button
def action():
    km = int(input.get()) * 1.609344 
    KM_value.config(text=str(km))

button = tkinter.Button(window, text="Calculate", command=action)
button.grid(row=2, column=1)
window.config(padx=20,pady=20)

window.mainloop()  # This should be at the end