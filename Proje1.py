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

    number = input( "Lütfen bir işlem seçiniz: " )

    if (number == "1"):
        dictionary = {'Dilek CAN': '21/05/1994',
                  'Aslı Koçak': '16/12/1994',
                  'Esra Aydın': '24/05/1993',
                  'Sedat CAN': '20/01/2001',
                  'Samet CAN': '16/05/2010'}  # bir dictionary oluşturdum.

        key = input( "Lütfen Ad Soyad  giriniz: " )
        value = input( "Lütfen doğum tarihi giriniz: " )

        dictionary[key]=value   #dışardan girilen bilgileri  dictionary' e attım.
        print(dictionary)

    elif(number  == "2"):
        print( dictionary )
        #kayıt güncellemek için önce boş bir dictionary oluşturdum.
        new_dictionary={} #new_dictionary adındaki Dictionary içinden güncellenmek istenen veri buraya yazılacak
        new_key=input("Lütfen Ad Soyad  giriniz: ")
        new_value=input("Lütfen doğum tarihi giriniz: ")
        if (new_key in dictionary):
            new_dictionary[new_key]=new_value
            dictionary.update(new_dictionary)
            print("Güncelleme yapıldı !",new_dictionary)
            print(dictionary)
        else:
            print("Kayıt bulunamadı...")


    elif (number  == "3"):#Silme
        print(dictionary)
        record=input("Silmek istediğiniz kaydı giriniz: ")
        if (record in dictionary):
            dictionary.pop(record)
            print("Silme işlemi başarılı!\nSildiğiniz değer: {}\n".format(record),dictionary)
        else:
            print("Kayıt bulunamadı...")

    elif (number == "4"):
        my_List=[dictionary]
        print("Tüm kayıtlar listeleniyor...")
        time.sleep(1)#program bir saniye beklesin.
        my_List=dictionary.items() #Kayıtları listelemek için items() metodu kullandım.
        print(my_List)

    elif (number  == "5"):
        name=input("Lütfen Ad Soyad giriniz: ")
        if (name in dictionary):
            print("{}'nin doğum tarihi: {}'dir.\n".format(name,dictionary[name]) )
        else:
            print("Kayıt bulunamadı...")


    elif (number == "6"):
        print("Program sonlandırılıyor...!")
        break

    else:
        print("Geçersiz işlem...")
        break























