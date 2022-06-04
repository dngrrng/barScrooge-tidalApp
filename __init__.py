import app
import urequests

drinks_url = 'https://bar.emf.camp/api/on-tap.json'
pintVolume = 568.0 

def abv2Value(abv,cost,volume=pintVolume):
    units = abv * volume / 100.0
    return cost / units

def pprintDrinkJson(jsonRaw):
    v = round(abv2Value(float(jsonRaw['abv']),float(jsonRaw['price'])),3)
    return str(v) + ' ' + jsonRaw['name'] + ', £' + jsonRaw['price']
    
class barScrooge(app.TextApp):

    def on_activate(self):
        super().on_activate()
        drinks = urequests.get(drinks_url).json()
        for cat in drinks:
            self.window.println(cat)
            for item in drinks[cat]:
                self.window.println(pprintDrinkJson(item))

main = barScrooge
