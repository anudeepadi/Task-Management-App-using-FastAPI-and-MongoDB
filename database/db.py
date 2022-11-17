from pymongo import MongoClient
from models.model import TaskModel, CreateTaskModel
connection = MongoClient("mongodb+srv://m001-student:Factory2$@cluster0.qxiwj.mongodb.net/?retryWrites=true&w=majority")

db = connection['store_tasks']
collection = db['task']


def create_task(task):
    ids = [task["_id"] for task in collection.find()]
    for i in range(1, 1000):
        if i not in ids:
            id = i
            break
    collection.insert_one({"_id": id
                            , "title": task.title
                            , "is_completed": False})
    return {"id": id}

def get_tasks():
    tasks = collection.find()
    return {"tasks": [{"id": task["_id"]
                        , "title": task["title"]
                        , "is_completed": task["is_completed"]} for task in tasks]}

def get_task(id):
    task = collection.find_one({"_id": id})
    if task == None:
        return None
    return {"id": task["_id"], "title": task["title"], "is_completed": task["is_completed"]}

def delete_task(id):
    collection.delete_one({"_id": id})
    return None

def update_complete(id, title, is_completed):
    collection.update_one({"_id": id}, {"$set": {"title": title, "is_completed": is_completed}})
    return None

def add_multiple(tasks):
    ids = [task["_id"] for task in collection.find()]
    for i in range(1, 1000):
        if i not in ids:
            id = i
            break
    for task in tasks:
        ids.append(task.id)
        collection.insert_one({"_id": id
                                , "title": task.title
                                , "is_completed": task.is_completed})
        ids.append(id)
    return {"tasks": [
        {"id": id} for id in ids
    ]}

def delete_all(tasks):
    for task in tasks:
        collection.delete_one({"_id": task.id})
    return None
