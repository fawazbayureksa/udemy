# x = input('Ketikkan Barang yang diinginkan: ')
# x = str(x)


# if x == "q":
#     print("daftar barang di keranjang")
#     print(f'- {x}')
# else:

# contoh_list = ['a', 'b', 'c', 'd']
# print(len(contoh_list))

# tasks = ["install python", "learn python", "take a break"]

# friends = ["ikki", "callu", "iqbal"]
# # print(friends[0])
# print("ikki" in friends) true/false
# print("callu" in friends) true/false


# friends = ["ikki", "callu", "iqbal"]

# for friend in friends:
#     print(friend)

# number = [2, 3, 4, 5, 6, 7, 8]

# x = 0
# for num in number:
#     print(num * num)

# while x < len(number):
#     print(number[x])
#     # print(f'{x} = {number[x]}')
#     x += 1


# ------------------------------------------------------------------------------------

num = [5,6,7,8,9,10]
# num.append(11) #untuk satu angka
# num.extend([11,12,13,14]) # untuk banyak angka
# num.insert(0, 4) #untuk memasukkan data tambahan , 0 adalah index dan 4 adalah angka yang ingin ditambahkan
# num.insert(len(num), "LAST") #untuk memasukkan data tambahan di akhir data
# num.clear() akan menghapus semua isi arraynya
# num.pop(1) akan menampilkan isi array sesuai angka index yang ada di kolom lalu menghapusnya , jika kolom kosong maka akan otomatis memilih data array yng terakhir
# num.remove(5) # akan menghapus data array sesuai isi yang ada di dalam kolom , contoh menghapus angka 5 dalam data 

# -------------------------
# x = int(input("Masukkan Angka selanjutanya: "))
# num.insert(len(num), x)
# print(len(num))
# -------------------------

# cart = []
# brg = input("Tuliskan barang yang ingin dibeli: ")
# cart.insert(len(cart), brg)

# while brg != "stop":
#     brg = input("Tuliskan stop jika sudah tidak ada: ")
#     cart.insert(len(cart), brg)

# print('Daftar barang Pesanan anda:')

# for brg in cart:
#     print(f'-{brg}')
