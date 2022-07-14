import os
import PIL
from resizeimage import resizeimage
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showinfo


def targetdirectory(path, dirname):
    """
    fonction qui créé le répertoire cible s'il n'existe pas
    :param dirname: Nom du répertoire tester
    :param path: chemin du répertoire de travail du script
    """
    if not os.path.exists(path + "/" + dirname):
        os.mkdir(dirname)


def Resizer(resolution, pathDir):
    """
        fonction qui à partir des paramètres entrée,
        redimensionne les photo d'un dossier à une résolution définit en paramètre
        :param resolution: Resolution souhaité en format list
        :param pathDir: chemin du répertoire de travail du script
        """
    labelResolution = str(resolution[0]) + "x" + str(resolution[1])
    try:
        os.chdir(pathDir)
    except OSError:
        quit()

    dirGoalName = "Resized Pictures at " + labelResolution
    targetdirectory(pathDir, dirGoalName)
    listFile = os.listdir(os.getcwd())

    for listItem in listFile:
        if listItem == dirGoalName:
            listFile.remove(dirGoalName)

    for nameFile in listFile:
        try:
            with open(nameFile, 'rb') as f:
                img = PIL.Image.open(f)
                img = resizeimage.resize_thumbnail(img, resolution)
                os.chdir("./" + dirGoalName)
                img.save(nameFile, img.format)
                os.chdir("..")
        except PermissionError:
            quit()


def dirBTN():
    """
            fonction de choix de répertoire.
            """
    directoryPath = askdirectory()
    chemin.set(directoryPath)
    button_VAL["state"] = NORMAL


def run():
    """
            fonction de lancement du script de redimensionnement.
            elle récupère le chemin et la résolution souhaité
            """
    resolutionSet = []
    path = str(chemin.get())
    if v.get() == 10:
        resolutionSet = [800, 600]
    elif v.get() == 20:
        resolutionSet = [1280, 960]
    elif v.get() == 30:
        resolutionSet = [2000, 1500]
    Resizer(resolutionSet, path)
    showinfo("Picture Resizer", "Conversion terminée")


root = Tk()
cadre = Frame(root, width=300, height=300, borderwidth=1)
cadre.pack()
chemin = StringVar()
root.title("Picture Resizer")
label = Label(cadre, text="Choisir un dossier et une configuration", pady=30)
v = IntVar()
case800 = Radiobutton(cadre, variable=v, value=10, text="800x600", pady=10)
case1280 = Radiobutton(cadre, variable=v, value=20, text="1280x960", pady=10)
case2000 = Radiobutton(cadre, variable=v, value=30, text="2000x1500", pady=10)
button_DIR = Button(cadre, text="Choisir un dossier", command=dirBTN, pady=10)
button_VAL = Button(cadre, text="Valider", state=DISABLED, command=run, pady=10)

label.pack(side=TOP)
case800.pack()
case1280.pack()
case2000.pack()
button_DIR.pack()
button_VAL.pack()


root.mainloop()
