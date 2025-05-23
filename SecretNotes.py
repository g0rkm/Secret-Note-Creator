import tkinter
import tkinter.messagebox
from tkinter import PhotoImage
import cryptocode

window=tkinter.Tk()
photo=PhotoImage(file="logo.png")
window.iconphoto(False,photo)
window.minsize(height=600,width=350)

def Encrypt():
    title=titleBox.get("1.0",tkinter.END).strip()
    masterKey=keyBox.get("1.0",tkinter.END).strip()
    note=noteBox.get("1.0",tkinter.END).strip()
    if title=="" or note=="" or masterKey=="":
        tkinter.messagebox.showerror("Error", "Enter all information")
    else:
        encNote = cryptocode.encrypt(note,masterKey)
        with open("secret.txt","a") as myFile:
            myFile.write(f"{title}\n")
            myFile.write(f"{encNote}\n")
def Decrypt():
    masterKey=keyBox.get("1.0",tkinter.END).strip()
    note=noteBox.get("1.0",tkinter.END).strip()
    if masterKey=="" or note=="":
        tkinter.messagebox.showerror("Error", "Enter all information")
    else:
        decNote=cryptocode.decrypt(note,masterKey)
        noteBox.delete("1.0","end")
        noteBox.insert("1.0",decNote)
#LOGO
imageLabel=tkinter.Label(image=photo)
imageLabel.place(relx=0.5,y=0,anchor="n")


#Enter your title kısmı
topLabel=tkinter.Label(text="Enter your title",font=("Arial",13,"normal"))
topLabel.place(relx=0.5,y=93,anchor="n")

#Title için textbox
titleBox=tkinter.Text(width=25,height=1)
titleBox.place(relx=0.5,y=120,anchor="n")


#Enter your note kısmı
midLabel=tkinter.Label(text="Enter your note",font=("Arial",13,"normal"))
midLabel.place(relx=0.5,y=155,anchor="n")


#Not için textbox
noteBox=tkinter.Text(width=35,height=13)
noteBox.place(relx=0.5,y=183,anchor="n")

#Enter master key kısmı
bottomLabel=tkinter.Label(text="Enter master key",font=("Arial",13,"normal"))
bottomLabel.place(relx=0.5,y=400,anchor="n")


#Master key için textbox
keyBox=tkinter.Text(width=25,height=1)
keyBox.place(relx=0.5,y=425,anchor="n")

#Save & Encrypt button
saveButton=tkinter.Button(text="Save & Encrypt",font=("Arial",10,"normal"),width=11,height=1,command=Encrypt)
saveButton.place(relx=0.5,y=480,anchor="n")


#Decrypt button
decButton=tkinter.Button(text="Decrypt",font=("Arial",10,"normal"),width=11,height=1,command=Decrypt)
decButton.place(relx=0.5,y=520,anchor="n")




window.mainloop()