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
