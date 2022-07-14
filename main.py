from tkinter import *
import customtkinter
from tkinter import filedialog as fd
from path_finder import findPath
from tkinter import messagebox
import cv2

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


def browseFiles():
    filepath = fd.askopenfilename(
        initialdir="/", title="Select a File", filetypes=(("PNG", "*.png"), ("JPEG", "*.jpeg"), ("JPG", "*.jpg")))

    if(filepath):
        img = cv2.imread(filepath, 0)
        browseFiles.filepath = filepath

        browseFiles.height = img.shape[0]
        browseFiles.width = img.shape[1]

        dimensionDetail = "Height: " + \
            str(img.shape[0]) + "px " + \
            "; Width: " + str(img.shape[1]) + "px"

        coordinates = "Coordinates: (0, 0) -> (" + \
            str(img.shape[1] - 1) + ", " + str(img.shape[0] - 1) + ")"
        imageDimensions.set(dimensionDetail)
        imageCoordinates.set(coordinates)


def validate():
    isValid = True

    startX = startInputX.get()
    startY = startInputY.get()

    endX = endInputX.get()
    endY = endInputY.get()

    if(not hasattr(browseFiles, 'filepath')):
        messagebox.showerror("Validation Error", "Image not imported")

    if(len(startX) <= 0):
        isValid = False
        messagebox.showerror("Validation Error", "Start X cannot be empty")

    if(len(startX) > 0 and int(startX) > int(browseFiles.height)):
        isValid = False
        messagebox.showerror("Validation Error", "Start X out of range")

    if(len(startY) <= 0):
        isValid = False
        messagebox.showerror("Validation Error", "Start Y cannot be empty")

    if(len(startY) > 0 and int(startY) > int(browseFiles.width)):
        isValid = False
        messagebox.showerror("Validation Error", "Start Y out of range")

    ###

    if(len(endX) <= 0):
        isValid = False
        messagebox.showerror("Validation Error", "End X cannot be empty")

    if(len(endX) > 0 and int(endX) > int(browseFiles.width)):
        isValid = False
        messagebox.showerror("Validation Error", "End X out of range")

    if(len(endY) <= 0):
        isValid = False
        messagebox.showerror("Validation Error", "End Y cannot be empty")

    if(len(endY) > 0 and int(endY) > int(browseFiles.height)):
        isValid = False
        messagebox.showerror("Validation Error", "End Y out of range")

    return isValid


def generate():
    if(validate()):
        filepath = browseFiles.filepath

        startX = int(startInputX.get())
        startY = int(startInputY.get())

        endX = int(endInputX.get())
        endY = int(endInputY.get())

        diagonal = diagonalAllowed.get()
        output = outputType.get()

        findPath(filepath, startX, startY, endX, endY, diagonal, output)


root = customtkinter.CTk()

root.geometry("450x350")
root.resizable(False, False)
root.title("Find Shortest Path")

diagonalAllowed = BooleanVar()
outputType = IntVar()
imageDimensions = StringVar()
imageCoordinates = StringVar()

# import image button
importImageButton = customtkinter.CTkButton(
    root, text="+ Import Image", command=browseFiles, width=300, fg_color=("gray75", "gray30"))

# start and end coordinates label and input
startLabel = customtkinter.CTkLabel(root, text="Start (x, y)")
startInputX = customtkinter.CTkEntry(root, placeholder_text="x")
startInputY = customtkinter.CTkEntry(root,  placeholder_text="y")

endLabel = customtkinter.CTkLabel(root, text="End (x, y)")
endInputX = customtkinter.CTkEntry(root, placeholder_text="x")
endInputY = customtkinter.CTkEntry(root, placeholder_text="y")

# diagonal allowed label and radio button
diagonalsLabel = customtkinter.CTkLabel(root, text="Diagonal")

diagonalTrueRadioBtn = customtkinter.CTkRadioButton(
    root, text="Yes", value=True, variable=diagonalAllowed)

diagonalFalseRadioBtn = customtkinter.CTkRadioButton(
    root, text="No", value=False, variable=diagonalAllowed)

# output type
outputTypeLabel = customtkinter.CTkLabel(root, text="Output type")

orignalRadioBtn = customtkinter.CTkRadioButton(
    root, text="Orignal", value=0, variable=outputType)

grayscaleRadioBtn = customtkinter.CTkRadioButton(
    root, text="Grayscale", value=1, variable=outputType)

# generate button
generateButton = customtkinter.CTkButton(
    root, text="Generate", command=generate, width=300)

imageDimensionsLabel = customtkinter.CTkLabel(
    root, text="Image Dimensions : N/A", textvariable=imageDimensions)

maxCoordinatesLabel = customtkinter.CTkLabel(
    root, textvariable=imageCoordinates)

# import image button
importImageButton.grid(row=0, column=0, pady=10,
                       padx=5, sticky="w", columnspan=2)

imageDimensionsLabel.grid(row=6, column=0, columnspan=2, sticky="w")
maxCoordinatesLabel.grid(row=7, column=0, columnspan=2, sticky="w")

# start and end coordinates label and input
startLabel.grid(row=1, column=0, sticky="w")
startInputX.grid(row=1, column=1)
startInputY.grid(row=1, column=2)

endLabel.grid(row=2, column=0, sticky="w")
endInputX.grid(row=2, column=1, pady=15)
endInputY.grid(row=2, column=2)

# diagonal allowed label and radio button
# turning off the diagonal allowed option for now

# diagonalsLabel.grid(row=3, column=0, pady=15, sticky="w")
# diagonalTrueRadioBtn.grid(row=3, column=1)
# diagonalFalseRadioBtn.grid(row=3, column=2)

# output type
outputTypeLabel.grid(row=4, column=0, sticky="w")

orignalRadioBtn.grid(row=4, column=1)
grayscaleRadioBtn.grid(row=4, column=2)

# generate button
generateButton.grid(row=5, column=0, columnspan=2, pady=20, padx=5, sticky="w")

# main window config
root.mainloop()
