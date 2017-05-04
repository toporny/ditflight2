# my modules
import dit_planes
import dit_currency_rates
import dit_airport
import dit_country
import dit_app
import dit_app_form
from tkinter import *


# Start point
def main():

    planes = dit_planes.Planes()
    currency = dit_currency_rates.CurrencyRate()
    airport = dit_airport.Airport()
    country = dit_country.Country()

    # pass all objects to app
    app = dit_app.App(airport, country, currency, planes)
    
    # TK initialization
    root = Tk()
    root.title('DIT Flight 1.0')
    root.resizable(width  = False, height = False)
    root.geometry('600x600')
    photo = PhotoImage(file = "img/toporny.png")
    label1 = Label(image = photo)
    label1.place(x = 15, y = 10)

    # launch the app
    app = dit_app_form.ditForm(root, app)
    root.mainloop() 


if (__name__ == '__main__'):  # for unit tests
    main()