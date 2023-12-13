from PIL import Image
import pilgram
import os

class Program():

    def __init__(self) -> None:
        files = []
        print("Wellcome to ACFE!")
        print("Choose the picture you want to edit:" + "\n")
        counter = 1
        for file in os.scandir('.'):
            if file.is_file() and file.path.split(".")[-1].lower() in ['png','jpg','jpeg']:
                files.append(file)
                print(f'{counter}. {file.name}')
        print("\n")
        file = input("File you will work with: ")
        file = int(file)
        file = files[file-1]

    def mainloop(self):
        run = True
        print("ABOBA")



pr = Program()
pr.mainloop()