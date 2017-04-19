# my modules
import dit_planes
import dit_currency_rates
import dit_io_library
import dit_airport
import dit_country
import dit_command_line
import dit_app
import sys





def main():
    print (1000000*6.29E-05)
    sys.exit(1)
    planes = dit_planes.Planes()
    currency = dit_currency_rates.CurrencyRate()
    airport = dit_airport.Airport()
    country = dit_country.Country()
    app = dit_app.App(airport, country, currency, planes)


    param_choosen = dit_command_line.CommandLine(airport)
    if (isinstance(param_choosen, list)):
        app.calculate(param_choosen)

        app.showResults()


        planes.showAvailablePlanes(app.getLongestSingleTrip())


    else:
        eval(param_choosen)
   


main()