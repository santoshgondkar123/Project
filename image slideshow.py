import tkinter as tk
from itertools import cycle
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Image Slideshow Viewer")

# list of image paths
image_paths = [
    r"C:\Users\GAJANAN RATHOD\Downloads\python.jpg",
    r"C:\Users\GAJANAN RATHOD\Downloads\java.jpg",
    r"C:\Users\GAJANAN RATHOD\Downloads\car1.jpeg",
]

# load and resize images
images = []
for path in image_paths:
    img = Image.open(path)
    img = img.resize((600, 400))  # resize as needed
    images.append(ImageTk.PhotoImage(img))

# create an endless cycle of images
image_cycle = cycle(images)

label = tk.Label(root)
label.pack()

def update_image():
    photo = next(image_cycle)
    label.config(image=photo)
    label.image = photo  # prevent garbage collection
    root.after(3000, update_image)  # change every 3 seconds

play_button = tk.Button(root, text="Play Slideshow", command=update_image)
play_button.pack(pady=10)

root.mainloop()
