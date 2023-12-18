from PIL import Image
import pilgram
import os

global run
run = True

class Program():

    def __init__(self):
        commands = ["black_and_white", "rotate", "resize", "stop"]
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
        file = files[int(file)-1]
        self.file = file

    def stop(self):
        run = False

    def black_and_white(self):
        im = Image.open(self.file.name)
        pilgram.moon(im).save(f'{self.file.name}-moon.jpg')


    def rotate(self):
        angles = ["90", "180", "270"]
        im = Image.open(self.file.name)
        print("How will you rotate picture?")
        counter = 1
        for angle in angles:
            print(f"{counter}. {angle}")
            counter += 1
        
        command_angle = input("Choose angle: ")
        match command_angle:
            case "1":
                rotated = im.transpose(Image.ROTATE_90)
            case "2":
                rotated = im.transpose(Image.ROTATE_180)
            case "3":
                rotated = im.transpose(Image.ROTATE_270)
        rotated.save(f"{self.file.name}-{angles[int(command_angle) - 1]}.png")
        rotated.show()
    

    def resize(self):
        im = Image.open(self.file.name)
        im.thumbnail([1080, 1080])
        im.save(f"{self.file.name}-1080.png")



    def mainloop(self):
        run = True
        print("What do you want to do with picture?")
        counter = 1
        for command in self.commands:
            print(f"{counter}. {command}")
            counter += 1
        while run:
            command = int(input("File you will work with: "))
            exec(f"self.{self.commands[command - 1]}()")



pr = Program()
pr.mainloop()