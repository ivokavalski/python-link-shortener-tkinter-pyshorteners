import tkinter
import pyshorteners

root = tkinter.Tk()

root.geometry("250x180")
root.title("URL shortener")
root.configure(bg='#8c9cb8')


#functionality for the button
def shorten():
    url = long_url_entry.get()
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(url)
    short_url_entry.insert(0, short_url)

    
    

#add widgets
long_url_label = tkinter.Label(root, text="Enter a URL",bg='#8c9cb8', fg='#1a1a1c', font=("'Ariel', 20"))
long_url_label.pack(pady=8)

long_url_entry = tkinter.Entry(root)
long_url_entry.pack()

short_url_label = tkinter.Label(root, text="Short URL" ,bg='#8c9cb8', fg='#1a1a1c', font=("'Ariel', 20"))
short_url_label.pack()

short_url_entry = tkinter.Entry(root)
short_url_entry.pack()

button = tkinter.Button(root, text="Shorten", command=shorten, bg='#8c9cb8', fg='#1a1a1c')
button.pack(pady=5)




root.mainloop()