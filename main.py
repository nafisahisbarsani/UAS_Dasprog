import json
# Function to load data from a JSON file
def loadData(namaFile):
    with open(namaFile, 'r') as f:
        return json.load(f)

def simpanData(namaFile, data):
    with open(namaFile, 'w') as f:
        json.dump(data, f, indent=2)

def tampilkanMaskapai(daftar):
    print('DAFTAR MASKAPAI')
    for i in range(len(daftar)):
        print(i + 1, daftar[i]['nama'], formatRupiah(daftar[i]['harga']))

def sortMaskapai(daftar, kunci):
    hasil = daftar.copy()
    for i in range(len(hasil) - 1):
        for j in range(len(hasil) - 1 - i):
            if hasil[j][kunci] > hasil[j + 1][kunci]:
                hasil[j], hasil[j + 1] = hasil[j + 1], hasil[j]
    return hasil

def tampilkanKodeMaskapai(daftar):
    print('DAFTAR KODE MASKAPAI')
    for m in daftar:
        print(m['kode'], '-', m['nama'])

def searchMaskapai(daftar, kata):
    hasil = []
    for m in daftar:
        if kata.lower() in m['nama'].lower():
            hasil.append(m)
    return hasil
# Function to sort the list of airlines using quicksort algorithm
def quickSort(daftar, kunci):
    if len(daftar) <= 1:
        return daftar
    pivot = daftar[0]
    kiri = []
    kanan = []
    for m in daftar[1:]:
        if m[kunci] < pivot[kunci]:
            kiri.append(m)
        else:
            kanan.append(m)
    return quickSort(kiri, kunci) + [pivot] + quickSort(kanan, kunci)

def binarySearchKode(daftar_terurut, kode):
    kiri = 0
    kanan = len(daftar_terurut) - 1
    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        if daftar_terurut[tengah]['kode'] == kode:
            return daftar_terurut[tengah]
        elif daftar_terurut[tengah]['kode'] < kode:
            kiri = tengah + 1
        else:
            kanan = tengah - 1
    return None
# Function to format the price in Indonesian Rupiah format
def formatRupiah(angka):
    return f'Rp {angka:,}'.replace(',', '.')

daftarMaskapai = loadData('data/maskapai.json')
daftarPesanan = loadData('data/pesanan.json')

# Menus
while True:
    print('================================')
    print('Selamat Datang di Bookplane, Aplikasi Pemesanan Tiket Pesawat!')
    print('================================')
    print('Silakan pilih menu yang tersedia:') 
    print('1. Lihat Daftar Maskapai')
    print('2. Cari Maskapai')
    print('3. Pesan Tiket')
    print('4. Ubah Pesanan')
    print('5. Batalkan Pesanan')
    print('6. Keluar')
    print('===============================')
    inputMenu = input('Masukkan pilihan menu (1-6): ')
    if inputMenu == '1': # Show list of airlines
        print('Urutkan berdasarkan: ')
        print('1. Nama')
        print('2. Harga')
        print('3. Tanpa Urutan')
        inputUrut = input('Masukkan pilihan (1-3): ')
        if inputUrut == '1':
            tampilkanMaskapai(sortMaskapai(daftarMaskapai, 'nama'))
        elif inputUrut == '2':
            tampilkanMaskapai(sortMaskapai(daftarMaskapai, 'harga'))
        elif inputUrut == '3':
            tampilkanMaskapai(daftarMaskapai)
        else:
            print('Pilihan tidak valid.')
    elif inputMenu == '2': # Search for airlines
        print('Cari berdasarkan:')
        print('1. Nama')
        print('2. Kode maskapai')
        inputCari = input('Masukkan pilihan (1-2): ')

        if inputCari == '1':
            kata = input('Masukkan nama: ').strip()
            hasil = searchMaskapai(daftarMaskapai, kata)
            if len(hasil) == 0:
                print('Maskapai tidak ditemukan.')
            else:
                tampilkanMaskapai(hasil)

        elif inputCari == '2':
            terurut = quickSort(daftarMaskapai, 'kode')
            tampilkanKodeMaskapai(terurut)
            kode = input('Masukkan kode: ').strip().upper()
            hasil = binarySearchKode(terurut, kode)
            if hasil == None:
                print('Maskapai tidak ditemukan.')
            else:
                tampilkanMaskapai([hasil])
    elif inputMenu == '6': # Exit the program
        print('Terima kasih telah menggunakan Bookplane!')
        break
    else:
        print('Pilihan tidak valid, coba lagi.')