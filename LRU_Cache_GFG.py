from collections import OrderedDict
# design the class in the most optimal way


class LRUCache:

    #Constructor for initializing the cache capacity with the given value.
    def __init__(self, cap: int):
        #code here
        self.cap = cap
        self.cache = OrderedDict()

    #Function to return value corresponding to the key.
    def get(self, key) -> int:
        #code here
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    #Function for storing key-value pair.
    def set(self, key, value):
        #code here
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)


#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        cap = int(input())  # capacity of the cache
        qry = int(input())  #number of queries
        a = list(map(str,
                     input().strip().split()))  # parent child info in list

        lru = LRUCache(cap)

        i = 0
        q = 1
        while q <= qry:
            qtyp = a[i]

            if qtyp == 'SET':
                lru.set(int(a[i + 1]), int(a[i + 2]))
                i += 3
            elif qtyp == 'GET':
                print(lru.get(int(a[i + 1])), end=' ')
                i += 2
            q += 1
        print()
# } Driver Code Ends