#!/usr/bin/env python3
from pymongo import MongoClient
client = pymongo.MongoClient("mongodb://localhost:27017/")

def list_all(mongo_collection):
    return list(mongo_collection.find())
