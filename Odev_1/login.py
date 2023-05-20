def bilgi_kaydet():
    kullanici_adi = input("Kullanıcı adınızı girin: ")
    sifre = input("Şifrenizi girin: ")

    with open("kullanici_bilgileri.txt", "a") as dosya:
        dosya.write(kullanici_adi + "," + sifre + "\n")

def giris():
    kullanici_adi = input("Kullanıcı adınızı girin: ")
    sifre = input("Şifrenizi giriniz: ")

    with open("kullanici_bilgileri.txt", "r") as dosya:
        for line in dosya:
            bilgiler = line.strip().split(",")
            if bilgiler[0] == kullanici_adi and bilgiler[1] == sifre:
                print("Giriş yapıldı.")
            else:
                print("Kullanıcı adı veya şifre yanlış.")

bilgi_kaydet()
giris()
