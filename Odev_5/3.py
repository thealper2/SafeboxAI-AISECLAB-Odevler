from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB bağlantısı için gerekli bilgiler
mongo_username = "your_username"
mongo_password = "your_password"
mongo_cluster = "your_cluster_url"

# MongoDB bağlantısı
client = MongoClient(f"mongodb+srv://{mongo_username}:{mongo_password}@{mongo_cluster}/test?retryWrites=true&w=majority")

# Veritabanı ve koleksiyon seçimi
db = client.flaskmongodb
collection = db.Users

# 1. Endpoint - Kullanıcı ekleme
@app.route('/adduser', methods=['POST'])
def add_user():
    user_data = request.get_json()
    collection.insert_one(user_data)
    return jsonify({'message': 'Kullanıcı eklendi.'})

# 2. Endpoint - Yaşı 25'ten fazla olan kullanıcıları döndürme
@app.route('/25', methods=['GET'])
def get_users_over_25():
    result = collection.find({"Age": {"$gt": 25}})
    users = []
    for document in result:
        users.append(document)
    return jsonify(users)

# 3. Endpoint - Tüm kullanıcıları döndürme
@app.route('/', methods=['GET'])
def get_all_users():
    result = collection.find()
    users = []
    for document in result:
        users.append(document)
    return jsonify(users)

# 4. Endpoint - Belirli bir ID'ye sahip kullanıcıyı silme
@app.route('/deleteuser', methods=['POST', 'DELETE'])
def delete_user():
    user_id = request.args.get('id')
    result = collection.delete_one({"_id": user_id})
    if result.deleted_count == 1:
        return jsonify({'message': 'Kullanıcı silindi.'})
    else:
        return jsonify({'message': 'Kullanıcı bulunamadı.'})

if __name__ == '__main__':
    app.run()
