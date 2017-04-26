import dit_flight
from tkinter import *
import sys


class fruitlist:
    def entryupdate(self, sv, i):
        print(sv, i, self.fruit[i], sv.get())

    def __init__(self, root):
        cf = Frame(root)
        cf.pack()
        self.sva = []
        self.fruit = ("Apple", "Banana", "Cherry", "Date")
        for f in self.fruit:
            i = len(self.sva)
            self.sva.append(StringVar())
            self.sva[i].trace("w", lambda name, index, mode, var=self.sva[i], i=i:
                              self.entryupdate(var, i))
            Label(cf, text=f).grid(column=2, row=i)
            Entry(cf, width=6, textvariable=self.sva[i]).grid(column=4, row=i)

root = Tk()
root.title("EntryUpdate")
app = fruitlist(root)
root.mainloop() 

sys.exit(1)


def fetch(entries):
   for entry in entries:
      field = entry[0]
      text  = entry[1].get()
      print('%s: "%s"' % (field, text)) 

def makeform(root):
	entries = []
	Label(root, text="Please insert airport codes",font=("Helvetica", 20)).place(x=190, y=5)
	# Label(master, text="Airport 0", font=("Helvetica", 16)).place(x=190, y=y_offset+40)
	# Label(master, text="Airport 1", font=("Helvetica", 16)).place(x=190, y=y_offset+80)
	# Label(master, text="Airport 2", font=("Helvetica", 16)).place(x=190, y=y_offset+120)
	# Label(master, text="Airport 3", font=("Helvetica", 16)).place(x=190, y=y_offset+160)
	# Label(master, text="Airport 4", font=("Helvetica", 16)).place(x=190, y=y_offset+200)
	# Label(master, text="Airport 5", font=("Helvetica", 16)).place(x=190, y=y_offset+240)


	y_offset = 80
	city_array = ["" for x in range(6)]

	for counter in range(6):
		Label(root, text="Airport "+str(counter),font=("Helvetica", 16)).place(x=190, y=y_offset)
		city_array[counter] = StringVar()
		city_array[counter].set('red'+str(counter))
		lr1 = Label(root, textvariable=city_array[counter], font=("Helvetica", 16)).place(x=540, y=y_offset)
		e1 = Entry(root, font=("Helvetica", 16)).place(x=285, y=y_offset)

		#code1 = StringVar()
		city_array[counter].trace("w", lambda name, index, mode, code1=code1: callback(lr1, city_array[counter]))
		e1 = Entry(master, font=("Helvetica", 16), textvariable=code1).place(x=285, y=y_offset+40)
		e1.config(width=100)


		y_offset = y_offset + 40
      # row = Frame(root)
      # lab = Label(row, width=15, text='Airport '+str(field), anchor='w')
      # ent = Entry(row)
      # row.pack(side=TOP, fill=X, padx=5, pady=5)
      # lab.pack(side=LEFT)
      # ent.pack(side=RIGHT, expand=YES, fill=X)
      # entries.append((field, ent))
	return entries

if __name__ == '__main__':
	root = Tk()
	root.title('DIT Flight 1.0')
	root.resizable(width=False, height=False)
	root.geometry('900x600')
	photo = PhotoImage(file="img/toporny.png")
	label1 = Label(image=photo)
	label1.place(x=5, y=10)



	#root = Tk()
	ents = makeform(root)
	root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
	b1 = Button(root, text='Show',
	      command=(lambda e=ents: fetch(e)))
	b1.pack(side=LEFT, padx=5, pady=5)
	b2 = Button(root, text='Quit', command=root.quit)
	b2.pack(side=LEFT, padx=5, pady=5)
	root.mainloop()


sys.exit(1)

def callback(lr, sv):
	sv.set('error')
	#sys.exit()
	pass



master = Tk()
master.title('DIT Flight 1.0')


master.resizable(width=False, height=False)
master.geometry('900x600')
photo = PhotoImage(file="img/toporny.png")
label1 = Label(image=photo)
label1.place(x=5, y=10)

