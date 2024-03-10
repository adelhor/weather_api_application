import requests
from unidecode import unidecode
from translate import Translator
import pandas as pd  # type: ignore
from datetime import datetime


api_key = '0cc44c0d753d47508b891435240903'

# Connect to API
while True:
    city = input('Enter the name of the city. ')
    city_unidecode = unidecode(city)
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_unidecode}&aqi=yes'
    try:
        response = requests.get(url)  # get = select in sql
        if response.status_code == 200:
            response = response.json()
            break
        else:
            if response.status_code == 400:
                print("Error! Invalid city input. Try again")
    except:
        print("Unable to connect to API.")
        exit()

input_message = f'Select what you want to display for {city}: ' \
                f'\n1) Temperature' \
                f'\n2) Pressure' \
                f'\n3) Humidity' \
                f'\n4) Everything' \
                f'\nYour choice: '

while True:
    try:
        user_choice = int(input(input_message))
        if 1 <= user_choice <= 4:
            break
        else:
            print(f"{user_choice} is not supported. The choice should be between 1 and 4.")
    except ValueError:  # wleci tutaj jak podasz np. string
        print(f"Invalid value! "
              "\nTry again")

temperature = response['current']['temp_c']
pressure = response['current']['pressure_mb']
humidity = response['current']['humidity']
condition = response['current']['condition']['text']
translator = Translator(to_lang='pl')
condition_pl = translator.translate(condition)


def display_temp_icon(temp_f):
    if temp_f > 15:
        print("☀️")
    elif temp_f < -1:
        print("❄️")
    elif -1 <= temp_f <= 15:
        print("💨")


def display_pressure_icon(pressure_f):
    if pressure_f >= 1000:
        print("😃")
    elif pressure_f < 1000:
        print("😴")


def display_humidity_icon(humidity_f):
    if humidity_f <= 50:
        print("🌵")
    elif humidity_f > 50:
        print("💦")


# Display the retrieved data
if user_choice == 1:
    display_temp_icon(temp_f=temperature)
    print(f"Temperature in {city} is {temperature} degrees Celsius.")
elif user_choice == 2:
    display_pressure_icon(pressure_f=pressure)
    print(f"Pressure in {city} is {pressure} mb.")
elif user_choice == 3:
    display_humidity_icon(humidity_f=humidity)
    print(f"Humidity in {city} is {humidity}%.")
elif user_choice == 4:
    print(f'It is {condition} (PL: {condition_pl}) in {city}. Temperature is {temperature} degrees Celsius.'
        f'\nPressure in {city} is {pressure} mb.'
        f'\nHumidity in {city} is {humidity} %.')
else:
    print("Invalid input")


#prepare datetime
current_date = datetime.now().strftime("%d%m%Y")
data = {'Data': datetime.now().strftime("%d/%m/%Y"),
        'Miasto': city,
        'Temperatura': temperature,
        'Ciśnienie': pressure,
        'Humidity': humidity,
        'Stan pogodowy': condition_pl}
df = pd.DataFrame([data])
#Save data to file
excel_filename = f'dane_pogoda_{city.lower()}_{current_date}.xlsx'
df.to_excel(excel_filename, index=False, engine='openpyxl')
