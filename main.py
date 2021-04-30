from tkinter import Tk, filedialog, Button
import PIL

def open_file():
    file = filedialog.askopenfilename()




window = Tk()
window.title("Watermarkingapp")
window.minsize(width=400, height=400)


browse_files = Button(text="Browse files", font=("arial", 16, "normal"), command=open_file,)
browse_files.grid(column=0, row=0)









window.mainloop()
