import Tkinter as tk
from Tkinter import StringVar

def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

class mainApp(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)

		v = StringVar()
		tk.Label(width=75, height=2, textvariable=v, relief='ridge').grid(row=7, column=0, columnspan=2, padx=5, pady=5)

		def getInput():
			payRate = int(entry1.get())
			totalHours = int(entry2.get())
			minusIncomeTax = float(entry3.get())
			minusBill1 = int(entry4.get())
			minusBill2 = int(entry5.get())
			minusBill3 = int(entry6.get())
			
			grossCheck = payRate * totalHours
			totalTaxes = grossCheck * minusIncomeTax
			netCheck = grossCheck - totalTaxes
			
			funMoney = netCheck - minusBill1
			funMoney -= minusBill2
			funMoney -= minusBill3

			print netCheck
			print funMoney

			finArray = [netCheck, funMoney]

			v.set("Net Check: %s\n Fun Money: %s" % (finArray[0], finArray[1]))

		self.bind('<Return>', (lambda event: getInput()))

		getAllInputs0 = tk.Button(text='Gather Inputs', width=74, height=2, command=lambda: getInput())
		getAllInputs0.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

		label1 = tk.Label(width=30, anchor='n', relief='ridge', text="Pay Rate")
		label1.grid(row=1, column=0, padx=5, pady=1)
		entry1 = tk.Entry(self, width=50)
		entry1.grid(row=1, column=1, padx=5, pady=1)

		label2 = tk.Label(width=30, anchor='n', relief='ridge', text="Hours Worked")
		label2.grid(row=2, column=0, padx=5, pady=5)
		entry2 = tk.Entry(self, width=50)
		entry2.grid(row=2, column=1, padx=5, pady=1)

		label3 = tk.Label(width=30, height=0, anchor='n', relief='ridge', text="Income Tax Percent\n (Avg = 15-17%, In/Out = 20-25%)")
		label3.grid(row=3, column=0, padx=5, pady=1)
		entry3 = tk.Entry(self, width=50)
		entry3.grid(row=3, column=1, padx=5, pady=1)

		label4 = tk.Label(width=30, height=0, anchor='n', relief='ridge', text="Rent")
		label4.grid(row=4, column=0, padx=5, pady=5)
		entry4 = tk.Entry(self, width=50)
		entry4.grid(row=4, column=1, padx=5, pady=1)

		label5 = tk.Label(width=30, height=0, anchor='n', relief='ridge', text="Total Credit Due")
		label5.grid(row=5, column=0, padx=5, pady=1)
		entry5 = tk.Entry(self, width=50)
		entry5.grid(row=5, column=1, padx=5, pady=1)

		label6 = tk.Label(width=30, height=0, anchor='n', relief='ridge', text="Misc Bills")
		label6.grid(row=6, column=0, padx=5, pady=1)
		entry6 = tk.Entry(self, width=50)
		entry6.grid(row=6, column=1, padx=5, pady=1)

if __name__ == "__main__":
	root = mainApp()
	#root.resizable(0,0)
	center(root)
	root.title('Paycheck Calculator')
	root.mainloop()
