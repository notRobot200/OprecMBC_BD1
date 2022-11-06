# membuat program pola n*n 
# bintang dan tanda pagar dengan jumlah n (integer)

n = int(input("masukkan nilai n : "))

# cara 1
for x in range(n):
    for y in range(n):
        # jika pada baris pertama dan terakhir (x*y print "*")
        # jika pada kolom pertama dan terakhir print *
        # jika tidak print #
        if x == 0 or x == n-1 or y == 0 or y == n-1:
            print("*", end = '')
        else:
            print("#", end = '')
    print("")

# cara 2
# for i in range(n):
#     for j in range(n):
#         if (j == 0 or j == n-1):
#             print("*", end = '') 
#         else:
#             if (i == 0 or i== n-1):
#                 print("*", end = '')
#             else:
#                 print("#", end = '')
#     print("")