# code1.trace("w", lambda name, index, mode, code1=code1: callback(lr1, city1_var))
# e1 = Entry(master, font=("Helvetica", 16), textvariable=code1).place(x=285, y=y_offset+40)
# e1.config(width=100)


Label(master, text="Please insert airport codes",font=("Helvetica", 20)).place(x=190, y=5)
y_offset = 10;
Label(master, text="Airport 0",font=("Helvetica", 16)).place(x=190, y=y_offset+40)
Label(master, text="Airport 1",font=("Helvetica", 16)).place(x=190, y=y_offset+80)
Label(master, text="Airport 2",font=("Helvetica", 16)).place(x=190, y=y_offset+120)
Label(master, text="Airport 3",font=("Helvetica", 16)).place(x=190, y=y_offset+160)
Label(master, text="Airport 4",font=("Helvetica", 16)).place(x=190, y=y_offset+200)
Label(master, text="Airport 5",font=("Helvetica", 16)).place(x=190, y=y_offset+240)

#e1 = Entry(master, font=("Helvetica", 16)).place(x=285, y=y_offset+40)
city1_var = StringVar()
city2_var = StringVar()
city3_var = StringVar()
city4_var = StringVar()
city5_var = StringVar()
city6_var = StringVar()

city1_var.set('red')
city2_var.set('Poznan')
city3_var.set('Czarek WERWEQ RWE QWER QWER QWER QWER QWER ')
city4_var.set('dupa')
city5_var.set('zimna')
city6_var.set('extra')


code1 = StringVar()
code1.trace("w", lambda name, index, mode: callback(lr1, city1_var))
e1 = Entry(master, font=("Helvetica", 16), textvariable=code1).place(x=285, y=y_offset+40)
e1.config(width=100)

e2 = Entry(master, font=("Helvetica", 16)).place(x=285, y=y_offset+80)
e3 = Entry(master, font=("Helvetica", 16)).place(x=285, y=y_offset+120)
e4 = Entry(master, font=("Helvetica", 16)).place(x=285, y=y_offset+160)
e5 = Entry(master, font=("Helvetica", 16)).place(x=285, y=y_offset+200)
e6 = Entry(master, font=("Helvetica", 16)).place(x=285, y=y_offset+240)



lr1 = Label(master, textvariable=city1_var, font=("Helvetica", 16)).place(x=540, y=y_offset+40)
lr2 = Label(master, textvariable=city2_var, font=("Helvetica", 16)).place(x=540, y=y_offset+80)
lr3 = Label(master, textvariable=city3_var, font=("Helvetica", 16)).place(x=540, y=y_offset+120)
lr4 = Label(master, textvariable=city4_var, font=("Helvetica", 16)).place(x=540, y=y_offset+160)
lr5 = Label(master, textvariable=city5_var, font=("Helvetica", 16)).place(x=540, y=y_offset+200)
lr6 = Label(master, textvariable=city6_var, font=("Helvetica", 16)).place(x=540, y=y_offset+240)

 

master.mainloop()

sys.exit(1)
   
def main():
	"""
	Main loop for application
	"""

	
	# load all data and make whole big object name
	app = dit_flight.ditFlight()

	#config = flight_configuration.Configuration()


  
	whLoop = True
	while (whLoop):
		# flight_messages.printAvailableOptions()

		# menu structure
		# ------------------------------
		# 1 - show input data
		#		1 - show planes
		#		2 - show airports list
		#		3 - show currency rates
		#		4 - show countries		
		# 2 - calculate price
		# 3 - help
		# q - quit
		menu_choosen = app.menu.showMainMenu()

		if (menu_choosen == '1'):
			submenu_choosen = app.menu.showSubMenu()

		if (menu_choosen == '2'):
			app.price.getAirportsAndCalculate()


		if (menu_choosen == '3'):
			print ("3")

		if (menu_choosen == 'w'):
			app.showCountryCurrencyTable()
			# app.menu.messagesShowInputData()

		# if (menu_choosen == '2'):
		#   #print ("calculate_price")
		#   app.menu.MessagesCalculatePrice()
		#   #flight_price.calcluatePrice(config)

		if (menu_choosen == 'q'):
			whLoop = False

		pass
		  


main()