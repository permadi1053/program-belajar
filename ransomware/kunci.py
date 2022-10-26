#program untuk enskrpsi file
import os
from cryptography.fernet import Fernet

#membaca semua file yang ada direktori
files = []
for file in os.listdir():
  if file == "gembok.py" or file == "thekey.key" or file == "kunci.py":
          continue
  if os.path.isfile(file):
        files.append(file)

print(files)

with open("thekey.key","rb") as key: #membuka file enkripsi yang ada di file thekey.key
        secretkey = key.read()

secretphrase = "permadi" #pasword untuk dekrip
user_phrase = input("masukkan password untuk deskrip filemu\n")
if user_phrase == secretphrase:
        for file in files:
                with open(file, "rb") as thefile:
                        contents = thefile.read()
                contents_decrypted = Fernet(secretkey).decrypt(contents)
                with open(file,"wb") as thefile:
                        thefile.write(contents_decrypted)
                print("selamat, passwordnya sudah benar, filemu akan terdekrip")

else:
  print("password salah, masukkan password yang benar")



