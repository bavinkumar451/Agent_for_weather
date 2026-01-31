🌦️ Weather Agent – ADK Style (Python)

This project demonstrates a minimal Agent Development Kit (ADK) style agent implemented in Python.
The agent is capable of fetching the current temperature of a city by reasoning over user input and invoking a reusable weather tool.

The project is designed for beginners learning agent-based architectures, while still following clean software design principles.

🧠 Key Concepts Demonstrated

Agent-based design (ADK-style)

Tool abstraction

Single Responsibility Principle

Clean and readable Python code

Real-time API integration

⚙️ How It Works

User provides a natural language query (e.g., "What is the temperature in Chennai").

The agent extracts the city name.

The agent calls the weather tool.

The tool fetches real-time data from OpenWeatherMap.

The temperature is returned to the user.

🔧 Requirements

Python 3.9+

requests library

OpenWeatherMap API Key

Install dependency:

pip install requests

▶️ How to Run

Add your OpenWeatherMap API key inside weather_tool.py

Run:

python main.py

🧪 Example Output
The current temperature in Chennai is 32°C.

🚀 Future Improvements

Better NLP-based city extraction

Support for humidity and forecast

Agent memory

Async execution

Integration with LangGraph / LLM-based planners
