import requests

def get_weather(city):
    try:
        api_key = "your_openweathermap_api_key"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data["cod"] != 200:
            return "I couldn't find the weather for that location."
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        return f"The temperature in {city} is {temp}°C with {description}."
    except Exception as e:
        return "Sorry, I couldn't get the weather information."
