import tkinter

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
character_label = tkinter.Label(info_frame, text="Character Name:", bg="#fff0f5")
character_label.grid(row=0, column=0, padx=5, pady=5)
character_name_text = tkinter.Entry(info_frame, width=60)
character_name_text.grid(row=0, column=1, padx=5, pady=5)





window.mainloop()




