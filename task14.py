x = input("Email manzil kiriting: ").strip().lower()

if x.endswith(".jpg") or x.endswith(".png") or x.endswith(".svg"):
    print(x)
else:
    print(False)
