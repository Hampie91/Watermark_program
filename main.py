from tkinter import Tk, filedialog, Button, Canvas, PhotoImage, Label
from PIL import ImageTk, Image

def open_file():
    canvas = Canvas(window, width=400, height=400)

    canvas.grid(row=2, column=2, columnspan=3)
    pic = filedialog.askopenfilename()
    with Image.open(pic) as im:
        (width, height) = (im.width // 7, im.height // 7)
        img = im.resize((width, height))
        img = ImageTk.PhotoImage(img)
        canvas.create_image(200, 200, image=img)
        canvas.image = img  # keep reference to the image




window = Tk()
window.title("Watermarkingapp")
window.minsize(width=400, height=400)


browse_files = Button(text="Browse files", font=("arial", 16, "normal"), command=open_file,)
browse_files.grid(column=0, row=0)









window.mainloop()
