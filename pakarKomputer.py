# Knowladge Base
rules_kerusakan = {
    "Motherboard Bermasalah": {"tidak_ada_display", "beep_tidak_normal", "tidak_booting"},
    "Baterai Laptop Drop": {"baterai_cepat_habis", "tidak_bisa_charge", "mati_mendadak"},
    "Kipas Rusak": {"suara_berisik", "cepat_panas", "kipas_tidak_berputar"},
    "OS Corrupt": {"blue_screen", "sering_restart", "gagal_booting"},
    "Keyboard Rusak": {"tombol_tidak_respon", "input_sendiri", "beberapa_tombol_mati"}
}

# Solusi
solusi_kerusakan = {
    "Motherboard Bermasalah": "Periksa motherboard atau bawa ke teknisi.",
    "Baterai Laptop Drop": "Ganti baterai dengan yang baru.",
    "Kipas Rusak": "Bersihkan atau ganti kipas.",
    "OS Corrupt": "Install ulang sistem operasi.",
    "Keyboard Rusak": "Gunakan keyboard eksternal atau ganti keyboard."
}

# Semua gejala
semua_gejala = {
    "tidak_ada_display",
    "beep_tidak_normal",
    "tidak_booting",
    "baterai_cepat_habis",
    "tidak_bisa_charge",
    "mati_mendadak",
    "suara_berisik",
    "cepat_panas",
    "kipas_tidak_berputar",
    "blue_screen",
    "sering_restart",
    "gagal_booting",
    "tombol_tidak_respon",
    "input_sendiri",
    "beberapa_tombol_mati"
}

# Input User
print("=== SISTEM PAKAR DIAGNOSA KOMPUTER ===")
print("\nDaftar gejala yang tersedia:")
for g in semua_gejala:
    print("-", g)

print("\nMasukkan gejala yang dialami (pisahkan dengan koma):")
input_user = input("Gejala: ").lower()

gejala_user = set(g.strip() for g in input_user.split(","))

# Jika semua gejala cocok
def diagnosa_strict(gejala_input):
    hasil = []
    for kerusakan, syarat in rules_kerusakan.items():
        if syarat.issubset(gejala_input):
            hasil.append(kerusakan)
    return hasil

#Jika hanya beberapa yang memenuhin rules kerusakan
def diagnosa_skor(gejala_input):
    skor_tertinggi = 0
    hasil = None

    for kerusakan, syarat in rules_kerusakan.items():
        skor = len(gejala_input.intersection(syarat))

        if skor > skor_tertinggi:
            skor_tertinggi = skor
            hasil = kerusakan

    return hasil, skor_tertinggi


# OUTPUT
print("\n=== HASIL DIAGNOSA ===")
hasil_strict = diagnosa_strict(gejala_user)

if hasil_strict:
    for h in hasil_strict:
        print(f"\nKerusakan: {h}")
        print(f"Solusi: {solusi_kerusakan[h]}")
else:
    print("Tidak ditemukan kecocokan penuh.")

    hasil_skor, nilai = diagnosa_skor(gejala_user)

    if hasil_skor and nilai > 0:
        print("\n=== DIAGNOSA BERDASARKAN KEMIRIPAN ===")
        print(f"Kemungkinan kerusakan: {hasil_skor}")
        print(f"Jumlah gejala cocok: {nilai}")
        print(f"Solusi: {solusi_kerusakan[hasil_skor]}")
    else:
        print("Tidak ada kerusakan yang mendekati.")