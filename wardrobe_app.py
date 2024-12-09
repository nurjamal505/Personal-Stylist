import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class WardrobeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Stylist")
        self.root.geometry("900x700")
        self.root.config(bg="#FAD2E1")

        self.bg_image = Image.open("Background.jpg")
        self.bg_image = self.bg_image.resize((900, 700))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        self.add_button = tk.Button(self.root, text="Добавить ваше фото", command=self.add_photo, font=("Arial", 16), bg="#FF66B2", fg="white", relief="flat", bd=0, padx=20, pady=10, highlightthickness=0, activebackground="#FF3385", borderwidth=2)
        self.add_button.pack(pady=30)

        self.main_image_label = tk.Label(self.root)
        self.main_image_label.pack(pady=20)

        self.next_button = tk.Button(self.root, text="Следующий лук", command=self.show_next, font=("Arial", 16), bg="#FF66B2", fg="white", relief="flat", bd=0, padx=20, pady=10, highlightthickness=0, state="disabled", activebackground="#FF3385", borderwidth=2)
        self.next_button.place(relx=0.5, rely=0.95, anchor="center")

        self.wardrobe = []
        self.current_index = -1

    def add_photo(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if file_path:
            self.wardrobe = [file_path, "Look 1.jpg", "Look 2.jpg", "Look 3.jpg", "Look 4.jpg"]
            self.current_index = 0
            self.show_image()
            self.add_button.config(state="disabled")
            self.next_button.config(state="normal")

    def show_image(self):
        if self.current_index >= 0 and self.current_index < len(self.wardrobe):
            image_path = self.wardrobe[self.current_index]
            img = Image.open(image_path)
            if self.current_index != 0:
                img = img.resize((700, 800))
            photo = ImageTk.PhotoImage(img)

            self.main_image_label.config(image=photo)
            self.main_image_label.image = photo

    def show_next(self):
        if self.wardrobe:
            self.current_index += 1
            if self.current_index >= len(self.wardrobe):
                self.current_index = 0
            self.show_image()

if __name__ == "__main__":
    root = tk.Tk()
    app = WardrobeApp(root)
    root.mainloop()
