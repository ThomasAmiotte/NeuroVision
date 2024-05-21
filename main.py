import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

class ImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")

        # Configuration de la fenêtre principale
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")

        # Cadre pour les boutons
        self.frame_buttons = tk.Frame(self.root, bg="#f0f0f0")
        self.frame_buttons.pack(pady=20)

        # Bouton pour importer une image
        self.button_import = tk.Button(self.frame_buttons, text="Importer une image", command=self.import_image, bg="#4CAF50", fg="white", padx=20, pady=10)
        self.button_import.pack(side=tk.LEFT, padx=10)

        # Canvas pour afficher l'image
        self.canvas = tk.Canvas(self.root, bg="white", highlightthickness=1, highlightbackground="gray")
        self.canvas.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        # Variable pour stocker l'image
        self.image_on_canvas = None

    def import_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
        if file_path:
            try:
                image = Image.open(file_path)
                image = image.resize((800, 600), Image.ANTIALIAS)
                self.photo = ImageTk.PhotoImage(image)
                
                if self.image_on_canvas:
                    self.canvas.delete(self.image_on_canvas)
                self.image_on_canvas = self.canvas.create_image(400, 300, anchor=tk.CENTER, image=self.photo)
            except Exception as e:
                messagebox.showerror("Erreur", f"Impossible d'ouvrir l'image : {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageApp(root)
    root.mainloop()