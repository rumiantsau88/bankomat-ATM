pin = ""
myfile = open("pass.txt", "r")
for i in myfile:
    pin = str(i)
myfile.close()
print(f"Your pin code {pin}")
