#The program determines the award a person competing in atriathlon will receive
s = int(input("Please enter in minutes the result of swimming :"))
c = int(input("Please enter in minutes the result of cycling :"))
r = int(input("Please enter in minutes the result of running :"))
total = s + c + r

if total <=100:
    print("Your award is Provincial Colours")
elif total >=101 and total <=105:
    print("Your award is Provincial Half Colours")
elif total >=106 and total <=110:
    print("Your award is Provincial Scroll")
else:
    print("Sorry. You have no award today.")