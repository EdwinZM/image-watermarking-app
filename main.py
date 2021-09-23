import tkinter as tk

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
    watermark = watermark.get()
    print(watermark)

get_image_button = tk.Button(window, text="Upload Image", command=get_image)
get_image_button.grid(row=3, column=1, columnspan=2)

window.mainloop()