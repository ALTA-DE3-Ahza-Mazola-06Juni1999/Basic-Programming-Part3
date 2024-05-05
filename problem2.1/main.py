bilangan = int(input("masukkan bilangan "))

for i in range (1, bilangan + 1):
    if bilangan % i == 0:
        print(i)