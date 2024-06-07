
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer



from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog

import cv2
import os
from PIL import Image
import tensorflow as tf
from tensorflow import keras
import numpy as np
from sklearn.model_selection import train_test_split
from time import sleep

text_element = None
response = None
path = ""

def convert_jpg_to_png(jpg_path, png_path):
    # Ouvrir l'image JPG
    with Image.open(jpg_path) as img:
        # Convertir l'image en PNG et l'enregistrer
        img.save(png_path, 'PNG')

def resize_image_if_needed(image_path, max_height=500):
    with Image.open(image_path) as img:
        width, height = img.size

        # Calculer le nouveau rapport d'aspect
        new_width = int((max_height / height) * width)
        # Redimensionner l'image
        resized_img = img.resize((new_width, max_height), Image.LANCZOS)
        # Sauvegarder l'image redimensionnée en écrasant l'originale
        resized_img.save(image_path)
        print(f"L'image a été redimensionnée et sauvegardée à : {image_path}")




def import_file():
    global image_image_14,image_14

    global text_element
    global path
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg"), ("All Files", "*.*")]
    )
    if file_path:
        print(f"Fichier importé: {file_path}")
        path = file_path

    if text_element:
        canvas.delete(text_element)
    text_element = canvas.create_text(680.0*ratio_largeur,916.0*ratio_hauteur,anchor="nw",text=file_path,fill="#000000",font=("Anton Regular", 10 * -1))
    convert_jpg_to_png(file_path, "temp/temp.png")
    resize_image_if_needed("temp/temp.png")
    image_image_14 = PhotoImage(file=relative_to_assets("../../temp/temp.png"))
    image_14 = canvas.create_image(1018.0*ratio_largeur,562.0*ratio_hauteur,image=image_image_14)

image_15 = None
image_image_15 = None
image_13 = None
def calcul():
    global image_15,image_image_15,image_13
    INPUT_SIZE = 64
    global path

    # Charger le modèle déjà fait précedement 
    model = keras.models.load_model('BrainTumor10Epochs.h5')

    # Compiler le modèle
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Lire et préparer l'image
    if path:
        global response
        print(path)
        new_image = cv2.imread(path)
        new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB)  # Convertir en RGB
        new_image = Image.fromarray(new_image, 'RGB')
        new_image = new_image.resize((INPUT_SIZE, INPUT_SIZE))
        new_image = np.array(new_image)  # Convertir en tableau NumPy
        new_image = new_image / 255.0  # Normaliser l'image

        # Ajouter une dimension supplémentaire pour le batch
        new_image = np.expand_dims(new_image, axis=0)

        # Faire la prédiction
        prediction = model.predict(new_image)
        print(f'Prediction: {"Tumor" if prediction[0][0] > 0.5 else "No Tumor"}') 
        image_image_15 = PhotoImage(file=relative_to_assets("image_15.png"))
        image_15 = canvas.create_image(1061.0*ratio_largeur,190.0*ratio_hauteur,image=image_image_15)
        rounds = round(prediction[0][0],4)

        if prediction[0][0]>0.5:
            rounds = str(rounds*100) + "%" + " de précision"
        else:
            rounds = str((1-rounds)*100) + "%" + " de précision"
        if image_13:
            canvas.delete(image_13)
        print(prediction[0][0])
        if response:
            canvas.delete(response)
        if prediction[0][0]>0.5:
            image_13 = canvas.create_text(1550*ratio_largeur,750.0*ratio_hauteur,anchor="nw",text=rounds,fill="#000000",font=("Inter Medium", 26 * -1))

            response = canvas.create_text(1494.0*ratio_largeur,650.0*ratio_hauteur,anchor="nw",text="Tumeur détécté !",fill="#000000",font=("Inter Medium", 26 * -1))
        else:
            image_13 = canvas.create_text(1550.0*ratio_largeur,750.0*ratio_hauteur,anchor="nw",text=rounds,fill="#000000",font=("Inter Medium", 26 * -1))
            response = canvas.create_text(1494.0*ratio_largeur,650.0*ratio_hauteur,anchor="nw",text="Tumeur non détécté !",fill="#000000",font=("Inter Medium", 26 * -1))
    else:
        image_image_15 = PhotoImage(file=relative_to_assets("image_18.png"))
        image_15 = canvas.create_image(1061.0*ratio_largeur,190.0*ratio_hauteur,image=image_image_15)






repertoire_courant = os.getcwd()
# Définir le chemin relatif ou utiliser une variable d'environnement
relative_path = "/assets/frame0"

# Construire le chemin complet
ASSETS_PATH = repertoire_courant + relative_path


