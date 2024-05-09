import requests
import json
import pyttsx3

# json used for making parts of dictionary
city = input("Enter the name of the city: \n")

url = f"https://api.weatherapi.com/v1/current.json?key=c421c5bb50a64e3082753836240805&q={city}"

r = requests.get(url)
# print(r.text)
print(type(r.text))
wdic = json.loads(r.text)
w = wdic['current']['temp_c']

engine = pyttsx3.init()
    
engine.say(f"The current weather in {city} is {w} degrees") 

engine.runAndWait()