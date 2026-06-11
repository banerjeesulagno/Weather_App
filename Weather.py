from tkinter import *
from tkinter import ttk
import requests


def data_get() :
    city = city_name.get()

    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=3adec154c4cd46c14b421119c6a5d449").json()
    w_label1.config(text = data["weather"][0]["main"])
    wd_label1.config(text = data["weather"][0]["description"])
    wt_label1.config(text =str(int(data["main"]["temp"]-273)))
    humidity_label1.config(text = str(data["main"]["humidity"]) + " %")
    pressure_label1.config(text = str(data["main"]["pressure"]) + " hPa")
    wind_label1.config(text = str(data["wind"]["speed"]) + " m/s")
    feels_label1.config(text = str(round(data["main"]["feels_like"] - 273.15, 1)) + " °C")


pop = Tk()

pop.title("Banerjee's First App")

pop.config(bg = "Light Green")
pop.geometry("500x800")


pop_label = Label (pop,text = "Banerjee's Weather App", font = ("Times New Roman", 30, "bold"))
pop_label.place(x = 25, y = 50, height = 50, width = 450)

list_city = india_states = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]

city_name = StringVar()

com = ttk.Combobox(pop,values = list_city , font = ("Times New Roman", 20, "bold"), textvariable = city_name)
com.place(x = 25, y = 120, height = 50, width = 450)


button = ttk.Button(text ="Done", command= data_get)
button.place(x = 175, y = 200, height = 30, width = 150)

w_label = Label (pop,text = "Weather", font = ("Times New Roman", 20, "bold"))
w_label.place(x = 25, y = 250, height = 50, width = 210)

w_label1 = Label (pop,font = ("Times New Roman", 20, "bold"))
w_label1.place(x = 250, y = 250, height = 50, width = 210)


wd_label = Label (pop,text = "Weather Description", font = ("Times New Roman", 15, "bold"))
wd_label.place(x = 25, y = 330, height = 50, width = 210)

wd_label1 = Label (pop, font = ("Times New Roman", 15, "bold"))
wd_label1.place(x = 250, y = 330, height = 50, width = 210)



wt_label = Label (pop,text = "Weather Temperature", font = ("Times New Roman", 15, "bold"))
wt_label.place(x = 25, y = 400, height = 50, width = 210)

wt_label1 = Label (pop, font = ("Times New Roman", 15, "bold"))
wt_label1.place(x = 250, y = 400, height = 50, width = 210)



humidity_label = Label(pop, text="Humidity", font=("Times New Roman", 15, "bold"))
humidity_label.place(x=25, y=470, height=50, width=210)

humidity_label1 = Label(pop, font=("Times New Roman", 15, "bold"))
humidity_label1.place(x=250, y=470, height=50, width=210)



pressure_label = Label(pop, text="Pressure", font=("Times New Roman", 15, "bold"))
pressure_label.place(x=25, y=540, height=50, width=210)

pressure_label1 = Label(pop, font=("Times New Roman", 15, "bold"))
pressure_label1.place(x=250, y=540, height=50, width=210)



wind_label = Label(pop, text="Wind Speed", font=("Times New Roman", 15, "bold"))
wind_label.place(x=25, y=610, height=50, width=210)

wind_label1 = Label(pop, font=("Times New Roman", 15, "bold"))
wind_label1.place(x=250, y=610, height=50, width=210)



feels_label = Label(pop, text="Feels Like", font=("Times New Roman", 15, "bold"))
feels_label.place(x=25, y=680, height=50, width=210)

feels_label1 = Label(pop, font=("Times New Roman", 15, "bold"))
feels_label1.place(x=250, y=680, height=50, width=210)


pop.mainloop()


