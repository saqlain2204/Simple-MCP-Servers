from mcp.server.fastmcp import FastMCP
import requests
import os

mcp = FastMCP(name="weather-server")

@mcp.tool()
def get_current_weather(city: str):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": os.getenv('OPENWEATHER_API_KEY'),
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        location = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        weather_condition = data['weather'][0]['description']

        print(f"Weather in {location}, {country}:")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {weather_condition.capitalize()}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    

if __name__ == '__main__':
    mcp.run()