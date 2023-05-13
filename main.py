import sys

from datetime import date, timedelta

class Celengan:

    def __init__(self, target_harian):

        self.saldo = 0

        self.target_harian = target_harian

    def simpan(self, jumlah):

        self.saldo += jumlah

        print("Berhasil menyimpan uang sebesar Rp.{}".format(jumlah))

    def ambil(self, jumlah):

        if jumlah > self.saldo:

            print("Maaf, saldo tidak mencukupi")

        else:

            self.saldo -= jumlah

            print("Berhasil mengambil uang sebesar Rp.{}".format(jumlah))

    def cek_saldo(self):

        print("Saldo Anda saat ini adalah Rp.{}".format(self.saldo))

    def cek_target_harian(self):

        print("Target harian Anda adalah Rp.{}".format(self.target_harian))

    def ingin_menabung(self):

        print("Anda ingin menabung sebesar Rp.{} lagi untuk mencapai target harian.".format(self.target_harian - self.saldo))

    def perkirakan_hari(self):

        hari_ini = date.today()

        hari_tujuan = hari_ini + timedelta(days=round((self.target_harian - self.saldo) / self.target_harian * 30))

        print("Anda memerlukan waktu sekitar {} hari lagi untuk mencapai target harian".format((hari_tujuan - hari_ini).days))

def main():

    target_harian = int(input("Masukkan target harian Anda: "))

    celengan = Celengan(target_harian)

    while True:

        print("Selamat datang di Celengan Dhika")

        print("Silakan pilih menu :")

        print("1. Simpan uang")

        print("2. Ambil uang")

        print("3. Cek saldo")

        print("4. Cek target harian")

        print("5. Ingin menabung berapa lagi untuk mencapai target harian")

        print("6. Perkirakan hari mencapai target harian")

        print("7. Keluar")

        try:

            menu = int(input("Masukkan pilihan Anda: "))

        except ValueError:

            print("Masukkan pilihan yang valid")

            continue

        if menu == 1:

            try:

                jumlah = int(input("Masukkan jumlah uang yang ingin disimpan: "))

            except ValueError:

                print("Masukkan jumlah uang yang valid")

                continue

            celengan.simpan(jumlah)

        elif menu == 2:

            try:

                jumlah = int(input("Masukkan jumlah uang yang ingin diambil: "))

            except ValueError:

                print("Masukkan jumlah uang yang valid")

                continue

            celengan.ambil(jumlah)

        elif menu == 3:

            celengan.cek_saldo()

        elif menu == 4:

            celengan.cek_target_harian()

        elif menu == 5:

            celengan.ingin_menabung()

        elif menu == 6:

            celengan.perkirakan_hari()

        elif menu == 7:

            print("Terima kasih telah menggunakan Celengan Saya")

            sys.exit()

        else:

            print("Masukkan pilihan yang valid")

if __name__ == '__main__':

    main()
