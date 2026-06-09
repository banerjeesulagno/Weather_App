import tkinter as tk
import requests

API_KEY = "YOUR_API_KEY"

def get_weather():
    city = city_entry.get()

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        result.config(text=f"{temp}°C\n{desc}")
    else:
        result.config(text="City not found")

root = tk.Tk()
root.title("Weather App")

city_entry = tk.Entry(root)
city_entry.pack(pady=10)

btn = tk.Button(root, text="Get Weather", command=get_weather)
btn.pack()

result = tk.Label(root, text="")
result.pack(pady=10)

root.mainloop()