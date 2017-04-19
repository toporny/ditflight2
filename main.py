# my modules
import dit_planes
import dit_currency_rates
import dit_io_library
import dit_airport
import dit_country
import dit_command_line
import dit_app
import sys
import prettytable

def arrayToString(array):
    s = ''
    for i in range(0,len(array)-1):
        s=s+array[i]+','
    s=s[:-1]
    return s


def main():
    planes = dit_planes.Planes()
    currency = dit_currency_rates.CurrencyRate()
    airport = dit_airport.Airport()
    country = dit_country.Country()
    app = dit_app.App(airport, country, currency, planes)


    param_choosen = dit_command_line.CommandLine(airport)
    if (isinstance(param_choosen, list)):
        app.calculate(param_choosen)

        x = prettytable.PrettyTable(["NAME", "RESULT"])
        x.align = "r"
        x.header = False

        column1 = "cheapest price"
        column2 = str(app.getCheapestPrice())+' euro'
        x.add_row([column1, column2])

        column1 = "cheapest route"
        column2 = app.getCheapestRoute()
        x.add_row([column1, column2])

        column1 = "cheapest km summary"
        column2 = str(app.getCheapestKmSummary())+' km'
        x.add_row([column1, column2])

        column1 = "URL map"
        column2 = 'http://alltic.home.pl/d16127504/?airports='+arrayToString(app.getCheapestRoute())
        x.add_row([column1, column2])

        print (x)

        x = prettytable.PrettyTable(["NAME", "RESULT"])
        x.align = "r"
        x.header = False

        column1 = "shortest price"
        column2 = str(app.getShortestPrice())+' euro'
        x.add_row([column1, column2])

        column1 = "shortest route"
        column2 = app.getShortestRoute()
        x.add_row([column1, column2])

        column1 = "shortest km summary"
        column2 = str(app.getShortestKmSummary())+' km'
        x.add_row([column1, column2])

        column1 = "URL map"
        column2 = 'http://alltic.home.pl/d16127504/?airports='+arrayToString(app.getShortestRoute())
        x.add_row([column1, column2])
        print (x)

        x = prettytable.PrettyTable(["NAME", "RESULT"])
        x.align = "r"
        x.header = False

        column1 = "longest single trip"
        column2 = str(app.getLongestSingleTrip())+' km'
        x.add_row([column1, column2])
        print (x)


    else:
        eval(param_choosen)
   



main()