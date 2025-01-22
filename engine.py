from getpass import getpass
import re
print("Welcome In Rock_Paper_Scisors Game!")
firstChoose = getpass('First player choose: ')
secondChoose = getpass('Second player choose: ')
def check(first,second):
 searchFirstInput=re.search("^r|s|p",first,re.I)
 searchSecondInput=re.search("^r|s|p",second,re.I)
 firstResult=searchFirstInput.group().lower()
 secondResult=searchSecondInput.group().lower()
 print("The First Player Choosed {} \nThe Second Player Choosed {}".format(firstResult,secondResult))
 if firstResult==secondResult:
  print("draw!!")
 if firstResult=="r" and secondResult=="s" :
   print(f"""The First Player Won!!""")
 if firstResult=="s" and secondResult=="r" :
   print(f"""The Second Player Won!!""")
 if firstResult=="p" and secondResult=="r" :
   print(f"""The First Player Won!!""")
 if firstResult=="r" and secondResult=="p" :
   print(f"""The Second Player Won!!""")
 if firstResult=="s" and secondResult=="p" :
   print(f"""The First Player Won!!""")
 if firstResult=="p" and secondResult=="s" :
   print(f"""The Second Player Won!!""")

check(firstChoose,secondChoose)