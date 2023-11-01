import time

# #Iterable
# d=[]

# for i in range (1,20):
#     if i%2 ==0:
#        d.append(i)
# print(d)
# print(len(d))

# while True:
#     time.sleep(3)




good_guess=10
number_of_try=0

while number_of_try <=2 :
    number_of_try=+1
    try:
        choice = int(input("Please enter a number between 1 and 20:"))
        if choice not in range(1,21):
            print("Invalid entry")
        elif choice not in range == good_guess:
             print("Good job you won!!")
             break
        elif choice < good_guess:
             print("Sorry your number is lower")
        elif choice > good_guess:
            print("Sorry your number is bigger")
    except  :
        print("something went wrong please try again")


            
