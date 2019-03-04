import pymongo

from pymongo import MongoClient

client = MongoClient()

db = client.trydatabase#创建数据库
collection = db.user #创建表
data1 = {"name":"tom",'age':20}
collection.insert_one(data1)#插入数据