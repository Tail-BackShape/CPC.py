#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#cpc.py : Ciphertext and Plaintext Converter

import tkinter as tk
import tkinter.filedialog

root = tk.Tk()
root.title("C. P. C.")
root.geometry("600x500")
root.resizable(0, 0)

label1 = tk.Label(text="Plaintext or Ciphertext")
label1.place(x=30, y=30)

textbox1 = tk.Entry(width=70)
textbox1.place(x=30, y=50)

textbox2 = tk.Text(width=70, height=28)
textbox2.place(x=30, y=110)


def cov():
    textbox2.delete(1.0, tk.END)
    for KEY in range(26):
        date = textbox1.get()
        if (10 > KEY):
            plain = "Key " + str(KEY) + ":"
        else:
            plain = "Key" + str(KEY) + ":"

        for char in list(date):
            ASCII = ord(char)
            if (32 <= ASCII and ASCII <= 64):
                plain += chr(ASCII)

            if (65 <= ASCII and ASCII <= 90):
                a = ASCII - 65
                a = (a - KEY) % 26
                ASCII = a + 65
                plain += chr(ASCII)

            if (91 <= ASCII and ASCII <= 96):
                plain += chr(ASCII)

            if (97 <= ASCII and ASCII <= 122):
                a = ASCII - 97
                a = (a - KEY) % 26
                ASCII = a + 97
                plain += chr(ASCII)

            if (123 <= ASCII and ASCII <= 126):
                plain += chr(ASCII)

        textbox2.insert(tk.END, plain + "\n")


button1 = tk.Button(root, text="Convert", command=cov).place(x=30, y=80)


def val():

    filename = tk.filedialog.asksaveasfilename(
        filetypes=[("テキストファイル", "*.txt")],
        initialdir="./",
        defaultextension="txt",
    )
    if (filename != ""):
        with open(filename, mode="w") as f:
            f.write(textbox2.get("1.0", "end-1c"))
            f.close


button2 = tk.Button(root, text="SAVE", command=val).place(x=100, y=80)

root.mainloop()
