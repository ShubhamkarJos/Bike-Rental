import math
import time
import winsound
from random import randint
#import os
from openpyxl import Workbook, load_workbook

workbook = load_workbook(filename="user.xlsx")
sheet = workbook.active
import sys



class customer:


    def name(self):
        Name = input("Enter your name : ")
        return Name



    def email(self):
        Email = input("Enter your email id : ")
        return Email



    def mobile(self):
        while True:
            i = 0
            Mobile = int(input("Mobile No. : "))
            temp = Mobile
            p = Mobile
            p //= 1000000000
            while temp > 0:
                # print(Mobile)
                temp = temp // 10
                i = i + 1

            if i == 10 and (p == 9 or p == 8 or p == 7 or p == 6):
                return Mobile
            print("Invalid Mobile No.! \nPlease try again")



    def countdown(n):
        while n > 0:
            print(n)
            time.sleep(1)
            n = n - 1
            if (n == 0):
                print("Timer has Stopped\n")



    def aadhaar(self):
        while True:
            i = 0

            Aadhaar = int(input("Aadhaar Number : "))
            temp = Aadhaar
            while temp > 0:
                temp = temp // 10
                i += 1

            if i == 12:
                return Aadhaar

            print("Invalid Aadhaar Number! \nPlease try Again.")


    def age(self):
        while True:
            AGE = int(input("Age : "))
            if AGE >= 18:
                break
            else:
                print("The customer is Underage!")
                exit()
        return AGE


nestedlist = [["1.Hero Pleasure", "Scooty", 100, 1500, 8000, 2],
             ["2.Honda Dio", "Scooty", 105, 1600, 8300, 2],
             ["3.Honda Activa", "Scooty", 115, 1680, 8500, 2],
             ["4.Suzuki Access", "Scooty", 120, 1750, 8700, 0],
             ["5.Hero Honda", "Bike", 140, 1900, 9600, 2],
             ["6.Avenger Cruise", "Bike", 150, 2200, 10500, 2],
             ["7.Avenger Street", "Bike", 150, 2200, 10500, 2],
             ["8.CBR FireBlade", "Bike", 180, 2600, 12000, 2],
             ["9.Benelli 600i", "Bike", 200, 2800, 13000, 2],
             ["10.Ducati Monster", "Bike", 210, 3000, 13600, 2]
             ]


ans = 'y'

#Customer Information

