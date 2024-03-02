from pymongo import MongoClient

atlas_connection_string = "mongodb+srv://amitcarpenter:amitcarpenter@bms.oboxpe2.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(atlas_connection_string)
db = client.test

collection = db.emails
collection_youtube = db.videos
collection_order = db.orders
collection_ips = db.ips
