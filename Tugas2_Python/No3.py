nama_hari = ["Senin", "Selasa", "Rabu", "kamis", "Jumat", "Sabtu"]
print("=======================================================")
print("==Selamat datang di Program pencarian jadwal seragam==")
print("=======================================================")
hari = input('Masukan nama hari dengan huruf kapital sebagai awalan :')
if hari == "Senin":
  print('Seragam anda hari ini Kemeja Teknik Merah')
if hari == "Selasa" :
  print('Seragam anda hari ini Kemeja Teknik Merah')
if hari == "Rabu":
  print('Seragam anda hari ini Kemeja Teknik Merah')
if hari == "Kamis":
  print('Seragam anda hari ini Baju Bebas Sopan Yaa')
if hari == "Jumat":
  print('Seragam anda hari ini Batik yaa')
if hari == "Sabtu":
  print('Seragam anda hari ini Baju Bebas Sopan Yaa')
if not hari in nama_hari :
    print ('Hari ini hari Minggu, kamu Libur lohh jadi gausa pake seragam')