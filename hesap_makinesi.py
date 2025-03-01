def hesap_makinesi(sayi1, sayi2, islem):
    if islem == "+":
        return f"{sayi1} + {sayi2} = {sayi1 + sayi2}"
    elif islem == "-":
        return f"{sayi1} - {sayi2} = {sayi1 - sayi2}"
    elif islem == "*":  
        return f"{sayi1} * {sayi2} = {sayi1 * sayi2}"
    elif islem == "/":
        if sayi2 != 0:
            return f"{sayi1} / {sayi2} = {sayi1 / sayi2}"
        else:
            return "Hata: Bölme işlemi için ikinci sayı 0 olamaz!"
    else:
        return "Hata: Geçersiz işlem türü!"

# Kullanıcıdan giriş alma
sayi1 = int(input("Lütfen birinci sayıyı giriniz: "))
sayi2 = int(input("Lütfen ikinci sayıyı giriniz: "))
islem = input("Yapmak istediğiniz işlemi seçiniz (+, -, *, /): ")

# Sonucu ekrana yazdır
print(hesap_makinesi(sayi1, sayi2, islem))
