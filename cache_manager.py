import logging
import time
from functools import lru_cache
from app.config import CACHE_TTL

class CacheManager:
    def __init__(self):
        self.cache = {}

    @lru_cache(maxsize=1024)
    def get_from_cache(self, key):
        if key in self.cache and self.cache[key]["expires"] > time.time():
            return self.cache[key]["data"]
        else:
            return None

    def set_in_cache(self, key, data):
        self.cache[key] = {"data": data, "expires": time.time() + CACHE_TTL}
        logging.debug(f"Cached data for key: {key}")

    def clear_cache(self):
        self.cache.clear()
        logging.info("Cache cleared.")
