import Tkinter as tk
import os, subprocess, youtube_dl

class mainApp(tk.Tk): # The core class for creating tkinter GUI
	def __init__(self):
		tk.Tk.__init__(self)

		def getInput():
			urlInput = str(urlStringInput.get())
			nameInput = str(outputNameString.get())

			ydl_opts = {'outtmpl' : unicode(nameInput)+".mp4"}
			with youtube_dl.YoutubeDL(ydl_opts) as ydl:
				ydl.download([urlInput])

		labelUrl = tk.Label(text="Url String:")
		labelUrl.place(relx=.015, rely=.059)

		labelOutputName = tk.Label(text="File Name:")
		labelOutputName.place(relx=.015, rely=.2)

		urlStringInput = tk.Entry(width=63)#, background='orange')
		urlStringInput.place(relx=.16, rely=.059)
		urlStringInput.focus_set()

		outputNameString = tk.Entry(width=63)#, background='orange')
		outputNameString.place(relx=.16, rely=.2)

		EnterButton = tk.Button(text="youtube-dl \"UrlString\" --output \"FileName.mp4\"", width=63, height=5, background='orange', command=lambda: getInput())
		EnterButton.place(relx=.015, rely=.38)
		self.bind('<Return>', (lambda event: getInput()))

if __name__ == "__main__":
	root = mainApp()
	root.resizable(0,0) # Not resizeable
	root.geometry("465x150") # Static width/height of tkinter GUI
	root.title('Rando Vid Url Namer (youtube-dl)') # Name GUI Window
	root.mainloop()