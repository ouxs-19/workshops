#!/usr/bin/python3

enc = 'furyyzngrf{EBG13_K_Clguba_fhpu_4_PY4ffvp}'
flag = ""

for key in range(1,26):	
	for char in enc : 
		if char.isalpha() : 
			if char.isupper():
				flag+=chr((ord(char)-65-key)%26+65)
			else :
				flag+=chr((ord(char)-97-key)%26+97)
		else : 
			flag+=char
	print(flag)
	flag = ""