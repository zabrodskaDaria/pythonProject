import eel
import pyowm


owm = pyowm.OWM("6d00d1d4e704068d70191bad2673e0cc")

@eel.expose
def get_weather(place):
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(place)
    w = observation.weather

    temp = w.temperature('celsius')['temp']

    return "В городе" + place + "сейчас" + str(temp) + "градусов."


