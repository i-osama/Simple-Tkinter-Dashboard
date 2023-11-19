
from pathlib import Path
# from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\PROGRAMMING\Python\GUI\Practice 1 (f)\build\assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("870x600")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 870,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    870.0,
    96.0,
    fill="#A00AAD",
    outline="")

canvas.create_text(
    79.0,
    16.0,
    anchor="nw",
    text="ZeeBook",
    fill="#FFFFFF",
    font=("MontserratRoman Bold", 48 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    224.0,
    157.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    432.0,
    261.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    641.0,
    157.0,
    image=image_image_3
)

canvas.create_text(
    63.0,
    130.0,
    anchor="nw",
    text="Income",
    fill="#711D1D",
    font=("MontserratRoman Bold", 22 * -1)
)

canvas.create_text(
    100.0,
    234.0,
    anchor="nw",
    text="Balance",
    fill="#164D64",
    font=("MontserratRoman Bold", 22 * -1)
)

canvas.create_text(
    480.0,
    130.0,
    anchor="nw",
    text="Expense",
    fill="#135024",
    font=("MontserratRoman Bold", 22 * -1)
)

canvas.create_text(
    61.0,
    160.0,
    anchor="nw",
    text=" $500 USD",
    fill="#6D0A0A",
    font=("MontserratRoman SemiBold", 16 * -1)
)

canvas.create_text(
    96.0,
    264.0,
    anchor="nw",
    text=" $240 USD",
    fill="#164D64",
    font=("MontserratRoman SemiBold", 16 * -1)
)

canvas.create_text(
    478.0,
    160.0,
    anchor="nw",
    text=" $1000 USD",
    fill="#135024",
    font=("MontserratRoman SemiBold", 16 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    710.0,
    453.0,
    image=image_image_4
)

canvas.create_text(
    42.0,
    321.0,
    anchor="nw",
    text="Add Expense",
    fill="#700579",
    font=("MontserratRoman Bold", 24 * -1)
)

canvas.create_text(
    47.0,
    352.0,
    anchor="nw",
    text="Name",
    fill="#700579",
    font=("MontserratRoman SemiBold", 16 * -1)
)

canvas.create_text(
    47.0,
    435.0,
    anchor="nw",
    text="Name",
    fill="#700579",
    font=("MontserratRoman SemiBold", 16 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    203.0,
    401.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=60.5,
    y=379.0,
    width=285.0,
    height=43.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    203.0,
    481.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=60.5,
    y=459.0,
    width=285.0,
    height=43.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=42.0,
    y=521.0,
    width=326.0,
    height=57.0
)
window.resizable(False, False)
window.mainloop()
