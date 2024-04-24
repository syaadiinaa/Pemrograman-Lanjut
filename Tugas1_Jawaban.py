def hitung_nilai_akhir(tugas, uts, uas):
    """Menghitung nilai akhir dari nilai tugas, UTS, dan UAS"""
    nilai_akhir = (tugas * 0.25) + (uts * 0.35) + (uas * 0.4)
    return nilai_akhir

def main():
    tugas = float(input("Masukkan nilai tugas: "))
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))

    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)

    if nilai_akhir > 85:
        print("Nilai akhir: A")
    elif nilai_akhir > 80:
        print("Nilai akhir: A-")
    elif nilai_akhir > 75:
        print("Nilai akhir: B+")
    elif nilai_akhir > 70:
        print("Nilai akhir: B")
    elif nilai_akhir > 65:
        print("Nilai akhir: B-")
    elif nilai_akhir > 60:
        print("Nilai akhir: C+")
    elif nilai_akhir > 55:
        print("Nilai akhir: C")
    elif nilai_akhir > 50:
        print("Nilai akhir: C-")
    elif nilai_akhir > 30:
        print("Nilai akhir: D")
    else:
        print("Nilai akhir: E")

if __name__ == "__main__":
    main()