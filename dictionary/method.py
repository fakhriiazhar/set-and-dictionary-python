bio = {
    "nama" : "fakhrii azhar",
    "nim" : 2311102441169,
}

print("===="*5, "method clear", "===="*5)
bio1 = bio.copy()
print(bio1)
bio1.clear()
print(bio1)

print("===="*5, "method formkeys", "===="*5)
M_formkeys = dict.fromkeys(["nama"], "fakhrii azhar")
print(M_formkeys)

print("===="*5, "method copy", "===="*5)
copy_bio = bio.copy()
print(copy_bio)

print("===="*5, "method get", "===="*5)
items = bio.get("nama")
print(nama)

print("===="*5, "method items", "===="*5)
items = bio.items()
print(items)

print("===="*5, "method pop", "===="*5)
bio2 = bio.copy()
bio3 = bio.copy()
bio2.pop("nama")
bio3.popitem()
print("bio 2 = ", bio2)
print("bio3 = ", bio3)

print("===="*5, "method setdefault", "===="*5)
bio4 = bio.copy()
default1 = bio.setdefault("nama")
default2 = bio.setdefault("angkatan")
default3 = bio.setdefault("prodi", "Teknik Informatika")
print(default1)
print(default2)
print(default3)

print("===="*5, "method update", "===="*5)
salin = bio.copy()
salin.update({"angkatan" : 2023})
print(salin)

print("===="*5, "method values", "===="*5)
nilai = bio.values()
print(nilai)
