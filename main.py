
day=input("Enter y/n")
soldiers=int(input("Enter numbers of soldiers: "))
engines=int(input("Enter number of engines: "))
poison=input("Enter y/n")
rain=input("Enter y/n")
strategyA="Silent Attack !!"
strategyB="Crossfire!!"
strategyC="Kill the King"

if day=="n" and soldiers>=500 and engines==50 :
  print(strategyA)
elif day=="y" and soldiers>=10000 :
  print(strategyB)
elif day=="n" and soldiers==1 and poison=="n" :
  print(strategyC)
else:
  print("nothing")