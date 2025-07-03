from base64 import b64decode

f = open("encoded_flag").read()

while True :
  try : 
    f = b64decode(f)
  except : 
    print(f)
    break