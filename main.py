import requests
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.image import Image
import json

Window.clearcolor = [1,1,1,1]

'''https://api.openweathermap.org/data/2.5/weather?lat=23.16&lon=82.07&appid=6d3e583b769125a8f6001301238be20d'''

# Sending an request for weather condition using API

response = requests.get(
"http://api.weatherapi.com/v1/current.json?key=1d1d37cc1a5547e3b9f134901250201&q=India Madhya Predesh  Annuppur&aqi=no")

json = response.json()

# with open("weather_report.json") as f:
#     report = f.read()

# json = json.loads(report)


# Starting the building of App using Kivy

class WeatherApp(App):

    def build(self):
        layout = BoxLayout(orientation="vertical")


        Image_layout = BoxLayout(orientation="vertical", size_hint=[1, 0.6])

        img = Image(source="night.png")
        Image_layout.add_widget(img)

        layout.add_widget(Image_layout)


        Text_layout = BoxLayout(orientation="vertical", size_hint=[1, 0.4])
        
        location = Label(text=f"Location = {json['location']['name']} {json['location']['country']}", size_hint=[1,0.1], color="black")
        Text_layout.add_widget(location)

        time = Label(text=f"Time: {json['location']['localtime']}", size_hint=[1,0.1], color="black")
        Text_layout.add_widget(time)

        currnet_temp_c = Label(text=f"Current tempreature in C {json['current']['temp_c']}", size_hint=[1,0.1], color="black")
        Text_layout.add_widget(currnet_temp_c)

        currnet_temp_f = Label(text=f"Current tempreature in F {json['current']['temp_f']}", size_hint=[1,0.1], color="black")
        Text_layout.add_widget(currnet_temp_f)

        currnet_weather_condition = Label(text=f"Current Weather condition {json['current']['condition']['text']}", size_hint=[1,0.1], color="black")
        Text_layout.add_widget(currnet_weather_condition)

        humidity = Label(text=f"Humidity: {json['current']["humidity"]}", size_hint=[1,0.1], color="black")
        Text_layout.add_widget(humidity)

        cloud = Label(text=f"Cloud: {json['current']['cloud']}", size_hint=[1,0.1], color="black")
        Text_layout.add_widget(cloud)

        layout.add_widget(Text_layout)


        return layout
    

if __name__ == "__main__":
    app = WeatherApp()
    app.run()
