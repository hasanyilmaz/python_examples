# hesap makinesini fonksiyon ile yaz

operation = int(input("Hangi işlemi yapmak istiyorsunuz: \n\t 1 - Toplama \n\t 2 - Çıkarma \n\t 3 - Çarpma \n\t "
                      "4 - Bölme\n"
                      "Lütfen işlem sıra numarası giriniz: "))

if operation == 1:
    plus = lambda x, y: x + y
    print("Sonuç: ", plus(x=float(input("İlk sayı: ")), y=float(input("İkinci sayı: "))))
elif operation == 2:
    minus = lambda x, y: x - y
    print("Sonuç: ", minus(x=float(input("İlk sayı: ")), y=float(input("İkinci sayı: "))))
elif operation == 3:
    multi = lambda x, y: x * y
    print("Sonuç: ", multi(x=float(input("İlk sayı: ")), y=float(input("İkinci sayı: "))))
elif operation == 4:
    divide = lambda x, y: x / y
    print("Sonuç: ", divide(x=float(input("İlk sayı: ")), y=float(input("İkinci sayı: "))))
else:
    print("Yanlış bir işlem numarası girdiniz!")
