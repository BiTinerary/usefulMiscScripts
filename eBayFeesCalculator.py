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
		tk.Label(width=75, height=3, textvariable=v, relief='ridge').grid(row=7, rowspan=3, column=0, columnspan=2, padx=5, pady=5)

		def getInput():
			tk.Label(width=75, height=3, textvariable=v, relief='ridge').grid(row=7, rowspan=3, column=0, columnspan=2, padx=5, pady=5)
			try:
				grossSales = float(entry1.get())
				costOfGoods = float(entry2.get())

				ebayFees = float(grossSales * .10)
				payPalFees = float(grossSales * .03) + .30
				shippingCosts = float(entry3.get())
				miscellaneousCosts = float(entry4.get())

				totalFees = round(ebayFees + payPalFees + shippingCosts + miscellaneousCosts, 2)
				netProfits = round(grossSales - costOfGoods - totalFees, 2)
				netMargin = round(netProfits / costOfGoods * 100, 2)

				print grossSales
				print costOfGoods
				print ebayFees
				print payPalFees
				print shippingCosts

				print "Gross: %s" % grossSales
				print "Net: %s" % netProfits
				#print "Margin: %s" 

				v.set("Gross Sales:    %s\n Net Profits: %s          Net Margin: %s\n Total Fees: %s            Cost of Goods: %s" % (grossSales, netProfits, netMargin, totalFees, costOfGoods))
			
			except:
				tk.Label(width=75, height=3, textvariable=v, relief='ridge', fg='red').grid(row=7, rowspan=3, column=0, columnspan=2, padx=5, pady=5)
				v.set("INVALID INPUT/S")

		self.bind('<Return>', (lambda event: getInput()))
		getAllInputs0 = tk.Button(text='Calculate Inputs', width=74, height=2, command=lambda: getInput())
		getAllInputs0.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

		label1 = tk.Label(width=30, anchor='n', relief='ridge', text="Gross Sales", fg='dark green')
		label1.grid(row=1, column=0, padx=5, pady=2)
		entry1 = tk.Entry(self, width=50)
		entry1.grid(row=1, column=1, padx=5, pady=2)

		label2 = tk.Label(width=30, anchor='n', relief='ridge', text="Cost Of Goods", fg='dark orange')
		label2.grid(row=2, column=0, padx=5, pady=2)
		entry2 = tk.Entry(self, width=50)
		entry2.grid(row=2, column=1, padx=5, pady=2)

		label3 = tk.Label(width=30, height=0, anchor='n', relief='ridge', text="Shipping Costs", fg='red')
		label3.grid(row=3, column=0, padx=5, pady=2)
		entry3 = tk.Entry(self, width=50)
		entry3.grid(row=3, column=1, padx=5, pady=2)

		label4 = tk.Label(width=30, height=0, anchor='n', relief='ridge', text="Misc. Fees", fg='red')
		label4.grid(row=4, column=0, padx=5, pady=2)
		entry4 = tk.Entry(self, width=50)
		entry4.grid(row=4, column=1, padx=5, pady=2)

		label5 = tk.Label(width=75, height=0, anchor='n', relief='ridge', text="Ebay Fees: 10%", fg='red')
		label5.grid(row=5, column=0, padx=5, pady=2, columnspan=2)

		label6 = tk.Label(width=75, height=0, anchor='n', relief='ridge', text="PayPal Fees: 2.9% + $0.30", fg='red')
		label6.grid(row=6, column=0, padx=5, pady=2, columnspan=2)

if __name__ == "__main__":
	root = mainApp()
	root.resizable(0,0)
	center(root)
	root.title('eBay Fees Calculator')
	root.mainloop()
