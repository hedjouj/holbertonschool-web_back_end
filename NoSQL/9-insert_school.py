#!/usr/bin/env python3
"""list all"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """insert un doc"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
