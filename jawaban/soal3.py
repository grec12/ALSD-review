def hitung_rata2(list_nilai):
    t = 0
    s = 0
    for i in list_nilai:
        t += 1
        s += 1
        print(f"Nilai ke-{s}:{i}")
    rata2 = t / len (list_nilai)
    return f"Rata_rata: {rata2}"

print(hitung_rata2(list_nilai = [80, 75, 90, 65, 88]))

