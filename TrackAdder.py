import json
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import os
import shutil
from pydub import AudioSegment
from pathlib import Path


window = tk.Tk()
window.title("Song Adder")
window.geometry("800x650")

def file1():
    filename = askopenfilename()
    path1text.delete("1.0", tk.END)
    path1text.insert(tk.END, filename)
    print(filename)

def file2():
    filename = askopenfilename()
    path2text.delete("1.0", tk.END)
    path2text.insert(tk.END, filename)
    print(filename)

def file3():
    filename = askopenfilename()
    path3text.delete("1.0", tk.END)
    path3text.insert(tk.END, filename)
    print(filename)

def file4():
    filename = askopenfilename()
    path4text.delete("1.0", tk.END)
    path4text.insert(tk.END, filename)
    print(filename)



inputname = tk.Text(window,height = 2,width = 80)
labelname = tk.Label(window, text="Track Name", foreground="black")
labelname.pack(padx=10, pady=2)
inputname.pack(padx=10, pady=2)

path1text = tk.Text(window,height = 2,width = 80)
labelpath1 = tk.Label(window, text="Track 1 Path", foreground="black")
labelpath1.pack(padx=10, pady=2)
path1text.pack(padx=10, pady=2)
B1 = tk.Button(window, text ="Set Track 1 Path", command = file1)
B1.pack(padx=10, pady=2)

path2text = tk.Text(window,height = 2,width = 80)
labelpath2 = tk.Label(window, text="Track 2 Path", foreground="black")
labelpath2.pack(padx=10, pady=2)
path2text.pack(padx=10, pady=2)
B1 = tk.Button(window, text ="Set Track 2 Path", command = file2)
B1.pack(padx=10, pady=2)

path3text = tk.Text(window,height = 2,width = 80)
labelpath3 = tk.Label(window, text="Track 3 Path", foreground="black")
labelpath3.pack(padx=10, pady=2)
path3text.pack(padx=10, pady=2)
B1 = tk.Button(window, text ="Set Track 3 Path", command = file3)
B1.pack(padx=10, pady=2)

path4text = tk.Text(window,height = 2,width = 80)
labelpath4 = tk.Label(window, text="Track 4 Path", foreground="black")
labelpath4.pack(padx=10, pady=2)
path4text.pack(padx=10, pady=2)
B1 = tk.Button(window, text ="Set Track 4 Path", command = file4)
B1.pack(padx=10, pady=2)


def updatejson():
    trackname = inputname.get("1.0", tk.END + "-1c")
    newpath = trackname
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        with open('datatemplate.json') as f:
            data = json.load(f)

        with open(trackname + '/data.json', 'w') as f:
            json.dump(data, f, indent=2)
            print("New json file is created from data.json file")
        path1 = path1text.get("1.0", tk.END + "-1c")
        path2 = path2text.get("1.0", tk.END + "-1c")
        path3 = path3text.get("1.0", tk.END + "-1c")
        path4 = path4text.get("1.0", tk.END + "-1c")

        #compressing the tracks and turning them into mp3's if needed.
        #track1
        sound = AudioSegment.from_file(path1)
        track1corrected = Path(path1).stem #hehe stem
        sound.export(trackname + '/' + track1corrected + '.mp3', format="mp3", bitrate="128k")
        
        #track2
        sound = AudioSegment.from_file(path2)
        track2corrected = Path(path2).stem
        sound.export(trackname + '/' + track2corrected + '.mp3', format="mp3", bitrate="128k")
        
        #track3
        sound = AudioSegment.from_file(path3)
        track3corrected = Path(path3).stem
        sound.export(trackname + '/' + track3corrected + '.mp3', format="mp3", bitrate="128k")
        
        #track4
        sound = AudioSegment.from_file(path4)
        track4corrected = Path(path4).stem
        sound.export(trackname + '/' + track4corrected + '.mp3', format="mp3", bitrate="128k")

        track1 = track1corrected + '.mp3'
        track2 = track2corrected + '.mp3'
        track3 = track3corrected + '.mp3'
        track4 = track4corrected + '.mp3'

        tracknameCorrectedForURL = trackname.replace(" ", "%20")

        track1 = "https://github.com/spicyshotz/StemStuff/raw/main/" + tracknameCorrectedForURL + '/' + track1
        track2 = "https://github.com/spicyshotz/StemStuff/raw/main/" + tracknameCorrectedForURL + '/' + track2
        track3 = "https://github.com/spicyshotz/StemStuff/raw/main/" + tracknameCorrectedForURL + '/' + track3
        track4 = "https://github.com/spicyshotz/StemStuff/raw/main/" + tracknameCorrectedForURL + '/' + track4

        datajsonURL = "https://raw.githubusercontent.com/spicyshotz/StemStuff/main/" + tracknameCorrectedForURL + "/data.json"

        with open(trackname + '/data.json', "r") as jsonFile:
            data = json.load(jsonFile)

        data["Name"] = trackname
        data["Track1URL"] = track1
        data["Track2URL"] = track2
        data["Track3URL"] = track3
        data["Track4URL"] = track4
        with open(trackname + '/data.json', "w") as jsonFile:
            json.dump(data, jsonFile)

        addthis = trackname + "~" + datajsonURL
        with open("tracks.json", "r") as jsonFile:
            data = json.load(jsonFile)

        data["tracks"].append(addthis)
        with open("tracks.json", "w") as jsonFile:
            json.dump(data, jsonFile)
        
        messagebox.showinfo("Done", 'Added track "' + trackname + '" to playlist')
    else:
        messagebox.showinfo("Track Already Exists", 'track"' + trackname + '" alreay exists. Delete it or rename your track.')


B1 = tk.Button(window, text ="Save Track", command = updatejson)
B1.pack(padx=10, pady=60)

window.resizable(False, False)
window.mainloop()
