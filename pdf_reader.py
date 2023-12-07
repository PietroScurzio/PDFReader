import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader
from gtts import gTTS
import os

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return text

def text_to_speech_from_pdf(pdf_path, output_path):
    text = extract_text_from_pdf(pdf_path)
    tts = gTTS(text)
    tts.save(output_path)

def browse_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    pdf_path_var.set(file_path)

def browse_output():
    file_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
    output_path_var.set(file_path)

def convert_to_speech():
    pdf_path = pdf_path_var.get()
    output_path = output_path_var.get()

    if pdf_path and output_path:
        text_to_speech_from_pdf(pdf_path, output_path)
        status_label.config(text="Conversion successful!")
    else:
        status_label.config(text="Please select PDF and output paths.")

# Create the main window
window = tk.Tk()
window.title("PDF to Speech Converter")

# Calculate the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the window width and height
window_width = 400
window_height = 300

# Calculate the x and y coordinates for the Tk window
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Set the window size and position
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

# Variables to store file paths
pdf_path_var = tk.StringVar()
output_path_var = tk.StringVar()

# UI Elements
pdf_label = tk.Label(window, text="Select PDF file:")
pdf_label.pack(pady=5)

pdf_entry = tk.Entry(window, textvariable=pdf_path_var, width=50)
pdf_entry.pack(pady=5)

pdf_button = tk.Button(window, text="Browse", command=browse_pdf)
pdf_button.pack(pady=5)

output_label = tk.Label(window, text="Select output MP3 file:")
output_label.pack(pady=5)

output_entry = tk.Entry(window, textvariable=output_path_var, width=50)
output_entry.pack(pady=5)

output_button = tk.Button(window, text="Browse", command=browse_output)
output_button.pack(pady=5)

convert_button = tk.Button(window, text="Convert to Speech", command=convert_to_speech)
convert_button.pack(pady=10)

status_label = tk.Label(window, text="")
status_label.pack()

# Run the Tkinter event loop
window.mainloop()
