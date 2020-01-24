'''Fonksiyonları kullanarak bir notification sistemi yazalım;

	1-) Kullanıcılarımızı kaydetmek için bir veri yapısından yaralanalım (İlk durumda boş olsun)

	2-) Program başlangıcında seçenekler sunsun
		a-) kayıt ekle
		b-) kayıt sil
		c-) tüm kayıtları listele
		d-) sms gönder
		e-) rehberi boşalt
		q-) programdan çık

	3-) kayıt ekleme işlemi seçildiğinde ilgili fonksiyon üzerinden kullanıcının
"adı soyadı", "telefon numarası", "sms almak istiyorum (evet/hayır)" bilgileri alınsın

	4-) kayıt sil dendiğinde kullanıcının "adı soyadı" bilgisi istenip eğer listede mevcutsa
"kayıt silindi", listede böyle bir kayıt yoksa "kayıt listede bulunamadı" mesajı verilsin

	5-) tüm kayıtları listele seçeneği seçilirse kaydedilmiş tüm kayıtları ekrana bassın

	6-) sms gönder seçeneği seçilirse sms "sms almak istiyorum" seçeneği "evet" olan
tüm kullanıcıların bilgilerini ekrana basıp sms gönderildi yazdırsın

	7-) rehberi boşalt seçeneği seçilirse rehberdeki tüm kayıtlar silinsin

	8-) programdan çık dendiğinde program bitirilsin.

	9-) q "programdan çık" seçeneği haricinde hangi işlem yapılırsa yapılsın
program ilk ekrana yani 2. maddeye geri dönüp işlem listesini ekrana bassın.'''


kayitlistesi = [["Ad", "Telefon", "SMS"],
                ["Hamdi", "536", "Evet"],
                ["Hasan", "536", "Hayır"],
                ['Osman', "888", "Evet"]
                ]


def options():
    opt = input("Seçenekler:\n"
                "1 - Kayıt ekle\n"
                "2 - Kayıt sil\n"
                "3 - Tüm kayıtları listele\n"
                "4 - SMS gönder\n"
                "5 - Rehberi boşalt\n"
                "9 - Uygulamadan çık\n"
                )
    print(opt)
    if opt == '1':
        new_reg()
    elif opt == '2':
        del_reg()
    elif opt == '3':
        prnt_liste()
    elif opt == '4':
        sms_ok()
    elif opt == '5':
        del_all()
    elif opt == '9':
        ex_all()
    else:
        print("Hatalı bir giriş yaptınız.")
        print("--------------------------")
        options()


def new_reg():
    kayit_adi = input("Adınız: ")
    kayit_tel = input("Tel: ")
    kayit_sms = input("SMS (Evet/Hayır): ")
    yeni_kayit = [kayit_adi, kayit_tel, kayit_sms]
    kayitlistesi.append(yeni_kayit)
    print(kayitlistesi)
    print("--------------------------")
    options()


def del_reg():
    arama = str(input("Silmek istediğiniz kişinin adını giriniz: \n"))
    for kayit in kayitlistesi[1:]:
        if arama == kayit[0]:
            print("Silinen kişi bilgisi: {}".format(kayit))
            kayitlistesi.remove(kayit)
            print("Kalan liste: ", kayitlistesi)
            break
        else:
            print("aranıyor..")
    print("--------------------------")
    options()


def prnt_liste():
    print("Kalan liste: \n", kayitlistesi)
    print("--------------------------")
    options()


def sms_ok():
    arama = str(input("SMS göndermek istiyor musunuz (Evet/Hayır): \n"))
    for kayit in kayitlistesi[1:]:
        if arama == 'Evet' and arama == kayit[2]:
            print("SMS gönderilen kişi bilgisi: {}".format(kayit))
        else:
            pass
    print("--------------------------")
    options()


def del_all():
    del kayitlistesi[1:]
    # kayitlistesi = kayitlistesi[1:] ya da []
    print("Mevcut liste: ", kayitlistesi)
    print("--------------------------")
    options()


def ex_all():
    soru = input("Uygulama kapatılsın mı? (Evet/Hayır): ")
    if soru == 'Evet':
        print("Teşekkürler")
    elif soru == 'Hayır':
        print("--------------------------")
        options()


options()
