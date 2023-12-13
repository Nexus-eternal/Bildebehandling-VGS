from PIL import Image
import pilgram
import os

def mainloop():
    run = True
    files = []
    print("Wellcome to ACFE!")
    print("Choose the picture you want to edit:")
    counter = 1
    for file in os.scandir('.'):
        if file.is_file() and file.path.split(".")[-1].lower() in ['png','jpg','jpeg']:
            files.append(file)
            print(f'{counter}. {file.name}')


    while run:
        pass

mainloop()