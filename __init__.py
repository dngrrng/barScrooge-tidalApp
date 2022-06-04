###############
# Bar Scrooge #
###############

# Armed only with your EMF badge, and wondering which pint to get at the bar?
# Now make your decision with the aid of the alchohol-cost efficiency of each tap drink

import app
import urequests

#####################
# Main Logic of App #
#####################

drinks_url = 'https://bar.emf.camp/api/on-tap.json'

pintVolume = 568.0 #d Who knew a UK pint was different to a US pint?

#d For those of you that took Volunteer bar training 
#d https://www.emfcamp.org/volunteer/bar-training
def abv2Value(abv,cost,volume=pintVolume):
    # Calculate units of drink
    # = ABV * (volume/100)
    units = abv * volume / 100.0
    return cost / units

# Some kind of pretty print (returns string)
#d TODO: Properly decide format here, and make writing over lines easier
def pprintDrinkJson(jsonRaw):
    # Value (price of a unit)
    v = round(abc2Volume(float(jsonRaw['abv']),float(jsonRaw['price'])),3)
    return str(v) + ' ' + jsonRaw['name'] + ', £' + str(p) 

#d Liberally stolen from examples
class barScrooge(app.TextApp):

    def on_activate(self):
        super().on_activate()
        # Little title
        self.window.println("Bar Scrooge")
        self.window.println("what's the cheap")
        self.window.println("est drink?")
        self.window.println("---")
       
	 # Collect drinks from API
        drinks = urequests.get(drinks_url).json()
       
	# Iterate over the drink categories
        for cat in drinks:
            self.window.println(cat)
            self.window.println('---') #d TODO: make a nice line divide
            for item in drinks[cat]:
                self.window.println(pprintDrinkJson(item))
        
        self.window.println('End of Items') #d - mainly for debugging

main = barScrooge

