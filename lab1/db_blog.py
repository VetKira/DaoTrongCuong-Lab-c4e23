from pymongo import MongoClient

uri = "mongodb://admin:VetKira.96@ds249503.mlab.com:49503/c4e23-kira"

# 1 connect
client = MongoClient(uri)

# 2 get default database lay ra data mac dinh
db = client.get_database()

# 3 get collection lay ra bo suu tap

posts = db["posts"]
movies = db["movies"]

# 4 create data
new_post={
    "title": "hôm nay trời nứng",
    "content" : "kimochiiiiii!",
}

new_movie ={
    "title" : " nứng là 1 nghệ thuật",
    "rating": 9.9
}



# 5 insert data

# posts.insert_one(new_post)
# movies.insert_one(new_movie) # sai # de no k them bua bai

# 5.1 read data

post_list = posts.find()

# doc tung phan tu

# p=post_list[1]
for p in post_list:
    print(p["title"])



# 6 close connection

client.close()
