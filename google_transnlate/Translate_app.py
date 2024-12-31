from tkinter import *
from tkinter import ttk, messagebox
# from translate import Translator
from langdetect import detect

# Initialize the main window
window = Tk()
window.title("Google Translator")
window.geometry("1080x400")

# Function to update labels dynamically
def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    window.after(1000, label_change)

# Function to translate text
def translate_now():
    try:
        text_ = text1.get(1.0, END).strip()
        source_lang = combo1.get()
        target_lang = combo2.get()

        if not text_:
            messagebox.showwarning("Input Error", "Please enter text to translate.")
            return

        # Detect source language if not explicitly selected
        detected_lang = detect(text_)
        translator = Translator(from_lang=source_lang if source_lang != "Auto" else detected_lang, 
                                 to_lang=target_lang)
        translation = translator.translate(text_)

        # Display the translation
        text2.delete(1.0, END)
        text2.insert(END, translation)
    except Exception as e:
        messagebox.showerror("Translation Error", f"An error occurred: {e}")

# Load icon and arrow image
image_icon = PhotoImage(file="Google_Translate_Icon.png")
window.iconphoto(False, image_icon)

arrow_image = PhotoImage(file="arrow_image.png")
image_label = Label(window, image=arrow_image, width=150)
image_label.place(x=460, y=60)

# Define languages
languages = ["Auto"] + ["English", "French", "German", "Spanish", "Hindi", "Chinese"]  # Add more as needed

# Language selection comboboxes
combo1 = ttk.Combobox(window, values=languages, font="ROBOTO 14", state="readonly")
combo1.place(x=110, y=20)
combo1.set("Auto")

label1 = Label(window, text="Source Language", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

combo2 = ttk.Combobox(window, values=languages, font="ROBOTO 14", state="readonly")
combo2.place(x=730, y=20)
combo2.set("English")

label2 = Label(window, text="Target Language", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

# Source text frame
f = Frame(window, bg="black", bd=5)
f.place(x=10, y=118, width=440, height=210)

text1 = Text(f, font="ROBOTE 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

Scrollbar1 = Scrollbar(f)
Scrollbar1.pack(side="right", fill=Y)
Scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=Scrollbar1.set)

# Target text frame
f1 = Frame(window, bg="black", bd=5)
f1.place(x=620, y=118, width=440, height=210)

text2 = Text(f1, font="ROBOTE 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

Scrollbar2 = Scrollbar(f1)
Scrollbar2.pack(side="right", fill=Y)
Scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=Scrollbar2.set)

# Translate button
translate_button = Button(window, text="Translate", font="ROBOTO 15 bold italic", activebackground="purple", 
                          cursor="hand2", bd=5, bg="red", fg="white", command=translate_now)
translate_button.place(x=480, y=250)

label_change()

window.configure(bg="white")
window.mainloop()
