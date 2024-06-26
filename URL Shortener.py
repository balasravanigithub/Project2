from tkinter import *
import pyshorteners

root=Tk()
root.title("URL Shortener")
#root.iconbitmap('c:/gui/codemy.ico')
root.geometry("600x600")

def shorten():
    if shorty.get():
        shorty.delete(0,END)
    
    if my_entry.get():
        #convert to tiny url
        url=pyshorteners.Shortener().tinyurl.short(my_entry.get())
        #output to screen
        shorty.insert(END,url)

        #Reverse URL
        print(pyshorteners.Shortener().tinyurl.expand(url))


my_label=Label(root,text="Enter Link To Shorten",font=("Helvetica",34))
my_label.pack(pady=20)

my_entry=Entry(root,font=("Helvetica",24))
my_entry.pack(pady=20)

my_button=Button(root,text="Shorten Link",command=shorten , font=("Helvetica",24))
my_button.pack(pady=20)

shorty_label=Label(root,text="Shortened Link",font=("Helvetica",14))
shorty_label.pack(pady=50)

shorty=Entry(root,font=("Helvetica",32),justify=CENTER,width=30,bd=0,bg="systembuttonface")
shorty.pack(pady=10)




               

root.mainloop()