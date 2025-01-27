from getpass import getpass
import re
print("Welcome In Rock_Paper_Scissors Game!")
print("The Choices Are R=Rock P=Paper And S=Scisors ")
firstChoose = getpass('First player choose: ')
secondChoose = getpass('Second player choose: ')
def check(first,second):
 mode=""
 if first and second : 
  checkTheResults(dataBase()[0],dataBase()[1])
  print(mode,"moder")
 else: 
  mode=False
  if mode==False:
   print("\n")
   print("sorry but you must add a choice from the game") 
   print("\n")
   global firstChoose,secondChoose
   firstChoose = getpass('First player choose: ')
   secondChoose = getpass('Second player choose: ')
   check(firstChoose,secondChoose)
  #  recursion function 
def dataBase():
 searchFirstInput=re.search("^r|s|p",firstChoose,re.I)
 searchSecondInput=re.search("^r|s|p",secondChoose,re.I)
 return searchFirstInput,searchSecondInput

def checkTheResults(first,second):
 firstResult=first.group().lower()
 secondResult=second.group().lower()
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
check(dataBase()[0],dataBase()[1])
