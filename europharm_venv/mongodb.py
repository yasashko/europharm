from pymongo import MongoClient
from settings import MONGO_DB
from settings import MONGODB_LINK

mdb = MongoClient(MONGODB_LINK)[MONGO_DB] #переменные для работы с базой данных

def search_or_save_user(mdb, effective_user, message):
    user = mdb.user.find_one({"user_id": effective_user.id}) #поиск в коллекции users по user.id
    if not user:  #если такого нет, то создаем словарь с данными
        user = {
            "user_id": effective_user.id,
            "first_name": effective_user.first_name,
            "last_name": effective_user.last_name,
            "chat_id": message.chat.id
        }
        mdb.user.insert_one(user) #сохраняем в коллекцию users
    return user