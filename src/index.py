import tkinter as tk
from PIL import Image, ImageTk

flag = True
global n
n = 0

# Get the button size
ear_button_width = 320
ear_button_height = 300

# Add symbol size
add_symbolWidth = 60
add_symbolHeight = 60


# def resize_image(event):
#     window_width = event.width
#     window_height = event.height
#     global n
#     global original_image_resized
#     global second_image_resized
#     global settings_image_resized
#     global current_image
#     global add_CommandScreen_resized

#     # Resize original and second images according to the screen size
#     original_image_resized = home_image_one.resize((window_width, window_height))
#     second_image_resized = home_image_two.resize((window_width, window_height))
#     settings_image_resized = setting_image.resize((window_width, window_height))
#     add_CommandScreen_resized = addCommandScreen.resize((window_width, window_height))

#     # Display the current image based on the flag
#     if n == 0:
#         AddButton.place_forget()
#         text_box2.place_forget()
#         text_box.place_forget()
#         if flag:
#             current_image = original_image_resized
#         else:
#             current_image = second_image_resized
#     elif n == 1:
#         text_box2.place_forget()
#         text_box.place_forget()
#         b.place_forget()
#         AddButton.place(x=648, y=280)
#         current_image = settings_image_resized
#     elif n == 2:
#         b.place_forget()
#         AddButton.place_forget()
#         text_box.place(x=270,y=175,width=460,height=35)
#         text_box2.place(x=270,y=265,width=460,height=35)
#         current_image = add_CommandScreen_resized
       

#     set_Image()


def set_Image():
    tk_current_image = ImageTk.PhotoImage(current_image)
    label.config(image=tk_current_image)
    label.image = tk_current_image


def toggle_flag():
    global flag
    flag = not flag
    update_images()


def onSettingsClick():
    global n
    n = 1
    update_images()


def onHomeClick():
    global n
    n = 0
    update_images()


def onAddButton():
    global n
    n = 2
    update_images()

def onEnterClick():
    global n
    n=3
    update_images()
def update_images():
    global current_image
    global n
    global original_image_resized
    global original_image_resized
    global second_image_resized
    global settings_image_resized
    global current_image
    global add_CommandScreen_resized
    global ErrorImageResized
    original_image_resized = home_image_one.resize((screen_width-368, screen_height-148))
    second_image_resized = home_image_two.resize((screen_width-368, screen_height-148))
    settings_image_resized = setting_image.resize((screen_width-368, screen_height-150))
    add_CommandScreen_resized = addCommandScreen.resize((screen_width-368, screen_height-143))
    ErrorImageResized=errorScreen.resize((screen_width-368, screen_height-145))    
    if n == 0:
        AddButton.place_forget()
        text_box2.place_forget()
        text_box.place_forget()
        back.place_forget()
        home.place(x=34, y=111)
        settings.place(x=34, y=158)
        AboutButton.place(x=34, y=205)
        CloseButton.place(x=34, y=299)
        InstructionsButton.place(x=34, y=252)
        if flag:
            current_image = original_image_resized
            resized_button_image = ImageTk.PhotoImage(ear.resize((ear_button_width, ear_button_height)))
        else:
            current_image = second_image_resized
            resized_button_image = ImageTk.PhotoImage(bright_ear.resize((ear_button_width, ear_button_height)))

        set_Image()

        b.config(image=resized_button_image)
        b.image = resized_button_image
        b.place(x=338, y=120)
    elif n == 1:
        cross.place_forget()
        text_box2.place_forget()
        text_box.place_forget()
        back.place_forget()
        enter.place_forget()
        home.place(x=34, y=111)
        settings.place(x=34, y=158)
        AboutButton.place(x=34, y=205)
        CloseButton.place(x=34, y=299)
        InstructionsButton.place(x=34, y=252)
        b.place_forget()
        current_image = settings_image_resized
        AddButton.place(x=648, y=280)
        set_Image()
    elif n == 2:
        AddButton.place_forget()
        cross.place_forget()
        home.place_forget()
        AboutButton.place_forget()
        InstructionsButton.place_forget()
        back.place(x=45,y=485)
        enter.place(x=415,y=370)
        settings.place_forget()
        CloseButton.place_forget()
        text_box.place(x=270,y=175,width=460,height=35)
        text_box2.place(x=270,y=265,width=460,height=35)
        current_image = add_CommandScreen_resized
        current_image = add_CommandScreen_resized
        set_Image()
    elif n==3:
        text_box.place_forget()
        text_box2.place_forget()
        enter.place_forget()
        cross.place(x=728,y=174)
        current_image=ErrorImageResized
        set_Image()


root = tk.Tk()
root.title("Talkify")
root.geometry("1000x600")

# Load the original and second images using PIL
home_image_one = Image.open("HOME SCREEN 1.png")
home_image_two = Image.open("HOME SCREEN 2.png")
ear = Image.open("Frame 8.png")
bright_ear = Image.open("Frame 9.png")
Add_image = Image.open("AddSymbol.png")
addCommandScreen = Image.open("ADD COMMAND SCREEN.png")
errorScreen=Image.open("ERROR.png")
# loading the settings screen
setting_image = Image.open("SETTINGS SCREEN.png")
# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Resize original and second images to screen size
original_image_resized = home_image_one.resize((screen_width-368, screen_height-145))
second_image_resized = home_image_two.resize((screen_width-368, screen_height-145))
settings_image_resized = setting_image.resize((screen_width-368, screen_height-145))
add_CommandScreen_resized = addCommandScreen.resize((screen_width-368, screen_height-145))
# Initialize current_image to original_image
current_image = original_image_resized
AddSymbolImage_resized = ImageTk.PhotoImage(Add_image.resize((add_symbolWidth, add_symbolHeight)))
ErrorImageResized=errorScreen.resize((screen_width-368, screen_height-145))
# Resize the image to fit the screen size
tk_image = ImageTk.PhotoImage(current_image)

