import tkinter as tk
window = tk.Tk()
greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()

label = tk.Label(text="Hello, Tkinter")
label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  
    background="black"  
)
label.pack()
label1 = tk.Label(text="Hello, Tkinter", background="#34A2FE")
label1.pack()
label2 = tk.Label(text="Hello, Tkinter", fg="white", bg="black")
label2.pack()

label3 = tk.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=10,
    height=10
)
label3.pack()

button = tk.Button(     
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
button.pack()

entry = tk.Entry(fg="yellow", bg="blue", width=50)
entry.pack()

label4= tk.Label(text="Name")
entry1 = tk.Entry()
name = entry1.get()
name
entry1.delete(0)
entry1.delete(0, 4)
entry1.delete(0, tk.END)

entry1.insert(0, "Python")
entry1.insert(0, "Real ")
label4.pack()
entry1.pack()
window.destroy()

window = tk.Tk()
text_box = tk.Text()
text_box.get("1.0")
text_box.delete("1.0")
text_box.insert("1.0", "Hello")

text_box.insert("2.0", "\nWorld")
text_box.insert(tk.END, "Put me at the end!")

text_box.pack()
window.destroy()

window = tk.Tk()
frame = tk.Frame()
label5 = tk.Label(master=frame,text="a")
label5.pack()
frame.pack()


frame_a = tk.Frame()
label_a = tk.Label(master=frame_a, text="I'm in Frame A")
label_a.pack()

frame_b = tk.Frame()
label_b = tk.Label(master=frame_b, text="I'm in Frame B")
label_b.pack()


frame_a.pack()
frame_b.pack()


frame_c = tk.Frame()
label_c = tk.Label(master=frame_a, text="I'm in Frame A")
label_c.pack()

frame_d = tk.Frame()
label_d = tk.Label(master=frame_b, text="I'm in Frame B")
label_d.pack()


frame_d.pack()
frame_c.pack()
window.destroy()

border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

window = tk.Tk()

for relief_name, relief in border_effects.items():
    frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=relief_name)
    label.pack()
window.destroy()

window = tk.Tk()

frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
frame1.pack()

frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
frame2.pack()

frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
frame3.pack()

frame4 = tk.Frame(master=window, height=100, bg="red")
frame4.pack(fill=tk.X)

frame5 = tk.Frame(master=window, height=50, bg="yellow")
frame5.pack(fill=tk.X)

frame6 = tk.Frame(master=window, height=25, bg="blue")
frame6.pack(fill=tk.X)

frame7= tk.Frame(master=window, width=200, height=100, bg="red")
frame7.pack(fill=tk.Y, side=tk.LEFT)

frame8 = tk.Frame(master=window, width=100, bg="yellow")
frame8.pack(fill=tk.Y, side=tk.LEFT)

frame9 = tk.Frame(master=window, width=50, bg="blue")
frame9.pack(fill=tk.Y, side=tk.LEFT)

frame10 = tk.Frame(master=window, width=200, height=100, bg="red")
frame10.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame11= tk.Frame(master=window, width=100, bg="yellow")
frame11.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame12 = tk.Frame(master=window, width=50, bg="blue")
frame12.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

window.destroy()

window = tk.Tk()

frame = tk.Frame(master=window, width=150, height=150)
frame.pack()

label13= tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
label13.place(x=0, y=0)

label14 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow")
label14.place(x=75, y=75)
window.destroy()

window = tk.Tk()

for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j,padx=5, pady=5)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack(padx=5, pady=5)
window.destroy()


window = tk.Tk()


def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)
window.bind("<Key>", handle_keypress)

def handle_click(event):
    print("The button was clicked!")

button = tk.Button(text="Click me!")

button.bind("<Button-1>", handle_click)

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)



btn_decrease = tk.Button(master=window, text="-",  )
btn_decrease.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(master=window, text="0")
lbl_value.grid(row=0, column=1)

btn_increase = tk.Button(master=window, text="+",)
btn_increase.grid(row=0, column=2, sticky="nsew")
window.mainloop()







