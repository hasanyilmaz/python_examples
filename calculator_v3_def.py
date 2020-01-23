# hesap makinesini fonksiyon ile yaz

operation = int(input("Hangi işlemi yapmak istiyorsunuz: \n\t 1 - Toplama \n\t 2 - Çıkarma \n\t 3 - Çarpma \n\t "
                      "4 - Bölme\n"
                      "Lütfen işlem sıra numarası giriniz: "))


def calc(num1=float(input("İlk sayı: ")), num2=float(input("İkinci sayı: "))):
    if operation == 1:
        plus = num1 + num2
        print("İşlem sonucu: ", plus)
    elif operation == 2:
        minus = num1 - num2
        print("İşlem sonucu: ", minus)
    elif operation == 3:
        multi = num1 * num2
        print("İşlem sonucu: ", multi)
    elif operation == 4:
        divide = num1 / num2
        print("İşlem sonucu: ", divide)
    else:
        print("Yanlış bir işlem numarası girdiniz!")


calc()
