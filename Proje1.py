import time #programın bir saniye beklemesi için ekledim.
print("""
____________İŞLEMLER_____________

1-Yeni Kayıt Ekle

2-Kayıt Güncelle

3-kayıt Sil

4-Tüm Kayıtları Listele

5-İsme Göre Listele

6-Programdan çık


""")
while True:
    Sözlük={'Dilek CAN':'21/05/1994',
            'Aslı Koçak':'16/12/1994',
            'Esra Aydın':'24/05/1993',
            'Sedat CAN':'20/01/2001',
            'Samet CAN':'16/05/2010'} #bir dictionary oluşturdum.
    işlem = input( "Lütfen bir işlem seçiniz: " )

    if (işlem == "1"):
        anahtar = input( "Lütfen Ad Soyad  giriniz: " )
        deger = input( "Lütfen doğum tarihi giriniz: " )
        Sözlük[anahtar]=deger   #dışardan girilen bilgileri  dictionary' e attım.
        print(Sözlük)
    elif (işlem == "2"):
        print( Sözlük )
        #kayıt güncellemek için önce boş bir dictionary oluşturdum.
        yeni_Sözlük={} #Sözlük adındaki Dictionary içinden güncellenmek istenen veri buraya yazılacak
        yeni_anahtar=input("Lütfen Ad Soyad  giriniz: ")
        yeni_deger=input("Lütfen doğum tarihi giriniz: ")
        yeni_Sözlük[yeni_anahtar]=yeni_deger

        Sözlük.update(yeni_Sözlük)
        print("Güncelleme yapıldı !",Sözlük)

    elif (işlem == "3"):
        print(Sözlük)
        kayıt=input("Silmek istediğiniz kaydı giriniz: ")
        Sözlük.pop(kayıt)
        print("Silme işlemi başarılı!\nSildiğiniz değer: {}\n".format(kayıt),Sözlük)

    elif (işlem== "4"):
        Liste=[]
        print("Tüm kayıtlar listeleniyor...")
        time.sleep(1)#program bir saniye beklesin.
        Liste=Sözlük.items() #Kayıtları listelemek için items() metodu kullandım.
        print(Liste)

    elif (işlem== "5"):
        Liste=[]
        print("kayıtlar isimlere göre listeleniyor...")
        time.sleep(1)
        Liste= Sözlük.keys()#sadece isimlere göre sıralamak için keys() metodu kullandım.
        print(Liste)

    elif (işlem== "6"):
        print("Program sonlandırılıyor...!")
        break

    else:
        print("Geçersiz işlem...")
        break























