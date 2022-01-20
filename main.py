import webbrowser
from datetime import datetime

clock = datetime.now()
current_time = clock.strftime("%H:%M:%S")
currentHour=clock.hour
dayOfWeek = datetime.today().weekday() #Monday=0, Sunday=6
print(dayOfWeek)


webbrowser.open("www.youtube.com")
webbrowser.open("https://trends.google.com/trends/?geo=US")

if dayOfWeek != 0 and dayOfWeek != 6:
    if currentHour <= 16 and currentHour >= 8:
        webbrowser.open("https://www.google.com/finance/?tab=re&authuser=0")


#Start-Process "https://www.youtube.com/results?search_query=$askYoutubeFor"

if currentHour < 18:
    webbrowser.open("https://www.livesportsontv.com/")
    webbrowser.open("www.google.com/search?q=weather")


if dayOfWeek == 5 or dayOfWeek == 6:
    webbrowser.open("https://www.chess.com/play/computer")


webbrowser.open("https://www.youtube.com/watch?v=gNi_6U5Pm_o&list=PLI_7Mg2Z_-4I-W_lI55D9lBUkC66ftHMg")

