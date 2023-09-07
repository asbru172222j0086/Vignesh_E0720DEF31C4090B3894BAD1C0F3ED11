def checkleapyear (year):
  if (year%400==0)and(year%100==0):
      return True
  elif (year % 4 == 0 and 
year % 100 !=0) : 
      return True
  else:
      return False

year=int(input("Enter the year :")) 

if checkleapyear(year):
     print("{} is a leap year. ".format(year))
elif checkleapyear(year):
     print("{} is a leap year. ".format(year))
else:
    print("{} is not a leap year.".format(year))