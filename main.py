txt = "welcome to the jungle"
harfler = {kelime: len(kelime) for kelime in txt.split()}
print(harfler)


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {günler: temp * 9/5 + 32 for (günler, temp) in weather_c.items()}


print(weather_f)