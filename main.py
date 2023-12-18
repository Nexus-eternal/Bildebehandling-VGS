from PIL import Image
import pilgram
import os, sys

# Added global variable to run while-loop
global run
run = True

#Defining Programm class
class Program():

# Initializing ogject of class
    def __init__(self):
        commands = ["black_and_white", "rotate", "resize", "add_filter", "polaroiid_frame", "exit"]
        self.commands = commands
        files = []
        exceptions = ["examples.png", "polaroid-frame.png"]
        print("Wellcome to ACFE! (Amazing Consoll Foto Editor)")
        print("Choose the picture you want to edit:" + "\n")
        counter = 1
        # Starting loop to tell all options
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

        self.im = Image.open(self.file.name)


# Exit function
    def exit(self):
        # Canseling  loop
        run = False
        # Exits programm
        sys.exit()


# Oppgave B
    def black_and_white(self):
        # Saving edited file
        pilgram.moon(self.im).save(f'{self.file.name}-b&w.png')


# Oppgave C
    def rotate(self):
        angles = ["90", "180", "270"]
        print("How will you rotate picture?")
        counter = 1
        # Starting loop to tell all options
        for angle in angles:
            print(f"{counter}. {angle}")
            counter += 1

# Match-case structure (Better then if-elif to compare 1 parameter)        
        command_angle = input("Choose angle (enter num): ")
        match command_angle:
            case "1":
                rotated = self.im.transpose(Image.ROTATE_90)
            case "2":
                rotated = self.im.transpose(Image.ROTATE_180)
            case "3":
                rotated = self.im.transpose(Image.ROTATE_270)
        # Saving edited file
        rotated.save(f"{self.file.name}-{angles[int(command_angle) - 1]}.png")
    

# Oppgave D
    def resize(self):
        self.im.thumbnail([1080, 1080])
        # Saving edited file
        self.im.save(f"{self.file.name}-1080.png")
    

# Oppgave A + F
    def add_filter(self):
        examples = Image.open("examples.png")
        examples.show()
        choosen_filter = input("Choose filter you would like to use: ")
        # Saving edited file
        exec(f"pilgram.{choosen_filter}(self.im).save(f'{self.file.name}-{choosen_filter}.png')")

    
# Oppgave G
    def polaroiid_frame(self):
        width, heigth = self.im.size
        if width > heigth:
            top_left_y = (heigth - 760)/2
            top_left_x = (width - 760)/2
            bottom_right_y = heigth -(heigth - 760)/2
            bottom_right_x = width - (width - 760)/2
            im = self.im.crop((top_left_x, top_left_y, bottom_right_x, bottom_right_y))
        elif self.im.size >= (760, 760):
            im = self.im.crop((0,0,760, 760))
        frame = Image.open("polaroid-frame.png")
        frame.paste(im, (64,64))
        # Saving edited file
        frame.save(f"{self.file.name}-polaroid.png")


# Mainloop to run
    def mainloop(self):
        while run:
            print("What do you want to do with picture?")
            counter = 1
            # Starting loop to tell all options
            for command in self.commands:
                print(f"{counter}. {command}")
                counter += 1
            print("\n")
            command = int(input("What do you want to do with picture (enter num): "))
            exec(f"self.{self.commands[command - 1]}()")
            print("\n")



pr = Program()
pr.mainloop()