x = input("Email manzil kiriting: ").strip().lower()

if x.endswith(".@com"):
    print(x)
else:
    print(False)
