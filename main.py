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

def tampilkanKodeMaskapai(daftar):
    print('DAFTAR KODE MASKAPAI')
    for m in daftar:
        print(m['kode'], '-', m['nama'])

def cariMaskapai(daftar, kata):
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
    return f'Rp{angka:,}'.replace(',', '.')

def kembaliKeMenu():
    input('\nTekan Enter untuk kembali ke menu utama...')

def buatDaftarKursi():
    daftar = []
    for i in range(1, 4):
        for huruf in ['A', 'B', 'C', 'D']:
            daftar.append(f'{huruf}{i}')
    return daftar

def tampilkanDenahKursi(jadwal):
    print('DENAH KURSI ( X = Terisi')
    for kursi in buatDaftarKursi():
        if kursi in jadwal['kursi_terisi']:
            print('[X]', end=' ')
        else:
            print('[' + kursi + ']', end=' ')
        if kursi.startswith('D'):
            print()

def pilihKursi(jadwal):
    semuaKursi = buatDaftarKursi()
    while True:
        kursi = input('Pilih kursi: ').strip().upper()
        if kursi not in semuaKursi:
            print('Kursi tidak ada')
        elif kursi in jadwal['kursi_terisi']:
            print('Kursi sudah terisi')
        else:
            return kursi

def pilihMaskapai(daftar):
    tampilkanMaskapai(daftar)
    while True:
        try:
            pilihan = int(input('Masukkan nomor maskapai yang ingin dipilih: '))
            if 1 <= pilihan <= len(daftar):
                return daftar[pilihan - 1]
            else:
                print('Pilihan tidak valid.')
        except ValueError:
            print('Input harus berupa angka, coba lagi')
            
def pilihJadwal(maskapai):
    print('Jadwal', maskapai['nama'])
    for i in range(len(maskapai['jadwal'])):
        print(i + 1, maskapai['jadwal'][i]['waktu'])
    while True:
        try:
            pilihan = int(input('Masukan nomor jadwal yang ingin dipilih: '))
            if 1 <= pilihan <= len(maskapai['jadwal']):
                return maskapai['jadwal'][pilihan - 1]
            else:
                print('Pilihan tidak valid.')
        except ValueError:
            print('Input harus berupa angka, coba lagi')

def konfirmasi(pertanyaan):
    while True:
        jawab = input(pertanyaan + ' (y/n): ').strip().lower()
        if jawab == 'y':
            return True
        elif jawab == 'n':
            return False
        else:
            print('Masukan y untuk ya atau n untuk tidak.')

def inputNama():
    while True:
        nama = input('Masukan nama: ').strip()
        if nama.replace(' ', '').isalpha():
            return nama.title()
        else:
            print('Nama hanya boleh berisi huruf')

def buatKodeTiket(kodeMaskapai, daftarPesanan):
    terbesar = 0
    for p in daftarPesanan:
        nomor = int(p['kode_tiket'].split('-')[1])
        if nomor > terbesar:
            terbesar = nomor
    return kodeMaskapai + '-' + str(terbesar + 1).zfill(4)

def tampilkanTiket(pesanan):
    print('================================')
    print('TIKET PESAWAT'.center(40))
    print('================================')
    print('Kode Tiket:', pesanan['kode_tiket'])
    print('Nama Penumpang:', pesanan['nama_penumpang'])
    print('Maskapai:', pesanan['maskapai'])
    print('Jadwal:', pesanan['jadwal'])
    print('Kursi:', pesanan['kursi'])
    print('Harga:', formatRupiah(pesanan['harga']))

def cariPesanan(daftar, kode):
    for p in daftar:
        if p['kode_tiket'] == kode:
            return p
    return None

def cariMaskapaiByNama(daftar, nama):
    for m in daftar:
        if m['nama'] == nama:
            return m
    return None

def cariJadwalByWaktu(maskapai, waktu):
    for j in maskapai['jadwal']:
        if j['waktu'] == waktu:
            return j
    return None

def konfirmasiPerubahan(pesanan, jadwal, kursi):
    print('===============================')
    print('Konfirmasi Perubahan'.center(40))
    print('Maskapai:', pesanan['maskapai'])
    print('Jadwal:', pesanan['jadwal'], '->', jadwal['waktu'])
    print('Kursi:', pesanan['kursi'], '->', kursi)
    print('===============================')
    return konfirmasi('Apakah Anda ingin menyimpan perubahan?')

def pindahkanJadwal(maskapai, pesanan, jadwalBaru, kursiBaru):
    # Kosongkan kursi di jadwal lama
    jadwalLama = cariJadwalByWaktu(maskapai, pesanan['jadwal'])
    if pesanan['kursi'] in jadwalLama['kursi_terisi']:
        jadwalLama['kursi_terisi'].remove(pesanan['kursi'])

    # Isi kursi di jadwal baru, lalu perbarui pesanan
    jadwalBaru['kursi_terisi'].append(kursiBaru)
    pesanan['jadwal'] = jadwalBaru['waktu']
    pesanan['kursi'] = kursiBaru

