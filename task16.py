x = 80_000
y = int(input("Yoshizni kiriting: "))

if 0 <= x and x <= 5:
    print(f"sizning yoshingiz {y}, sizga 60% chegirma beriladi summa {x*60/100}")
elif 6 <= x and x <= 12:
    print(f"sizning yoshingiz {y}, sizga 30% chegirma beriladi summa {x*30/100}")
elif 55 <= x:
    print(f"sizning yoshingiz {y}, sizga 40% chegirma beriladi summa {x*40/100}")
else:
    print(f"{y} yoshga chegirma ajratilmagan.")
