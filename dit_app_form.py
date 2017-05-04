from tkinter import *
import webbrowser
import copy

class ditForm:

    # tkinter interface contructor
    def __init__(self, root, app):
        # class variables
        cf = Frame(root)
        cf.pack()
        self.__app = app
        self.sva = []
        self.cities = []
        self.chepest_string = StringVar()
        self.shortest_string = StringVar()
        self.show_map_button1_state = StringVar()
        self.show_map_button2_state = StringVar()
        self.planes_string = StringVar()

        find_route_button_state = StringVar()
        y_offset = 55
        self.show_map_button1_state.set(DISABLED)
        self.show_map_button2_state.set(DISABLED)
        self.planes_string.set('')

        # tkinter label title
        Label(root, text="Please insert airport codes",font=("Helvetica", 20)).place(x=210, y=5)

        for airport_index in range(6):
            i = len(self.sva)
            self.sva.append(StringVar())
            self.cities.append(StringVar())
            self.sva[i].trace("w", lambda name, index, mode, var=self.sva[i], i=i: self.entryupdate(var, i))
            Label(root, text="Airport "+str(airport_index),font=("Helvetica", 16)).place(x=210, y=y_offset)
            Entry(root, textvariable=self.sva[i], font=("Helvetica", 16)).place(x=305, y=y_offset)          
            Label(root, textvariable=self.cities[i], font=("Helvetica", 9)).place(x=300, y=y_offset+28)
            y_offset = y_offset + 50

        # tkinter button Find Route
        self.find_route_button_state = Button(root, text ="Find Route", font=("Helvetica", 10), width="41", command = self.findRoute)
        self.find_route_button_state.config(state='disabled')
        self.find_route_button_state.place(x=210, y=y_offset)
 
        # tkinter button Shortest Route Map
        self.show_map_button1 = Button(root, text ="Shortest Route Map", font=("Helvetica", 10), width="19", command = self.showShortestMap)
        self.show_map_button1.config(state='disabled')
        self.show_map_button1.place(x=210, y=y_offset + 35)

        # tkinter button Cheapest Route Map
        self.show_map_button2 = Button(root, text ="Cheapest Route Map", font=("Helvetica", 10), width="19", command = self.showCheapestMap)
        self.show_map_button2.config(state='disabled')
        self.show_map_button2.place(x=385, y=y_offset + 35)

        # initialization textvariables
        y_offset = y_offset + 50
        self.shortest_string.set("")
        self.chepest_string.set("")

        # 3 result labels. 1- left column "Shortest", 2-right column "Chepest", 3- "planes result"
        Label(root, font=("Helvetica", 11), justify = LEFT,textvariable= self.shortest_string ).place(x=15, y=180)
        Label(root, font=("Helvetica", 11), justify = LEFT, textvariable=self.chepest_string ).place(x=120, y=180)
        Label(root, font=("Helvetica", 11), justify = LEFT, textvariable=self.planes_string ).place(x=15, y=430)
        

    # this method is run after keypressed
    def entryupdate(self, sv, i):
        # print(sv, i, self.cities[i], sv.get())
        
        # code its string in my entry field
        code =  sv.get().upper();

        # disable show_map_button1 and show_map_button2
        self.show_map_button1.config(state='disabled')
        self.show_map_button2.config(state='disabled')

        __all = []
        codes_array = []
        for airport_index in range(6):
            c = self.sva[airport_index].get().upper();
            codes_array.append(c)
            if (c != ''):
                __all.append(c)

        # make find_route_button_state visible only if are at leas 2 codes
        if (len(__all)>2):
            self.find_route_button_state.config(state='normal')
        else:
            self.find_route_button_state.config(state='disabled')
            self.shortest_string.set('')
            self.chepest_string.set('')
            self.planes_string.set('')


        # if len(airportcode) > 3  then show error message under entry field
        if (len(code)>3):
            self.cities[i].set('- - - - - - -  INVALID CODE  - - - - - - - -')
            self.find_route_button_state.config(state='disabled')

        # if len(airportcode) < 3 then remove any error message if was any
        if (len(code)<3):
            self.cities[i].set('')
            return 

        # if len(airportcode) == 3 then try to find city name and country
        if (len(code) == 3):
            if (self.__app.oAirport.airportExist(code)):
                city = self.__app.oAirport.getAirportCity(code)
                country = self.__app.oAirport.getAirportCountry(code)
                city_country = city[:20]+ ' / '+ country[:20]
                self.cities[i].set(city_country)
            else:
                self.cities[i].set(' - - - unknown airport code - - - ')
                self.find_route_button_state.config(state='disabled')


        # check if is any duplicated airport code
        del codes_array[i]
        if (code in codes_array):
            self.cities[i].set(' - - - duplicated code !!! - - - ')
            self.find_route_button_state.config(state='disabled')




    # Find route - its called after click FIND ROUTE button
    def findRoute(self):

        param_choosen = []
        for airport_index in range(6):
            code = self.sva[airport_index].get().upper();
            if (code == ''):
                continue

            if (self.__app.oAirport.airportExist(code)):
                param_choosen.append(code)                
            else:
                self.find_route_button_state.config(state='disabled')
                self.cities[airport_index].set(' - - - unknown airport code - - - ')
                self.show_map_button1.config(state='disabled')
                self.show_map_button2.config(state='disabled')
                return False

         # duplicate first airport on the end (but only if user forgot it).
        if (param_choosen[-1] != param_choosen[0]):
            param_choosen.append(param_choosen[0])

        self.__app.calculate(param_choosen)

        self.chepest_string.set(self.__app.getCheapestRouteString() + '\nPrice:\n'+str(self.__app.getCheapestPrice()) + ' €\n\n'+ str(self.__app.getCheapestKmSummary()) + ' km')
        self.shortest_string.set(self.__app.getShortestRouteString() + '\nPrice:\n'+str(self.__app.getShortestPrice()) + ' €\n\n'+ str(self.__app.getShortestKmSummary()) + ' km')
        self.show_map_button1.config(state='normal')
        self.show_map_button2.config(state='normal')

        planes_summary = 'Longest distance of the route: '+ str(self.__app.getLongestSingleTrip()) + ' km\n\n'
        planes_summary = planes_summary + self.__app.oPlanes.getAvailablePlanesString(self.__app.getLongestSingleTrip())

        self.planes_string.set(planes_summary)
        

    # opens browser with shortest map
    def showShortestMap(self):
        url = 'http://alltic.home.pl/d16127504/?airports='
        airports = copy.copy(self.__app.getCheapestRoute())
        airports.pop(-1)
        for airport in airports:
            url = url + airport + ','
        webbrowser.open(url.strip(','))


    # opens browser with cheapest map
    def showCheapestMap(self):
        url = 'http://alltic.home.pl/d16127504/?airports='
        airports = copy.copy(self.__app.getShortestRoute())
        airports.pop(-1)
        for airport in airports:
            url = url + airport + ','
        webbrowser.open(url.strip(','))


