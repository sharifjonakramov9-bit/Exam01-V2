x = input("Text: ")
undosh = "qwrtypsdfghjklzxcvbnm"
count = 0

for i in x:
    if i.lower() in undosh:
        count += 1

print(count)
    