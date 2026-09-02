
def grade(rentannilai):
    if rentannilai >= 85:
        print(f"Nilai {rentannilai} -> Grade A")
    elif rentannilai >= 70:
        print(f"Nilai {rentannilai} -> Grade B")
    elif rentannilai >= 60:
        print(f"Nilai {rentannilai} -> Grade C")
    elif rentannilai >= 50:
        print(f"Nilai {rentannilai} -> Grade D")
    else:
        print(f"Nilai {rentannilai} -> Grade E")

grade(98)
grade(88)
grade(100)