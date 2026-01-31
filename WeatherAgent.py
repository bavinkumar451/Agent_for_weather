import requests

# ---------- TOOL LAYER ----------
def get_weather_temperature(city: str) -> str:
    API_KEY = "14d3697b3ae27c505fb0ca599137d454"
    URL = "https://api.openweathermap.org/data/2.5/weather"
    # Format city to match OpenWeatherMap naming: capitalize first letters
    city_for_api = city.strip().title()

    params = {
        "q": city_for_api,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(URL, params=params)
    data = response.json()

    if response.status_code != 200:
        return "Unable to fetch weather data."

    temperature = data["main"]["temp"]
    return f"The current temperature in {city_for_api} is {temperature}°C."


# ---------- AGENT LAYER ----------
class WeatherAgent:
    def __init__(self, name):
        self.name = name

    def run(self, user_input: str) -> str:
        city = self.extract_city(user_input)
        if not city:
            return "Please provide a city name."

        return get_weather_temperature(city)

    def extract_city(self, text: str) -> str:
        # Try to extract a city name from phrases like 'in <city>' or 'at <city>' (case-insensitive)
        if not text:
            return ""

        stripped = text.strip()
        lower = stripped.lower()
        for sep in (" in ", " at "):
            if sep in lower:
                idx = lower.rfind(sep)
                city = stripped[idx + len(sep):].strip()
                return city.strip(" ,.?!)\n\r\t")

        # Fallback: use the last token (remove common punctuation)
        words = stripped.split()
        if words:
            return words[-1].strip(" ,.?!)\n\r\t")
        return ""


# ---------- ENTRY POINT ----------
if __name__ == "__main__":
    agent = WeatherAgent("WeatherBot")

    user_query = input("Ask about the weather (e.g., 'What is the temperature in London'): ")
    response = agent.run(user_query)

    print(response)