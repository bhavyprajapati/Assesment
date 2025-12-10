import tkinter as tk
from tkinter import messagebox
import os


class Playlist:
    def __init__(self, name, songs):
        self.name = name
        self.songs = songs


def save_playlist():
    try:
        name = entry_name.get()
        
        if not name:
            messagebox.showerror("Error", "Enter playlist name")
            return
        
        songs_text = text_songs.get("1.0", tk.END)
        songs = songs_text.strip().split("\n")
        
        if not songs[0]:
            messagebox.showerror("Error", "Add some songs")
            return
        
        if not os.path.exists("playlists"):
            os.makedirs("playlists")
        
        filename = f"playlists/playlist_{name}.txt"
        
        if os.path.exists(filename):
            messagebox.showerror("Error", "Playlist already exists")
            return
        
        file = open(filename, "w")
        for song in songs:
            file.write(song + "\n")
        file.close()
        
        messagebox.showinfo("Success", "Playlist saved")
        
        entry_name.delete(0, tk.END)
        text_songs.delete("1.0", tk.END)
        
        load_playlists()
    
    except:
        messagebox.showerror("Error", "Could not save")


def load_playlists():
    listbox.delete(0, tk.END)
    
    if not os.path.exists("playlists"):
        return
    
    files = os.listdir("playlists")
    
    for file in files:
        if file.endswith(".txt"):
            name = file.replace("playlist_", "").replace(".txt", "")
            listbox.insert(tk.END, name)


def view_playlist(event):
    try:
        selected = listbox.curselection()
        if not selected:
            return
        
        name = listbox.get(selected[0])
        filename = f"playlists/playlist_{name}.txt"
        
        file = open(filename, "r")
        songs = file.readlines()
        file.close()
        
        text_view.config(state="normal")
        text_view.delete("1.0", tk.END)
        
        for i, song in enumerate(songs, 1):
            text_view.insert(tk.END, f"{i}. {song}")
        
        text_view.config(state="disabled")
    
    except:
        messagebox.showerror("Error", "Could not load playlist")


root = tk.Tk()
root.title("MusicBox")
root.geometry("550x450")

tk.Label(root, text="MusicBox", font=("Arial", 18)).pack(pady=10)

frame1 = tk.Frame(root)
frame1.pack(pady=10)

tk.Label(frame1, text="Playlist Name:").grid(row=0, column=0)
entry_name = tk.Entry(frame1, width=30)
entry_name.grid(row=0, column=1, padx=5)

tk.Label(frame1, text="Songs:").grid(row=1, column=0)
text_songs = tk.Text(frame1, width=30, height=6)
text_songs.grid(row=1, column=1, padx=5, pady=5)

tk.Button(frame1, text="Save Playlist", command=save_playlist).grid(row=2, column=1, pady=5)

frame2 = tk.Frame(root)
frame2.pack(pady=10)

tk.Label(frame2, text="Saved Playlists:").grid(row=0, column=0)
tk.Label(frame2, text="Songs:").grid(row=0, column=1)

listbox = tk.Listbox(frame2, width=25, height=8)
listbox.grid(row=1, column=0, padx=5)
listbox.bind("<<ListboxSelect>>", view_playlist)

text_view = tk.Text(frame2, width=30, height=8, state="disabled")
text_view.grid(row=1, column=1, padx=5)

tk.Button(frame2, text="Refresh", command=load_playlists).grid(row=2, column=0, pady=5)

load_playlists()

root.mainloop()
