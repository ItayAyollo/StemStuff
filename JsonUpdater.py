import json
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Track List JSON Updater")
window.geometry("800x260")

inputname = tk.Text(window,height = 2,width = 80)
labelname = tk.Label(window, text="Track Name", foreground="black")
labelname.pack(padx=10, pady=10)
inputname.pack(padx=10, pady=10)

inputurl = tk.Text(window,height = 2,width = 80)
labelurl = tk.Label(window, text="Track URL", foreground="black")
labelurl.pack(padx=10, pady=10)
inputurl.pack(padx=10, pady=10)

def updatejson():
    trackname = inputname.get("1.0", tk.END+"-1c")
    trackurl = inputurl.get("1.0", tk.END+"-1c")
    addthis = trackname + "~" + trackurl
    with open("tracks.json", "r") as jsonFile:
        data = json.load(jsonFile)

    data["tracks"].append(addthis)
    with open("tracks.json", "w") as jsonFile:
        json.dump(data, jsonFile)

    messagebox.showinfo("Done", 'Added track "' + trackname + '" to JSON file')


B = tk.Button(window, text ="Add", command = updatejson)
B.pack(padx=10, pady=10)

window.resizable(False, False)
window.mainloop()
