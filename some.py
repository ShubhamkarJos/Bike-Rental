def phone():
    while True:
        i = 0
        Mobile = int(input("Mobile : "))
        temp = Mobile
        p = Mobile
        p //= 1000000000
        while temp > 0:
            # print(Mobile)
            temp = temp // 10
            i = i + 1
        return Mobile
        if i == 10 and (p == 9 or p == 8 or p == 7):
            break
        print("Please Retry!")


def aadhaar_num():
    while True:
        i = 0
        Aadhaar = int(input("Aadhaar Number : "))
        temp = Aadhaar
        while temp > 0:
            temp = temp//10
            i += 1
            return Aadhaar
        if i == 12:
            break  
        print("Invalid Aadhaar Number!")


def age():
    while True:
        AGE = int(input("AGE : "))
        if AGE>=18:
          break
        else:
          print("Underage!")
          exit()
    return AGE
input(age())