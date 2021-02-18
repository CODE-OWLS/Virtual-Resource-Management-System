from tkinter import *
import requests 
import json 
import datetime 
from PIL import ImageTk, Image 
  
def call(): 
    # necessary details 
    root = Tk() 
    root.title("Weather App") 
    root.geometry("400x500")
    root.iconbitmap('images\mainlogo.ico') 
    root['background'] = "#24292e"
    
    # Dates 
    dt = datetime.datetime.now() 
    date = Label(root, text=dt.strftime('%A,'), bg='#24292e', font=("bold", 15),fg="white") 
    date.place(x=5, y=130) 
    month = Label(root, text=dt.strftime('%m %B'), bg='#24292e', font=("bold", 15),fg="white") 
    month.place(x=100, y=130) 
    
    # Time 
    hour = Label(root, text=dt.strftime('%I:%M %p'),bg='#24292e', font=("bold", 15),fg="white") 
    hour.place(x=10, y=160) 
    

    # City Search 
    city_name = StringVar() 
    city_entry = Entry(root,textvariable=city_name, width=35, borderwidth=5)
    city_entry.insert(0,"Enter a City Name or Zip Code Here") 
    city_entry.grid(row=1, column=0, ipady=10) 
    
    
    def city_name(): 
    
        # API Call 
        api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+ city_entry.get() + "&units=metric&appid="+"45cf08acb49a2f6aaa93254d8c277028") 
    
        api = json.loads(api_request.content) 
    
        # Temperatures 
        y = api['main'] 
        current_temprature = y['temp'] 
        humidity = y['humidity'] 
        tempmin = y['temp_min'] 
        tempmax = y['temp_max'] 
    
        # Coordinates 
        x = api['coord'] 
        longtitude = x['lon'] 
        latitude = x['lat'] 
    
        # Country 
        z = api['sys'] 
        country = z['country'] 
        citi = api['name'] 
    
        # Adding the received info into the screen 
        lable_temp.configure(text=current_temprature) 
        lable_humidity.configure(text=humidity) 
        lable_country.configure(text=country) 
        lable_citi.configure(text=citi) 
    
    
    # Search Bar and Button 
    city_nameButton = Button(root, text="Search", command=city_name,fg="white",bg="#1d2125") 
    city_nameButton.grid(row=1, column=1, padx=5, stick=W+E+N+S) 
    
    
    # Country  Names and Coordinates 
    lable_citi = Label(root, text="...", width=0,bg='#24292e',fg='white', font=("bold", 15)) 
    lable_citi.place(x=10, y=63) 
    
    lable_country = Label(root, text="...", width=0,bg='#24292e',fg='white', font=("bold", 15)) 
    lable_country.place(x=135, y=63) 
    
    # Current Temperature 
    
    lable_temp = Label(root, text="...", width=0, bg='#24292e',font=("Helvetica", 110), fg='white') 
    lable_temp.place(x=18, y=220) 
    
    # Other temperature details 
    
    humi = Label(root, text="Humidity: ", width=0,bg='#24292e', fg='white',font=("bold", 15)) 
    humi.place(x=3, y=400) 
    
    lable_humidity = Label(root, text="...", width=0,bg='#24292e', fg='white',font=("bold", 15)) 
    lable_humidity.place(x=107, y=400) 
    
    root.mainloop()
#hello test commit\
#hrere