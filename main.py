# Import the required Libraries
from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model
from keras_preprocessing import image

win = Tk()

win.geometry("480x480")
model = load_model('garbage_management_model.h5')


def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    load = Image.open(filename)
    load = load.resize((200, 200), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load)
    # images = Label(image=render)
    # images.image = render
    # a = img.place(x=100, y=50)

    path = filename
    img = image.load_img(path, target_size=(150, 100))
    imgplot = plt.imshow(img)
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    images = np.vstack([x])
    classes = model.predict(images)

    print(path)
    print(classes)

    ket = ''

    if classes[0][0]:
        ket = "CardBoard"
    elif classes[0][1]:
        ket = "Glass"
    elif classes[0][2]:
        ket = "Metal"
    elif classes[0][3]:
        ket = "Paper"
    elif classes[0][4]:
        ket = "Plastic"
    elif classes[0][5]:
        ket = "Trash"

    # label = Label(win, text=ket, image=render, compound='center')
    # a = label.place(x=100, y=50)
    gambar = Label(win, text=ket, image=render, compound='bottom')
    gambar.image = render
    a = gambar.place(x=100, y=50)
    return a


ttk.Button(win, text="Click", command=UploadAction).pack(pady=20)
win.wm_title("Tkinter window")
win.mainloop()