import tkinter as tk
from PIL import ImageTk, Image
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
        width = int(width * .5)
        height = int(height * .5)
        image_name = image_name.resize((width, height))
        size = 40
    elif width >= 2000 or height >= 2000:
        width = int(img_size[0] * .1)
        height = int(img_size[1] * .1)
        image_name = image_name.resize((width, height))
    img = ImageTk.PhotoImage(image_name)
    canvas = tk.Canvas(window, width = width, height=height)
    canvas.grid(row=4, column=1, columnspan=2)
    canvas.create_image(0, 0,image=img, anchor="nw")
    canvas.create_text(width/2,height/2,font=("Helvetica", size), fill="#ffffff", text=mark, anchor="center")
    canvas.image = img


get_image_button = tk.Button(window, text="Upload Image", command=get_image)
get_image_button.grid(row=3, column=1, columnspan=2)

window.mainloop()