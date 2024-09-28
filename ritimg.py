import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import Button, Label, Scale, HORIZONTAL
from PIL import Image, ImageTk, ImageOps, ImageEnhance

root = tk.Tk()
root.title("RitIMG")
root.geometry("600x500")

image = None
img_label = None

def open_image():
    global image, img_label
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    if file_path:
        image = Image.open(file_path)
        img = ImageTk.PhotoImage(image)
        if img_label:
            img_label.config(image=img)
            img_label.image = img
        else:
            img_label = Label(root, image=img)
            img_label.image = img
            img_label.pack()

def save_image():
    global image
    if image:
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
        if save_path:
            image.save(save_path)
            messagebox.showinfo("Save Image", "Image saved successfully!")

def to_grayscale():
    global image
    if image:
        image = ImageOps.grayscale(image)
        img = ImageTk.PhotoImage(image)
        img_label.config(image=img)
        img_label.image = img

def rotate_image():
    global image
    if image:
        image = image.rotate(90, expand=True)
        img = ImageTk.PhotoImage(image)
        img_label.config(image=img)
        img_label.image = img

def adjust_brightness(val):
    global image
    if image:
        enhancer = ImageEnhance.Brightness(image)
        img = enhancer.enhance(float(val))
        img_tk = ImageTk.PhotoImage(img)
        img_label.config(image=img_tk)
        img_label.image = img_tk

def adjust_contrast(val):
    global image
    if image:
        enhancer = ImageEnhance.Contrast(image)
        img = enhancer.enhance(float(val))
        img_tk = ImageTk.PhotoImage(img)
        img_label.config(image=img_tk)
        img_label.image = img_tk

open_btn = Button(root, text="Open Image", command=open_image)
open_btn.pack(side=tk.TOP, pady=10)

gray_btn = Button(root, text="Convert to Grayscale", command=to_grayscale)
gray_btn.pack(side=tk.TOP, pady=10)

rotate_btn = Button(root, text="Rotate Image", command=rotate_image)
rotate_btn.pack(side=tk.TOP, pady=10)

brightness_scale = Scale(root, from_=0.5, to=2.0, resolution=0.1, orient=HORIZONTAL, label="Brightness", command=adjust_brightness)
brightness_scale.set(1.0)
brightness_scale.pack(side=tk.TOP, pady=10)

contrast_scale = Scale(root, from_=0.5, to=2.0, resolution=0.1, orient=HORIZONTAL, label="Contrast", command=adjust_contrast)
contrast_scale.set(1.0)
contrast_scale.pack(side=tk.TOP, pady=10)

save_btn = Button(root, text="Save Image", command=save_image)
save_btn.pack(side=tk.TOP, pady=10)

root.mainloop()
