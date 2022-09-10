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

### This exercise cannot be done because the host asks for personal information such as address
### and creditcard number, and I am not comfortable giving it out to the host.
