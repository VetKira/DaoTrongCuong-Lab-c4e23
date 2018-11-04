from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)

db = client.get_database()

posts = db["posts"]

new_post ={
    "title" : "Tuôi nứng",
    "author" : "Kira",
    "content" : "Tôi nứng tôi thổi khúc tiêu xa . Nhờ cơn nứng mùa hạ mang qua bên nàng . Trăng thanh nứng ...... nứng n lần vẫn nứng "
}

posts.insert_one(new_post)

client.close