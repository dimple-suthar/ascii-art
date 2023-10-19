import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

class ArtGalleryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Art Gallery")

        self.canvas = tk.Canvas(root, width=800, height=600)
        self.canvas.pack()

        self.load_button = tk.Button(root, text="Load Image", command=self.load_image)
        self.load_button.pack()

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack()

        self.previous_button = tk.Button(root, text="Previous", command=self.show_previous)
        self.previous_button.pack()

        self.next_button = tk.Button(root, text="Next", command=self.show_next)
        self.next_button.pack()

        self.artworks = []
        self.current_artwork_index = -1

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            image = Image.open(file_path)
            image.thumbnail((800, 600))
            photo = ImageTk.PhotoImage(image)
            self.artworks.append((image, photo))
            self.show_next()

    def show_previous(self):
        if self.current_artwork_index > 0:
            self.current_artwork_index -= 1
            self.display_current_artwork()

    def show_next(self):
        if self.current_artwork_index < len(self.artworks) - 1:
            self.current_artwork_index += 1
            self.display_current_artwork()

    def display_current_artwork(self):
        if 0 <= self.current_artwork_index < len(self.artworks):
            current_artwork = self.artworks[self.current_artwork_index]
            self.canvas.delete("all")
            self.canvas.create_image(0, 0, anchor=tk.NW, image=current_artwork[1])
            self.display_artwork_info()

    def display_artwork_info(self):
        if 0 <= self.current_artwork_index < len(self.artworks):
            current_artwork = self.artworks[self.current_artwork_index]
            self.root.title(f"Art Gallery - Artwork {self.current_artwork_index + 1}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ArtGalleryApp(root)
    root.mainloop()
