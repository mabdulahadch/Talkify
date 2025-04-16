import speech_recognition as sr
import pyttsx3
import os
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from screen_brightness_control import set_brightness, get_brightness
import webbrowser
import pygame
import datetime
import requests
import json
import subprocess
import os
import sys
from pygame.locals import KEYDOWN, K_s

def open_application(app_path):
    try:
        subprocess.Popen([app_path], shell=True)
        print(f"Opened application at: {app_path}")
    except FileNotFoundError:
        print(f"Error: Application not found at {app_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def search_on_website(query, website_url):
    search_url = f"{website_url}/search?q={query}"
    webbrowser.open(search_url)

def date():
    current_date = datetime.date.today()
    date_text = current_date.strftime("%A, %B %d, %Y")
    say("Today is " + date_text)

def weather(city):
    try:
        url = f"http://api.weatherapi.com/v1/current.json?key=6fe3d2f3ceae41c8925103054232407&q={city}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        temperature = data['current']['temp_c']
        say(f'The weather in {city} is {temperature} degrees Celsius.')
        return temperature
    except requests.RequestException as e:
        say(f"Error fetching weather data: {e}")
        return None

def tell_weather(command):
    lis = list(command.split(" "))
    length = len(lis)
    city = (lis[length - 1])
    temp = weather(city)

def websites(web):
    sites = [
        ["Google ", "https://www.google.com"],
        ["YouTube", "https://www.youtube.com"],
        # Add more websites as needed
    ]
    web_lower = web.lower()

    for site in sites:
        if web_lower in site[0].lower():
            return site[1]

    return None

def music(name):
    address = [
        ["humsafar", "D:/Songs/Mere-Humsafar(PaglaSongs).mp3"],
        ["zara", "D:/Songs/Zara-Khabi-Meri-Nazar-Se-Khudko-Dekh-Bhi(PaglaSongs).mp3"],
    ]
    name_lower = name.lower()

    for i in address:
        if name_lower in i[0].lower():
            return i[1]

    return None

def search_keyword_in_file(keyword):
    try:
        with open("User Commands.txt", 'r') as file:
            line_number = 0
            for line in file:
                line_number += 1
                if keyword in line:
                    print(f"Found '{keyword}' in line {line_number}: {line.strip()}")
                    say("opening path ")
                    path=line.split(keyword+" ")[1].strip()
                    open_application(path)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")



def play_music(music_file_path):
        music_stopped=False
        pygame.init()

        try:
            pygame.mixer.init()
            pygame.mixer.music.load(music_file_path)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy() :
                pygame.time.Clock().tick(10)

            say(f"Music finished playing.")

        except pygame.error as e:
            say(f"Error playing music: {e}")
        finally:
            pygame.mixer.quit()
            
def adjust_volume(action):
    devices = AudioUtilities.GetSpeakers()
    interface = IAudioEndpointVolume._iid_
    volume = cast(devices.Activate(interface, CLSCTX_ALL, None), POINTER(IAudioEndpointVolume))

    current_volume = volume.GetMasterVolumeLevel()
    if action == "increase" and current_volume < volume.GetVolumeRange()[1]:
        volume.SetMasterVolumeLevel(current_volume + 6.0, None)
    elif action == "decrease" and current_volume > volume.GetVolumeRange()[0]:
        volume.SetMasterVolumeLevel(current_volume - 6.0, None)

def adjust_brightness(action):
    current_brightness = get_brightness()
    if isinstance(current_brightness, list):
        current_brightness = current_brightness[0]
    if action == "increase" and current_brightness < 100:
        set_brightness(current_brightness + 30)
    elif action == "decrease" and current_brightness > 0:
        set_brightness(current_brightness - 30)



def add_command(command_name, command_path):
    if not os.path.exists(command_path):
        print("Path does not exist. Please enter a valid path.")
    else:
        with open("User Commands.txt", "a") as file:
               file.write(f"{command_name} {command_path}\n")      
        \
        print(f"Command '{command_name}' added successfully.")
        
def delete_command():
    with open("text.txt", "r") as file:
        commands = file.readlines()

    if not commands:
        print("No commands to delete.")
        return

    print("Existing commands:")
    for i, command in enumerate(commands, 1):
        print(f"{i}. {command.strip()}")

    try:
        choice = int(input("Enter the number to delete: "))
        if 1 <= choice <= len(commands):
            deleted_command = commands.pop(choice - 1).strip()

            with open("text.txt", "w") as file:
                file.writelines(commands)

            print(f"Command '{deleted_command}' deleted successfully.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")
def execute_command(command_str, command_file_path):
    # Split the command string into command and optional arguments
    parts = command_str.split(maxsplit=1)
    if len(parts) < 1:
        print("Invalid command format.")
        return

    target_command = parts[0]

    # Check if the command exists in the file
    with open(command_file_path, 'r') as file:
        for line in file:
            try:
                stored_command, stored_arguments = line.strip().split(maxsplit=1)
            except ValueError:
                print(f"Error parsing line: {line}")
                continue

            if stored_command == target_command:
                # Command found, execute the specified action
                try:
                    os.startfile(stored_arguments)
                    print(f"Executed command: {target_command} {stored_arguments}")
                except Exception as e:
                    say(f"Error executing command: {e}")
                return

    say("Command not found in the file.")

def say(text):
    engine = pyttsx3.init()

    """ RATE"""
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 115)

    """VOLUME"""
    volume = engine.getProperty('volume')
    engine.setProperty('volume', 1.0)

    """VOICE"""
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    engine.say(text)
    engine.runAndWait()
    engine.stop()


def voice():
    say("Listening...")

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")

        try:
            while True:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio)
                say("You said:"+ text)
                

                if "weather" in text:
                    city_name = text.split("weather of ")[1].strip()
                    tell_weather(city_name)
                elif "play music" in text:
                    song_name = text.split("play music")[1].strip()
                
                    music_path = music(song_name)
                    if music_path:
                        say("Playing"+song_name)
                        play_music(music_path)
                    else:
                       say("Song not found.")
                elif "increase volume" in text:
                    adjust_volume("increase")
                    say("Volume increased.")
                elif "decrease volume" in text:
                    adjust_volume("decrease")
                    say("Volume decreased.")
                elif "increase brightness" in text:
                    adjust_brightness("increase")
                    say("Brightness increased.")
                elif "decrease brightness" in text:
                    adjust_brightness("decrease")
                    say("Brightness decreased.")
                elif "search" in text:
                    search_item = text.split("search")[1].strip().split()[0]
                    search_query=text.split("on")[1].strip()
                    website_url = websites(search_query)
                    if website_url:
                        print(search_item)
                        search_on_website(search_item, website_url)
                    else:
                        say("Website not found.")
                elif "date" in text:
                    date()

                elif "open" in text:
                    if len(text) > 1:
                        file_name=text.split("open ")[1].strip() 
                        execute_command(file_name,"User Commands.txt")   
                elif "exit" in text:
                    print("Exiting the program.")
                    break
                else:
                    say("Command not recognized.")

        except KeyboardInterrupt:
            say("\nProgram stopped by user.")
        except sr.UnknownValueError:
            say("Sorry, could not understand audio.")
        except sr.RequestError as e:
            say(f"Error fetching results; {e}")

if __name__ == "__main__":
    voice() 
