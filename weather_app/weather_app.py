import requests
try:

            latitude = float(input("Enter a latitude: "))
            longitude = float(input("Enter a longitude: "))

            url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

            response = requests.get(url,timeout=10)

            if response.status_code == 200:

                data = response.json()

                user = data["current_weather"]

            
                print(f"latitude is:  {latitude}")
                print(f"longitude is:  {longitude}")

                print(f"temperature is: {user["temperature"]}")
                print(f"Windspped is:  {user["windspeed"]}")

            else:
                print("error fetchecking data:")
except ValueError:
            print("Enter valid value")
except KeyError:
            print("Enter valid key")