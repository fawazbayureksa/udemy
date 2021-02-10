# Guessing Game
# import random
from random import randint

# random_number = random.randint(1, 10)
# print(random_number)

# Made by me --------------------------------------------------
# teks = input('Guess a number between 1 and 10: ')
# teks = int(teks)

# while teks != random_number and teks < random_number:
#     print('Too Low ,Try again')
#     teksn = str(input('Do You Want To Keep Playing ? (y/n) '))
#     if teksn == str('y'):
#         teks = input('Guess a number between 1 and 10: ')
#         teks = int(teks)
#     else:
#         print("You Lose,Bye")
# else:
#     print('You Guessed it, You won!')
# ----------------------------------------------------------------

# Setengah jadi -------------------------------------------
# teks = input('Pick a number from 1 - 10: ')
# teks = int(teks)

# if teks == random_number:
#     print('You Got it')
# elif teks < random_number:
#     print('Too Low')
# else:
#     print('Too High')
# ----------------------------------------------------------

# versi 1
# teks = None

# while teks != random_number:
#     teks = input('Pick a number from 1 - 10: ')
#     teks = int(teks)
#     if teks > random_number:
#         print('Too High')
#     elif teks < random_number:
#         print('Too Low')
#     else:
#         print('You Got it')
# versi 2


# teks = None
# while True:
#     teks = input('Pick a number from 1 - 10: ')
#     teks = int(teks)
#     if teks > random_number:
#         print('Too High')
#     elif teks < random_number:
#         print('Too Low')
#     else:
#         print('You Got it')
#         play_again = input('Do you want to play again ? (y/n)')
#         if play_again == "y":
#             random_number = random.randint(1, 10)
#             teks = None
#         else:
#             print("Thank You for playing")
#             break

# --------------------------------------------------------------------------------------------------------------------------


pemain = 0
komputer = 0
skor_menang = 0

skor_menang = int(input('Masukkan Jumlah Permainan (2/4/6) : '))

while pemain < skor_menang and komputer < skor_menang:
    print(f'Skor pemain : {pemain} Skor Komputer : {komputer}')
    print("...batu...")
    print("...kertas...")
    print("...gunting...")


    x = input("(masukkan pilihanmu) : ").lower()
    random_num = randint(0, 2)
    if x == "stop" or pemain == "berhenti":
        break
    if (random_num == 0):
        computer = "batu"
    elif (random_num == 1):
        computer = "kertas"
    else:
        computer = "gunting"

    print(f'pilihan komputer adalah: {computer}')

    if x == computer:
        print('Hasilnya sama')
    elif x == "batu":
        if computer == "kertas":
            print("komputer menang")
            komputer +=1
        else:
            print('Selamat anda menang')
            pemain +=1
    elif x == "gunting":
        if computer == "kertas":
            print('Selamat anda menang')
            pemain +=1
        else:
            print('komputer memang')
            komputer += 1
    elif x == "kertas":
        if computer == "batu":
            print('Selamat anda menang')
            pemain += 1
        else:
            print('komputer memang')
            komputer += 1
    else:
        print('masukkan pilhan yang benar')

if komputer > pemain:
    print('---Komputer Menang---')
elif pemain == komputer:
    print('---Hasilnya Imbang---')
else:
    print('---Selamat anda menang dalam permainan ini---')

print(f"Hasil Permainan Komputer : {komputer} Pemain : {pemain}")