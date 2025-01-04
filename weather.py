import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
import time

def getWeather(event=None):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=9aa547fa547121a7a83714aff730c6ae"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunrise'] + 3600))
    sunset = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunset'] + 3600))

    final_info = f"{condition}\n{temp}°C"
    final_data = (
        f"Max Temp: {max_temp}°C\n"
        f"Min Temp: {min_temp}°C\n"
        f"Pressure: {pressure} hPa\n"
        f"Humidity: {humidity}%\n"
        f"Wind Speed: {wind} m/s\n"
        f"Sunrise: {sunrise}\n"
        f"Sunset: {sunset}"
    )

    icon_path = f"icons/{condition.lower()}.png"
    icon = Image.open(icon_path)
    icon = icon.resize((100, 100), Image.LANCZOS)
    icon = ImageTk.PhotoImage(icon)

    icon_label.config(image=icon)
    icon_label.image = icon
    label1.config(text=final_info)
    label2.config(text=final_data)

canvas = tk.Tk()
canvas.geometry("450x550")
canvas.title("Weather App")
canvas.configure(background='lightblue') 

f = ("poppins", 15, "bold")
t = ("poppins", 20, "bold")

frame = ttk.Frame(canvas, padding="10")
frame.pack(fill=tk.BOTH, expand=True)
frame.configure(style='TFrame')

style = ttk.Style()
style.configure('TFrame', background='lightblue')  
style.configure('TLabel', background='lightblue')  
style.configure('TLabel', font=('Helvetica', 12))
style.configure('TEntry', foreground='grey', background='lightblue', font=('Helvetica', 12), borderwidth=2, relief="solid")
style.configure('TButton', background='lightblue', font=('Helvetica', 12), padding=10)

entry_frame = tk.Frame(frame, bg='gray', bd=2)
entry_frame.pack(pady=20)
entry_frame.pack_propagate(False)
entry_frame.config(width=300, height=40)

textField = tk.Entry(entry_frame, font=t, justify='center', bd=0, bg='lightgray', fg='black', relief='flat')
textField.pack(fill=tk.BOTH, expand=True)
textField.focus()
textField.bind('<Return>', getWeather)

button_frame = tk.Frame(frame, bg='lightblue', bd=2)
button_frame.pack(pady=10)
button_frame.pack_propagate(False)
button_frame.config(width=200, height=50)

button = tk.Button(button_frame, text="Get Weather", command=getWeather, font=('Helvetica', 12), bg='lightgray', fg='black', relief='flat', bd=0)
button.pack(fill=tk.BOTH, expand=True)

icon_label = ttk.Label(frame, anchor='center')
icon_label.pack()

label1 = ttk.Label(frame, font=t, anchor='center', justify="center")
label1.pack()
label2 = ttk.Label(frame, font=f, anchor='center', justify="center")
label2.pack()

canvas.mainloop()