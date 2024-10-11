from urllib.request import urlopen

html = urlopen('https://calendar.google.com/calendar/u/0/r/month/2024/12/1')
print(html.read())