from collections import deque

cache = {

}
recently_used = deque()
CACHE_SIZE = 3

db = {

}


def get_value(key):
    val = cache.get(key)
    if val:
        shuffle_queue(key)
    else:
        val = db.get(key)
        update_queue_cache(key, val)
    return val


def shuffle_queue(key):
    recently_used.remove(key)
    recently_used.append(key)


def update_queue_cache(key, val):
    if len(recently_used) < CACHE_SIZE:
        recently_used.append(key)
        cache.update({key: val})
    else:
        recently_used.pop()
        recently_used.append(key)
        cache.update({key: val})
