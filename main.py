from PIL import Image
import pilgram
import os, sys

global run
run = True

class Program():

    def __init__(self):
        commands = ["black_and_white", "rotate", "resize", "add_filter", "polaroiid_frame", "exit"]
        self.commands = commands
        files = []
        exceptions = ["examples.png", "polaroid-frame.png"]
        print("Wellcome to ACFE! (Amazing Consoll Foto Editor)")
        print("Choose the picture you want to edit:" + "\n")
        counter = 1
        for file in os.scandir('.'):
            if file.is_file() and file.path.split(".")[-1].lower() in ['png','jpg','jpeg']:
                if file.name not in exceptions:
                    files.append(file)
                    print(f'{counter}. {file.name}')
                    counter += 1
        print("\n")
        file = input("File you will work with (enter num): ")
        file = files[int(file)-1]
        self.file = file

    def exit(self):
        run = False
        sys.exit()


    def black_and_white(self):
        im = Image.open(self.file.name)
        pilgram.moon(im).save(f'{self.file.name}-moon.png')


    def rotate(self):
        angles = ["90", "180", "270"]
        im = Image.open(self.file.name)
        print("How will you rotate picture?")
        counter = 1
        for angle in angles:
            print(f"{counter}. {angle}")
            counter += 1
        
        command_angle = input("Choose angle (enter num): ")
        match command_angle:
            case "1":
                rotated = im.transpose(Image.ROTATE_90)
            case "2":
                rotated = im.transpose(Image.ROTATE_180)
            case "3":
                rotated = im.transpose(Image.ROTATE_270)
        rotated.save(f"{self.file.name}-{angles[int(command_angle) - 1]}.png")
    

    def resize(self):
        im = Image.open(self.file.name)
        im.thumbnail([1080, 1080])
        im.save(f"{self.file.name}-1080.png")
    

    def add_filter(self):
        examples = Image.open("examples.png")
        im = Image.open(self.file.name)
        examples.show()
        choosen_filter = input("Choose filter you would like to use: ")
        exec(f"pilgram.{choosen_filter}(im).save(f'{self.file.name}-{choosen_filter}.png')")

    
    def polaroiid_frame(self):
        im = Image.open(self.file.name)
        if im.size >= (760, 760):
            im = im.crop((0,0,760, 760))
        frame = Image.open("polaroid-frame.png")
        frame.paste(im, (64,64))
        frame.save(f"{self.file.name}-polaroid.png")



    def mainloop(self):
        run = True
        while run:
            print("What do you want to do with picture?")
            counter = 1
            for command in self.commands:
                print(f"{counter}. {command}")
                counter += 1
            print("\n")
            command = int(input("What do you want to do with picture (enter num): "))
            exec(f"self.{self.commands[command - 1]}()")
            print("\n")



pr = Program()
pr.mainloop()