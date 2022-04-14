# Open browser

import webbrowser
from tkinter import *

root = Tk( )

root.title( "Open Browser" )
root.geometry( "300x200" )

def google():
    webbrowser.open( "https://www.google.com" )

mygoogle = Button( root, text="Open o Google", command=google ).pack( pady=60)
root.mainloop( )