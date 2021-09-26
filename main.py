import tkinter as tk
from PIL import ImageTk, Image, ImageGrab
from tkinter import filedialog as fd



window = tk.Tk()
window.title("Image Watermarking App")
window.minsize(width="430", height="320")
window.config(padx=10, pady=20)
window.grid_columnconfigure(2, weight=1)

start_label = tk.Label(text="Welcome to the Image Watermarking App!", font=("Helvetica", 18, "bold"))
start_label.grid(row=1, column=1, columnspan=2)
# start_label.pack()

watermark_label = tk.Label(text="Enter your watermark:")
watermark_label.grid(row=2, column=1, sticky="E", pady=30)

watermark = tk.Entry()
watermark.grid(row=2, column=2, sticky="W")

def get_image():
    global watermark
    mark = watermark.get()
    print(mark)

    file = fd.askopenfilename()
    print(file)
    image_name = Image.open(file)
    img_size = image_name.size
    width = img_size[0]
    height = img_size[1]
    size = 30
    if (width >= 1000 and width < 2000) or (height >= 1000 and height < 2000):
        width = int(width * .4)
        height = int(height * .4)
        image_name = image_name.resize((width, height))
        size = 40
    elif width >= 2000 or height >= 2000:
        width = int(img_size[0] * .1)
        height = int(img_size[1] * .1)
        image_name = image_name.resize((width, height))
    img = ImageTk.PhotoImage(image_name)
    canvas = tk.Canvas(width=width, height=height, border=None)
    canvas.grid(row=4, column=1, columnspan=2)
    canvas.create_image(0, 0,image=img, anchor="nw")
    canvas.create_text(width/2,height/2,font=("Helvetica", size), fill="#ffffff", text=mark, anchor="center")
    canvas.image = img

    def save_image(): 
        filename = fd.asksaveasfilename(defaultextension=".png")
        x = window.winfo_rootx()+canvas.winfo_x()
        y = window.winfo_rooty()+canvas.winfo_y()
        x1 = x+canvas.winfo_width()
        y1 = y+canvas.winfo_height()
        ImageGrab.grab().crop((x,y,x1,y1)).save(filename)
        window.destroy()


    save_button = tk.Button(text="Save Image", command=save_image)
    save_button.grid(row=5, column=1, columnspan=2)


get_image_button = tk.Button(window, text="Upload Image", command=get_image)
get_image_button.grid(row=3, column=1, columnspan=2)


window.mainloop()