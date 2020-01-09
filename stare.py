import os
import webbrowser
url1 = "https://www.youtube.com/watch?v=vNShGL3PB3M"
url2 = "https://www.youtube.com/watch?v=HtVoOoATG-0"
url3 = "https://www.youtube.com/watch?v=WA3HgnDz0cc"
s1 = "trist"
s2 = "fericit"
s3 = "ok"
print("Buna cum esti astazi? ")
print("Raspunde cu: trist,fericit,ok ")
x = input("Spune starea: ")
if x == s1:
	webbrowser.open(url1)
elif x == s2:
	webbrowser.open(url2)
elif x == s3:
	webbrowser.open(url3)



