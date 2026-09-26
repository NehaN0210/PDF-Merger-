import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfWriter

def add_pdfs():
    files = filedialog.askopenfilenames(
        title="Select PDF Files",
        filetypes=[("PDF Files", "*.pdf")]
    )

    for file in files:
        if file not in pdfs:
            pdfs.append(file)
            listbox.insert(tk.END, file)

def merge_pdfs():
    if len(pdfs) < 2:
        messagebox.showwarning("Warning", "Select at least 2 PDFs")
        return

    output = filedialog.asksaveasfilename(
        title="Save Merged PDF",
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if output:
        merger = PdfWriter()

        for pdf in pdfs:
            merger.append(pdf)

        merger.write(output)
        merger.close()

        messagebox.showinfo("Success", "PDFs merged successfully!")

def clear():
    pdfs.clear()
    listbox.delete(0, tk.END)

# Main window
root = tk.Tk()
root.title("PDF Merger")
root.geometry("500x400")

pdfs = []

tk.Label(root, text="PDF Merger", font=("Arial", 20, "bold")).pack(pady=15)

listbox = tk.Listbox(root, width=60, height=12)
listbox.pack(pady=10)

tk.Button(root, text="Add PDFs", command=add_pdfs).pack(pady=5)
tk.Button(root, text="Merge PDFs", command=merge_pdfs).pack(pady=5)
tk.Button(root, text="Clear", command=clear).pack(pady=5)

root.mainloop()