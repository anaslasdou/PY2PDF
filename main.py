import PyPDF2
import pyttsx3
import tkinter as tk
from tkinter import filedialog

def read_pdf():
    # Open file dialog to select PDF
    book_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if not book_path:
        return  # User cancelled selection or no file chosen

    # Initialize PDF reader
    with open(book_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        engine = pyttsx3.init()

        # Read each page and convert text to speech
        for page_num, page in enumerate(pdf_reader.pages, start=1):
            text = page.extract_text()
            engine.say(text)
            engine.runAndWait()

        engine.stop()  # Stop speech engine when finished

# Create GUI
root = tk.Tk()
root.title("PDF Text-to-Speech")
root.geometry("300x100")

# Button to trigger PDF selection and text-to-speech conversion
button = tk.Button(root, text="Select PDF", command=read_pdf)
button.pack(pady=20)

root.mainloop()
