import requests as r, sys as sus, bs4 as bs
b = r.get(f"https://www.youtube.com/results?search_query={sus.argv[-1]}").text
s = bs.BeautifulSoup(b, features="html.parser")

if "watch?v=" in b:
	print(b.split("watch?v=")[2].split('"')[0])
else:
	print("wft dis shet, didnt find anything")