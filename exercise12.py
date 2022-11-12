#1
import requests

request = "https://api.chucknorris.io/jokes/random" 

try:
    response = requests.get(request)
    if response.status_code==200:
        json_response = response.json()
        print(json_response["value"])
except requests.exceptions.RequestException as e:
    print ("Request could not be completed.")

#2
#Based on the API  https://openweathermap.org/api/forecast30
#Key is deactivated for security reasons, it will not work.
import requests

def k_to_c(t):
    return t - 273.15

#Use only if you need fahrenheit instead
def k_to_f(t):
    return t*9/5 - 459.67

name = input("Municipality name?:")
key =  "982530b74829ae9c3cca99c2eb1804fd"
request = "https://pro.openweathermap.org/data/2.5/forecast/climate?q=" + str(name) +",FI" + "&appid=" + key
response_data = ""

try:
    response = requests.get(request)
    response_data = response.json()
    print(response_data)

except requests.exceptions.RequestException as e:
    print("error")


print("The weather in the municipality is:", response_data["weather"]["main"])
print("The windspeed in the municipality is:", response_data["main"]["temp"], " m/s")
print("The temperature in the municipality is:", k_to_c(int(response_data["main"]["temp"])), " degrees celsius")
