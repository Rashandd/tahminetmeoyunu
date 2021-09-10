# HİLESİZ ŞANS OYUNU KÖTÜ ALGORİTMA KULLANILMIŞ KOD VAR EDİTLEMEK İSTERSEN BOL ŞANS
import random
from os import system, name
clear = lambda: system("clear" if name == "posix" else "cls")
def oyun1(): #%2.94 sans

 harf = ["q" ,"w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "I", "z", "c", "v", "b", "n", "m"]
 sayi = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


 a = random.choice(harf + sayi)
 print(harf + sayi)
 print("yukardıdaki seçeneklerden gelecek olanı tahmin ediniz")
 tahmin = input()
 if a == tahmin:
    print("---%2.94 ŞANSLA DOĞRU BİLDİNİZ---") 
    print("yeniden oynamak için (1)i tuşlayın")
    sed = input()
    if sed == "1" :
        oyun1()

 else:
    print("Yanlış tahmin ettinniz :(")
    print("doğru secenek asagıdakidir")
    print(a)
    print("yeniden oynamak için (1)i tuşlayın")
    sed = input()
    if sed == "1" :
        oyun1()
    else:
        return
def oyun2():#%50 şans
    kume = ["1", "2"]
    print(" 1 mi 2 mi")
    tahmin = input()
    a = random.choice(kume)
    if a == tahmin :
        print("---DOĞRU BİLDİNİZ---")
        print("yeniden oynamak için (1) i tuşlayın")
        sed = input()
        if sed == "1":
            oyun2()
        else:
            return
    else:
        print("---YANLIŞ BİLDİNİZ---")
        print("yeniden oynamak için (1)i tuşlayın")
        sed = input()
        if sed == "1":
            oyun2()
        else:
            return
def oyun3():#zar atma
    zar = ["1", "2", "3", "4", "5", "6"]
    ta = random.choice(zar)
    print("zarda hangi sayının geldiğini tahmin ediniz")
    sec = input()
    if ta == sec :
        print("---DOĞRU BİLDİNİZ---")
        print("yeniden oynamak için (1) i tuşlayın")
        sed = input()
        if sed == "1":
            oyun3()
        else:
            return
    else:
        print("---YANLIŞ BİLDİNİZ---")
        print('dogru secenek assagidakidir')
        print(ta)
        print("yeniden oynamak için (1)i tuşlayın")
        sed = input()
        if sed == "1":
            oyun3()
        else:
            return clear
def oyun4():#100 oyunu 
    listem = []#0,100
    for q in range(0,101, 1):
        listem.append(str(q))    
    choice1 = random.choice(listem)
    choice2 = random.choice(listem)
    print("ilk sayıyı giriniz")
    secim1 = input()
    print("ikinci sayıyı giriniz")
    secim2 = input()
    if secim1 == choice1:
        if secim2 == choice2:
            print("doğru bildiniz")
        else:
            print("1 ini doğru bildiniz ")
            print(choice1 , choice2)
    else:
        print("2 sinide yanlış bildiniz")
        print(choice1 , choice2)
    print("yeniden oynamak için (1)i tuşlayın")
    sed = input()
    if sed == "1":
        oyun4()
    else:
        return

    
def oyun5():#renk secme
    renkler =["sari",'mavi','siyah','beyaz']
    print('asagidaki renklerden hangisi cikcagini tahmin edin')
    oyun90 = random.choice(renkler)
    print(renkler)
    secs = input()
    if secs == oyun90:
        print('DOGRU BILDINIZ')
        print("yeniden oynamak için (1)i tuşlayın")
        sed = input()
        if sed == "1":
            oyun5()
        else:
            return
    else:
        print('yanlis bildiniz')
        print("yeniden oynamak için (1)i tuşlayın")
        print(oyun90)
        sed = input()
        if sed == "1":
            oyun5()
        else:
            return


a = '1'
while a == '1':
 clear()
 print("\033[1m Hangi oyunu oynamak istersiniz")
 print("ilk secenek %2.94 şanslı tahmin etme oyunu için --> (1)i tuşlayınız  ")
 print("%50 şansla tahmin etme oyunu için --> (2)yi tuşlayınız  ")
 print("Zar oyunu için --> (3)ü tuşlayınız  ")
 print("100 oyunu icin (4)u tuslayiniz  ")
 print('renk secme oyunu icin (5) i tuslayiniz')
 print("oyundan cıkamk ıcın 6  yı tuşlayın")
 secim = input()
 if secim == "1":
     oyun1()
 if secim == "2":
     oyun2()
 if secim == "3":
      oyun3()
 if secim == "4":
     oyun4()
 if secim == '5':
     oyun5()
 if secim == '6':
     a = '0'

 


















#onceden kullandigim komutlar
"""for i in range(len(harf)):
    print(i)
for i in range(len(sayi)):
    print(i)"""
    #BUNLARI KAÇ ADET HARF VE SAYI OLDUĞUNU ÖĞRENMEK İÇİN YAPTIM
