import json

class Film:
    def __init__(self, filmAdi, filmYili, yonetmen, tur):
        self.filmAdi = filmAdi
        self.filmYili = filmYili
        self.yonetmen = yonetmen
        self.tur = tur

def film_olustur():
    filmAdi = input("Film adı: ")
    filmYili = input("Film yılı: ")
    yonetmen = input("Yönetmen: ")
    tur = input("Tür: ")

    film = Film(filmAdi, filmYili, yonetmen, tur)
    film_ekle(film)

def film_ekle(film):
    with open("filmler.json", "r") as dosya:
        filmler = json.load(dosya)

    filmler.append(vars(film))

    with open("filmler.json", "w") as dosya:
        json.dump(filmler, dosya)

def film_sil(filmAdi):
    with open("filmler.json", "r") as dosya:
        filmler = json.load(dosya)

    yeni_filmler = [film for film in filmler if film['filmAdi'] != filmAdi]

    with open("filmler.json", "w") as dosya:
        json.dump(yeni_filmler, dosya)

def film_ara(filmAdi):
    with open("filmler.json", "r") as dosya:
        filmler = json.load(dosya)

    bulunan_filmler = [film for film in filmler if film['filmAdi'] == filmAdi]

    if len(bulunan_filmler) > 0:
        print("Bulunan filmler:")
        for film in bulunan_filmler:
            print(film['filmAdi'], film['filmYili'], film['yonetmen'], film['tur'])
    else:
        print("Film bulunamadı.")

def filmleri_goster():
    with open("filmler.json", "r") as dosya:
        filmler = json.load(dosya)

    for film in filmler:
        print(film['filmAdi'], film['filmYili'], film['yonetmen'], film['tur'])

def menu_goster():
    print("\nFilm Uygulaması")
    print("1. Filmleri göster")
    print("2. Film oluştur")
    print("3. Film sil")
    print("4. Film ara")
    print("5. Çıkış")

while True:
    menu_goster()
    secim = input("\nBir işlem seçin (1-5): ")

    if secim == "1":
        print("\nFilmler:")
        filmleri_goster()
    elif secim == "2":
        print("\nFilm oluştur")
        film_olustur()
    elif secim == "3":
        print("\nFilm sil")
        filmAdi = input("Silmek istediğiniz film adı: ")
        film_sil(filmAdi)
    elif secim == "4":
        print("\nFilm ara")
        filmAdi = input("Aramak istediğiniz film adı: ")
        film_ara(filmAdi)
    elif secim == "5":
        print("\nÇıkış yapılıyor...")
        break
    else:
        print("\nGeçersiz seçim! Lütfen tekrar deneyin.")
