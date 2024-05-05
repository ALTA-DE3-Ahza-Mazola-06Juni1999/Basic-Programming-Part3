bilangan = int(input("masukkan bilangan "))

for i in range (bilangan, 0, -1):
    if bilangan % i == 0:
        print(i);