print(ASSETS_PATH)





def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)




window = Tk()


largeur_ecran = window.winfo_screenwidth()
hauteur_ecran = window.winfo_screenheight()
ratio_largeur = largeur_ecran/1920
ratio_hauteur = hauteur_ecran/1080

window.geometry(str(largeur_ecran)+"x"+str(hauteur_ecran)) # PROJET NON RESPONSIVE, amélioration possible 

window.configure(bg = "#FFFFFF")
window.iconbitmap("assets/frame0/image_1.ico")
window.title("NeuroVision")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1080*ratio_hauteur,
    width = 1920*ratio_largeur,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    75.0*ratio_largeur,
    74.0*ratio_hauteur,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    220.0*ratio_largeur,
    75.0*ratio_hauteur,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    1018.0*ratio_largeur,
    559.0*ratio_hauteur,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    290.0*ratio_largeur,
    752.0*ratio_hauteur,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    289.0*ratio_largeur,
    328.0*ratio_hauteur,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    1651.0*ratio_largeur,
    510.0*ratio_hauteur,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    1015.0*ratio_largeur,
    931.0*ratio_hauteur,
    image=image_image_7
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: import_file(),
    relief="flat"
)
button_1.place(
    x=1018.0*ratio_largeur,
    y=901.0*ratio_hauteur,
    width=326.0,
    height=52.3607177734375
)


button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: calcul(),
    relief="flat"
)
button_2.place(
    x=1452.0*ratio_largeur,
    y=869.7373046875*ratio_hauteur,
    width=330.0,
    height=102.7991943359375
)



canvas.create_text(
    233.0*ratio_largeur,
    559.0*ratio_hauteur,
    anchor="nw",
    text="History",
    fill="#000000",
    font=("Anton Regular", 32 * -1)
)

canvas.create_text(
    217.0*ratio_largeur,
    190.0*ratio_hauteur,
    anchor="nw",
    text="Log loss",
    fill="#000000",
    font=("Anton Regular", 32 * -1)
)

canvas.create_text(
    233.0*ratio_largeur,
    427.0*ratio_hauteur,
    anchor="nw",
    text="99.96%\n",
    fill="#000000",
    font=("Anton Regular", 32 * -1)
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    285.0*ratio_largeur,
    756.0*ratio_hauteur,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    287.0*ratio_largeur,
    684.0*ratio_hauteur,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    283.0*ratio_largeur,
    828.0*ratio_hauteur,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    287.0*ratio_largeur,
    900.0*ratio_hauteur,
    image=image_image_12
)



image_image_20 = PhotoImage(
    file=relative_to_assets("image.png"))
image_20 = canvas.create_image(
    287.0*ratio_largeur,
    330.0*ratio_hauteur,
    image=image_image_20
)



image_image_16 = PhotoImage(
    file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(
    437.0*ratio_largeur,
    580.0*ratio_hauteur,
    image=image_image_16
)

image_image_17 = PhotoImage(
    file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(
    438.0*ratio_largeur,
    213.0*ratio_hauteur,
    image=image_image_17
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    1650.5*ratio_largeur,
    355.0*ratio_hauteur,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F3F2F2",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=1506.0*ratio_largeur,
    y=330.0*ratio_hauteur,
    width=289.0,
    height=40.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    1651.0*ratio_largeur,
    481.0*ratio_hauteur,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#F3F2F2",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=1507.0*ratio_largeur,
    y=455.0*ratio_hauteur,
    width=288.0,
    height=40.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    1651.0*ratio_largeur,
    599.0*ratio_hauteur,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#F3F2F2",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=1507.0*ratio_largeur,
    y=571.0*ratio_hauteur,
    width=288.0,
    height=40.0
)

canvas.create_text(
    1494.0*ratio_largeur,
    284.0*ratio_hauteur,
    anchor="nw",
    text="Prénom",
    fill="#000000",
    font=("Inter Medium", 16 * -1)
)

canvas.create_text(
    1494.0*ratio_largeur,
    396.0*ratio_hauteur,
    anchor="nw",
    text="Nom",
    fill="#000000",
    font=("Inter Medium", 16 * -1)
)

canvas.create_text(
    1494.0*ratio_largeur,
    527.0*ratio_hauteur,
    anchor="nw",
    text="Date",
    fill="#000000",
    font=("Inter Medium", 16 * -1)
)

canvas.create_rectangle(
    1381.0*ratio_largeur,
    132.0*ratio_hauteur,
    1407.0*ratio_largeur,
    152.0*ratio_hauteur,
    fill="#FFFFFF",
    outline="")
window.resizable(False, False)
window.mainloop()
