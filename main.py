# my modules
import dit_planes
import dit_currency_rates
import dit_airport
import dit_country
import dit_menu
import dit_app
import sys


def main():
    planes = dit_planes.Planes()
    currency = dit_currency_rates.CurrencyRate()
    airport = dit_airport.Airport()
    country = dit_country.Country()
    app = dit_app.App(airport, country, currency, planes)


    menu = dit_menu.Menu()
    app.calculate()

    print ("getCheapestPrice",     app.getCheapestPrice())
    print ("getCheapestRoute",     app.getCheapestRoute())
    print ("getShortestPrice",     app.getShortestPrice())
    print ("getShortestRoute",     app.getShortestRoute())
    print ("getLongestSingleTrip", app.getLongestSingleTrip())

    sys.exit(1)



    whLoop = True
    while (whLoop):
        menu_choosen = menu.showMenu()
        if (menu_choosen == 'q'):
            whLoop = False

        if (menu_choosen in menu.getPossibleChoosen()):
            eval(menu.getPossibleChoosen()[menu_choosen])        

        if (menu_choosen == '2'):
            app.calculate()
        

    if (menu_choosen == 'q'):
        whLoop = False

main()