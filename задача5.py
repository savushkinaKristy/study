cache = {}
def set_value(key, value):
    cache[key] = value
def get_value(key):
    return cache.get(key)
set_value("user_1", "Данные")
print(get_value("user_1"))