# Create a label to display the image
label = tk.Label(root, image=tk_image)
label.pack(fill=tk.BOTH, expand=True)

# Create a button with the initial image
initial_button_image = ImageTk.PhotoImage(ear.resize((ear_button_width, ear_button_height)))
b = tk.Button(root, border=0, width=ear_button_width, height=ear_button_height, bd=0, image=initial_button_image,
              highlightthickness=0, activebackground='#364958', command=toggle_flag)
b.place(x=338, y=120)
# home button
home_image = Image.open("Home.png")
home_height = 42
home_width = 42
button_image = ImageTk.PhotoImage(home_image.resize((home_height, home_width)))
home = tk.Button(root, border=0, width=home_width, height=home_height, bd=0, image=button_image,
                 highlightthickness=0, activebackground='#55828B', command=onHomeClick)
home.place(x=34, y=111)
# setting button
settings_image = Image.open("setting.png")
setting_height = 42
setting_width = 42
settingButton_image = ImageTk.PhotoImage(settings_image.resize((setting_width, setting_height)))
settings = tk.Button(root, border=0, width=home_width, height=home_height, bd=0, image=settingButton_image,
                    highlightthickness=0, activebackground='#55828B', command=onSettingsClick)
settings.place(x=34, y=158)
# About Button
# AboutButton
about_image = Image.open("about.png")
about_symbol_height = 42
about_symbol_width = 42
AboutSymbolImage = ImageTk.PhotoImage(about_image.resize((about_symbol_width, about_symbol_height)))
AboutButton = tk.Button(root, border=0, width=home_width, height=home_height, bd=0, image=AboutSymbolImage,
                        highlightthickness=0, activebackground='#55828B')
AboutButton.place(x=34, y=205)
# AboutButton initially hidden
# AboutButton.place_forget()
# InstructionsButton
instructions_image = Image.open("instruct.png")
instructions_height = 42
instructions_width = 42
InstructionsImage = ImageTk.PhotoImage(instructions_image.resize((instructions_width, instructions_height)))
InstructionsButton = tk.Button(root, border=0, width=home_width, height=home_height, bd=0, image=InstructionsImage,
                                highlightthickness=0, activebackground='#55828B')
InstructionsButton.place(x=34, y=252)
# CloseButton
close_image = Image.open("Close.png")
close_height = 42
close_width = 42
CloseImage = ImageTk.PhotoImage(close_image.resize((close_width, close_height)))
CloseButton = tk.Button(root, border=0, width=home_width, height=home_height, bd=0, image=CloseImage,
                        highlightthickness=0, activebackground='#55828B')
CloseButton.place(x=34, y=299)

# AddSymbolButton
AddButton = tk.Button(root, border=0, width=add_symbolHeight, height=add_symbolWidth, bd=0,
                        image=AddSymbolImage_resized, highlightthickness=0, activebackground='#FFFFFF', command=onAddButton)

# AddButton initially hidden
AddButton.place_forget()
#Back Buttion
backImage=Image.open("Vector.png")
back_width=100
back_height=100
backImg=ImageTk.PhotoImage(backImage.resize((back_width,back_height)))
back=tk.Button(root,border=0, width=back_width, height=back_height, bd=0,
                        image=backImg, highlightthickness=0, activebackground='#364958',command=onSettingsClick)
back.place_forget()
#Enter Button on Add Command Screen
EnterImage=Image.open("enterbutton.png")
enter_height=82
enter_width=175
EnterImg=ImageTk.PhotoImage(EnterImage.resize((enter_width,enter_height)))
enter=tk.Button(root,border=0, width=enter_width, height=enter_height, bd=0,
                        image=EnterImg, highlightthickness=0, activebackground='#364958',background="#364958",command=onEnterClick)
enter.place_forget()
#cross button on error screen
crossImage=Image.open("cross.png")
crossheight=40
crossImg=ImageTk.PhotoImage(crossImage.resize((crossheight,crossheight)))
cross=tk.Button(root,border=0, width=35, height=35, bd=0,
                        image=crossImg, highlightthickness=0, activebackground='#FFFFFF',background="#FFFFFF",command=onAddButton)
cross.place_forget()
command="hello"
path=""
# Text box (Entry widget) for the Add Command Screen
text_box = tk.Entry(root,bg="#55828B",fg="white",font=20,textvariable=command)
text_box.place(x=400, y=400)
text_box.place_forget()
# Text box (Entry widget) for the Adding path  Screen
text_box2 = tk.Entry(root,bg="#55828B",fg="white",font=20,textvariable=path)
text_box2.place(x=400, y=400)
text_box2.place_forget()
# Bind the resizing function to the window resize event
#root.bind("<Configure>", resize_image)

root.mainloop()
