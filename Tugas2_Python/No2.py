# membuat program python untuk menghitung total belanja seorang pembeli
# output total diskon konsumen dalam bentuk persen

X = int(input("masukkan total belanja : ")) # minta input total belanja
y = input("apakah member (y/t): ") # apakah konsumen member/bukan?

if y == 'y': # jika member diskon 5%
    disc = 5/100
    tot = int(X - (X*disc))
    if 500000 <= X <= 1000000: # total belanja 500ribu-1jt diskon 2%
        disc = disc + 2/100
        tot = int(X - (X*disc))
        print("selamat anda mendapatkan diskon", "{:.0%}".format(disc))
        # print("Total belanja adalah", tot)
    elif X > 1000000: # total belanja > 1jt diskon 3%
        disc = disc + 3/100
        tot = int(X - (X*disc))
        print("Selamat anda mendapatkan diskon", "{:.0%}".format(disc))
    else: # total belanja < 500000 dan member
        print("selamat anda mendapatkan diskon", "{:.0%}".format(disc))