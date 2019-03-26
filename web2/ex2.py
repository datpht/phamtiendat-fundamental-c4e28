from pymongo import MongoClient

mongo_uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

client = MongoClient(mongo_uri)

db = client.c4e

new_post = {
    "title":"C4E28",
    "author":"Đạt Phạm",
    "content":"Cố gắng để nổi bật trước người khác thật là một trò lồ,Họ chỉ cố nhận lại sự thương hại của người khác, Điều đó càng chứng tỏ họ đang đánh mất chính mình"
}
db.posts.insert_one(new_post)
