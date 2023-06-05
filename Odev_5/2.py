import random
from pymongo import MongoClient

# MongoDB bağlantısı için gerekli bilgiler
mongo_username = "your_username"
mongo_password = "your_password"
mongo_cluster = "your_cluster_url"

# MongoDB bağlantısı
client = MongoClient(f"mongodb+srv://{mongo_username}:{mongo_password}@{mongo_cluster}/test?retryWrites=true&w=majority")

# Veritabanı ve koleksiyon seçimi
db = client.flaskmongodb
collection = db.Users

# Rastgele veri eklemek için kullanılacak listeler
names = ["John", "Alice", "Bob", "Emma", "Michael", "Sophia", "Oliver", "Isabella", "Daniel", "Mia"]
jobs = ["Engineer", "Doctor", "Teacher", "Artist", "Writer", "Scientist", "Lawyer"]
descriptions = ["Description 1"]

# 50 adet random kullanıcı ekleme
for _ in range(50):
    name = random.choice(names)
    age = random.randint(0, 50)
    job = random.choice(jobs)
    description = random.choice(descriptions)

    user = {
        "Name": name,
        "Age": age,
        "Job": job,
        "Description": description
    }

    collection.insert_one(user)

print("Veri ekleme tamamlandı.")

# Users koleksiyonundaki tüm verileri getiren sorgu
result = collection.find()
for document in result:
    print(document)

# İsmi "Ahmet" olan kullanıcıları getiren sorgu
result = collection.find({"Name": "Ahmet"})
for document in result:
    print(document)

# Yaşı 20'den fazla olan kullanıcıları getiren sorgu
result = collection.find({"Age": {"$gt": 20}})
for document in result:
    print(document)

# Yaşı 25'den fazla olan ve description'u 0 olan kullanıcıları getiren sorgu
result = collection.find({"$and": [{"Age": {"$gt": 25}}, {"Description": 0}]})
for document in result:
    print(document)

# Yaşı 45-48 arasında olan kullanıcıları silen sorgu
collection.delete_many({"Age": {"$gte": 45, "$lte": 48}})
print("Silme işlemi tamamlandı.")
