import threading
import time


class TokenBuckets:
    def __init__(self, size: int, add: int, every: int = 1000):
        ## homework:replace:on
        #.raise NotImplementedError
        self._size = size
        self._add = add
        self._every = every
        self._buckets: dict[str, int] = {}
        self._lock = threading.Lock()
        self._refill_thread = threading.Thread(target=self._refill, daemon=True)
        self._refill_thread.start()
        ## homework:replace:off

    def too_many(self, key: str) -> bool:
        ## homework:replace:on
        with self._lock:
            buckets = self._buckets
            tokens = buckets.get(key, self._size)
            if tokens == 0:
                return True
            tokens -= 1
            buckets[key] = tokens
        return False
        ## homework:replace:off

    ## homework:delete:on
    def _refill(self) -> None:
        seconds = self._every / 1000
        while True:
            with self._lock:
                for k, v in self._buckets.items():
                    new_value = v + self._add
                    if new_value <= self._size:
                        self._buckets[k] = new_value
            time.sleep(seconds)
    ## homework:delete:off
