import tkinter
import os

# Load token from Git_Tokens.txt in Documents
token_path = os.path.expanduser("~/Documents/Git_Tokens.txt")
with open(token_path, "r") as file:
    token = file.read().strip()

def set_hp(event=None):
    current_hp.set(total_hp.get())

#create the window that will hold all the information
window = tkinter.Tk()
window.title("HP Tracker")
window.geometry("500x300")
window.configure(bg="#ffc0cb")

#create the purple border around the header
border_frame = tkinter.Frame(window, bg="#800080", height=90, bd=5, relief="sunken")
border_frame.pack(fill="x", side="top")

#create the header with a darker pink than the window
banner = tkinter.Frame(border_frame, bg="#ff69b4", height=60)
banner.pack(fill="x", expand=True, padx=5, pady=5)

#create the label text
header_label = tkinter.Label(banner, text="HP Tracker", font=("Comic Sans MS", 18, "bold"), bg="#ff69b4", fg="white")
header_label.pack(padx=10, pady=10)

#frame to hold input fields
info_frame = tkinter.Frame(window, bg="#fff0f5", height=200)
info_frame.pack(fill="x", side="top", padx=10 , pady=10)

#character name input field
character_label = tkinter.Label(info_frame, text="Character Name:", bg="#fff0f5", fg="black")
character_label.grid(row=0, column=0, padx=5, pady=5)
character_name_text = tkinter.Entry(info_frame, width=60, bg="#fff0f5", fg="black")
character_name_text.grid(row=0, column=1, padx=5, pady=5)

# Total HP and Current HP variables
total_hp = tkinter.IntVar(value=0)
current_hp = tkinter.IntVar(value=0)
damage_input = tkinter.IntVar(value=0)

# Total HP
total_hp_label = tkinter.Label(info_frame, text="Total HP:", bg="#fff0f5", fg="black")
total_hp_label.grid(row=1, column=0, padx=5, sticky="e")
total_hp_entry = tkinter.Entry(info_frame, textvariable=total_hp, width=10, bg="#fff0f5", fg="black")
total_hp_entry.bind("<Return>", set_hp)
total_hp_entry.grid(row=1, column=1, sticky="w", padx=5, pady=5)

def clear_on_focus(event):
    if total_hp_entry.get() == "0":
        total_hp_entry.delete(0, tkinter.END)

total_hp_entry.bind("<FocusIn>", clear_on_focus)

# Current HP
current_hp_label = tkinter.Label(info_frame, text="Current HP:", bg="#fff0f5", fg="black")
current_hp_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
current_hp_display = tkinter.Label(info_frame, textvariable=current_hp, bg="#fff0f5", fg="black", width=10, relief="sunken")
current_hp_display.grid(row=2, column=1, sticky="w", padx=5, pady=5)

# Button to set current HP equal to total HP
set_hp_button = tkinter.Button(info_frame, text="Set HP", command=set_hp)
set_hp_button.grid(row=3, column=1, sticky="w", padx=5, pady=5)

# Damage input
damage_label = tkinter.Label(info_frame, text="Damage:", bg="#fff0f5", fg="black")
damage_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
damage_entry = tkinter.Entry(info_frame, textvariable=damage_input, width=10, bg="#fff0f5", fg="black")
damage_entry.grid(row=4, column=1, sticky="w", padx=5, pady=5)

def apply_damage():
    dmg = damage_input.get()
    new_hp = current_hp.get() - dmg
    current_hp.set(max(new_hp, 0))

subtract_button = tkinter.Button(info_frame, text="Subtract", command=apply_damage)
subtract_button.grid(row=5, column=1, sticky="w", padx=5, pady=5)



window.mainloop()




