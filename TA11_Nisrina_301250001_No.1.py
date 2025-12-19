# simpan_baca_biodata.py

def simpan_biodata(file_path="biodata.txt"):
    print("Masukkan biodata:")
    nama = input("Nama  : ").strip()
    nim  = input("NIM   : ").strip()
    prodi= input("Prodi : ").strip()

    # Simpan dalam format CSV sederhana: Nama,NIM,Prodi
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"{nama},{nim},{prodi}\n")

    print(f"\nBiodata disimpan ke '{file_path}'.")


def baca_dan_tampilkan(file_path="biodata.txt"):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            # Ambil baris pertama (asumsi hanya satu record)
            line = f.readline().strip()
            if not line:
                print("File kosong.")
                return

            parts = line.split(",")
            # Pastikan ada 3 bagian
            if len(parts) < 3:
                print("Format file tidak sesuai. Harus: Nama,NIM,Prodi")
                return

            nama, nim, prodi = parts[0], parts[1], parts[2]

            # Tampilkan sesuai format yang diminta
            print("\nHasil pembacaan file:")
            print(f"Nama : {nama}")
            print(f"NIM  : {nim}")
            print(f"Prodi: {prodi}")

    except FileNotFoundError:
        print(f"File '{file_path}' tidak ditemukan.")


if __name__ == "__main__":
    simpan_biodata()        # Meminta input & menyimpan
    baca_dan_tampilkan()    # Membaca kembali & menampilkan hasil