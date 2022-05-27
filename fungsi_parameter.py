def selamat_datang(nama):

    print('halo',nama,'apa kabar?')

selamat_datang('Bubu')

def greetings(nama, waktu):
    print('Hello',nama,'selamat',waktu)
    print('Apakah ', nama,'sudah datang', waktu, 'ini?')

greetings('Adin','Pagi')
greetings('Rico','Siang')
greetings('Nadir','Malam')

def greetings(nama, waktu):
    print('hello',nama, 'selamat',waktu)

greetings ('malam', 'wahyu')

greetings (waktu='malam', nama='wahyu')

def penjumlahan(a,b):
    hasil = a+b
    return hasil

data_greeting = greetings('wahyu','pagi')
hasil_jumlah = penjumlahan(2,5)

print (data_greeting)
print (hasil_jumlah)