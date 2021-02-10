# input and loop
# print('How many times do i have to tell you? ')
# x = int(input())

# for y in range(x) :
#    print(f'Time {y}: CLEAN UP YOUR ROOM!!')
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Unlucky Numbers , Ganjil Genap
# or y in range(1, 21):

# if y == 13 or  y == 4:
#     print(f'{y} is UNLUCKY!')
# elif y%2 == 0:
#     print(f'{y} Is Even')
# else:
#     print(f'{y} Is Odd')
# OR
# if y == 13 or  y == 4:
#     state= "UNLUCKY!"
# elif y%2 == 0:
#     state='Even'
# else:
#     state='odd'

# print(f'{y} Is {state}')

# --------------------------------------------------------------------------------------------------

# WHILE

# user_res= "please"
# while user_res != "please":
#     user_res = input("You didn't say the magic word")
#     break
# -------------------------------------------------------

# msg = input("whats the secret password ")
# while msg != "bananas":
#     print("WRONG!")
#     msg = input("Whats The seccret password? ")
#     print("CORRECT!")

# Menampilkan angka 1-10

# for num in range(1, 11):
#     print(num)

# num = 1
# while num < 11:
#     print(num)
#     num = num + 1

# ket num+=1 sama dengan num = num+1

# menampilkan angka ganjil

# num = 1
# while  num < 11:
#     print(num)
#     num+=2
# --------------------------------------------------------------------------------------------
# Excercise Emoji Loop

emot = str('\U0001F600')
x = 1
for x in range(1, 11):
    print(emot)
    emot += str("\U0001F600")

while x < 11:
    x += 1
    print(emot)
    emot += str('\U0001F600')

# Loop berkali-kali sesuai range
# for y in range(3):
#     for num in range(1, 11):
#         print("\U0001F600" * num)
# -------------------------------------

# for num in range(1, 11):
#     print("\U0001F600" * num)

# x = 1
# while x <= 11:
#     print("\U0001F600" * x)
#     x += 2

# Colt Talking To His SOster Exercise

# msg = input("Hey How's going ? ")
# while  msg != "stop" :
#     print(msg)
#     msg = input(msg)
# else:
#     print("UGH FINE YOU WIN")

#Or / atau

# msg = input("Hey How's going ? ")
# while  msg != "stop" :
#     msg = input(f'{msg}\n')
# else:
#     print("UGH FINE YOU WIN")

# ---------------------------------------------------------------------------------------------------

# WHILE BREAK

# while True:
#     command = input("Type 'Exit' to exit: ")
#     if (command == "exit"):
#         # print("Keluar")
#         break

# for x in range(1, 100):
#     print(x)
#     if x == 30:
#         break

# x = input("How many times do i have tell you? ")
# x = int(x)

# for y in range(1, x):
#     print("CLEAN UP YOUR ROOM")
#     if y >= 4:
#         print('Do you even listen anymore? ')
#         break

# 05 Januari 2021
