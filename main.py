# Dictionaries: MokéBeast

mb={"Name":None,"Type":None,"Special Move":None,"HP":None, "MP":None}

# Asking for input to fill the dictionary items for each key

for key in mb.keys():
  mb[key]=input(f"{key}\n").capitalize().strip()
  print()
  
print()
def c(color):
  if color=="Fire":
    print("\033[31m", end="")
  elif color=="Water":
    print("\033[34m", end="")
  elif color=="Air":
    print("\033[37m", end="")
  elif color=="Earth":
    print("\033[32m", end="")
  elif color=="Spirit":
    print("\033[35m", end="")

# Checking input

if mb["Type"]=="Fire":
  c("Fire")
elif mb["Type"]=="Water":
  c("Water")
elif mb["Type"]=="Air":
  c("Air")
elif mb["Type"]=="Earth":
  c("Earth")
elif mb["Type"]=="Spirit":
  c("Spirit")

# Printing result for each value

for key,value in mb.items():
  print(f"{key:<12}:{value}")
  