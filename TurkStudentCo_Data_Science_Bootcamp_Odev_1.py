#Soru1:Basit


#Kullanıcıdan iki sayı alıyoruz
a= float(input("Birinci sayıyı girin: "))
b= float(input("İkinci sayıyı girin: "))

#Sayıları topluyoruz ve toplam değişkenine atıyoruz
toplam = a+b

#Sonucu ekrana yazdırıyoruz
print("Sayıların toplamı:", toplam)


#Soru2:Orta


#1'den 100'e kadar olan sayıları toplamak için değişken tanımlıyoruz
toplam = 0

#1'den 100'e kadar sayıları for döngüsü kullanarak topluyoruz
for sayi in range(1, 101):
    toplam += sayi

#Sonucu ekrana yazdırıyoruz
print("1'den 100'e kadar olan sayıların toplamı:", toplam)


#Soru3: İleri


#Asal sayıyı kontrol eden bir fonksiyon tanımlıyoruz
def asal_mi(sayi):
    if sayi < 2:
        return False
    for i in range(2, int(sayi**0.5) + 1):
        if sayi % i == 0:
            return False
    return True

#Kullanıcıdan sayı alıyoruz
sayi = int(input("Bir sayı girin: "))

#Asal olup olmadığını kontrol edip sonucu ekrana yazdırıyoruz.
if asal_mi(sayi):
    print(sayi, "Asal sayıdır.")
else:
    print(sayi, "Asal sayı değildir.")
