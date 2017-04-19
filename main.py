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
    planes = dit_planes.Planes()
    currency = dit_currency_rates.CurrencyRate()
    airport = dit_airport.Airport()
    country = dit_country.Country()
    app = dit_app.App(airport, country, currency, planes)


    param_choosen = dit_command_line.CommandLine()
    if (isinstance(param_choosen, list)):
        app.calculate(param_choosen)
    else:
        eval(param_choosen)
   

    #app.calculate(travel_points)

    # travel_points =['DUB', 'GDN', 'BVA', 'WAW', 'DUB']
    # app.calculate(travel_points)

    # print ("getCheapestPrice",     app.getCheapestPrice())
    # print ("getCheapestRoute",     app.getCheapestRoute())
    # print ("getShortestPrice",     app.getShortestPrice())
    # print ("getShortestRoute",     app.getShortestRoute())
    # print ("getLongestSingleTrip", app.getLongestSingleTrip())

    # sys.exit(1)


main()