while(ans == 'Y' or ans == 'y'):

    sheet.insert_rows(idx=2)
    c = customer
    Name = c.name(customer)
    Email = c.email(customer)
    Age = c.age(customer)
    Aadhaar = c.aadhaar(customer)
    Mobile = c.mobile(customer)


    #os.system('cls')
   # print("Please enter your Information Again\n\n")
    #Name = input("Enter your name : ")
    #Age = Excelsome.age()
    #Mobile = Excelsome.phone()
    #Aadhaar = Excelsome.aadhaar_num()
    #Email = input("Enter your email id : ")


    print('-'*120)
    print(" "*40 + 'Bike Rental System')
    print('-'*120)


    def instock(a,nestedlist):
        if(nestedlist[int(a)-1][5]>0):
            return 1
        else:
            print("Vehicle is out of stock!")


    def decrement(a, nestedlist):
        nestedlist[int(a)-1][5] = nestedlist[int(a)-1][5]-1
        return nestedlist
        #return [(item[5] - 1) for item in nestedlist[(int(a) - 1):(int(a))]]




    print(" " * 40, "Bikes Catalogue ")
    #while True:
    print("|        Name        |     Type    | Hourly |  Daily |   Weekly  |  Stock  |")

    for item in nestedlist:
            print("|", item[0], " " * (17 - len(item[0])), "|  ",
                  item[1], " " * (8 - len(item[1])), "| ",
                  item[2], " " * (4 - len(str(item[2]))), "| ",
                  item[3], " " * (4 - len(str(item[3]))), "|  ",
                  item[4], " " * (6 - len(str(item[4]))), "|  ",
                  item[5], " " * (3 - len(str(item[5]))), " |")


    a = input("Enter the choice of bike you want :")


    if(instock(a,nestedlist)):
        nestedlist = decrement(a,nestedlist)

        print(" " * 40, "Update Catelogue")
        print("|        Name        |     Type    | Hourly |  Daily |   Weekly  |  Stock  |")

        for item in nestedlist:
            print("|", item[0], " " * (17 - len(item[0])), "|  ",
                  item[1], " " * (8 - len(item[1])), "| ",
                  item[2], " " * (4 - len(str(item[2]))), "| ",
                  item[3], " " * (4 - len(str(item[3]))), "|  ",
                  item[4], " " * (6 - len(str(item[4]))), "|  ",
                  item[5], " " * (3 - len(str(item[5]))), " |")


        b = input("1.Hourly Basis\n2.Daily Basis\n3.Weekly Basis\n")

        if(int(b) == 1 or int(b) == 2 or int(b) == 3):
            print("\nDisplaying Data! \n")
        else:
            print("Invalid Response! ")



        print(f'\nVehicle = {nestedlist[int(a) - 1][0]}')

        if(int(b)==1):
            print(f'Rent = {nestedlist[int(a) - 1][int(b) + 1]}/hour')
        elif(int(b)==2):
            print(f'Rent = {nestedlist[int(a) - 1][int(b) + 1]}/day')
        elif(int(b)==3):
            print(f'Rent = {nestedlist[int(a) - 1][int(b) + 1]}/week')


        c = input("\nPress any keep to generate OTP ")
        #os.system('cls')
        flag = 0

        i = randint(100000, 999999)
        print(i)

        print("\nYour timer will be started after entering the OTP")

        while True:
            otp = int(input("Enter OTP : "))
     #   for i in lol:
            if otp == int(i):
                start = time.perf_counter()
                flag = 1
                break
            if flag == 0:
                print("Incorrect OTP! Please try again.")
            elif flag == 1:
                break


        while (True):
            stop = int(input("\nPress 1 to stop the timer : "))
            if stop == 1:
                end = time.perf_counter()
                break

        winsound.PlaySound('when.mp3', winsound.SND_FILENAME)

        total = end - start


        if(int(b) == 1):
            total = total/3600
        elif(int(b) == 2):
            total = total/86400
        elif(int(b) == 3):
            total = total/604800

        print(f'Total time : {total}')



        total = math.ceil(total)
        rent = total*int(nestedlist[int(a)-1][int(b) + 1])
        roundoff = math.ceil(rent)

        print(f'Round off time : {total}')


        rows = [Name, Age, Mobile, Aadhaar, Email]

        sheet['A1'] = "Name"
        sheet['B1'] = "Age"
        sheet['C1'] = "Mobile No."
        sheet['D1'] = "Aadhaar No."
        sheet['E1'] = "Email Id"
        sheet['F1'] = "Bike"
        sheet['G1'] = "Rent"



        sheet["A2"] = Name
        sheet["B2"] = Age
        sheet['C2'] = Mobile
        sheet["D2"] = Aadhaar
        sheet["E2"] = Email
        sheet["F2"] = nestedlist[int(a)-1][0]
        sheet["G2"] = rent

        workbook.save(filename="user.xlsx")

        print("************************************************************************"*10)
        print(f'\t\t\t\t\t\t\tReceipt                                                 \n'
              f'                                                                      \n'
              f'NAME  : {Name}                                                         \n'                                                                    
              f'BIKE  : {nestedlist[int(a)-1][0]}                                      \n'
              f'USAGE : {total} units                                                 \n'
              f'RENT  : {rent} Rs.                                                     \n'
              f'ROUND OFF : {roundoff}                                                \n'
              f'\t\t\t\t THANK YOU FOR CHOOSING US!                                   ')
        print("************************************************************************"*10)

    ans = input("\nWould you like to continue? Y/N ")

f = customer
f.countdown(30)


winsound.PlaySound('when.mp3', winsound.SND_FILENAME)




nestedlist[int(a) - 1][5] = nestedlist[int(a) - 1][5] + 1



print(" " * 40, "Bikes Catalogue ")
# while True:
print("|        Name        |     Type    | Hourly |  Daily |   Weekly  |  Stock  |")

for item in nestedlist:
    print("|", item[0], " " * (17 - len(item[0])), "|  ",
          item[1], " " * (8 - len(item[1])), "| ",
          item[2], " " * (4 - len(str(item[2]))), "| ",
          item[3], " " * (4 - len(str(item[3]))), "|  ",
          item[4], " " * (6 - len(str(item[4]))), "|  ",
          item[5], " " * (3 - len(str(item[5]))), " |")



print("The vehicle is now available to use again!\n")
print("\nProgram has been Terminated!")
#print("\nSelf Destruct in 10,9,8,...:)))")



#print(nestedlist[int(a)-1][0])
#print(" "*31 + " Bikes Catelogue ")
#for item in nestedlist:
#    print("|", item[0], " " * (17 - len(item[0])), "|  ",
#          item[1], " " * (8 - len(item[1])), "| ",
#          item[2], " " * (4 - len(str(item[2]))), "| ",
#          item[3], " " * (4 - len(str(item[3]))), "|  ",
#          item[4], " " * (6 - len(str(item[4]))), "|  ",
#          item[5], " " * (3 - len(str(item[5]))), " |")

