from PIL import Image
import pilgram
import os

class Program():

    def __init__(self) -> None:
        commands = []
        self.commands = commands
        files = []
        print("Wellcome to ACFE!")
        print("Choose the picture you want to edit:" + "\n")
        counter = 1
        for file in os.scandir('.'):
            if file.is_file() and file.path.split(".")[-1].lower() in ['png','jpg','jpeg']:
                files.append(file)
                print(f'{counter}. {file.name}')
                counter += 1
        print("\n")
        file = input("File you will work with: ")
        file = int(file)
        file = files[file-1]
        self.file = file

    def mainloop(self):
        run = True
        print("What do you want to do with picture?")
        counter = 1
        for command in self.commands:
            print(f"{counter}. {command}")
        im = Image.open(self.file.name)
        pilgram.moon(im).save(f'{self.file.name}-moon.jpg')





pr = Program()
pr.mainloop()