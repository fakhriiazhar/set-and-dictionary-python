#operation on dictionary
data_mahasiswa = {
    "Nama" : "fakhrii azhar",
    "Prodi" : "S1 Teknik Informatika",
    "Nim" : "2311102441169",
    "Angkatan" : "2023"

}

print("===="*5, "operasi menambahkan", "====="*5)
data_mahasiswa["tempat_tinggal"] = "Jl. Pemuda 4"
print(data_mahasiswa)

print("===="*5, "operasi mengakses data", "===="*5)
print(data_mahasiswa["Nama"], data_mahasiswa["Nim"])

print("===="*5, "operasi mengecek value", "===="*5)
if "S1 Teknik Informatika" in data_mahasiswa.values():
    print("merupakan mahasiswa prodi S1 Teknik Informatika")
