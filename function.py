from menu_item import MenuItem
import hashlib, os, getpass, csv


# Inisiasi
file_saldo = '.bukukas/saldo.csv'
file_passwd = '.bukukas/passwd.csv'
isFile = os.path.isfile(file_saldo)

# Enkripsi dan hide inputan password dari user
def encript_str(string):
    sha_signature = \
        hashlib.sha256(string.encode()).hexdigest()
    return sha_signature

# Buat file jika belum ada
def jalankan():
    isFile = os.path.isfile(file_saldo)
    if isFile:
        show_menu()
    else:
        with open('saldo.csv', mode='w') as file:
            # Menentukan label
            fieldnames = ['Nominal']
            # Membuat objek writer
            writer = csv.DictWriter(file, delimiter=',', fieldnames=fieldnames)
            # Meminta saldo pertama pada user
            try:
                nominal = int(input('Masukkan saldo pertama Anda dalam angka: '))
            except ValueError:
                print('Masukkan angka yang benar!')
            else:
                # Menulis baris ke file csv
                writer.writerow({'Nominal': nominal})
                os.system('mkdir .bukukas && mv saldo.csv .bukukas')

def login():
    if os.name == 'nt':
        print('Maaf, Aplikasi ini hanya mendukung sistem operasi linux')
        exit()
    # Jika Password user benar, cetak output sesuai kenyataan
    user_password_input = getpass.getpass('Ketikan password Anda: ')
    encripted_password = encript_str(user_password_input)
    password_default = ['8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92']

    if encripted_password == password_default[0]:
        print('Password Anda benar')
        clear_screen()
        jalankan()
        show_menu()
    else:
        print('Password Anda salah!')
        exit()

# Bersihkan Layar
def clear_screen():
    os.system('clear')

def menu():
    print('\n')
    input('Tekan Enter untuk kembali...')
    show_menu()

def show_menu():
    clear_screen()
    # Instansiasi
    menu1 = MenuItem('Lihat saldo')
    menu2 = MenuItem('Tambah Saldo')
    menu3 = MenuItem('Ganti password')
    menu4 = MenuItem('Keluar')
    menu_items = [menu1, menu2, menu3, menu4]
    print('--------------------')
    # definisikan index dari 1
    index = 1
    for menu_item in menu_items:
        print(str(index) + '. ' + menu_item.info())
        index += 1
    print('--------------------')
    selected_menu = input('Masukkan pilihan Anda: ')
    # Jalankan menu sesuai inputan user
    if selected_menu == '1':
        cek_saldo()
    elif selected_menu == '2':
        tambah_saldo()
    elif selected_menu == '3':
        ganti_password()
    elif selected_menu == '4':
        exit()
    else:
        print('Masukkan angka yang benar!')
        os.system('sleep 0.5')
        show_menu()

def cek_saldo():
    clear_screen()
    csv_saldo = file_saldo
    with open(csv_saldo, mode='r') as csv_saldo:
        print_text = csv_saldo.readlines()
        try:
            print('Saldo Anda saat ini Rp. ' + print_text[-1])
        except IndexError:
            print('Saldo Anda saat ini Rp. 0')
    menu()

def tambah_saldo():
    clear_screen()
    csv_saldo = file_saldo
    with open(csv_saldo, mode='r+') as csv_saldo:
        for saldo_old in csv_saldo:
                pass
        fieldnames = ['Nominal']
        writer = csv.DictWriter(csv_saldo, delimiter=',', fieldnames=fieldnames)
        # jika user tidak memasukkan angka/kosong
        try:
            nominal = int(input('Masukkan nominal: '))
        except ValueError:
            print('Masukkan angka dengan benar!')
        else:
            try:
                nominal += int(saldo_old)
                writer.writerow({'Nominal': nominal})
                print('Saldo berhasil dicatat kedalam buku')
            except UnboundLocalError:
                saldo_old = 0
                nominal += int(saldo_old)
                writer.writerow({'Nominal': nominal})
                print('Saldo berhasil dicatat kedalam buku')
    menu()

def ganti_password():
    clear_screen()
    print('Tunggu update-an berikutnya yaa :D')
    menu()

# Looping
if __name__ == "__main__":
    while True:
        show_menu()
