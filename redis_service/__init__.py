import redis

# Создать подключения к редису
redis_db = redis.from_url('redis://redis_db')

# Создать запись в базу редис
redis_db.set("spam", 10) # {"spam": 10}

# Получить значения из базы
data = redis_db.get("spam")
print(data)