def ubahPesanan(daftarMaskapai, pesanan):
    maskapai = cariMaskapaiByNama(daftarMaskapai, pesanan['maskapai'])
    jadwal = pilihJadwal(maskapai)

    if jadwal['waktu'] == pesanan['jadwal']:
        print('Jadwal sama dengan jadwal saat ini.')
        return False
    if len(jadwal['kursi_terisi']) == len(buatDaftarKursi()):
        print('Maaf, penerbangan ini sudah penuh. Silakan pilih jadwal lain.')
        return False

    tampilkanDenahKursi(jadwal)
    kursi = pilihKursi(jadwal)
    if konfirmasiPerubahan(pesanan, jadwal, kursi):
        pindahkanJadwal(maskapai, pesanan, jadwal, kursi)
        return True
    print('Perubahan dibatalkan.')
    return False

def kosongkanKursi(daftarMaskapai, pesanan):
    for m in daftarMaskapai:
        if m['nama'] == pesanan['maskapai']:
            for j in m['jadwal']:
                if j['waktu'] == pesanan['jadwal']:
                    if pesanan['kursi'] in j['kursi_terisi']:
                        j['kursi_terisi'].remove(pesanan['kursi'])
                    return

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
    print('')
    inputMenu = input('Masukkan pilihan menu (1-6): ')
    if inputMenu == '1': # Show list of airlines
        print('Urutkan berdasarkan: ')
        print('1. Nama')
        print('2. Harga')
        print('3. Tanpa Urutan')
        inputUrut = input('Masukkan pilihan (1-3): ')
        if inputUrut == '1':
            tampilkanMaskapai(quickSort(daftarMaskapai, 'nama'))
        elif inputUrut == '2':
            tampilkanMaskapai(quickSort(daftarMaskapai, 'harga'))
        elif inputUrut == '3':
            tampilkanMaskapai(daftarMaskapai)
        else:
            print('Pilihan tidak valid.')
        kembaliKeMenu()

    elif inputMenu == '2': # Search for airlines
        print('Cari berdasarkan:')
        print('1. Nama')
        print('2. Kode maskapai')
        inputCari = input('Masukkan pilihan (1-2): ')

        if inputCari == '1':
            kata = input('Masukkan nama: ').strip()
            hasil = cariMaskapai(daftarMaskapai, kata)
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
        else:
            print('Pilihan tidak valid.')
        kembaliKeMenu()
    
    elif inputMenu == '3': # Book a ticket
        m = pilihMaskapai(daftarMaskapai)
        jadwal = pilihJadwal(m)
        if len(jadwal['kursi_terisi']) == len(buatDaftarKursi()):
            print('Maaf, penerbangan ini sudah penuh. Silakan pilih jadwal lain.')
        else:
            tampilkanDenahKursi(jadwal)
            kursi = pilihKursi(jadwal)

            print('===============================')
            print('Konfirmasi Pemesanan'.center(40))
            print('Maskapai:', m['nama'])
            print('Jadwal:', jadwal['waktu'])
            print('Kursi:', kursi)
            print('Harga:', formatRupiah(m['harga']))
            print('===============================')
            if konfirmasi('Apakah Anda ingin melanjutkan pemesanan?'):
                nama = inputNama()
                pesananBaru = {
                    'kode_tiket': buatKodeTiket(m['kode'], daftarPesanan),
                    'nama_penumpang': nama,
                    'maskapai': m['nama'],
                    'jadwal': jadwal['waktu'],
                    'kursi': kursi,
                    'harga': m['harga']
                }
                daftarPesanan.append(pesananBaru)
                jadwal['kursi_terisi'].append(kursi)
                simpanData('data/pesanan.json', daftarPesanan)
                simpanData('data/maskapai.json', daftarMaskapai)

                tampilkanTiket(pesananBaru)
            else:
                print('Pemesanan dibatalkan.')
            kembaliKeMenu()

    elif inputMenu == '4': # Edit an order
        if len(daftarPesanan) == 0:
            print('Belum ada pesanan.')
        else:
            kode = input('Masukkan kode pemesanan: ').strip().upper()
            pesanan = cariPesanan(daftarPesanan, kode)
            if pesanan == None:
                print('Pesanan tidak ditemukan.')
            else:
                tampilkanTiket(pesanan)
                if ubahPesanan(daftarMaskapai, pesanan):
                    simpanData('data/pesanan.json', daftarPesanan)
                    simpanData('data/maskapai.json', daftarMaskapai)
                    print('Pesanan berhasil diubah!')
                    tampilkanTiket(pesanan)
        kembaliKeMenu()
    elif inputMenu == '5': # Cancel an order
        kodeTiket = input('Masukkan kode tiket: ').strip().upper()
        pesanan = cariPesanan(daftarPesanan, kodeTiket)

        if pesanan is None:
            print('Pesanan tidak ditemukan.')
        else:
            tampilkanTiket(pesanan)
            if konfirmasi('Apakah Anda yakin ingin membatalkan pesanan ini?'):
                kosongkanKursi(daftarMaskapai, pesanan)
                daftarPesanan.remove(pesanan)
                simpanData('data/pesanan.json', daftarPesanan)
                simpanData('data/maskapai.json', daftarMaskapai)
                print('Pesanan berhasil dibatalkan.')
            else:
                print('Pembatalan dibatalkan.')
        kembaliKeMenu()

    elif inputMenu == '6': # Exit the program
        print('Terima kasih telah menggunakan Bookplane!')
        break
    
    else:
        print('Pilihan tidak valid, coba lagi.')