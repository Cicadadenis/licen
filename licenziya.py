
from os import system
system("curl -s -O 'https://raw.githubusercontent.com/bednakovdenis/licen/master/API.txt'")

pas = open("API.txt", "r")
ss = pas.read()
pas.close()

while True:
	if ss == "1294962":
		print("ok")
		break
	else:
		try:
			ss == int(ss)
		except ValueError:
			print("Лицензия закончилась")
