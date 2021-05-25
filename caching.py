from collections import deque


# For the caching method we will assume that newer entries are most likely to be reused,
# so we will implement a strategy FIFO
class Cache:
    """This class implements the Least Recently Used caching method"""
    # Let's assume that the file has 5000 IPs and the probability of repeated ips is 10% so
    # 500 items should be a good number.
    # Also assuming that this is not a memory issue for the machine. If we assume we need to
    # save space we could implement a LRU, MRU, LFU to dynamically clean the cache.

    def __init__(self):
        self.hashmap = dict()
        self.size = 500
        # We are using dequeue instead of primitive list because it is more efficient
        # for poping on index 0. O(1) against O(n).
        self.queue = deque()

    def get_value(self, key):
        cached_response = self.hashmap.get(key)
        if cached_response:
            print(f'Got {key} from cache')
            return cached_response

    def put(self, key, response_json):
        if len(self.queue) >= self.size:
            first_out = self.queue.popleft()
            self.hashmap.pop(first_out)

        if key not in self.hashmap:
            self.hashmap[key] = response_json
            self.queue.append(key)
            print(f'added {key} to cache')


